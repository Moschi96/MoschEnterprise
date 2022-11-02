#Modul Importe
from pathlib import Path
import openpyxl
import pandas as pd

import warnings
import os
import glob

# Get Data from excel File
dataFolder = Path(__file__).resolve().parent.parent.parent # Absoluter Pfad zum Ordner dieser Datei, findet ihn automatisch heraus
import sys; sys.path.append(str(dataFolder.parent)) # Füge Ordner zur Laufzeitumgebung damit die selbst erstellte Module gefunden werden

def getdataZHI18K1P():
    #print(os.listdir(dataFolder))
    ZHI18K1P_raw_csv = dataFolder/ '03_Code' / 'Input_Data' /'Data' / 'ZHI18K1P-TFM_10C_R410A.xlsx'
    rawdata_ZHI18K1P = pd.read_excel(ZHI18K1P_raw_csv)
    return rawdata_ZHI18K1P

def getdata_R410A():
    rawdata_R410A_dic = dataFolder/ '03_Code'/'Input_Data'  / 'Data' / 'R410A_erweitert.csv'
    rawdata_R410A = pd.read_csv(rawdata_R410A_dic)
    #print(rawdata_R410A)

    return rawdata_R410A

def getdata_R32():
    rawdata_R32_dic = dataFolder/ '03_Code'/'Input_Data'  / '03_MeanData' / 'R32_MeanData.csv'
    rawdata_R32 = pd.read_csv(rawdata_R32_dic)

    return rawdata_R32

def getdata_R290():
    rawdata_R290_dic = dataFolder/ '03_Code'/'Input_Data'  / '03_MeanData' / 'R290_MeanData.csv'
    rawdata_R290 = pd.read_csv(rawdata_R290_dic)

    return rawdata_R290

def getdata_R454C():
    rawdata_R454C_dic = dataFolder/ '03_Code'/'Input_Data'  / '03_MeanData' / 'R454C_MeanData.csv'
    rawdata_R454C = pd.read_csv(rawdata_R454C_dic)

    return rawdata_R454C

def getdataZHI18K1P_Temp_old():
    #print(os.listdir(dataFolder))
    ZHI18K1P_raw_csv = dataFolder/ '03_Code' / 'Data' / 'ZHI18K1P-TFM_10C_R410A.xlsx'
    rawdata_ZHI18K1P = pd.read_excel(ZHI18K1P_raw_csv)
    coolcap_Cdata = rawdata_ZHI18K1P.iloc[0]
    power_Cdata= rawdata_ZHI18K1P.iloc[1]
    current_Cdata = rawdata_ZHI18K1P.iloc[2]
    sucmassflow_Cdata = rawdata_ZHI18K1P.iloc[3]

    return rawdata_ZHI18K1P, coolcap_Cdata,power_Cdata,current_Cdata,sucmassflow_Cdata
