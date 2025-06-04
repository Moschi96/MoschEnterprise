import matplotlib.pyplot as plt
import pandas as pd






def plot_eta_vergleich(Df, lam, KM):
    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.axis([2, 7, 0, 1])
    plt.title('Isentroper Wirkungsgrad über das Druckverhältnis' + str(KM), fontdict=font1)
    plt.xlabel('PI = p2/p1', fontdict=font2)
    plt.ylabel('isentroper Wirkungsgrad', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)


    plt.plot(Df.index.values, Df['eta_is_rosk'],  color='blue', label='Eta_is')
    plt.plot(lam.index.values, lam['lambda'], color='red', label='lambda')

    plt.legend()
    plt.show()





def plot_eta_komplett(R32, R290, R410A, R454C):
    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}


    plt.grid(color='black', linestyle='--', linewidth=0.5)
    #plt.axis([2,7,0,0.2])

    plt.plot(R32.index.values, R32['P_is']/1000,  color='lime', label='R32')


    plt.plot(R290.index.values, R290['P_is'] /1000, color='cyan', label='R290')


    plt.plot(R410A.index.values, R410A['P_is']/1000, color='coral', label='R410A')


    plt.plot(R454C.index.values, R454C['P_is']/1000, color='violet', label='R454C')

    plt.legend()
    plt.show()


def plot_eta_proR32( R290, R410A):
    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}

    plt.xlabel('PI = p2/p1', fontdict=font2)
    plt.ylabel('P_is', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)
    plt.axis([2,7,0,1.5])




    plt.scatter(R290.index.values, R290['rho_1'], color='cyan', label='R290')


    plt.scatter(R410A.index.values, R410A['rho_1'], color='coral', label='R410A')


    plt.legend()
    plt.show()