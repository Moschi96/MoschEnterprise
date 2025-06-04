import matplotlib.pyplot as plt
import pandas as pd
import matplotlib



'''Ist total wichtig wegen Latex
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
'''
def plot_LR_KM_PI(P_KM_PI, LR_KM_PI, name):

    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Linear Regression' + str(name) , fontdict= font1)
    plt.xlabel('P1_Process [MPa]' , fontdict= font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter(P_KM_PI[['P1_Process']],P_KM_PI[['P_loss']], )
    plt.plot(P_KM_PI[['P1_Process']], LR_KM_PI.predict(P_KM_PI[['P1_Process']]), color = 'red')
    plt.legend()
    plt.show()


'''
def plot_LR_R32(P_KM_PI, LR_KM_PI, name):
    
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Linear Regression' + str(name) , fontdict= font1)
    plt.xlabel('P1_Process [MPa]' , fontdict= font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter(P_KM_PI[['P1_Process']],P_KM_PI[['P_loss']], )
    plt.plot(P_KM_PI[['P1_Process']], LR_KM_PI.predict(P_KM_PI[['P1_Process']]), color = 'red')
    plt.legend()
    plt.show()
'''

def plot_LR_R32(P_KM_PI, LR_KM_PI, name):
    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('Linear Regression' + str(name), fontdict=font1)
    plt.xlabel('P1_Process [bar]', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)

    plt.scatter(P_KM_PI[['P1_Process']], P_KM_PI[['P_loss']], )
    plt.plot(P_KM_PI[['P1_Process']], LR_KM_PI.predict(P_KM_PI[['P1_Process']]), color='red')
    plt.legend()



def plot_LR_R32_PI(P_R32_PI25,linP_R32_PI25,P_R32_PI3,linP_R32_PI3,P_R32_PI35,linP_R32_PI35,P_R32_PI4,linP_R32_PI4,P_R32_PI45,linP_R32_PI45):

    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Lineare Regression R32'  , fontdict= font1)
    plt.xlabel('P1_Process [MPa]' , fontdict= font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)


    plt.plot(P_R32_PI25[['P1_Process']], linP_R32_PI25.predict(P_R32_PI25[['P1_Process']]), color = 'green' , label = 'PI 2.5')
    plt.plot(P_R32_PI3[['P1_Process']], linP_R32_PI3.predict(P_R32_PI3[['P1_Process']]), color='lime' , label = 'PI 3')
    plt.plot(P_R32_PI35[['P1_Process']], linP_R32_PI35.predict(P_R32_PI35[['P1_Process']]), color = 'aquamarine' , label = 'PI 3.5')
    #plt.plot(P_R32_PI4[['P1_Process']], linP_R32_PI4.predict(P_R32_PI4[['P1_Process']]), color = 'red')
    #plt.plot(P_R32_PI45[['P1_Process']], linP_R32_PI45.predict(P_R32_PI45[['P1_Process']]), color = 'red')

    plt.legend()
    plt.show()

def plot_LR_R290_PI(P_R290_PI25,linP_R290_PI25, P_R290_PI3,linP_R290_PI3,linP_R290_PI35,P_R290_PI35,P_R290_PI4,linP_R290_PI4,P_R290_PI45,linP_R290_PI45,P_R290_PI5,linP_R290_PI5,P_R290_PI55,linP_R290_PI55,P_R290_PI6,linP_R290_PI6,linP_R290_PI65,P_R290_PI65):

    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Lineare Regression R290'  , fontdict= font1)
    plt.xlabel('P1_Process [MPa]' , fontdict= font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)


    #plt.plot(P_R290_PI25[['P1_Process']], linP_R290_PI25.predict(P_R290_PI25[['P1_Process']]), color = 'red' , label = 'PI 2.5')
    plt.plot(P_R290_PI3[['P1_Process']], linP_R290_PI3.predict(P_R290_PI3[['P1_Process']]), color = 'lime' , label = 'PI 3')
    plt.plot(P_R290_PI35[['P1_Process']], linP_R290_PI35.predict(P_R290_PI35[['P1_Process']]), color = 'aquamarine' , label = 'PI 3.5')
    plt.plot(P_R290_PI4[['P1_Process']], linP_R290_PI4.predict(P_R290_PI4[['P1_Process']]), color='aqua', label='PI 4')
    plt.plot(P_R290_PI45[['P1_Process']], linP_R290_PI45.predict(P_R290_PI45[['P1_Process']]), color = 'teal' , label = 'PI 4.5')
    plt.plot(P_R290_PI5[['P1_Process']], linP_R290_PI5.predict(P_R290_PI5[['P1_Process']]), color = 'dodgerblue' , label = 'PI 5')
    plt.plot(P_R290_PI55[['P1_Process']], linP_R290_PI55.predict(P_R290_PI55[['P1_Process']]), color = 'navy' , label = 'PI 5.5')
    plt.plot(P_R290_PI6[['P1_Process']], linP_R290_PI6.predict(P_R290_PI6[['P1_Process']]), color='blueviolet', label='PI 6')
    #plt.plot(P_R290_PI65[['P1_Process']], linP_R290_PI65.predict(P_R290_PI65[['P1_Process']]), color='red',
             #label='PI 6.5')
    plt.legend()
    plt.show()

def plot_LR_R410A_PI(P_R410A_PI3,linP_R410A_PI3,P_R410A_PI35,linP_R410A_PI35,P_R410A_PI4,linP_R410A_PI4,P_R410A_PI45,linP_R410A_PI45,P_R410A_PI5,linP_R410A_PI5,linP_R410A_PI55,P_R410A_PI55,P_R410A_PI6,linP_R410A_PI6,P_R410A_PI65,linP_R410A_PI65):

    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Lineare Regression R410A'  , fontdict= font1)
    plt.xlabel('P1_Process [MPa]' , fontdict= font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)



    plt.plot(P_R410A_PI3[['P1_Process']], linP_R410A_PI3.predict(P_R410A_PI3[['P1_Process']]), color = 'lime' , label = 'PI 3')
    plt.plot(P_R410A_PI35[['P1_Process']], linP_R410A_PI35.predict(P_R410A_PI35[['P1_Process']]), color = 'aquamarine' , label = 'PI 3.5')
    plt.plot(P_R410A_PI4[['P1_Process']], linP_R410A_PI4.predict(P_R410A_PI4[['P1_Process']]), color='aqua', label='PI 4')
    plt.plot(P_R410A_PI45[['P1_Process']], linP_R410A_PI45.predict(P_R410A_PI45[['P1_Process']]), color = 'teal' , label = 'PI 4.5')
    plt.plot(P_R410A_PI5[['P1_Process']], linP_R410A_PI5.predict(P_R410A_PI5[['P1_Process']]), color = 'dodgerblue' , label = 'PI 5')
    plt.plot(P_R410A_PI55[['P1_Process']], linP_R410A_PI55.predict(P_R410A_PI55[['P1_Process']]), color = 'navy' , label = 'PI 5.5')
    plt.plot(P_R410A_PI6[['P1_Process']], linP_R410A_PI6.predict(P_R410A_PI6[['P1_Process']]), color='blueviolet', label='PI 6')
    plt.plot(P_R410A_PI65[['P1_Process']], linP_R410A_PI65.predict(P_R410A_PI65[['P1_Process']]), color='red',
             label='PI 6.5')
    plt.legend()
    plt.show()

def plot_LR_R454C_PI(P_R454C_PI35,linP_R454C_PI35,P_R454C_PI45,linP_R454C_PI45,P_R454C_PI5,linP_R454C_PI5,P_R454C_PI55,linP_R454C_PI55,P_R454C_PI6,linP_R454C_PI6,P_R454C_PI65,linP_R454C_PI65):

    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('Lineare Regression R454C'  , fontdict= font1)
    plt.xlabel('P1_Process [MPa]' , fontdict= font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)



    plt.plot(P_R454C_PI35[['P1_Process']], linP_R454C_PI35.predict(P_R454C_PI35[['P1_Process']]), color = 'aquamarine' , label = 'PI 3.5')

    plt.plot(P_R454C_PI45[['P1_Process']], linP_R454C_PI45.predict(P_R454C_PI45[['P1_Process']]), color = 'teal', label = 'PI 4.5')
    plt.plot(P_R454C_PI5[['P1_Process']], linP_R454C_PI5.predict(P_R454C_PI5[['P1_Process']]), color = 'dodgerblue' , label = 'PI 5')
    plt.plot(P_R454C_PI55[['P1_Process']], linP_R454C_PI55.predict(P_R454C_PI55[['P1_Process']]), color = 'navy', label = 'PI 5.5')
    plt.plot(P_R454C_PI6[['P1_Process']], linP_R454C_PI6.predict(P_R454C_PI6[['P1_Process']]), color = 'blueviolet', label = 'PI 6')
    plt.plot(P_R454C_PI65[['P1_Process']], linP_R454C_PI65.predict(P_R454C_PI65[['P1_Process']]), color = 'magenta', label = 'PI 6.5')
    plt.savefig('LineareRegression_R454C.pgf')
    plt.legend()
    plt.show()