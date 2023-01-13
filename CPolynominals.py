import pandas as pd
import numpy as np
import xlsxwriter
'''Lädt die Daten aus dem Script ein'''
from Data_handling.data_cleaning import clean_ZHI18K1P
from Calculation.Main_calculation import Poly_10C_Calculation
from Data_handling.data_cleaning import clean_R410A_DF

ZHI18K1P_Df = clean_ZHI18K1P()
#print(ZHI18K1P_Df)

R410A_Df = clean_R410A_DF()
R410A_Df_MF = pd.DataFrame()


'''Der folgende Abschnitt ist zum bestimmen des MassFlow'''
R410A_Df_MF['P1_Process'] = R410A_Df['P1_Process']
R410A_Df_MF['P1_Set'] = R410A_Df['P1_Set']
R410A_Df_MF['P2_Process'] = R410A_Df['P2_Process']
R410A_Df_MF['MF_Suc'] = R410A_Df['MF_Suc']
R410A_Df_MF['PI_Set'] = R410A_Df['PI_Set']
R410A_Df_MF['T_Evaps'] = R410A_Df['T_Evaps']
R410A_Df_MF['T_Conds'] = R410A_Df['T_Conds']

C10_Polynome_Cooling_Capayity = ZHI18K1P_Df[0] # 0 ist Cooling Capacity in kW, 1 ist Power in kW, 2 ist Current in A, 3 ist Suction Mass Flow in g/s
C10_Polynome_Power = ZHI18K1P_Df[1] # 0 ist Cooling Capacity in kW, 1 ist Power in kW, 2 ist Current in A, 3 ist Suction Mass Flow in g/s

C10_Polynome_Suction_Massflow = ZHI18K1P_Df[3]

#Massflow = Poly_10C_Calculation(C10_Polynome_Suction_Massflow,3.885481,45.122675)

R410A_Df_MF['C10_MF'] = Poly_10C_Calculation(C10_Polynome_Suction_Massflow,R410A_Df_MF['T_Evaps'],R410A_Df_MF['T_Conds'])
R410A_Df_MF['MF_Verhältnis'] = (( R410A_Df_MF['C10_MF'] / R410A_Df_MF['MF_Suc']) -1 ) *100
'''Die Angabe MF_Verhältnis sind in der Spalte in Prozent angegeben.'''

#print(R410A_Df_MF)
'''Der folgende Abschnitt beschreibt die Bestimmung der Power'''
R410A_Df_POW = pd.DataFrame()

R410A_Df_POW['P1_Process'] = R410A_Df['P1_Process']
R410A_Df_POW['P1_Set'] = R410A_Df['P1_Set']
R410A_Df_POW['P2_Process'] = R410A_Df['P2_Process']
R410A_Df_POW['Power'] = R410A_Df['Power']
R410A_Df_POW['PI_Set'] = R410A_Df['PI_Set']
R410A_Df_POW['T_Evaps'] = R410A_Df['T_Evaps']
R410A_Df_POW['T_Conds'] = R410A_Df['T_Conds']

C10_Polynome_Power = ZHI18K1P_Df[1] # 0ist Cooling Capacity in kW, 1 ist Power in kW, 2 ist Current in A, 3 ist Suction Mass Flow in g/s



#Massflow = Poly_10C_Calculation(C10_Polynome_Suction_Massflow,3.885481,45.122675)

R410A_Df_POW['C10_Power'] = (Poly_10C_Calculation(C10_Polynome_Power,R410A_Df_POW['T_Evaps'],R410A_Df_POW['T_Conds']))*1000
R410A_Df_POW['Power_Verhältnis'] = (( R410A_Df_POW['C10_Power'] / R410A_Df_POW['Power']) -1 ) *100
'''Die Angaben in der Spalte Power_Verhältnis sind in Prozent'''



pub = pd.DataFrame()

pub['P1_Set'] = R410A_Df['P1_Set']
pub['PI_Set'] = R410A_Df['PI_Set']
pub['Power'] = R410A_Df['Power']
pub['C10_Power'] = R410A_Df_POW['C10_Power']
pub['Power_Verhältnis'] = R410A_Df_POW['Power_Verhältnis']
pub['MF_Suc'] = R410A_Df['MF_Suc']
pub['C10_MF'] = R410A_Df_MF['C10_MF']
pub['MF_Verhältnis'] = R410A_Df_MF['MF_Verhältnis']

insert_einheiten = pd.DataFrame({'P1_Set': 'Bar', 'PI_Set': 'p2/p1', 'Power':'Watt', 'C10_Power': 'Watt', 'Power_Verhältnis':'%', 'MF_Suc': 'g/s', 'C10_MF':'g/s', 'MF_Verhältnis':'%'}, index=[0] )




pub = pd.concat([insert_einheiten, pub[:]]).reset_index(drop=True)

#print(pub, 'Das ist Pub')



df_mask = pub['PI_Set'] == 3
pup_pi3=pub[df_mask]


df_mask = pub['PI_Set'] == 3.5
pup_pi35=pub[df_mask]


df_mask = pub['PI_Set'] == 4
pup_pi4=pub[df_mask]


df_mask = pub['PI_Set'] == 4.5
pup_pi45=pub[df_mask]


df_mask = pub['PI_Set'] == 5
pup_pi5=pub[df_mask]


df_mask = pub['PI_Set'] == 5.5
pup_pi55=pub[df_mask]


df_mask = pub['PI_Set'] == 6
pup_pi6=pub[df_mask]


df_mask = pub['PI_Set'] == 6.5
pup_pi65=pub[df_mask]



print('Hier sollten eigentlich auch Werte drinstehen',pup_pi3)





with pd.ExcelWriter('C10_Publicity.xlsx',engine= 'xlsxwriter') as writer:
    pub.to_excel(writer, sheet_name='ResultsData')



