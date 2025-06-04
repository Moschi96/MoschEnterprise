# -*- coding: utf-8 -*-
"""
Created on 21.03.2020

@author: Christoph Hoeges
"""
# ======================================================================================================================
#                                                    Imports
# ======================================================================================================================


# ======================================================================================================================
#                                            Thermodynamic State class
# ======================================================================================================================
class ThermodynamicState:
    """ Thermodynamic state class
    Specifies specific state within cycle. Does not necessarily need to have all state variables defined!

    Version notes:
    --------------
    0.1.0 (21.03.2020, Christoph Hoeges):
        First implementation
    0.1.1 (22.04.2020, Christoph Hoeges):
        Minor changes in init-function:
            - Added d as possible input
            - v calculation in case only d is given
            - raise error in case 1/v is not equal to d in case both are given
    """
    # General information
    #
    __version__ = "0.1.1"
    __author__ = "Christoph Hoeges"

    # Init function
    #
    def __init__(self,
                 p=None,
                 T=None,
                 u=None,
                 h=None,
                 s=None,
                 v=None,
                 q=None,
                 d=None):
        """ Initialization function of state class
        In case only v or d is given, the other attribute will be calculated. In case both are given and they are and
        similar, an error will be raised.

        Parameters:
        -----------
        :param float p:
            Pressure at state in Pa
        :param float T:
            Temperature at state in K
        :param float u:
            Inner energy at state in J/kg
        :param float h:
            Enthalpy at state in J/kg
        :param float s:
            Entropy at state in J/(kg * K)
        :param float v:
            Specific volume at state in m^3/kg
        :param float q:
            Quality at state (between 0 and 1)
        :param float d:
            Density at state in kg/m^3
        """
        self.p = p
        self.T = T
        self.u = u
        self.h = h
        self.s = s
        self.v = v
        self.q = q
        self.d = d
        # Define density
        if v and d:
            if not round(1/v, 4) == round(d, 4):
                raise ValueError("At current state d and v do not match", d, v)
        elif v:
            self.d = 1/v
        elif d:
            self.v = 1/d

    # Convert function 1
    #
    @staticmethod
    def conv_k_to_c(T):
        """ Convert temperature in K to temperature in °C

        Parameters:
        -----------
        :param float T: Temperature in K

        Return:
        -------
        :return float T: Temperature in °C
        """
        return T - 273.15

    # Convert function 2
    #
    @staticmethod
    def conv_c_to_k(T):
        """ Convert temperature in °C to temperature in K

        Parameters:
        -----------
        :param float T: Temperature in °C

        Return:
        -------
        :return float T: Temperature in K
        """
        return T + 273.15


# ======================================================================================================================
#                                            Transport properties class
# ======================================================================================================================
class TransportProperties:
    """ Transport Properties class
    Specifies transport properties at a specific Thermodynamic State

    Version notes:
    --------------
    0.1.0 (22.05.2020, Christoph Hoeges):
        First implementation
    """
    # General information
    #
    __version__ = "0.1.0"
    __author__ = "Christoph Hoeges"

    # Init function
    #
    def __init__(self,
                 lam=None,
                 dyn_vis=None,
                 kin_vis=None,
                 pr=None,
                 cp=None,
                 cv=None,
                 beta=None,
                 state=None):
        """ Initialization function of class TransportProperties

        :param float lam:
            Thermal conductivity in W/(m*K)
        :param float dyn_vis:
            Dynamic viscosity in Pa*s
        :param float kin_vis:
            Kinematic viscosity in m^2/s
        :param float pr:
            Prandtl number
        :param float cp:
            Isobaric specific heat capacity in J/(kg*K)
        :param float cv:
            Isochoric specific heat capacity in J/(kg*K)
        :param float beta:
            Thermal expansion coefficient in 1/K
        :param ThermodynamicState state:
            State transport properties belong to
        """
        self.lam = lam
        self.dyn_vis = dyn_vis
        self.kin_vis = kin_vis
        self.Pr = pr
        self.cp = cp
        self.cv = cv
        self.beta = beta
        self.state = state
