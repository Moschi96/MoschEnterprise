# -*- coding: utf-8 -*-
"""
Created on 25.04.2020

@author: Christoph Hoeges & Benedikt Schuler

Test script for RefProp class


Notes to current version: 
-------------------------
Do not change the tested fluids. In case you have to change them, change teh fluids.xlsx too!


Testing method:
---------------
The refprop wrapper is tested with 3 pure fluids and 3 mixtures
For each fluid 4 different states are calculated: The subcooled liquid, the superheated vapor, within the two-phase
region (Q = 0.5) and at the edge of the two-phase region (Q = 1)
For each state the wrapper is tested for all kinds of possible inputs
Furthermore the fixed properties e. g. the critical temperature, molar mass, mass and mole fraction are tested

Known errors:
-------------
Pure fluids: Within the two-state region some errors will occur for the input T, P due to thermodynamic reasons
Sometimes some errors occur for the calculation of Q (Quality) - This is because the wrapper returns 998 if Q >1 
and -998 if Q<0


How to use:
-----------
When installing REFPROP the first time on a computer or when the dll changed, run this script to check, whether
everything works fine still.
In case an error or an incorrect value is calculated by this REFPROP-wrapper, a statement like:
    "Isobutane edge_point:
     PT: Difference: D 5.15%"
is returned / printed. The statement states the fluid (Isobutane), the calculated state point (edge point),
the state variables used to calculate state (PT), the attribute where the error occurred (D) and the relative deviation
(5.15%).


Adjustment notes:
-----------------
- Pep-8 conform
- Maybe add some more comments (optional)
"""
# ======================================================================================================================
#                                                    Imports
# ======================================================================================================================
from rp_wrapper import RefProp
import xlrd


# ======================================================================================================================
#                                                    Test function
# ======================================================================================================================

def run_test():
    """ For each of the six fluids test the fixed properties and the calculation of thermodynamic states for 4 states"""

    # Define tolerance
    tol = 0.01
    
    # Tested fluids - Do not change or you have to change tes_fluids.xlsx too!!
    fluids = ["R32", "Isobutane", "CO2", "R410A", "R453A", "R407C.MIX"]
    ref_points, ref_values = get_reference_data(fluids)

    for fluid in ref_points.keys(): 
        # for fluid in fluids:
        print("\n")
        
        # Create instance of RefProp
        rp = RefProp(fluid)
        # Test the fixed properties
        fixed_properties(rp, ref_values[fluid], tol)
        
        for point in ref_points[fluid].keys():
            # print(fluid + ":" + point + ":")
            state = ref_points[fluid][point]
            
            # Create a dict for the results 
            results = {}
            fl_point = fluid + " " + point
            results[fl_point] = []

            # Test the variable properties
            results[fl_point] = variable_properties(rp, state, tol, results[fl_point], point)

            # Print results
            if results[fl_point]:
                for fl_point in results.keys():
                    print(fl_point + ":")
                    for start_val in range(len(results[fl_point])):
                        print(results[fl_point][start_val])
            """
            # Only print something when error occurs: no mistake --> no print
            else:
                for fl_point in results.keys():
                    print(fl_point + ": " + "No mistake")
            """


def get_reference_data(fluids):
    """ Creates a dictionary with the reference points that are tested
    The value is an array consisting of the values for temperature, pressure, density, spec. internal energy,
    spec. enthalpy, spec. entropy and quality
    
    Parameters:
    -----------
    :param list fluids:
        List of all fluids to be tested

    Return:
    -------
    :return dictionary ref_points:
        Dictionary with name of the fluid as key.
        Value is another dictionary with the reference state and the properties.
    :return dictionary ref_values:
        Dictionary with name of the fluid as key.
        Value is another dictionary with the name of zhe fix property and its name.
    """

    book = xlrd.open_workbook(r"Data\test_fluids.xlsx")
    sheet_states = book.sheet_by_name("states")
    sheet_prop = book.sheet_by_name("properties")

    ref_points = {}
    ref_values = {}
    for fluid in fluids:
        
        # Get reference states
        ref_points[fluid] = {}
        
        for i in range(1, sheet_states.nrows):
            if fluid == sheet_states.cell_value(i, 0):
                val = []
                for j in range(2, sheet_states.ncols):
                    value = sheet_states.cell_value(i, j)
                    val.append(value)
                
                ref_points[fluid][sheet_states.cell_value(i, 1)] = val
                
        # Get reference properties
        ref_values[fluid] = {}
        for i in range(1, sheet_prop.nrows):
            if fluid == sheet_prop.cell_value(i, 0):
                for j in range(1, sheet_prop.ncols - 1):
                    key = sheet_prop.cell_value(0, j).split(" ")
                    if i <= 3:
                        prop = sheet_prop.cell_value(i, j)
                        if j < 7:
                            ref_values[fluid][key[0]] = prop
                        else:
                            ref_values[fluid][key[0]] = [prop]
                    else:
                        if j < 7:
                            prop = sheet_prop.cell_value(i, j)
                            ref_values[fluid][key[0]] = prop

                        if 7 <= j <= 8:
                            fraction = sheet_prop.cell_value(i, j).split(",")
                            ref_values[fluid][key[0]] = [float(r) for r in fraction]

    return ref_points, ref_values


# ======================================================================================================================
#                                       Test calc_state possibilities
# ======================================================================================================================
def variable_properties(rp, ref, tol, res, point):
    """ Test the calculation of properties for specific state points

    Parameters:
    -----------
    :param RefProp rp:
        Contains object of class RefProp, see also refprop.py
    :param dictionary ref:
        Contains temperature, pressure, density, sepc. internal energey, spec. entahlpy, spec. entropy, quality
    :param float tol:
        Contains tolerance
    :param list res:
        Contains a dictionary with fluid name and state point
    :param string point:
        Definition were current state point is located (two-phase, subcooled, superheat, ...)
        
    Return:
    -------
    :return list res:
        Dictionary with name of the fluid and state point and the mistakes found
    """
    # Define String for output
    names = ["T", "P", "D", "U", "H", "S", "Q"]

    # PD
    state = rp.calc_state("PD", ref[1], ref[2])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]

    # Differences for Q when Q should be 1 or 0 and 998 or -998 is returned should be filtered as well
    # (error occures due to rounding error)
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0

    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            # error is displayed as percentage
            res.append("PD: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")

    # PH
    state = rp.calc_state("PH", ref[1], ref[4])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0
    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            res.append("PH: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")

    # PQ
    # Q can only be used within the two-phase region
    if 0 <= ref[6] <= 1.0:
        state = rp.calc_state("PQ", ref[1], ref[6])
        T_diff_norm = (state.T - ref[0]) / ref[0]
        p_diff_norm = (state.p - ref[1]) / ref[1]
        d_diff_norm = (state.d - ref[2]) / ref[2]
        u_diff_norm = (state.u - ref[3]) / ref[3]
        h_diff_norm = (state.h - ref[4]) / ref[4]
        s_diff_norm = (state.s - ref[5]) / ref[5]
        q_diff_norm = (state.q - ref[6]) / ref[6]
        if state.q == 998 or state.q == -998:
            q_diff_norm = 0
        diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
        for i in range(len(diff)):
            if diff[i] > tol:
                res.append("PQ: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")
    
    # PS
    state = rp.calc_state("PS", ref[1], ref[5])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0
    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            res.append("PS: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")
    
    # PT
    state = rp.calc_state("PT", ref[1], ref[0])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0
    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            # PT for pure substance in two-phase region needs to be an exception
            # (there will always be a mistake since there are infinite possibilities)
            if not (not rp.is_mixture() and (point == "two-phase_region" or point == "edge_point")):
                res.append("PT: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")

    # PU
    state = rp.calc_state("PU", ref[1], ref[3])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0
    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            res.append("PU: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")

    # TD
    state = rp.calc_state("TD", ref[0], ref[2])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0
    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            res.append("TD: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")

    # TQ
    # Q can only be used within the two-phase region
    if 0 <= ref[6] <= 1.0:
        state = rp.calc_state("TQ", ref[0], ref[6])
        T_diff_norm = (state.T - ref[0]) / ref[0]
        p_diff_norm = (state.p - ref[1]) / ref[1]
        d_diff_norm = (state.d - ref[2]) / ref[2]
        u_diff_norm = (state.u - ref[3]) / ref[3]
        h_diff_norm = (state.h - ref[4]) / ref[4]
        s_diff_norm = (state.s - ref[5]) / ref[5]
        q_diff_norm = (state.q - ref[6]) / ref[6]
        if state.q == 998 or state.q == -998:
            q_diff_norm = 0
        diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
        for i in range(len(diff)):
            if diff[i] > tol:
                res.append("TQ: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")

    # TS
    state = rp.calc_state("TS", ref[0], ref[5])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0
    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            res.append("TS: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")

    # DH
    state = rp.calc_state("DH", ref[2], ref[4])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0
    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            res.append("DH: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")
    
    # DS
    state = rp.calc_state("DS", ref[2], ref[5])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0
    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            res.append("DS: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")
            
    # DU
    state = rp.calc_state("DU", ref[2], ref[3])
    T_diff_norm = (state.T - ref[0]) / ref[0]
    p_diff_norm = (state.p - ref[1]) / ref[1]
    d_diff_norm = (state.d - ref[2]) / ref[2]
    u_diff_norm = (state.u - ref[3]) / ref[3]
    h_diff_norm = (state.h - ref[4]) / ref[4]
    s_diff_norm = (state.s - ref[5]) / ref[5]
    q_diff_norm = (state.q - ref[6]) / ref[6]
    if state.q == 998 or state.q == -998:
        q_diff_norm = 0
    diff = [T_diff_norm, p_diff_norm, d_diff_norm, u_diff_norm, h_diff_norm, s_diff_norm, q_diff_norm]
    for i in range(len(diff)):
        if diff[i] > tol:
            res.append("DU: Difference: " + names[i] + " " + str(round(diff[i]*100, 2)) + "%")

    return res


# ======================================================================================================================
#             Further tests of additional functions
# ======================================================================================================================

def fixed_properties(rp, ref_val, tol):
    """ Test the functions, which read the fixed properties such as GWP, ODP...

    Parameters:
    -----------
    :param RefProp rp:
        Contains object of class RefProp, see also refprop.py
    :param dictionary ref_val:
        Contains reference values for Tc, pc, etc. for each fluid
    :param float tol:
        Contains the tolerance for the calculated values
    """

    # Get longname (includes mass fraction and components)
    longname = rp.get_longname()
    print("Longname:", longname)
    # Component names
    names = rp.get_comp_names()
    print("Components:", names)

    # Get values
    gwp = rp.get_gwp()
    gwp_diff = (gwp - ref_val["GWP"])
    if gwp_diff >= (tol * 25):
        print("GWP: Difference:", gwp_diff)
    
    # Get ODP
    odp = rp.get_odp()
    odp_diff = (odp - ref_val["ODP"])
    if odp_diff >= tol:
        print("GWP: Difference:", odp_diff)
    
    # Get safety class
    # safety class is only calculated properly for pure substances -> do not output for mixtures
    safety = "not calculated (mixture)"
    if not rp.is_mixture():
        safety = rp.get_safety()
    if safety != ref_val["SAFETY"]:
        print("Correct Safety: ", ref_val["SAFETY"], " ", "Safety calc.:", safety)
        
    #  Get T and p at critical point
    Tc, pc = rp.get_crit_point()
    if (Tc - ref_val["Tc"]) >= tol:
        print("Tc: Difference:", (Tc - ref_val["Tc"]))
    if (pc - ref_val["pc"]) >= tol:
        print("pc: Difference:", (pc - ref_val["pc"]))
    
    # Get Molar mass
    M = rp.get_molar_mass()
    if (M - ref_val["M"]) >= tol:
        print("M: Difference:", (M - ref_val["M"]))

    # Molar and mass fractions
    xi = rp.get_mol_fraction()
    yi = rp.get_mass_fraction()
    for i in range(0, len(xi)):
        if (xi[i] - ref_val["Mol_fraction"][i]) >= tol:
            print("Mol_fraction difference: Anteil:", i, " ", (xi[i] - ref_val["Mol_fraction"][i]))
        if (yi[i] - ref_val["Mass_fraction"][i]) >= tol:
            print("Mass_fraction difference: Anteil:", i, " ", (yi[i] - ref_val["Mass_fraction"][i]))


# ======================================================================================================================
#                                                    Main
# ======================================================================================================================
if __name__ == "__main__":
    
    run_test()
    
    # # Fluid
    # curr_fluid = "CO2"
    # # # Create instance of RefProp
    # refProp = RefProp(curr_fluid)
    # Ttr, ptr = refProp.get_triple_point()
    # print(Ttr, ptr)
