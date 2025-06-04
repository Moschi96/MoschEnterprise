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
    sf = RP.SETFLUIDSdll(fluid)
    z = [1]
    T = 263.15
    rpdll = RP.REFPROPdll("", "TQ", "M;D;E;P;H;S", MOLAR_BASE_SI, 0, 0, T, 0.5, z)
    print("\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)
    M = rpdll.Output[0]
    d = rpdll.Output[1]
    print("---------------- First call ----------------")
    # Testing operation point
    rpdll = RP.REFPROPdll("", "PH", "T", MOLAR_BASE_SI, 0, 0, 2.499e5, 260.382e3 * M, z)
    print("\n", rpdll.Output[0], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)

    # Testing operation point
    rpdll = RP.REFPROPdll("", "PH", "T", MOLAR_BASE_SI, 0, 0, 2.499e5, 260.382e3 * M, z)
    print("\n", rpdll.Output[0], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)

    rpdll = RP.REFPROPdll("", "TD", "M;D;E;P", MOLAR_BASE_SI, 0, 0, T, d, z)
    print("\n", rpdll.Output[0:4], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)

    # Testing operation point
    rpdll = RP.REFPROPdll("", "PH", "T", MOLAR_BASE_SI, 0, 0, 2.499e5, 260.382e3 * M, z)
    print("\n", rpdll.Output[0:4], "\nerror code:", rpdll.ierr, "\nerror message:", rpdll.herr)