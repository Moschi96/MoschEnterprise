import pandas as pd
import numpy as np
import sklearn.utils
import xlsxwriter
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from pathlib import Path
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


from sklearn import tree


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
from Data_handling.data_cleaning import clean_R410A_PI42_DF
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
R410A_PI42_Df = clean_R410A_PI42_DF()
R410A_PI45_Df = clean_R410A_PI45_DF()
R410A_PI5_Df = clean_R410A_PI5_DF()
R410A_PI55_Df = clean_R410A_PI55_DF()
R410A_PI6_Df = clean_R410A_PI6_DF()
R410A_PI65_Df = clean_R410A_PI65_DF()

#R410A_PI4_Df = R410A_PI4_Df.append(R410A_PI42_Df)

P_R410A_PI3 = P_R410A_Pi3(R410A_PI3_Df)
P_R410A_PI35 = P_R410A_Pi35(R410A_PI35_Df)
#P_R410A_PI4 = P_R410A_Pi4(R410A_PI4_Df)
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
PI4 = [P_R290_PI4, ]
PI45 = [P_R290_PI45, P_R410A_PI45, P_R454C_PI45]
PI5 = [P_R290_PI5, P_R410A_PI5, P_R454C_PI5]
PI55 = [P_R290_PI55, P_R410A_PI55, P_R454C_PI55]
PI6 = [P_R290_PI6, P_R410A_PI6, P_R454C_PI6]
PI65 = [P_R410A_PI65, P_R454C_PI65]



full_R32 = pd.DataFrame()

temp_R32= pd.DataFrame()
full_PI35 = pd.DataFrame()
temp_R32['P_loss'] = P_R32_PI35['P_loss']
temp_R32['P1_Process'] = P_R32_PI35['P1_Process']
temp_R32['KM']= 1
full_PI35 = full_PI35.append(temp_R32, ignore_index= True)
full_R32 = full_R32.append(temp_R32, ignore_index= True)




temp_R32['P_loss'] = P_R32_PI3['P_loss']
temp_R32['P1_Process'] = P_R32_PI3['P1_Process']
temp_R32['KM']= 1

full_R32 = full_R32.append(temp_R32, ignore_index= True)

temp_R32['P_loss'] = P_R32_PI4['P_loss']
temp_R32['P1_Process'] = P_R32_PI4['P1_Process']
temp_R32['KM']= 1

full_R32 = full_R32.append(temp_R32, ignore_index= True)

temp_R32['P_loss'] = P_R32_PI45['P_loss']
temp_R32['P1_Process'] = P_R32_PI45['P1_Process']
temp_R32['KM']= 1

print(P_R32_PI45, 'Das ist R32 45')

full_R32 = full_R32.append(temp_R32, ignore_index= True)

temp_R32['P_loss'] = P_R32_PI25['P_loss']
temp_R32['P1_Process'] = P_R32_PI25['P1_Process']
temp_R32['KM']= 1

full_R32 = full_R32.append(temp_R32, ignore_index= True)


full_R32.to_excel('Full_R32.xlsx')



full_R290 = pd.DataFrame()






temp_R290= pd.DataFrame()

temp_R290['P_loss'] = P_R290_PI3['P_loss']
temp_R290['P1_Process'] = P_R290_PI3['P1_Process']
temp_R290['KM']= 2
full_R290 = full_R290.append(temp_R290, ignore_index= True)





temp_R290['P_loss'] = P_R290_PI35['P_loss']
temp_R290['P1_Process'] = P_R290_PI35['P1_Process']
temp_R290['KM']= 2
full_PI35 = full_PI35.append(temp_R290, ignore_index= True)
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI4['P_loss']
temp_R290['P1_Process'] = P_R290_PI4['P1_Process']
temp_R290['KM']= 2
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI45['P_loss']
temp_R290['P1_Process'] = P_R290_PI45['P1_Process']
temp_R290['KM']= 2
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI45['P_loss']
temp_R290['P1_Process'] = P_R290_PI45['P1_Process']
temp_R290['KM']= 2
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI5['P_loss']
temp_R290['P1_Process'] = P_R290_PI5['P1_Process']
temp_R290['KM']= 2
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI55['P_loss']
temp_R290['P1_Process'] = P_R290_PI55['P1_Process']
temp_R290['KM']= 2
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI6['P_loss']
temp_R290['P1_Process'] = P_R290_PI6['P1_Process']
temp_R290['KM']= 2
full_R290 = full_R290.append(temp_R290, ignore_index= True)

temp_R290['P_loss'] = P_R290_PI65['P_loss']
temp_R290['P1_Process'] = P_R290_PI65['P1_Process']
temp_R290['KM']= 2
full_R290 = full_R290.append(temp_R290, ignore_index= True)







temp_R410A= pd.DataFrame()
full_R410A = pd.DataFrame()
temp_R410A['P_loss'] = P_R410A_PI3['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI3['P1_Process']
temp_R410A['KM']= 3
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)


temp_R410A['P_loss'] = P_R410A_PI35['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI35['P1_Process']
temp_R410A['KM']= 3
full_PI35 = full_PI35.append(temp_R410A, ignore_index= True)
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)
'''
temp_R410A['P_loss'] = P_R410A_PI4['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI4['P1_Process']
temp_R410A['KM']= 3
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)
'''
temp_R410A['P_loss'] = P_R410A_PI45['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI45['P1_Process']
temp_R410A['KM']= 3
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI5['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI5['P1_Process']
temp_R410A['KM']= 3
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI55['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI55['P1_Process']
temp_R410A['KM']= 3
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI6['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI6['P1_Process']
temp_R410A['KM']= 3
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R410A['P_loss'] = P_R410A_PI65['P_loss']
temp_R410A['P1_Process'] = P_R410A_PI65['P1_Process']
temp_R410A['KM']= 3
full_R410A = full_R410A.append(temp_R410A, ignore_index= True)

temp_R454C= pd.DataFrame()
full_R454C = pd.DataFrame()



temp_R454C['P_loss'] = P_R454C_PI35['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI35['P1_Process']
temp_R454C['KM']= 4
full_PI35 = full_PI35.append(temp_R454C, ignore_index= True)
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)



temp_R454C['P_loss'] = P_R454C_PI45['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI45['P1_Process']
temp_R454C['KM']= 4
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)

temp_R454C['P_loss'] = P_R454C_PI5['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI5['P1_Process']
temp_R454C['KM']= 4
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)

temp_R454C['P_loss'] = P_R454C_PI55['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI55['P1_Process']
temp_R454C['KM']= 4
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)

temp_R454C['P_loss'] = P_R454C_PI6['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI6['P1_Process']
temp_R454C['KM']= 4
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)

temp_R454C['P_loss'] = P_R454C_PI65['P_loss']
temp_R454C['P1_Process'] = P_R454C_PI65['P1_Process']
temp_R454C['KM']= 4
full_R454C = full_R454C.append(temp_R454C, ignore_index= True)
full_R290.to_excel('full_R290.xlsx')
print(full_R290)
full = pd.DataFrame()

full = full.append(full_R32 , ignore_index= True)
full = full.append(full_R290 , ignore_index= True)
full = full.append(full_R410A , ignore_index= True)
full = full.append(full_R454C , ignore_index= True)

full=full.dropna().reset_index(drop=True)

full = sklearn.utils.shuffle(full)
full.to_excel('Full.xlsx')
Xtemp = pd.DataFrame() #Xen soll X_Test und X_Train zusammenstellen.
Ytemp = pd.DataFrame()
Xtemp['P_loss'] = full['P_loss']
Xtemp['P1_Process'] = full['P1_Process']
Ytemp['KM'] = full['KM']




X = Xtemp
Y = Ytemp
#X_Train_PI35, X_Test_PI35 ,Y_Train_PI35,Y_Test_PI35 = X_PI35[:9000], X_PI35[9000:], Y_PI35[:9000], Y_PI35[9000:]

X_Train, X_Test,Y_Train,Y_Test = X[:40000], X[40000:], Y[:40000], Y[40000:]

'''
from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier(random_state=42)
x = sgd_clf.fit(X_Train_PI35,Y_Train_1)

print(x)
'''
def Plot_Ploss_PI35(temp_R32, temp_R290, temp_R410A, temp_R454C):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Verlustleistung über den Eingangsdruck bei PI: 3.5 ' , fontdict= font1)
    plt.xlabel('P1_Process [bar]', fontdict= font2)
    plt.ylabel('Verlustleistung [kW]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter(temp_R32['P_loss'], temp_R32['P1_Process'], label='R32', color = 'magenta')
    plt.scatter(temp_R290['P_loss'], temp_R290['P1_Process'], label='R290', color='blue')
    plt.scatter(temp_R410A['P_loss'], temp_R410A['P1_Process'], label='R410A', color='green')
    plt.scatter(temp_R454C['P_loss'], temp_R454C['P1_Process'], label='R454C', color='red')
    plt.legend()
    plt.show()

#Plot_Ploss_PI35(temp_R32, temp_R290, temp_R410A, temp_R454C)
'''
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
bag_clf = BaggingClassifier(
            DecisionTreeClassifier(), n_estimators=500,
            max_samples=100, bootstrap=True, n_jobs=-1
        )
bag_clf.fit(X_Train_PI35, Y_Train_PI35)
y_pred = bag_clf.predict(X_Train_PI35)
print(y_pred)


bag_clf = BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=500,
    max_samples=100,
    bootstrap=True,
    n_jobs=-1,
    oob_score=True
)
bag_clf.fit(X_Train_PI35, Y_Train_PI35)
print(bag_clf.oob_score_)

from sklearn.metrics import accuracy_score
y_pred = bag_clf.predict(X_Train_PI35)
accuracy = accuracy_score(Y_Train_PI35, y_pred)
print(accuracy)
'''

'''
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

rnd_clf = RandomForestClassifier(
    n_estimators=500,
    max_leaf_nodes=16,
    n_jobs=-1
)
print(X_Test_PI35)
rnd_clf.fit(X_Train_PI35, Y_Train_PI35)
y_pred = rnd_clf.predict(X_Test_PI35)
print(y_pred)
accuracy = accuracy_score(Y_Test_PI35, y_pred)
print(f'Accuracy of Random Forest: {accuracy*100}%')

print(rnd_clf.classes_)
'''
feature_cols = ['P_loss', 'P1_Process']
class_names = ['1','2','3','4']

# Create Decision Tree classifer object
clf = DecisionTreeClassifier(max_depth= 20, random_state=0)

# Train Decision Tree Classifer
clf = clf.fit(X_Train,Y_Train)

#Predict the response for test dataset
y_pred = clf.predict(X_Test)
print("Accuracy:",metrics.accuracy_score(Y_Test, y_pred))
tree.plot_tree(clf)
fig = plt.figure(figsize=(500,500))
_ = tree.plot_tree(clf,
                   feature_names=feature_cols,
                   class_names=class_names,
                   filled=True)
fig.savefig("decistion_tree.png")

print('Process finesh')