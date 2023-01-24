import pandas as pd
import numpy as np
import sklearn.utils
import xlsxwriter
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from pathlib import Path
import matplotlib.pyplot as plt

# Get Data from excel File
dataFolder = Path(__file__).resolve().parent # Absoluter Pfad zum Ordner dieser Datei, findet ihn automatisch heraus
import sys; sys.path.append(str(dataFolder.parent)) # Füge Ordner zur Laufzeitumgebung damit die selbst erstellte Module gefunden werden

print(dataFolder)
''' Diese Datei lädt die Quasistätionären Data in abhängigkeit von dem Verdichtungsverhältnis ein und berechnet damit die Ploss nach Roskosch. '''


'''Lädt die  Input Daten aus dem Script ein'''


from Data_handling.data_cleaning import clean_R32_PI25_DF
from Data_handling.data_cleaning import clean_R32_PI3_DF
from Data_handling.data_cleaning import clean_R32_PI35_DF
from Data_handling.data_cleaning import clean_R32_PI4_DF
from Data_handling.data_cleaning import clean_R32_PI45_DF

'''Lädt die Berechnungen in das Script'''

from Calculation.Ploss_calculation import P_R32_Pi25
from Calculation.Ploss_calculation import P_R32_Pi3
from Calculation.Ploss_calculation import P_R32_Pi35
from Calculation.Ploss_calculation import P_R32_Pi4
from Calculation.Ploss_calculation import P_R32_Pi45


R32_PI25_Df = clean_R32_PI25_DF()
R32_PI3_Df =  clean_R32_PI3_DF()
R32_PI35_Df = clean_R32_PI35_DF()
R32_PI4_Df = clean_R32_PI4_DF()
R32_PI45_Df = clean_R32_PI45_DF()

P_R32_PI25 = P_R32_Pi25(R32_PI25_Df)
P_R32_PI3 = P_R32_Pi3(R32_PI3_Df)
P_R32_PI35 = P_R32_Pi35(R32_PI35_Df)
P_R32_PI4 = P_R32_Pi4(R32_PI4_Df)
P_R32_PI45 = P_R32_Pi45(R32_PI45_Df)
#print(R32_PI45_Df)

#print(P_R32_PI45, ' Das ist P_R32')



from Data_handling.data_cleaning import clean_R290_PI25_DF
from Data_handling.data_cleaning import clean_R290_PI3_DF
from Data_handling.data_cleaning import clean_R290_PI35_DF
from Data_handling.data_cleaning import clean_R290_PI4_DF
from Data_handling.data_cleaning import clean_R290_PI45_DF
from Data_handling.data_cleaning import clean_R290_PI5_DF
from Data_handling.data_cleaning import clean_R290_PI55_DF
from Data_handling.data_cleaning import clean_R290_PI6_DF
from Data_handling.data_cleaning import clean_R290_PI65_DF



from Calculation.Ploss_calculation import P_R290_Pi25
from Calculation.Ploss_calculation import P_R290_Pi3
from Calculation.Ploss_calculation import P_R290_Pi35
from Calculation.Ploss_calculation import P_R290_Pi4
from Calculation.Ploss_calculation import P_R290_Pi45
from Calculation.Ploss_calculation import P_R290_Pi5
from Calculation.Ploss_calculation import P_R290_Pi55
from Calculation.Ploss_calculation import P_R290_Pi6
from Calculation.Ploss_calculation import P_R290_Pi65

R290_PI25_Df = clean_R290_PI25_DF()
R290_PI3_Df = clean_R290_PI3_DF()
R290_PI35_Df = clean_R290_PI35_DF()
R290_PI4_Df = clean_R290_PI4_DF()
R290_PI45_Df = clean_R290_PI45_DF()
R290_PI5_Df = clean_R290_PI5_DF()
R290_PI55_Df = clean_R290_PI55_DF()
R290_PI6_Df = clean_R290_PI6_DF()
R290_PI65_Df = clean_R290_PI65_DF()


P_R290_PI25 = P_R290_Pi25(R290_PI25_Df)
P_R290_PI3 = P_R290_Pi3(R290_PI3_Df)
P_R290_PI35 = P_R290_Pi35(R290_PI35_Df)
P_R290_PI4 = P_R290_Pi4(R290_PI4_Df)
P_R290_PI45 = P_R290_Pi45(R290_PI45_Df)
P_R290_PI5 = P_R290_Pi5(R290_PI5_Df)
P_R290_PI55 = P_R290_Pi55(R290_PI55_Df)
P_R290_PI6 = P_R290_Pi6(R290_PI6_Df)
P_R290_PI65 = P_R290_Pi65(R290_PI65_Df)


from Data_handling.data_cleaning import clean_R410A_PI3_DF
from Data_handling.data_cleaning import clean_R410A_PI35_DF
from Data_handling.data_cleaning import clean_R410A_PI4_DF
from Data_handling.data_cleaning import clean_R410A_PI45_DF
from Data_handling.data_cleaning import clean_R410A_PI5_DF
from Data_handling.data_cleaning import clean_R410A_PI55_DF
from Data_handling.data_cleaning import clean_R410A_PI6_DF
from Data_handling.data_cleaning import clean_R410A_PI65_DF



from Calculation.Ploss_calculation import P_R410A_Pi3
from Calculation.Ploss_calculation import P_R410A_Pi35
from Calculation.Ploss_calculation import P_R410A_Pi4
from Calculation.Ploss_calculation import P_R410A_Pi45
from Calculation.Ploss_calculation import P_R410A_Pi5
from Calculation.Ploss_calculation import P_R410A_Pi55
from Calculation.Ploss_calculation import P_R410A_Pi6
from Calculation.Ploss_calculation import P_R410A_Pi65




R410A_PI3_Df = clean_R410A_PI3_DF()
R410A_PI35_Df = clean_R410A_PI35_DF()
R410A_PI4_Df = clean_R410A_PI4_DF()
R410A_PI45_Df = clean_R410A_PI45_DF()
R410A_PI5_Df = clean_R410A_PI5_DF()
R410A_PI55_Df = clean_R410A_PI55_DF()
R410A_PI6_Df = clean_R410A_PI6_DF()
R410A_PI65_Df = clean_R410A_PI65_DF()



P_R410A_PI3 = P_R410A_Pi3(R410A_PI3_Df)
P_R410A_PI35 = P_R410A_Pi35(R410A_PI35_Df)
P_R410A_PI4 = P_R410A_Pi4(R410A_PI4_Df)
P_R410A_PI45 = P_R410A_Pi45(R410A_PI45_Df)
P_R410A_PI5 = P_R410A_Pi5(R410A_PI5_Df)
P_R410A_PI55 = P_R410A_Pi55(R410A_PI55_Df)
P_R410A_PI6 = P_R410A_Pi6(R410A_PI6_Df)
P_R410A_PI65 = P_R410A_Pi65(R410A_PI65_Df)


from Data_handling.data_cleaning import clean_R454C_PI35_DF
from Data_handling.data_cleaning import clean_R454C_PI45_DF
from Data_handling.data_cleaning import clean_R454C_PI5_DF
from Data_handling.data_cleaning import clean_R454C_PI55_DF
from Data_handling.data_cleaning import clean_R454C_PI6_DF
from Data_handling.data_cleaning import clean_R454C_PI65_DF

from Calculation.Ploss_calculation import P_R454C_Pi35

from Calculation.Ploss_calculation import P_R454C_Pi45
from Calculation.Ploss_calculation import P_R454C_Pi5
from Calculation.Ploss_calculation import P_R454C_Pi55
from Calculation.Ploss_calculation import P_R454C_Pi6
from Calculation.Ploss_calculation import P_R454C_Pi65

R454C_PI35_Df = clean_R454C_PI35_DF()
R454C_PI45_Df = clean_R454C_PI45_DF()
R454C_PI5_Df = clean_R454C_PI5_DF()
R454C_PI55_Df = clean_R454C_PI55_DF()
R454C_PI6_Df = clean_R454C_PI6_DF()
R454C_PI65_Df = clean_R454C_PI65_DF()



P_R454C_PI35 = P_R454C_Pi35(R454C_PI35_Df)
P_R454C_PI45 = P_R454C_Pi45(R454C_PI45_Df)
P_R454C_PI5 = P_R454C_Pi5(R454C_PI5_Df)
P_R454C_PI55 = P_R454C_Pi55(R454C_PI55_Df)
P_R454C_PI6 = P_R454C_Pi6(R454C_PI6_Df)
P_R454C_PI65 = P_R454C_Pi65(R454C_PI65_Df)

PI3= [P_R32_PI3, P_R290_PI3, P_R410A_PI3]
PI35 = [P_R32_PI35, P_R290_PI35, P_R410A_PI35, P_R454C_PI35]
PI4 = [P_R290_PI4, P_R410A_PI4]
PI45 = [P_R290_PI45, P_R410A_PI45, P_R454C_PI45]
PI5 = [P_R290_PI5, P_R410A_PI5, P_R454C_PI5]
PI55 = [P_R290_PI55, P_R410A_PI55, P_R454C_PI55]
PI6 = [P_R290_PI6, P_R410A_PI6, P_R454C_PI6]
PI65 = [P_R410A_PI65, P_R454C_PI65]

print(len(PI35))
temp_R32= pd.DataFrame()
full_PI35 = pd.DataFrame()
temp_R32['P_loss'] = P_R32_PI35['P_loss']
temp_R32['P1_Process'] = P_R32_PI35['P1_Process']
temp_R32['KM']= 1

full_PI35 = full_PI35.append(temp_R32, ignore_index= True)

temp_R290= pd.DataFrame()

temp_R290['P_loss'] = P_R290_PI35['P_loss']
temp_R290['P1_Process'] = P_R290_PI35['P1_Process']
temp_R290['KM']= 2
full_PI35 = full_PI35.append(temp_R290, ignore_index= True)

temp_R410A= pd.DataFrame()

temp_R410A['P_loss'] = P_R410A_PI35['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI35['P1_Process']
temp_R410A['KM']= 3
full_PI35 = full_PI35.append(temp_R410A, ignore_index= True)

temp_R454C= pd.DataFrame()

temp_R454C['P_loss'] = P_R454C_PI35['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI35['P1_Process']
temp_R454C['KM']= 4
full_PI35 = full_PI35.append(temp_R454C, ignore_index= True)

print(full_PI35)


full_PI35 = sklearn.utils.shuffle(full_PI35)

Xtemp = pd.DataFrame() #Xen soll X_Test und X_Train zusammenstellen.
Ytemp = pd.DataFrame()
Xtemp['P_loss'] = full_PI35['P_loss']
Xtemp['P1_Process'] = full_PI35['P1_Process']
Ytemp['KM'] = full_PI35['KM']




X_PI35 = Xtemp
Y_PI35 = Ytemp
X_Train_PI35, X_Test_PI35 ,Y_Train_PI35,Y_Test_PI35 = X_PI35[:9000], X_PI35[9000:], Y_PI35[:9000], Y_PI35[9000:]

print(X_Train_PI35, Y_Train_PI35)

Y_Train_1 = (Y_Train_PI35==1)
Y_Test_1 = (Y_Test_PI35==1)

'''
from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier(random_state=42)
x = sgd_clf.fit(X_Train_PI35,Y_Train_1)

print(x)
'''
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(X_Train_PI35, Y_Train_PI35)

P_loss_predictions = tree_reg.predict(X_Train_PI35['P_loss'])
tree_mse = mean_squared_error(Y_Train_PI35, X_Train_PI35['P_Loss']) >>>
tree_rmse = np.sqrt(tree_mse)
>>> tree_rmse
0.0
from sklearn.model_selection import cross_val_score
scores = cross_val_score(tree_reg, housing_prepared, housing_labels,
                             scoring="neg_mean_squared_error", cv=10)
    rmse_scores = np.sqrt(-scores)