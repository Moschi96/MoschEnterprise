import pandas as pd
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt
'''Lädt die bereinigten Kältemitteldaten aus dem Script ein'''
from Data_handling.data_cleaning import clean_R410A_DF
from Data_handling.data_cleaning import clean_R32_DF
from Data_handling.data_cleaning import clean_R290_DF
from Data_handling.data_cleaning import clean_R454C_DF

from Calculation.Main_calculation import KM_Mean_Dif

'''Die Datenframes in abhängigkeit der jewailigen Kältemittel'''
R410A_Df = clean_R410A_DF()
R32_Df = clean_R32_DF()
R290_Df = clean_R290_DF()
R454C_Df = clean_R454C_DF()

'''Jetzt gucken wir mal ob der Bumms auch funktioniert'''


R32_Df_Mean,R32_Df_Dif  = KM_Mean_Dif(R32_Df)
R290_Df_Mean,R290_Df_Dif  = KM_Mean_Dif(R290_Df)
R410A_Df_Mean,R410A_Df_Dif  = KM_Mean_Dif(R410A_Df)
R454C_Df_Mean,R454C_Df_Dif  = KM_Mean_Dif(R454C_Df)

print(R32_Df_Dif)

R32_Df_Dif=R32_Df_Dif.transpose()
R290_Df_Dif=R290_Df_Dif.transpose()

R410A_Df_Dif=R410A_Df_Dif.transpose()
R454C_Df_Dif = R454C_Df_Dif.transpose()
#print(R454C_Df_Dif.loc['Dif_eta_is'])
#print(R32_Df_Dif['Dif_eta_is'])
R32_Df_Dif.mask(R32_Df_Dif.eq('None')).dropna()


with pd.ExcelWriter('Kältemittel.xlsx',engine= 'xlsxwriter') as writer:
    R410A_Df.to_excel(writer, sheet_name='R410A')
    R454C_Df.to_excel(writer, sheet_name='R454C')
    R32_Df.to_excel(writer, sheet_name='R32')
    R290_Df.to_excel(writer, sheet_name='R290')


print(R32_Df_Dif)

'''
fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
#Festlegen der Achsenbeschriftung
font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'black','size':10}
plt.title('Isentroper Wikrungsgrad der KM über das DruckVerhältnis' , fontdict= font1)
plt.xlabel('PI = p2/p1', fontdict= font2)
plt.ylabel('Isentroper Wirkungsgrad', fontdict=font2)
plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

plt.scatter(R32_Df['PI_Set'],R32_Df['eta_is'], label = 'R32')
plt.scatter(R290_Df['PI_Set'],R290_Df['eta_is'], label = 'R290')
plt.scatter(R410A_Df['PI_Set'], R410A_Df['eta_is'], label= 'R410A')
plt.scatter(R454C_Df['PI_Set'], R454C_Df['eta_is'], label = 'R454C')
plt.legend()
plt.show()

'''

'''
fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
#Festlegen der Achsenbeschriftung
font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'black','size':10}
plt.title('Isentroper Wikrungsgrad der KM über das DruckVerhältnis' , fontdict= font1)
plt.xlabel('PI = p2/p1', fontdict= font2)
plt.ylabel('Isentroper Wirkungsgrad', fontdict=font2)
plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

plt.scatter(R32_Df['PI_Set'],R32_Df_Dif['Dif_eta_is'], label = 'R32')

plt.legend()
plt.show()
'''



