# -*- coding: utf-8 -*-
"""
Created on 26.04.2020

@author: Christoph Hoeges
"""
# ======================================================================================================================
#                                                    Imports
# ======================================================================================================================
from rp_wrapper import RefProp


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
    # PT
    state = refProp.calc_state("PT", 4e5, 350)
    print("PT:", "Spec. Enthalpy", state.h)

    # =========================================================
    #             Further tests of additional functions
    # =========================================================
    #  Get T and p at critical point
    Tc, pc, dc = refProp.get_crit_point()
    print("Critical point:", Tc, pc)

    # Component names
    names = refProp.get_comp_names()
    print("Components:", names)
    # Molar and mass fractions
    xi = refProp.get_mol_fraction()
    yi = refProp.get_mass_fraction()
    print("Mol Frac:", xi, "Mass Frac:", yi)
    # Versions
    print("Versions:", refProp.get_version())

    # Definition limits
    def_limts = refProp.get_def_limits()
    print("Limits of definition of material model:", def_limts)

    # Print molar mass
    print("Molar mass:", refProp.get_molar_mass())

    # =========================================================
    #             Check transport properties calculation
    # =========================================================
    state = refProp.calc_state("PT", 1e6, 273.15)
    transp_props = refProp.calc_transp_props(state)
    print("viscosity=", transp_props.dyn_vis)

    # =========================================================
    #             Check triple point
    # =========================================================
    T_trp, p_trp = refProp.get_triple_point()
    print("Triple Point:", "T=", T_trp, "p=", p_trp)
