# -*- coding: utf-8 -*-
"""
Created on 19.05.2021

@author: Christoph Hoeges

Check experimental data and calculate isentropic compressor efficiency based on measurement data
"""
# ======================================================================================================================
#                                                     Imports
# ======================================================================================================================
import rp_wrapper as rpw
import numpy as np
# ======================================================================================================================
#                                                 Measurement data
# ======================================================================================================================
T_COMP_IN = np.array([16.4461, 20.6561, 24.7134, 10.3855, 16.0353, 20.7017]) + 273.15
T_COMP_OUT = np.array([64.4243, 68.3523, 75.4022, 59.5904, 72.8462, 83.0043]) + 273.15
P_COMP_IN = np.array([6.9134, 8.0241, 9.0385, 6.0348, 7.0645, 8.0152]) * 1e5
P_COMP_OUT = np.array([21.0084, 24.1164, 27.0672, 20.8497, 24.518, 28.0231]) * 1e5

# ======================================================================================================================
#                                                       Main
# ======================================================================================================================
if __name__ == "__main__":
    # Fluid name
    fluid_name = "R454C.MIX"
    # Create REFPROP instance
    rp = rpw.RefProp(fluid_name=fluid_name)
    states_in = []
    states_out = []
    states_s = []
    eta_s_arr = []
    # Loop
    for T_in, T_out, p_in, p_out in zip(T_COMP_IN, T_COMP_OUT, P_COMP_IN, P_COMP_OUT):
        state1 = rp.calc_state("PT", p_in, T_in)
        states_in.append(state1)
        state2 = rp.calc_state("PT", p_out, T_out)
        states_out.append(state2)

        # Calculate compressor efficiency
        state2_s = rp.calc_state("PS", state2.p, state1.s)
        states_s.append(state2_s)
        eta_s = (state2_s.h-state1.h) / (state2.h - state1.h)
        eta_s_arr.append(eta_s)
    print("Efficiencies:", eta_s_arr)
