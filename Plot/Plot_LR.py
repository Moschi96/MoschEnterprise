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


def plot_Tan_KM_3(Tan_R32, Tan_R290, Tan_R410A, x_Achse ):

    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('Linear Regression PI = 3.0' , fontdict=font1)
    plt.xlabel('x', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)


    plt.plot(x_Achse,Tan_R32 ,color='green', label = 'R32')
    plt.plot(x_Achse, Tan_R290, color='blue', label='R290')
    plt.plot(x_Achse, Tan_R410A, color='orange', label = 'R410A' )
    #plt.plot(x_Achse, Tan_R454C, color='magenta', label='R454C')
    plt.legend()
    plt.show()

def plot_Tan_KM_35(Tan_R32, Tan_R290, Tan_R410A, Tan_R454C, x_Achse ):

    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('Linear Regression PI = 3.5' , fontdict=font1)
    plt.xlabel('x', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)


    plt.plot(x_Achse,Tan_R32 ,color='green', label = 'R32')
    plt.plot(x_Achse, Tan_R290, color='blue', label='R290')
    plt.plot(x_Achse, Tan_R410A, color='orange', label = 'R410A' )
    plt.plot(x_Achse, Tan_R454C, color='magenta', label='R454C')
    plt.legend()
    plt.show()

def plot_Tan_KM_4( Tan_R290, Tan_R410A, x_Achse ):

    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('Linear Regression PI = 4.0' , fontdict=font1)
    plt.xlabel('x', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)



    plt.plot(x_Achse, Tan_R290, color='blue', label='R290')
    plt.plot(x_Achse, Tan_R410A, color='orange', label = 'R410A' )
    #plt.plot(x_Achse, Tan_R454C, color='magenta', label='R454C')
    plt.legend()
    plt.show()

def plot_Tan_KM_45(Tan_R454C, Tan_R290, Tan_R410A, x_Achse ):

    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('Linear Regression PI = 4.5' , fontdict=font1)
    plt.xlabel('x', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)



    plt.plot(x_Achse, Tan_R290, color='blue', label='R290')
    plt.plot(x_Achse, Tan_R410A, color='orange', label = 'R410A' )
    plt.plot(x_Achse, Tan_R454C, color='magenta', label='R454C')
    plt.legend()
    plt.show()

def plot_Tan_KM_5(Tan_R454C, Tan_R290, Tan_R410A, x_Achse ):

    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('Linear Regression PI = 5.0' , fontdict=font1)
    plt.xlabel('x', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)



    plt.plot(x_Achse, Tan_R290, color='blue', label='R290')
    plt.plot(x_Achse, Tan_R410A, color='orange', label = 'R410A' )
    plt.plot(x_Achse, Tan_R454C, color='magenta', label='R454C')
    plt.legend()
    plt.show()

def plot_Tan_KM_55(Tan_R454C, Tan_R290, Tan_R410A, x_Achse ):

    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('Linear Regression PI = 5.5' , fontdict=font1)
    plt.xlabel('x', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)



    plt.plot(x_Achse, Tan_R290, color='blue', label='R290')
    plt.plot(x_Achse, Tan_R410A, color='orange', label = 'R410A' )
    plt.plot(x_Achse, Tan_R454C, color='magenta', label='R454C')
    plt.legend()
    plt.show()

def plot_Tan_KM_6(Tan_R454C, Tan_R290, Tan_R410A, x_Achse ):

    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('Linear Regression PI = 6.0' , fontdict=font1)
    plt.xlabel('x', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)




    plt.plot(x_Achse, Tan_R290, color='blue', label='R290')
    plt.plot(x_Achse, Tan_R410A, color='orange', label = 'R410A' )
    plt.plot(x_Achse, Tan_R454C, color='magenta', label='R454C')
    plt.legend()
    plt.show()

'''def plot_Tan_KM_65( Tan_R410A, Tan_R454C, x_Achse ):

    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('Linear Regression PI = 6.5' , fontdict=font1)
    plt.xlabel('x', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)


    plt.plot(x_Achse, Tan_R410A, color='orange', label = 'R410A' )
    plt.plot(x_Achse, Tan_R454C, color='magenta', label='R454C')
    plt.legend()
    plt.show()'''

def plot_COE_KM(LR_KM_Data,  x_Achse , KM):

    fig, ax = plt.subplots(1, 1, figsize=(13, 8), layout='constrained', sharey=True)
    # Festlegen der Achsenbeschriftung
    font1 = {'family': 'serif', 'color': 'black', 'size': 15}
    font2 = {'family': 'serif', 'color': 'black', 'size': 10}
    plt.title('COE von'+ str(KM) , fontdict=font1)
    plt.xlabel('x', fontdict=font2)
    plt.ylabel('Verlustleistung [W]', fontdict=font2)
    plt.grid(color='black', linestyle='--', linewidth=0.5)




    plt.plot(x_Achse, LR_KM_Data, color='blue')

    plt.legend()
    #plt.show()