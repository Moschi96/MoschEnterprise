# -*- coding: utf-8 -*-
"""
Created on 

@author: Christoph Hoeges
"""
# ======================================================================================================================
#                                                     Imports
# ======================================================================================================================


# ======================================================================================================================
#                                                     Settings
# ======================================================================================================================


# ======================================================================================================================
#                                                       Main
# ======================================================================================================================
import os
from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary
if __name__ == "__main__":
    cwd = os.getcwd()
    root = os.environ["RPPREFIX"]
    RP = REFPROPFunctionLibrary(cwd+r"\\REFPRP64.DLL")
    RP.SETPATHdll(root)
    MOLAR_BASE_SI = RP.GETENUMdll(0, "MOLAR BASE SI").iEnum
    print("Version:", RP.RPVersion())
    mix = 'R407C.MIX'
    sm = RP.SETMIXdll(mix, 'HMX.BNC', 'DEF')
    RP.SETREFdll('DEF', 2, sm.z, 0, 0, 0, 0)
    # Define values, use SI-Units - one state
    T = 267.15
    P = 371450
    D = 15.964
    u = 383270
    h = 406530
    s = 1784
    Q = 1.0

    rpdll = RP.REFPROPdll(mix, "QT", "H;S;M", MOLAR_BASE_SI, 0, 0, Q, T, sm.z)
    Hmolar, Smolar, M = rpdll.Output[0:3]
    print("REFPROPdll", Hmolar / M, Smolar / M)

    tqflsh = RP.TQFLSHdll(T, Q, sm.z, 0)
    print("TQFLSHdll", tqflsh.h / M, tqflsh.s / M)

    abflsh_molar = RP.ABFLSHdll("TQ", T, Q, sm.z, 0)
    print("ABFLSHdll molar", abflsh_molar.h/M, abflsh_molar.s/M)
    abflsh_mass = RP.ABFLSHdll("TQ", T, Q, sm.z, 1)
    print("ABFLSHdll mass", abflsh_mass.h*1000, abflsh_mass.s*1000)

    print("RefProp GUI", h, s)
