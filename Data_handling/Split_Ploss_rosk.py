import pandas as pd
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

''' Diese Datei lädt die Mean Data ein und berechnet damit die Ploss nach Roskosch. '''


'''Lädt die  Input Daten aus dem Script ein'''
from Data_handling.data_cleaning import clean_R410A_DF
from Data_handling.data_cleaning import clean_R32_DF
from Data_handling.data_cleaning import clean_R290_DF
from Data_handling.data_cleaning import clean_R454C_DF


from Data_handling.data_cleaning import clean_R32_PI25_DF



'''Lädt die Berechnungen in das Script'''

from Calculation.Ploss_calculation import P_R410A
from Calculation.Ploss_calculation import P_R32
from Calculation.Ploss_calculation import P_R290
from Calculation.Ploss_calculation import P_R454C
from Calculation.Ploss_calculation import P_R32_Pi25

'''Lädt die Grafik Funktionen in das Script ein'''
from Plot.Plot_Loss_KM import Power_Loss_R410A_Plot_PI
from Plot.Plot_Loss_KM import Power_Loss_R32_Plot_PI
from Plot.Plot_Loss_KM import Power_Loss_R290_Plot_PI
from Plot.Plot_Loss_KM import Power_Loss_R454C_Plot_PI




from Plot.Plot_Loss_KM import Power_Loss_Plot_PI5
from Plot.Plot_Loss_KM import Power_Loss_Plot_PI45
from Plot.Plot_Loss_KM import Power_Loss_Plot_PI4

from Calculation.Main_calculation import func_Pistest




R410A_Df = clean_R410A_DF()

R32_Df = clean_R32_DF()
R290_Df = clean_R290_DF()
R454C_Df = clean_R454C_DF()



R32_PI25_Df = clean_R32_PI25_DF()
print(R32_PI25_Df)

#Pistest_R410A = func_Pistest(R410A_Df['h1'], R410A_Df['h2is'], R410A_Df['h2'], R410A_Df['MF_Suc'], R410A_Df['Power'])







#print(Pistest_R410A)


P_R410A, P_R410A_pi3,P_R410A_pi35,P_R410A_pi4,P_R410A_pi45,P_R410A_pi5, P_R410A_pi55, P_R410A_pi6, P_R410A_pi65  = P_R410A(R410A_Df)
P_R32_pi25, P_R32_pi3, P_R32_pi35, P_R32_pi4, P_R32_pi45, P_R32_pi5 = P_R32(R32_Df)
P_R290_pi25,P_R290_pi3, P_R290_pi35, P_R290_pi4, P_R290_pi45, P_R290_pi5, P_R290_pi55, P_R290_pi6, P_R290_pi65 = P_R290(R290_Df)
P_R454C_pi45, P_R454C_pi5, P_R454C_pi55,P_R454C_pi6,P_R454C_pi65 = P_R454C(R454C_Df)


'''Die Leistungsverluste pro Kältemittel in Abhängigkeit vom Eingangsdruck'''
Power_Loss_R410A_Plot_PI(P_R410A_pi3, P_R410A_pi35,P_R410A_pi4,P_R410A_pi45,P_R410A_pi5, P_R410A_pi55, P_R410A_pi6, P_R410A_pi65 )
Power_Loss_R32_Plot_PI(P_R32_pi25, P_R32_pi3, P_R32_pi35, P_R32_pi4, P_R32_pi45, P_R32_pi5)
Power_Loss_R290_Plot_PI(P_R290_pi25,P_R290_pi3, P_R290_pi35, P_R290_pi4, P_R290_pi45, P_R290_pi5, P_R290_pi55, P_R290_pi6, P_R290_pi65)
Power_Loss_R454C_Plot_PI(P_R454C_pi45, P_R454C_pi5, P_R454C_pi55,P_R454C_pi6,P_R454C_pi65)

Power_Loss_Plot_PI5(P_R410A_pi5, P_R32_pi5, P_R290_pi5,P_R454C_pi5)
Power_Loss_Plot_PI45(P_R410A_pi45, P_R32_pi45, P_R290_pi45,P_R454C_pi45)
Power_Loss_Plot_PI4(P_R410A_pi4, P_R32_pi4, P_R290_pi4 )

plt.show()

P_R32_PI25 = P_R32_Pi25(R32_PI25_Df)



'''
fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
#Festlegen der Achsenbeschriftung
font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'black','size':10}
plt.title('Powerloss over P1' , fontdict= font1)
plt.xlabel('PI = p2/p1', fontdict= font2)
plt.ylabel('Isentroper Wirkungsgrad', fontdict=font2)
plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

plt.scatter(P_R32_PI25['P1_Process'],P_R32_PI25['P_loss'], label = 'R32_PI25')

plt.legend()
plt.show()
'''




