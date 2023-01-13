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
    mix = 'R407C.mix'
    sm = RP.SETMIXdll(mix, 'HMX.BNC', 'DEF')
    RP.SETREFdll('DEF', 2, sm.z, 0, 0, 0, 0)
    T = 273.15
    P = 512290
    D = 41.745
    U = 294180
    H = 306450
    S = 1392.2
    Q = 0.5
    M = RP.REFPROPdll("", "QT", "M", MOLAR_BASE_SI, 0, 0, Q, T, sm.z).Output[0]
    tqflsh = RP.TQFLSHdll(T, Q, sm.z, 0)
    print("tqflsh", tqflsh.h / M, tqflsh.s / M)
    print(D / M / 1000)
    pdflsh = RP.PDFLSHdll(P / 1000, D / M / 1000, sm.z)
    print("pdflsh", pdflsh.h / M, pdflsh.s / M)
    rpdll = RP.REFPROPdll("", "QT", "H;S;P;D", MOLAR_BASE_SI, 0, 0, Q, T, sm.z)
    print(round(rpdll.Output[0] / M), round(rpdll.Output[1] / M))
    rpdll = RP.REFPROPdll("", "PD", "H;S", MOLAR_BASE_SI, 0, 0, P, D/M, sm.z)
    print(round(rpdll.Output[0] / M), round(rpdll.Output[1] / M))
    print(RP.RPVersion())

    # Test triple point calculation
    rpdll1 = RP.REFPROPdll("", "TRIP", "T", MOLAR_BASE_SI, 0, 0, 0, 0, sm.z)
    print(rpdll1.Output[0])
    rpdll2 = RP.REFPROPdll("", "QT", "TTRP", MOLAR_BASE_SI, 0, 0, 0, 0, sm.z)    # Command for single component
    print(rpdll2.Output[0])
    rpdll3 = RP.REFPROPdll("", "QT", "TR", MOLAR_BASE_SI, 0, 0, 0, 0, sm.z)
    print(rpdll3.Output[0])

    fluids = ["WATER", "CO2", "R134A"]
    for fl in fluids:
        RP.SETFLUIDSdll(fl)
        rpdll1 = RP.REFPROPdll("", "TRIP", "T;P", MOLAR_BASE_SI, 0, 0, 0, 0, [1])
        print(rpdll1.Output[0:2])

    mixtures = ["R410A.MIX"]
    for mix in mixtures:
        sm = RP.SETMIXdll(mix, 'HMX.BNC', 'DEF')
        RP.SETREFdll('DEF', 2, sm.z, 0, 0, 0, 0)
        rpdll1 = RP.REFPROPdll("", "TRIP", "T;P", MOLAR_BASE_SI, 0, 0, 0, 0, sm.z)
        print(rpdll1.Output[0:2])

