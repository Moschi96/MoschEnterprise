# -*- coding: utf-8 -*-
"""
Created on 26.04.2020

@author: Christoph Hoeges
"""
# ======================================================================================================================
#                                                    Imports
# ======================================================================================================================
from rp_wrapper import RefProp
import os
# ======================================================================================================================
#                                                    Main
# ======================================================================================================================
if __name__ == "__main__":
    # Fluid
    curr_fluid = "R32"
    # Create instance of RefProp
    refProp = RefProp(curr_fluid)

    # =========================================================
    #               Test calc_state possibilities
    # =========================================================
    # PD
    state = refProp.calc_state("PD", 4e5, 15)
    print("PD:", "Temperature", state.T)
    # PH
    state = refProp.calc_state("PH", 4e5, 500e3)
    print("PH:", "Pressure", state.T)
    # PQ
    state1 = refProp.calc_state("PQ", 4e5, 1)
    print("PQ:", "Temperature", state1.T)
    # PS
    state = refProp.calc_state("PS", 4e5, 2e3)
    print("PS:", "Temperature", state.T)
    # PT
    state = refProp.calc_state("PT", 4e5, 350)
    print("PT:", "Spec. Enthalpy", state.h)
    # PU
    state = refProp.calc_state("PU", 4e5, 300e3)
    print("PU:", "Temperature", state.T)
    # TD
    state = refProp.calc_state("TD", 270, 15)
    print("TD:", "Pressure", state.p)
    # TH
    state = refProp.calc_state("TH", 280, 300e3)
    print("TH:", "Pressure", state.p)
    # TQ
    state = refProp.calc_state("TQ", 253.15, 1)
    print("TQ:", "Pressure", state.p)
    # TS
    state = refProp.calc_state("TS", 253.15, 2e3)
    print("TS:", "Pressure", state.p)
    # TU
    state = refProp.calc_state("TU", 280.15, 300e3)
    print("TU:", "Pressure", state.p)
    # DH
    state = refProp.calc_state("DH", 28, 300e3)
    print("DH:", "Pressure", state.p)
    # DS
    state = refProp.calc_state("DS", 15, 2e3)
    print("DS:", "Pressure", state.p)
    # DU
    state = refProp.calc_state("DU", 28, 300e3)
    print("DU:", "Pressure", state.p)

    # =========================================================
    #             Further tests of additional functions
    # =========================================================
    # Get values
    gwp = refProp.get_gwp()
    print("GWP:", gwp)
    # Get ODP
    odp = refProp.get_odp()
    print("ODP:", odp)
    # Get safety class
    safety = refProp.get_safety()
    print("Safety class:", safety)
    #  Get T and p at critical point
    Tc, pc = refProp.get_crit_point()
    print("Critical point:", Tc, pc)

    # =========================================================
    #             Further tests of additional functions
    # =========================================================
    # Component names
    names = refProp.get_comp_names()
    print("Components:", names)
    # Molar and mass fractions
    xi = refProp.get_mol_fraction()
    yi = refProp.get_mass_fraction()
    print("Mol Frac:", xi, "Mass Frac:", yi)
    # Versions
    print("Versions:", refProp.get_version())

    # =========================================================
    #             Check whether fluids are available
    # =========================================================
    names = refProp.get_available_substances(save_txt=True)
    print(names)

    # Definition limits
    def_limts = refProp.get_def_limits()
    print(def_limts)

    # Print molar mass
    print("Molar mass:", refProp.M)

    # =========================================================
    #             Check transport properties calculation
    # =========================================================
    state = refProp.calc_state("PT", 1e6, 273.15)
    transp_props = refProp.calc_transp_props(state)
    print("Thermal conductivity:", transp_props.lam)
    print("Pr=", transp_props.Pr)
    print("eta=", transp_props.dyn_vis)
    print("muh=", transp_props.kin_vis)
    print("cp=", transp_props.cp)
    print("cv=", transp_props.cv)
    print("beta=", transp_props.beta)

    # =========================================================
    #             Check triple point
    # =========================================================
    T_trp, p_trp = refProp.get_triple_point()
    print("Triple Point:", "T=", T_trp, "p=", p_trp)
