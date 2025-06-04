import matplotlib.pyplot as plt
import pandas as pd






def plot_MF_R32(D25,D3,D35,  KM):
    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 20}
    #plt.axis([2, 7, 0, 1])
    plt.title('Mf_Suc' + str(KM), fontdict=font1)
    plt.xlabel('PI = p2/p1', fontdict=font2)
    plt.ylabel('Massenstrom', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)



    plt.plot(D25.index.values, D25['MF_Suc'],  color='blue', label='PI = 2.5')
    plt.plot(D3.index.values, D3['MF_Suc'], color='red', label='PI = 3.0')
    plt.plot(D35.index.values, D35['MF_Suc'], color='green', label='PI = 3.5')

    plt.legend()
    plt.show()


def plot_MF_R410A(D3,D35,D4,D45,D5,D55,D6,D65 ):
    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 20}
    font2 = {'family': 'serif', 'color': 'black', 'size': 20}
    #plt.axis([2, 7, 0, 1])


    plt.grid(color='black', linestyle='--', linewidth=0.5)




    plt.plot(D3.index.values, D3['MF_Suc'], color='red', label='PI = 3.0')
    plt.plot(D35.index.values, D35['MF_Suc'], color='green', label='PI = 3.5')
    plt.plot(D4.index.values, D4['MF_Suc'], color='purple', label='PI = 4.0')
    plt.plot(D45.index.values, D45['MF_Suc'], color='cyan', label='PI = 4.5')
    plt.plot(D5.index.values, D5['MF_Suc'], color='black', label='PI = 5.0')
    plt.plot(D55.index.values, D55['MF_Suc'], color='blue', label='PI = 5.5')
    plt.plot(D6.index.values, D6['MF_Suc'], color='lime', label='PI = 6.0')
    plt.plot(D65.index.values, D65['MF_Suc'], color='pink', label='PI = 6.5')
    plt.legend()
    plt.savefig('MF_Suc_R410A.svg')
    plt.show()

def plot_lambda(D1, D2, D3,D4 ):
    plt.rc('font', size=20)
    fig, ax = plt.subplots(1, 1, figsize=(18, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    plt.grid(color='black', linestyle='--', linewidth=0.5)


    plt.plot(D1.index.values,D1['delta_s'] ,color='green', label = 'R32')
    plt.plot(D2.index.values, D2['delta_s'], color='blue', label='R290')
    plt.plot(D3.index.values, D3['delta_s'], color='orange', label = 'R410A' )
    plt.plot(D4.index.values, D4['delta_s'], color='magenta', label='R454C')
    plt.legend()
    plt.savefig('deltas_KM.svg')
    plt.show()
def Plot_Ploss_Vergleich(df ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('P_Loss Vergleich' , fontdict= font1)
    plt.xlabel('delta_s', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter( df['ds'] , df['P_loss'] , color = 'red' ,label = 'Ploss')
    plt.scatter(df['ds'] , df['P_loss_theo'] , color = 'blue' ,label = 'P_loss_theo')


    plt.legend()
    plt.show()

def Plot_Ploss_PI(df, KM  ):
    fig, ax = plt.subplots(1,1,figsize=(13, 8), layout='constrained',sharey=True )
    #Festlegen der Achsenbeschriftung
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'black','size':10}
    plt.title('PI' , fontdict= font1)
    plt.xlabel('PI', fontdict= font2)
    plt.ylabel('Power Loss [W]', fontdict=font2)
    plt.grid(color = 'black', linestyle= '--', linewidth = 0.5)

    plt.scatter( df['PI'] , df['P_loss'] , color = 'red' ,label = 'Ploss')
    plt.scatter(df['PI'] , df['P_loss_theo'] , color = 'blue' ,label = 'P_loss_theo')


    plt.legend()
    plt.show()

