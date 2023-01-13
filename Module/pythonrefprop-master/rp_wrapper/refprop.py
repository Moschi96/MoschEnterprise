# -*- coding: utf-8 -*-
"""
Created on 21.04.2020

@author: Christoph Hoeges

To test:
- Transport properties are not fully tested (Status: 11.06.2020)
- Error raising is not implemented at all refprop calls
    - Additional change might be that not all errors and warning are excluded when 'use_error_check' is set to false but
        only warnings or errors?
"""
# ======================================================================================================================
#                                                    Imports
# ======================================================================================================================
import os
import warnings
from . import ThermodynamicState
from . import TransportProperties
from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary


# ======================================================================================================================
#                                                  RefProp Class
# ======================================================================================================================
class RefProp:
    """ Class to connect to refProp package.

    Note:
        - You need to install package ctREFPROP Package
          https://github.com/usnistgov/REFPROP-wrappers/tree/master/wrappers/python
        - In case you use a self-defined mixture: Entropy reference state might deviate from GUI!!
        - In case you want multiple instances (with possible different fluids) at the same time:
            1. Call RefProp.get_dll_path() to get the path of the dll
            2. Copy the file to a new location and name it as you like (here: path_to_dll)
                Tip: Include the fluid name into the dll path to identify which dll is for which fluid.
            3. Setup the wrapper using RefProp(fluid_name, z, use_dll=path_to_dll)
            4. Remember to delete the copied dll once you finish your script.


    Functionality:
        - It does not work to have multiple instances simultaneously. When calculating values the last fluid name
            somehow will be used even though instance includes "new" name. Need to be fixed at some point.


    How to use RefProp-Wrapper:
    ---------------------------
    1.) Create RefProp instance: rp = RefProp("R32")
    2.) In case you want to calculate fluid properties (state variables) for a specific state: Use calc_state() function
            Multiple inputs can be given (but you need to now two in order to define the values). For further
            information see function header.
    3.) Further get-Functions implemented
        - get_gwp(): Global warming potential
        - get_odp(): Ozone depletion potential
        - get_safety(): Safety class
        - get_mass_fraction(): Mass fractions of pure substances in fluid
        - get_molar_mass(): Molar mass of fluid
        - get_mol_fraction(): Mol fractions of pure substances in fluid
        - get_comp_names(): Pure substances names in fluid
        - get_longname(): Long name of fluid within RefProp
        - get_crit_point(): Crit. Temperature and Pressure
        - get_version(): Version of wrapper and of RefProp dll


    Version notes:
    --------------
    0.1.0 (21.04.2020, Christoph Hoeges):
        First implementation
            - Contains multiple functions to call RefProp instance
            - Can calculate state, crit, GWP, ODP, Safety class, molar mass etc. of fluid
            - Mixtures might work but it wasn't fully testet - R455A e.g. still deviates slightly

    0.1.1 (25.04.2020, Christoph Hoeges):
        Multiple changes, added functionality. Commands are still the same though
            - Self designed mixtures are possible now as well (see instructions in init
            - Added composition input to __init__ function
            - Added modes in calc_state function and removed bug in PH calculation
            - Additional protected functions due to different input
            - Adjusted _call_refprop function (z is not mass frac but mol fraction)
            - Added documentation / instruction

    0.1.2 (08.05.2020, Christoph Hoeges):
        Multiple adjustments
            - Added function to call ABFLSHdll function in refprop (high level function)
            - Changed function calls in calc_state function to ABFLSH and adjusted conversion
            - Change init-function so user can choose which dll shall be used
            - Add function to get version of this current wrapper as well as RefProp-dll version

    0.1.3 (12.05.2020, Christoph Hoeges):
        Multiple changes
            - Added function to get all files in MIXTURE and FLUIDS directory to check available fluids
            - Added error function in order to return errors when RefProp-Functions are called.
                NOTE: Not all instances where refprop is called are checked for errors. Currently, it is only used in
                    init and calc_state

    0.1.4 (19.05.2020, Christoph Hoeges):
        Multiple changes:
            - Debugged fluid properties calculation for predefined mixtures
            - Fixed option of self-defined mixtures

    0.1.5 (22.05.2020, Christoph Hoeges):
        Include transport properties calculation into wrapper

    0.1.6 (10.06.2020, Fabian Wuellhorst):
        Add option to use a custom dll path. This necessary to use multiple instances with possible
        different fluids at the same time.
    """
    # General information
    #
    __version__ = "0.1.6"
    __author__ = "Christoph Hoeges"

    # Init function
    #
    def __init__(self,
                 fluid_name,
                 z=None,
                 use_dll='local',
                 use_error_check=True,
                 use_warnings=True):
        """ Initialization function

        Notes:
        ------
        1.) When you want to use a self-design mixture to as follows:
                - Fluid-name needs to contain all component names within mixture: "R32.FLD|R125.FLD"
                - z needs to be a list with molar fractions: [0.697, 0.303]
                - Used example would be similar to R410A

        Parameters:
        -----------
        :param string fluid_name:
            Fluid name for RefProp use
        :param list or None z:
            Fluid composition. Should only be used, when a self-design mixture shall be used. Further information
            see notes.
        :param string use_dll:
            Specifier whether dll in package shall be used ('local')
            or the global one of installed RefProp version ('global')
            or a dll specified by you directly. In the latter case, specify the
            filepath to the dll, e.g. use_dll='C:\\path_to_dll\\RefProp64.dll'
            If you want to find and copy a dll, use the static method get_dll_path().
        :param boolean use_error_check:
            Specifier whether errors and warnings shall be checked when calling RefProp or not
        :param boolean use_warnings:
            Specifier whether warnings shall be used
        """
        # Get environment variable for path to dll
        root = os.environ["RPPREFIX"]
        # Local path to dll
        if use_dll.lower() == "local":
            path_to_dll = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"REFPRP64.dll")
        elif use_dll.lower() == "global":
            path_to_dll = os.path.join(root, r"REFPRP64.DLL")
        else:
            path_to_dll = use_dll
        #
        self._flag_check_errors = use_error_check
        self._flag_warnings = use_warnings
        # Set root to RefProp package
        self._root = root
        self.rp = REFPROPFunctionLibrary(path_to_dll)
        self.rp.SETPATHdll(root)
        # Define fluid - Only pure substances currently!
        self.molar_base_si = self.rp.GETENUMdll(0, "MOLAR BASE SI").iEnum
        # Set fluid name
        self.fluid_name = fluid_name
        # Get mass and mol fraction and number of components
        self._get_comp_frac(z)
        # Get component names
        self._comp_names = self._get_comp_names()
        # Mixture flag
        if self._n_comp > 1:
            self._mix_flag = True
        else:
            self._mix_flag = False

        # Setup
        self._setup_rp()
        # Calculate molar mass in kg/mol
        # self.M = self._call_refprop_allprop("M").Output[0]
        self.M = self._call_refprop("", "M").Output[0]

    #
    #
    def _call_refprop_abflsh(self,
                             inp_name,
                             value_a,
                             value_b,
                             i_flag=1):
        """ Call RefProp via ABFLSHdll method
        You can define multiple inputs but only "specific ones" where no input values are needed for
        e.g. M, Tcrit, pcrit

        Parameters:
        -----------
        :param string inp_name:
            Input commands: "PQ"
        :param float value_a:
            Value of parameter b defined in inp_name. In case of None 0 will be used.
        :param float value_b:
            Value of parameter b defined in inp_name. In case of None 0 will be used.
        :param int i_flag:
            Flag
        Return:
        -------
        :return ABFLSHdlloutput tmp:
            Returns ABFLSH output

        """
        # TODO
        tmp = self.rp.ABFLSHdll(inp_name, value_a, value_b, self._mol_frac, i_flag)

        return tmp

    #
    #
    def _call_refprop_allprop(self,
                              out_name,
                              T_val=None,
                              d_val=None,
                              i_mass=0,
                              i_flag=1):
        """ Call RefProp via ALLPROPSdll-method

        Parameters:
        -----------
        :param string out_name:
            Variables you want to calculate. Multiple outputs are possible:
                - Single: "M"
                - Multiple: "M,TC,PC"
        :param float T_val:
            Temperature in current state in K.
            Note: In case you want to get general fluid parameters such as M, Tcrit, .. Stick to default value!
        :param float d_val:
            Density in current state (unit depending on i_mass flag - either mol/m^3 or kg/m^3)
            Note: In case you want to get general fluid parameters such as M, Tcrit, .. Stick to default value!
        :param int i_mass:
            Specifies which units the inputs are given in.
                - 0: Molar based
                - 1: Mass based
            Note: In current version (10.0.0.72) Ian Bell says in multiple Git-Issues that you should stick to molar
                    base!
        :param int i_flag:
            In current version (10.0.0.72) i_flag is used to define whether a string containing the units is written in
            'hUnits'.
                - 0: Deactivated
                - 1: activated
        Return:
        -------
        :return ALLPROPSdlloutput result:
            List with values for parameters

        """
        # Check values of T and d
        if T_val is None:
            T_val = 0
        if d_val is None:
            d_val = 0
        # Define fraction used depending on i_mass flag
        if i_mass == 0:
            frac = self._mol_frac
        elif i_mass == 1:
            frac = self._mass_frac
        else:
            raise ValueError("Chosen i_mass flag '{}' is not possible in ALLPROPSdll function!".format(i_mass))

        # Call RefProp
        res = self.rp.ALLPROPSdll(out_name, self.molar_base_si, i_mass, i_flag, T_val, d_val, frac)

        return res

    #
    #
    def _call_refprop(self,
                      inp_name,
                      out_name,
                      value_a=None,
                      value_b=None,
                      i_mass=0,
                      i_flag=1,
                      frac=None,
                      fluid=None):
        """ Call general refProp function and calculate values

        Parameters:
        -----------
        :param string fluid:
            Fluid name - in case default value None is used, stored fluid name will be used for command
        :param string inp_name:
            Input parameter specification
        :param string out_name:
            Output string name
        :param float value_a:
            Value of parameter b defined in inp_name. In case of None 0 will be used.
        :param float value_b:
            Value of parameter b defined in inp_name. In case of None 0 will be used.
        :param integer i_flag:
            Defines further settings (see documentation)
        :param int i_mass:
            Specifies which units the inputs are given in.
                - 0: Molar based
                - 1: Mass based
            Note: In current version (10.0.0.72) Ian Bell says in multiple Git-Issues that you should stick to molar
                    base!
        :param list frac:
            List with either mol or mass fraction of pure substances in current fluid
                (in case of single pure substance: [1]).

        Return:
        -------
        :return REFPROPdlloutput output:
            Command of refprop
        """
        # Check inputs
        if value_a is None:
            value_a = 0
        if value_b is None:
            value_b = 0

        if fluid is None:
            if self._predefined:
                fluid = self.fluid_name
            else:
                fluid = ""
        if frac is None:
            if self._predefined:
                frac = ""
            else:
                if i_mass == 0:
                    frac = self._mol_frac
                elif i_mass == 1:
                    frac = self._mass_frac
                else:
                    raise ValueError("Variable i_mass has invalid input '{}'".format(i_mass))

        # Call refprop function
        tmp = self.rp.REFPROPdll(fluid,
                                 inp_name,
                                 out_name,
                                 self.molar_base_si,
                                 i_mass,
                                 i_flag,
                                 value_a,
                                 value_b,
                                 frac)

        return tmp

    #
    #
    def _check_error(self,
                     err_num,
                     err_msg,
                     func_name=""):
        """ Check error code and raise error in case it is critical

        Parameters:
        -----------
        :param integer err_num:
            Error return code
        :param string err_msg:
            Error message given in RefProp call
        :param string func_name:
            Name of function error needs to be checked in
        """
        # All fine in case error number is 0
        # Throw warning in case error number different than 0 and smaller than 100 is given
        # Throw error in case error number higher than 100 is given
        if err_num:
            if err_num < 100:
                if self._flag_warnings:
                    warnings.warn("[WARNING] Error number {} was given in function '{}'. No critical error but "
                                  "something went wrong maybe. \n Error message is: '{}'".format(str(err_num),
                                                                                                 func_name, err_msg))
            else:
                if self._flag_check_errors:
                    raise TypeError("[ERROR] When calling RefProp in function '{}' error number {} was "
                                    "returned. \n Error message is: '{}'".format(func_name, str(err_num), err_msg))

    #
    #
    def _get_comp_names(self):
        """ Get component names. In case current fluid is mixture, only component names will be returned.
        In case fluid is a pure substance, substance name is returned.

        Return:
        -------
        :return list comp_names:
            List with pure substances in current refrigerant
        """
        comp_names = []
        if self._predefined:
            # Note: While trying it was possible to get fluid name as well, therefore n_comp+1 is used.
            tmp = []
            for i in range(self._n_comp + 1):
                tmp.append(self.rp.NAMEdll(i).hnam)

            if tmp[1] == "":
                comp_names = []
            else:
                comp_names = tmp[1:]
        else:
            # Self-defined
            tmp_str = self.fluid_name.split("|")
            for i in tmp_str:
                i = i.replace(".FLD", "")
                i = i.replace(".MIX", "")
                if len(i) < 2:
                    continue
                else:
                    comp_names.append(i)

        # Replace Carbon Dioxide for CO2
        for i, tmp in enumerate(comp_names):
            if "Carbon dio" in tmp:
                comp_names[i] = "CO2"

        return comp_names

    #
    #
    def _get_comp_frac(self, z):
        """ Get mass/mol fraction and number of components of current fluid

        Parameters:
        -----------
        :param list z:
            Contains predefined molar fractions in case one is given. Otherwise, z will be None
        """
        # In case predefined mixture or pure substance is used
        if z is None:
            self._predefined = True
            # Dummy function to get values for z in order to specify number of components
            tmp = self._call_refprop("",
                                     "GWP",
                                     i_mass=1)
            # Check for errors
            self._check_error(tmp.ierr, tmp.herr, self._get_comp_frac.__name__)
            # Mass fractions of components
            self._mass_frac = [zi for zi in tmp.z if zi > 0]
            # Get number of components
            self._n_comp = len(self._mass_frac)
            # Check, whether error occurred
            if self._n_comp < 1:
                # It might be possible that z value bugs when calling RefProp. In case of a pure substance this does not
                # matter so an additional filter is included
                tmp_n = [1 for i in tmp.Output if i >= -1]
                if len(tmp_n) == 1:
                    self._n_comp = 1
                    self._mass_frac = [1]
                else:
                    raise ValueError("Number of components for current fluid '{}' is less than "
                                     "one!".format(self.fluid_name))
            # Get mol fraction
            self._mol_frac = self._transform_to_molfraction(self._mass_frac)
        else:
            self._predefined = False
            # Mol fraction
            self._mol_frac = z
            # _mass_frac is not allowed to be zero - values might not be correct but that does not matter when code
            # keeps going
            self._mass_frac = self._transform_to_massfraction(z)
            # Get number of components
            self._n_comp = len(self._mol_frac)

    #
    #
    def _setup_rp(self):
        """ Setup for RefProp """
        # In case of pure substance
        if self._n_comp == 1:
            self.rp.SETUPdll(self._n_comp, self.fluid_name, "HMX.BNC", "DEF")
        # In case of mixtures
        else:
            # TODO: Do I even need to check it this way (self._predefined exists..)
            # Check if mixture is predefined
            name = self.fluid_name.split(".")[0]
            if name in self.get_available_substances():
                # Pre defined mixture
                mode = 2
                mixture = self.fluid_name
            else:
                # Self defined mixture
                mode = 1
                # Define mixtures name
                # TODO: Mixtures can be used as input as well... and PPF is possible also
                # TODO: Ending is not necessary to create mixtures....
                mixture = "|".join([f+".FLD" for f in self._comp_names])

            # Setup for mixture
            setup = self.rp.SETUPdll(self._n_comp, mixture, 'HMX.BNC', 'DEF')
            self.rp.SETREFdll("DEF", mode, self._mol_frac, 0, 0, 0, 0)

            # Get mass fraction
            self._mass_frac = self._transform_to_massfraction(self._mol_frac)

            # Check whether mixing rules are available
            if setup.ierr == 117:
                if self._flag_check_errors:
                    raise ValueError(
                        "[MIXING ERROR] Mixing rules for mixture '{}' do not exist!".format(self._comp_names))
                else:
                    print(
                        "[MIXING ERROR] Mixing rules for mixture '{}' do not exist!".format(self._comp_names))
            elif setup.ierr == -117:
                if self._flag_warnings:
                    warnings.warn(
                        "[MIXING ERROR] Mixing rules for mixture '{}' are estimated!".format(self._comp_names))
                else:
                    print(
                        "[MIXING WARNING] Mixing rules for mixture '{}' are estimated!".format(self._comp_names))

    #
    #
    def _transform_to_massfraction(self,
                                   mol_frac):
        """ Transforms mol fraction to mass fraction

        Parameters:
        -----------
        :param list mol_frac:
            List containing floats for mol fraction

        Return:
        -------
        :return list mass_frac:
            List containing floats for mass fraction
        """
        tmp = self.rp.XMASSdll(mol_frac)
        mass_frac = [yi for yi in tmp.xkg if yi > 0]
        return mass_frac

    #
    #
    def _transform_to_molfraction(self,
                                  mass_frac):
        """ Transforms mass fraction to mol fraction

        Parameters:
        -----------
        :param list mass_frac:
            List containing floats for mass fraction

        Return:
        -------
        :return list frac:
            List containing floats for mol fraction
        """
        tmp = self.rp.XMOLEdll(mass_frac)
        mol_frac = [xi for xi in tmp.xmol if xi > 0]
        return mol_frac

    # Calculate state function
    #
    def calc_state(self,
                   mode,
                   var1,
                   var2):
        """ Calculate state. Depending on mode, different function will be chosen. Input state variables need to be in
        SI units!

        Notes:
        ------
        1.) PT does not work when state might be within the two-phase region!
        2.) Only functions for density are implemented. In case you know the specific volume instead use density
                functions with inverse value!
        3.) Quality can have values outside of 'physical' scope:
                q = -998: Subcooled liquid
                q = 998: Superheated vapor
                q = 999: Supercritical state

        Possible modes are currently:
            - "PD": Pressure, Density
            - "PH": Pressure, Enthalpy
            - "PQ": Pressure, Quality
            - "PS": Pressure, Entropy
            - "PT": Pressure, Temperature
            - "PU": Pressure, Internal Energy
            - "TD": Temperature, Density
            - "TH": Temperature, Enthalpy
            - "TQ": Temperature, Quality
            - "TS": Temperature, Entropy
            - "TU": Temperature, Internal Energy
            - "DH": Density, Enthalpy
            - "DS": Density, Entropy
            - "DU": Density, Internal Energy

        Parameters:
        -----------
        :param string mode:
            Defines which input state variables are given (see possible modes above)
        :param float var1:
            Value of state variable 1 (first one in name) - use SI units!
        :param float var2:
            Value of state variable 2 (second one in name) - use SI units!

        Return:
        -------
        :return ThermodynamicState state:
            Thermodynamic state with state variables
        """
        # Multiplier for pressure since kPa is used in RefProp
        p_multi = 1e-3
        # Multiplier for energy
        e_multi = self.M
        # Multiplier for density
        d_multi = 1 / self.M / 1000

        # Init all parameters
        p = None
        d = None
        T = None
        u = None
        h = None
        s = None
        q = None

        # Check modi

        # Pressure and density
        if mode == "PD":
            p = var1
            d = var2
            var1 = var1 * p_multi
            var2 = var2 * d_multi
            tmp = self.rp.PDFLSHdll(var1, var2, self._mol_frac)
        # Pressure and enthalpy
        elif mode == "PH":
            p = var1
            var1 = var1 * p_multi
            h = var2
            var2 = var2 * e_multi
            tmp = self.rp.PHFLSHdll(var1, var2, self._mol_frac)
        # Pressure and quality
        elif mode == "PQ":
            p = var1
            var1 = var1 * p_multi
            q = var2
            # In case current fluid is mixture you need to transform Q to molar base for RefProp-function
            if self._mix_flag:
                var2 = self._call_refprop("PQMASS", "QMOLE", p, q, i_mass=1).Output[0]
            tmp = self.rp.PQFLSHdll(var1, var2, self._mol_frac, 0)
        # Pressure and entropy
        elif mode == "PS":
            p = var1
            var1 = var1 * p_multi
            s = var2
            var2 = var2 * e_multi
            tmp = self.rp.PSFLSHdll(var1, var2, self._mol_frac)
        # Pressure and Temperature
        elif mode == "PT":
            p = var1
            var1 = var1 * p_multi
            T = var2
            tmp = self.rp.TPFLSHdll(var2, var1, self._mol_frac)
        # Pressure and internal energy
        elif mode == "PU":
            p = var1
            var1 = var1 * p_multi
            u = var2
            var2 = var2 * e_multi
            mode = "PE"
            tmp = self.rp.PEFLSHdll(var1, var2, self._mol_frac)
        # Temperature and density
        elif mode == "TD":
            T = var1
            d = var2
            var2 = var2 * d_multi
            tmp = self.rp.TDFLSHdll(var1, var2, self._mol_frac)
        # Temperature and enthalpy
        elif mode == "TH":
            T = var1
            h = var2
            var2 = var2 * e_multi
            tmp = self.rp.THFLSHdll(T, var2, self._mol_frac, 1)
        # Temperature and quality
        elif mode == "TQ":
            T = var1
            q = var2
            # In case current fluid is mixture you need to transform Q to molar base for RefProp-function
            if self._mix_flag:
                var2 = self._call_refprop("TQMASS", "QMOLE", T, q, i_mass=1).Output[0]
            tmp = self.rp.TQFLSHdll(T, var2, self._mol_frac, 1)
        # Temperature and entropy
        elif mode == "TS":
            T = var1
            s = var2
            var2 = var2 * e_multi
            tmp = self.rp.TSFLSHdll(T, var2, self._mol_frac, 1)
        # Temperature and internal energy
        elif mode == "TU":
            T = var1
            u = var2
            var2 = var2 * e_multi
            mode = "TE"
            tmp = self.rp.TEFLSHdll(T, var2, self._mol_frac, 1)
        # Density and enthalpy
        elif mode == "DH":
            d = var1
            var1 = var1 * d_multi
            h = var2
            var2 = var2 * e_multi
            tmp = self.rp.DHFLSHdll(var1, var2, self._mol_frac)
        # Density and entropy
        elif mode == "DS":
            d = var1
            var1 = var1 * d_multi
            s = var2
            var2 = var2 * e_multi
            tmp = self.rp.DSFLSHdll(var1, var2, self._mol_frac)
        # Density and inner energy
        elif mode == "DU":
            d = var1
            var1 = var1 * d_multi
            u = var2
            var2 = var2 * e_multi
            mode = "DE"
            tmp = self.rp.DEFLSHdll(var1, var2, self._mol_frac)
        else:
            raise ValueError("Chosen mode is not available in refprop calc_state function!")

        # Check for errors
        self._check_error(tmp.ierr, tmp.herr, self.calc_state.__name__)

        # Get all state variables
        if p is None:
            p = tmp.P / p_multi
        if T is None:
            T = tmp.T
        if u is None:
            u = tmp.e / e_multi
        if h is None:
            h = tmp.h / e_multi
        if s is None:
            s = tmp.s / e_multi
        if d is None:
            d = tmp.D / d_multi
        if q is None:
            if self._mix_flag:
                # Transform current q (molar) to mass based quality
                tmp2 = self._call_refprop("PH", "QMASS", p, h*e_multi, i_mass=1)
                if tmp2.Output[0] < 0:
                    q_mass = tmp2.ierr
                else:
                    q_mass = tmp2.Output[0]
                q = q_mass
            else:
                q = tmp.q

        # # In case not in two phase region reset q to -1
        # if q > 1 or q < 0:
        #     q = -1

        # Define state
        state = ThermodynamicState(p=p, T=T, u=u, h=h, s=s, d=d, q=q)
        return state

    #
    #
    def calc_transp_props(self,
                          state):
        """ Calculate transport properties of RefProp fluid at given state

        Parameters:
        -----------
        :param ThermodynamicState state:
            Current thermodynamic state
        Return:
        -------
        :return TransportProperties props:
            Instance of TransportProperties
        """
        # Get properties
        tmp = self._call_refprop_allprop("PRANDTL,VIS,TCX,KV,CV,CP,BETA", state.T, state.d/self.M, i_mass=0)
        # Create transport properties instance
        props = TransportProperties(lam=tmp.Output[2],
                                    dyn_vis=tmp.Output[1],
                                    kin_vis=tmp.Output[3],
                                    pr=tmp.Output[0],
                                    cp=tmp.Output[5]/self.M,
                                    cv=tmp.Output[4]/self.M,
                                    beta=tmp.Output[6],
                                    state=state)
        # Return props
        return props

    #
    #
    def get_available_substances(self,
                                 mode="all",
                                 include_ending=False,
                                 save_txt=False):
        """ Get all available RefProp fluids (mixtures and / or pure substances depending on mode)

        Parameters:
        -----------
        :param string mode:
            Mode defining which kind of fluids you want to have: 'pure': pure substances, 'mix': mixtures, 'all': all
        :param boolean include_ending:
            Defines, whether file ending shall be returned as well or not
        :param boolean save_txt:
            Defines, whether a text file with names shall be created in current working directory
        Return:
        -------
        :return list names:
            String list containing names of available fluids (depending on defined mode)
        """
        # Possible endings
        _endings = ["MIX", "FLD", "PPF"]

        # Folders where fluid data is located
        folders = [r"FLUIDS", r"MIXTURES"]

        # Define paths by mode
        if mode == "pure":
            paths = [os.path.join(self._root, folders[0])]
        elif mode == "mix":
            paths = [os.path.join(self._root, folders[1])]
        elif mode == "all":
            paths = [os.path.join(self._root, folders[0]),
                     os.path.join(self._root, folders[1])]
        else:
            raise ValueError("Chosen mode '{}' is not possible!".format(mode))

        # Get files in folders, remove ending and append to names
        names = []
        for p in paths:
            # Get all files in directory
            files = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
            # Remove ending
            if include_ending:
                tmp = [path for path in files if path.split(".")[1] in _endings]
            else:
                tmp = [path.split(".")[0] for path in files if path.split(".")[1] in _endings]
            # Append names to names list
            names.extend(tmp)

        # In case names shall be stored
        if save_txt:
            with open("available_fluids.txt", "w") as output:
                for i in names:
                    output.write("{} \n".format(i))

        if not names:
            raise ValueError("No fluids are in current root directory. Check path '{}'!".format(self._root))

        # Return names
        return names

    #
    #
    def get_comp_names(self):
        """ Get name of components within current fluid"

        Return:
        -------
        :return list comp_names:
            String names of components within current fluid
        """
        return self._comp_names

    #
    #
    def get_crit_point(self):
        """ Get T and p of critical point

        Return:
        -------
        :return float Tc:
            Temperature at critical point in K
        :return float pc:
            Pressure at critical point in Pa
        :return float dc:
            Density at critical point in kg/m^3
        """
        mode = 2
        if mode == 1:
            tmp = self._call_refprop("CRIT", "T,P,D", i_mass=1)
            Tc = tmp.Output[0]
            pc = tmp.Output[1]
            dc = tmp.Output[2] * self.M
        else:
            res = self._call_refprop_allprop("TC,PC,DC")
            Tc = res.Output[0]
            pc = res.Output[1]
            dc = res.Output[2] * self.M
        return Tc, pc, dc

    #
    #
    def get_def_limits(self):
        """ Get limits of current ref prop fluid
        Limits contain Tmin, Tmax, Dmax and Pmax (Temperatures, density, pressure)

        :return dict limits:
            Dictionary with definition limits in RefProp. Contains min/max temperature, max density, max pressure.
        """
        tmp = self._call_refprop_allprop("TMIN,TMAX,DMAX,PMAX")
        limits = {"Tmin": tmp.Output[0],
                  "Tmax": tmp.Output[1],
                  "Dmax": tmp.Output[2] * self.M,
                  "Pmax": tmp.Output[3]}
        return limits

    #
    #
    @staticmethod
    def get_dll_path(local=True):
        """
        Return the location of the dll in this repository

        Parameters:
        :param boolean local:
            If True, the dll in this repo is returned, else the
            dll in the RefProp installation folder is returned.
            Default is True.
        Return:
        :return: string path_to_dll:
            Path of a valid dll
        """

        # Local path to dll
        if local:
            path_to_dll = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"REFPRP64.dll")
        else:
            root = os.environ["RPPREFIX"]
            path_to_dll = os.path.join(root, r"REFPRP64.DLL")

        # Check if dll actually exists:
        if not os.path.exists(path_to_dll):
            raise FileNotFoundError("Selected dll not found automatically. "
                                    "Please alter the local attribute or search for yourself.")

        return path_to_dll

    #
    #
    def get_fluid_name(self):
        """ Get fluid name.

        Return:
        -------
        :return string fluid_name:
            Fluid name
        """
        return self.fluid_name

    #
    #
    def get_gwp(self):
        """ Get gwp of current fluid from refProp

        Return:
        -------
        :return float gwp:
            Global warming potential of fluid. In case calculation failed, None will be returned.
        """
        # Call refProp
        tmp = self._call_refprop("",
                                 "GWP",
                                 i_mass=1)
        # Calculate gwp
        gwp = round(sum(max(tmp.Output[i], 0) * self._mass_frac[i] for i in range(self._n_comp)), 2)
        # In case GWP cannot be calculated
        if gwp < 0:
            gwp = 0
        return gwp

    #
    #
    def get_longname(self):
        """ Get longname of fluid

        Return:
        -------
        :return string longname:
            Name of current fluid in refprop - provides mass fractions and components as well (in case of mixture)
        """
        longname = self._call_refprop("", "LONGNAME(0)").hUnits
        return longname

    #
    #
    def get_mass_fraction(self, use_round=True):
        """ Get mass fractions of pure substances in current fluid

        Parameters:
        :param boolean use_round:
            Flag to define, whether the exact values or rounded values (by the fourth number) shall be used
        Return:
        -------
        :return list mass_frac:
            List of component mass fractions
        """
        if use_round:
            mass_frac = [round(i, 4) for i in self._mass_frac]
        else:
            mass_frac = self._mass_frac
        return mass_frac

    #
    #
    def get_molar_mass(self):
        """ Get molar mass of current fluid

        Return:
        -------
        :return float M:
            Molar mass of current fluid in kg/mol
        """
        return self.M

    #
    #
    def get_mol_fraction(self, use_round=True):
        """ Get mol fractions of pure substances in current fluid

        Parameters:
        :param boolean use_round:
            Flag to define, whether the exact values or rounded values (by the fourth number) shall be used
        Return:
        -------
        :return list frac:
            List of component mol fractions
        """
        if use_round:
            mol_frac = [round(i, 4) for i in self._mol_frac]
        else:
            mol_frac = self._mol_frac
        return mol_frac

    #
    #
    def get_odp(self):
        """ Calculate ozone depletion potential
        In case of mixtures: Maximum value of pure substances will be used

        Return:
        -------
        :return float odp:
            ODP of fluid. In case calculation failed, None will be returned.
        """
        # Call refProp
        tmp = self._call_refprop("",
                                 "ODP",
                                 i_mass=1)
        # Calculate odp
        odp = max(max(tmp.Output), 0)
        # In case some error occured
        if odp < 0:
            odp = 0
        return odp

    #
    #
    def get_safety(self):
        """ Calculate safety class of refrigerant

        Return:
        -------
        :return string safety:
            Safety class of fluid.
        """
        # Call refProp
        tmp = self._call_refprop("",
                                 "SAFETY",
                                 i_mass=1)
        # Get safety class
        safety = tmp.hUnits
        # Return safety
        return safety

    #
    #
    def get_triple_point(self):
        """ Get temperature and pressure at triple point of current fluid

        Note: Works fine for pure substances, mixtures might not work properly

        Return:
        :return float T_tpl:
            Temperature at triple point in K
        :return float p_tpl:
            Pressure at triple point in Pa
        """
        # Call Refprop
        tmp = self._call_refprop("TRIP", "T;P")
        return tmp.Output[0], tmp.Output[1]

    #
    #
    def get_version(self):
        """ Get version of wrapper and used RefProp dll

        Return:
        :return string wrapper_version:
            Refprop wrapper version
        :return string refprop_version:
            Version of used RefProp dll
        """
        return self.__version__, self.rp.RPVersion()

    #
    #
    def is_mixture(self):
        """ Find out if fluid is mixture or not.
        In case current fluid is mixture, true is returned.
        In case current fluid is pure substance, false is returned.

        Return:
        -------
        :return boolean _mix_flag:
            Boolean for mixture (True), pure substance (False)
        """
        return self._mix_flag

    #
    #
    def set_error_flag(self, flag):
        """ Set error flag

        Parameters:
        :param boolean flag:
            New error flag
        Return:
        :return int err:
            Notifier for error code - in case everything went fine, 0 is returned
        """
        self._flag_check_errors = flag
        return 0

    #
    #
    def set_warning_flag(self, flag):
        """ Set warning flag

        Parameters:
        :param boolean flag:
            New warning flag
        Return:
        :return int err:
            Notifier for error code - in case everything went fine, 0 is returned
        """
        self._flag_warnings = flag
        return 0
