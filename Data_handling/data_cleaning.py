import pandas as pd

from Data_handling.load_data import getdata_R410A
from Data_handling.load_data import getdata_R32
from Data_handling.load_data import getdata_R290
from Data_handling.load_data import getdata_R454C
from Data_handling.load_data import getdataZHI18K1P


#Übergibt die Werte der Funktionen in eine neue Variabel.

R410A_Df_raw = getdata_R410A()
R32_Df_raw = getdata_R32()
R290_Df_raw = getdata_R290()
R454C_Df_raw = getdata_R454C()
ZHI18K1P_raw = getdataZHI18K1P()


def clean_ZHI18K1P():
    ZHI18K1P_Df = pd.DataFrame()
    ZHI18K1P_Df = ZHI18K1P_raw.transpose()
    #ZHI18K1P_Df = ZHI18K1P_Df
    #print(ZHI18K1P_Df)
    ZHI18K1P_Df.drop([ 'Einheiten', 'Übersicht'] , axis=0 , inplace= True)
    return ZHI18K1P_Df



def clean_R410A_DF():
    'Choose the rows for the data of Interest. I need: P1_Process, P2_Process, T1_Process, T2_Process, T_Amb_Process, Power, MF_Suc, Dens_Suc , h1 , s1, v1,cp1, h2, s2, v2, cp2, tc, PI_Set, T_Evaps, T_Conds '
    R410A_Df= pd.DataFrame()
    R410A_Df['P1_Process'] = R410A_Df_raw['P1_Process']
    R410A_Df['P1_Set'] = R410A_Df_raw['P1_Set']
    R410A_Df['P2_Process'] = R410A_Df_raw['P2_Process']
    R410A_Df['T1_Process'] = R410A_Df_raw['T1_Process']
    R410A_Df['T2_Process'] = R410A_Df_raw['T2_Process']
    R410A_Df['T_Amb_Process'] = R410A_Df_raw['T_Amb_Process']
    R410A_Df['Power'] = R410A_Df_raw['Power']
    R410A_Df['MF_Suc'] = R410A_Df_raw['MF_Suc']
    R410A_Df['Dens_Suc'] = R410A_Df_raw['Dens_Suc']
    R410A_Df['h1'] = R410A_Df_raw['h1']
    R410A_Df['s1'] = R410A_Df_raw['s1']
    R410A_Df['v1'] = R410A_Df_raw['v1']
    R410A_Df['cp1'] = R410A_Df_raw['cp1']
    R410A_Df['h2'] = R410A_Df_raw['h2']
    R410A_Df['h2is'] = R410A_Df_raw['h2is']
    R410A_Df['s2'] = R410A_Df_raw['s2']
    R410A_Df['cp2'] = R410A_Df_raw['cp2']
    R410A_Df['tc'] = R410A_Df_raw['tc']
    R410A_Df['PI_Set'] = R410A_Df_raw['PI_Set']
    R410A_Df['T_Evaps'] = R410A_Df_raw['T_Evaps']
    R410A_Df['T_Conds'] = R410A_Df_raw['T_Conds']
    R410A_Df['eta_is'] = R410A_Df_raw['eta_is']

    return R410A_Df

def clean_R32_DF():
    'Choose the rows for the data of Interest. I need: P1_Process, P2_Process, T1_Process, T2_Process, T_Amb_Process, Power, MF_Suc, Dens_Suc , h1 , s1, v1,cp1, h2, s2, v2, cp2, tc, PI_Set, T_Evaps, T_Conds '
    R32_Df= pd.DataFrame()
    R32_Df['P1_Process'] = R32_Df_raw['P1_Process']
    R32_Df['P1_Set'] = R32_Df_raw['P1_Set']
    R32_Df['P2_Process'] = R32_Df_raw['P2_Process']
    R32_Df['T1_Process'] = R32_Df_raw['T1_Process']
    R32_Df['T2_Process'] = R32_Df_raw['T2_Process']
    R32_Df['T_Amb_Process'] = R32_Df_raw['T_Amb_Process']
    R32_Df['Power'] = R32_Df_raw['Power']
    R32_Df['MF_Suc'] = R32_Df_raw['MF_Suc']
    R32_Df['Dens_Suc'] = R32_Df_raw['Dens_Suc']
    R32_Df['h1'] = R32_Df_raw['h1']
    R32_Df['s1'] = R32_Df_raw['s1']
    R32_Df['v1'] = R32_Df_raw['v1']
    R32_Df['cp1'] = R32_Df_raw['cp1']
    R32_Df['h2'] = R32_Df_raw['h2']
    R32_Df['h2is'] = R32_Df_raw['h2is']
    R32_Df['s2'] = R32_Df_raw['s2']
    R32_Df['cp2'] = R32_Df_raw['cp2']
    R32_Df['tc'] = R32_Df_raw['tc']
    R32_Df['PI_Set'] = R32_Df_raw['PI_Set']
    #R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    #R32_Df['T_Conds'] = R32_Df_raw['T_Conds']
    R32_Df['eta_is'] = R32_Df_raw['eta_is']

    return R32_Df

def clean_R290_DF():
    'Choose the rows for the data of Interest. I need: P1_Process, P2_Process, T1_Process, T2_Process, T_Amb_Process, Power, MF_Suc, Dens_Suc , h1 , s1, v1,cp1, h2, s2, v2, cp2, tc, PI_Set, T_Evaps, T_Conds '
    R290_Df= pd.DataFrame()
    R290_Df['P1_Process'] = R290_Df_raw['P1_Process']
    R290_Df['P1_Set'] = R290_Df_raw['P1_Set']
    R290_Df['P2_Process'] = R290_Df_raw['P2_Process']
    R290_Df['T1_Process'] = R290_Df_raw['T1_Process']
    R290_Df['T2_Process'] = R290_Df_raw['T2_Process']
    R290_Df['T_Amb_Process'] = R290_Df_raw['T_Amb_Process']
    R290_Df['Power'] = R290_Df_raw['Power']
    R290_Df['MF_Suc'] = R290_Df_raw['MF_Suc']
    R290_Df['Dens_Suc'] = R290_Df_raw['Dens_Suc']
    R290_Df['h1'] = R290_Df_raw['h1']
    R290_Df['s1'] = R290_Df_raw['s1']
    R290_Df['v1'] = R290_Df_raw['v1']
    R290_Df['cp1'] = R290_Df_raw['cp1']
    R290_Df['h2'] = R290_Df_raw['h2']
    R290_Df['h2is'] = R290_Df_raw['h2is']
    R290_Df['s2'] = R290_Df_raw['s2']
    R290_Df['cp2'] = R290_Df_raw['cp2']
    R290_Df['tc'] = R290_Df_raw['tc']
    R290_Df['PI_Set'] = R290_Df_raw['PI_Set']
    #R290_Df['T_Evaps'] = R290_Df_raw['T_Evaps']
    #R290_Df['T_Conds'] = R290_Df_raw['T_Conds']
    R290_Df['eta_is'] = R290_Df_raw['eta_is']

    return R290_Df

def clean_R454C_DF():
    'Choose the rows for the data of Interest. I need: P1_Process, P2_Process, T1_Process, T2_Process, T_Amb_Process, Power, MF_Suc, Dens_Suc , h1 , s1, v1,cp1, h2, s2, v2, cp2, tc, PI_Set, T_Evaps, T_Conds '
    R454C_Df= pd.DataFrame()
    R454C_Df['P1_Process'] = R454C_Df_raw['P1_Process']
    R454C_Df['P1_Set'] = R454C_Df_raw['P1_Set']
    R454C_Df['P2_Process'] = R454C_Df_raw['P2_Process']
    R454C_Df['T1_Process'] = R454C_Df_raw['T1_Process']
    R454C_Df['T2_Process'] = R454C_Df_raw['T2_Process']
    R454C_Df['T_Amb_Process'] = R454C_Df_raw['T_Amb_Process']
    R454C_Df['Power'] = R454C_Df_raw['Power']
    R454C_Df['MF_Suc'] = R454C_Df_raw['MF_Suc']
    R454C_Df['Dens_Suc'] = R454C_Df_raw['Dens_Suc']
    R454C_Df['h1'] = R454C_Df_raw['h1']
    R454C_Df['s1'] = R454C_Df_raw['s1']
    R454C_Df['v1'] = R454C_Df_raw['v1']
    R454C_Df['cp1'] = R454C_Df_raw['cp1']
    R454C_Df['h2'] = R454C_Df_raw['h2']
    R454C_Df['h2is'] = R454C_Df_raw['h2is']
    R454C_Df['s2'] = R454C_Df_raw['s2']
    R454C_Df['cp2'] = R454C_Df_raw['cp2']
    R454C_Df['tc'] = R454C_Df_raw['tc']
    R454C_Df['PI_Set'] = R454C_Df_raw['PI_Set']
    #R32_Df['T_Evaps'] = R32_Df_raw['T_Evaps']
    #R32_Df['T_Conds'] = R32_Df_raw['T_Conds']
    R454C_Df['eta_is'] = R454C_Df_raw['eta_is']

    return R454C_Df
