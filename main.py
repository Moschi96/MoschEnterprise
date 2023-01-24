import pandas as pd
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt
'''Lädt die Daten aus dem Script ein'''
from Data_handling.data_cleaning import clean_R410A_DF
from Calculation.Main_calculation import func_eta_isen_rosk
from Calculation.Main_calculation import func_eta_a
from Calculation.Main_calculation import func_eta_b
from Calculation.Main_calculation import func_split_PI
from Plot.Plot_Loss_KM import Eta_is_Ros_Vergleich_Plot



R410A_Df = clean_R410A_DF()

''' Verdichter DatenSatz für R410A'''
#print('Das ist der DataFrame R410A_Df', R410A_Df)




'''Reibungsfaktoren zur Bestimmung des Isentropen Wirkungsgrades nach Rosskosch'''
a_fac = 91.59 #W Der Reibungsfaktor für Hubkolben nach Rosskosch
#a_fac = 0


#b_fac = 155.11 * 1000000 #Der Luftwiderstandsfaktor für Hubkolben nach Rosskosch
b_fac = -200 * 1000000

eta_Motor = 0.7

''' Berechnung der Eingangsdichte'''

R410A_Df['rho_1'] = 1/ R410A_Df['v1']

#print(R410A_Df)
'''Berechnung des Isentropen Wirkungsgrad'''
eta_is_Modell , Rosk = func_eta_isen_rosk(R410A_Df['MF_Suc'] / 1000,R410A_Df['h2is'],R410A_Df['h1'],a_fac,b_fac,R410A_Df['rho_1'],eta_Motor, R410A_Df['PI_Set'])


print(Rosk)

h2is = R410A_Df['h2is']
h2 = R410A_Df['h2']
h1 = R410A_Df['h1']

''' Vergleich der Ergebnisse'''
Res = pd.DataFrame()
Res['eta_is'] = R410A_Df['eta_is']
Res['eta_is_Rosko']  = eta_is_Modell
Res['PI_Set'] = R410A_Df['PI_Set']


Res_Pi= func_split_PI(Res)
#print(Res_Pi)
Res_Pi=Res_Pi.transpose()

print(Res)
print(Res_Pi)

#plt.plot(Rosk)
#plt.show()
R410A_Df['eta_is_Rosk']= eta_is_Modell

'''Das ist die Funktion zum Plotten der Ergebnisse'''
etaplt = Eta_is_Ros_Vergleich_Plot(R410A_Df['eta_is'],eta_is_Modell,R410A_Df['PI_Set'],Res_Pi)

corr_Matrix = R410A_Df.corr()
zickzack=corr_Matrix['eta_is_Rosk'].sort_values(ascending=False)
print(zickzack)