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
    fluid = 'PROPYNE'
    sm = RP.SETFLUIDSdll(fluid)
    z = [1]
    T = 263.15
    rpdll = RP.REFPROPdll("", "TQ", "M;D;E;P;H;S", MOLAR_BASE_SI, 0, 0, T, 0.5, z)
    print("\n", rpdll.Output[0:4], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)
    M = rpdll.Output[0]
    # Calculate enthalpy by hand and compare to given h
    u = rpdll.Output[2]
    p = rpdll.Output[3]
    d = rpdll.Output[1]
    h = u + p / d
    s = rpdll.Output[5]
    print("\nDifference:", rpdll.Output[4] - h)
    rpdll = RP.REFPROPdll("", "DE", "M;H;P", MOLAR_BASE_SI, 0, 0, rpdll.Output[1], rpdll.Output[2], z)
    print("\n", rpdll.Output[0:4], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)

    rpdll = RP.REFPROPdll("", "DH", "M;D;E;P", MOLAR_BASE_SI, 0, 0, d, h, z)
    print("\n", rpdll.Output[0:4], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)

    rpdll = RP.REFPROPdll("", "DS", "M;D;E;P", MOLAR_BASE_SI, 0, 0, d, s, z)
    print("\n", rpdll.Output[0:4], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)

    rpdll = RP.REFPROPdll("", "HS", "M;D;E;P", MOLAR_BASE_SI, 0, 0, h, s, z)
    print("\n", rpdll.Output[0:4], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)

    rpdll = RP.REFPROPdll("", "TD", "M;D;E;P", MOLAR_BASE_SI, 0, 0, T, d, z)
    print("\n", rpdll.Output[0:4], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)

    # Testing operation point
    rpdll = RP.REFPROPdll("", "PH", "T", MOLAR_BASE_SI, 0, 0, 2.499e5, 260.382e3 * M, z)
    print("\n", rpdll.Output[0:4], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)