import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import numpy as np
import os
import xlsxwriter
import seaborn as sns
import shutil


from io import BytesIO
# WeatherData Pfade mit pathlib
dataFolder = Path(__file__).resolve().parent # Absoluter Pfad zum Ordner dieser Datei, findet ihn automatisch heraus

#Absolute Laufvariable
i = 1


index_list = [['Min' , 'Mean', 'Max']]


# Füge Ordner zur Laufzeitumgebung damit die selbst erstellte Module gefunden werden
import sys; sys.path.append(str(dataFolder.parent))
from analysisModels.weatherFile import plotdaytemp
from analysisModels.Geocoding import geocity

landkreisfolder = dataFolder / 'exampleData' / 'Thesis'
weatherFilesPath = dataFolder / "exampleData" / "DWD_Files" / 'Landkreise'
targetpath = dataFolder / 'exampleData' / 'Analyse' / 'csv-Dateien'
movefiles = dataFolder / 'exampleData' /'DWD_Files' / 'Thesis-Pics'
resultsdir = dataFolder /'exampleData' / 'Analyse'/'Counts-Bundesländer'
ldlk = os.listdir(landkreisfolder) #ldlk listederlankkreise
print(ldlk)
acab = pd.DataFrame(ldlk)
'''
for i in os.listdir(landkreisfolder) :
    if i.suffix == '.DS_Store':
        os.remove()

'''
#print(acab)
for i in range(len(acab)):
    Path = dataFolder / "exampleData" /  'DWD_Files' / 'Bundesländer' / 'Nordrhein-Westfalen'

    print(Path)
    # Try Wetter Datei Pfade auslesen und in einer Liste hinzufügen
    tryFilePaths = [] # Leere Liste
    for tryFile in Path.iterdir(): # Gehe durch alle Dateien im Ordner
        if tryFile.suffix == ".dat": # Nur Dateien mit .dat (TRY Dateien)
            tryFilePaths.append(tryFile) # Füge Pfad zur Datei in die Liste


    print(tryFilePaths)

    tryFiledic = {}  # Erstelle ein Dictonary für Excelausgabe

    # Leeren DataFrame mit Index von -12 -- +25 erstellen

    results = pd.DataFrame()

    mt = pd.DataFrame()  # Gesamter DataFrame mit den jewailgen ZeitStempeln
    vg = pd.DataFrame()  # Sortierter DataFrame wo die Min, Max, Mean Werte Aufgetragen sind
    ld = pd.DataFrame()  # Letzer DataFrame zur Ausgabe der Extremen

    # Laufvariable zur Kontrollierten Bestimmung der DataFrames

    i1 = 1  # laufvariable zur Regelung der Gebieten
    i2 = 1
    frames = ()
    tempResultDict = {}
    print(len(tryFilePaths))

    for tryFilePath in tryFilePaths:
        frames = tryFilePaths[int(i1): int(i1) + 1]
        # Finde Adresse und Koordinaten
        for frame in frames:
            location, corrdinates = geocity(frame)
            # Erstellt Dicitonary für die Excelausgabe mit den Koordinaten
            tryFiledic[str(corrdinates)] = frame
            axe , cd = plotdaytemp(frame)
           #DWDtab.to_csv(resultsdir / 'TRY-Fileraw.csv')
            #df_TryData.to_csv(resultsdir / 'Timeseries.csv')
            #cd.to_csv(resultsdir/'Bestimmungdermaxmeanminraw.csv')
            print(location)
            # Betrachtung der kältesten gemessenen Temperatur pro Location
            mt[str(corrdinates)] = cd['min']
            # print(location, i1)e
            print(i1)
            plt.show()
            i1 += 1
            print(cd, 'Das ist cd')
            #cd.to_csv(resultsdir/ 'cdtäglichminmeanmax.csv')
            print(mt)
            #mt.to_csv(resultsdir/ 'mtkompletterlk.csv')




        # print(mt)
        # print(mt, mt.describe())''' Der Abschnitt ist zur Ermittlung eines geeigneten DataFrames'''

        vg['abs.Max'] = mt.max()
        vg['rel.Max'] = mt.quantile(.75)
        vg['Mean'] = mt.mean()
        vg['rel.Min'] = mt.quantile(.25)
        vg['abs.Min'] = mt.min()
        vg.to_latex(index= True)

        try:
            # Hier wurde der mt Framezurückgesetzt
            mt = mt.drop(mt.columns[[0, 1]], axis=1)
        except:
            print(' Array wird nicht gefüllt')
        # print('Der Bumms ist für die Ordnung der kleinen Dataframes')
        print(vg , 'das ist vg')
        vg.to_csv(resultsdir/ 'vg.csv')
        ld = ld.append(vg)
        # Bestimmung der Durchschnitts Temperaturen
        aMax = ld['abs.Max']  # Durchschnitt der bewerteten WeatherFiles
        aMax = round(aMax.mean(), 1)  # CHECKEN  wie viele Nachkommer stellen optimal sind.
        rMax = ld['rel.Max']
        rMax = round(rMax.mean(), 1)
        Mean = ld['Mean']
        Mean = round(Mean.mean(), 1)
        rMin = ld['rel.Min']
        rMin = round(rMin.mean(), 1)
        aMin = ld['abs.Min']

        aMin = round(aMin.mean(), 1)

        # Hier wird der DataFrame vg zurückgesetzt.
        try:
            vg = vg.drop(vg.index[[0, 1]])
        except:
            print('Array wird nicht gefüllt')
        # vg = vg.reset_index(drop = True)
        print(i2)
        # print(vg)
        rex = pd.DataFrame({
            'abs.Max': [aMax],
            'rel.Max': [rMax],
            'Mean': [Mean],
            'rel.Min': [rMin],
            'abs.Min': [aMin],
        },
            index=[str(i2)]
        )
        results = results.append(rex)

        rex.to_csv(resultsdir/ 'dasistrex.csv')
        # print(rex)
        i2 += 1
        ''' Abruch Kommando'''
        if i1 == int(len(tryFilePaths)):
            break

        # print(results)
    print('Bis hier hin komme ich')
    ld = round(ld, 1)

    # Task Ich muss ein DataFrame entwickeln, der alle Durschschnitswerte der analysierten Files innehält.

    print(ld)
    ld.to_csv(resultsdir/ 'dasistld.csv')
    # print('Jetzt kommen die Durchschnittsvergleiche ''')
    # print(results)


    tempabsmax = round(results['abs.Max'].mean(), 1)


    temprelmax = round(results['rel.Max'].mean(), 1)
    tempmean = round(results['Mean'].mean(), 1)
    temprelmin = round(results['rel.Min'].mean(), 1)
    tempabsmin = round(results['abs.Min'].mean(), 1)
    jerry = pd.DataFrame({'max.Temp': [tempabsmax],
            '0,75 Temp': [temprelmax],
            'mean Temp': [tempmean],
            '0,25 Temp': [temprelmin],
            'min.Temp': [tempabsmin]})

    print(jerry, 'Das ist Jerry')

    jerry.to_csv(resultsdir / 'Dieeigenwerte.csv')


    print(tempabsmax , temprelmax , tempmean , temprelmin , tempabsmin , ' Das sind die Temps')
    sabsmax = abs((ld['abs.Max']).subtract(tempabsmax, fill_value=0))
    srelmax = abs((ld['rel.Max']).subtract(temprelmax, fill_value=0))
    smean = abs((ld['Mean']).subtract(tempmean, fill_value=0))
    srelmin = abs((ld['rel.Min']).subtract(temprelmin, fill_value=0))
    sabsmin = abs((ld['abs.Min']).subtract(tempabsmin, fill_value=0))

    #print(sabsmax , srelmax, smean, srelmin, sabsmax)

    stats = pd.DataFrame()
    stats['d.abs.Max'] = sabsmax
    stats['d.rel.Max'] = srelmax
    stats['d.Mean'] = smean
    stats['d.rel.Min'] = srelmin
    stats['d.abs.Min'] = sabsmin
    stats.to_csv(resultsdir / 'dassinddiestats.csv')
    print(stats)
    fuck = stats.cumsum(axis=1)
    print(fuck)
    fuck.to_csv(resultsdir / 'dasistfuck.csv')
    Ortx_min = fuck['d.abs.Min'].min(axis=0)
    Orty_min = fuck['d.abs.Min'].idxmin(axis=0)

    print('Der Durchschnittswert des absoluten Maximums ist:', aMax, '°C')
    print('Der Durchschnittswert des relativen Maximums ist:', rMax, '°C')
    print('Der Durchschnittswert des Durchschnitts ist:', Mean, '°C')
    print('Der Durchschnittswert des relativen Minimums ist:', rMin, '°C')
    print('Der Durchschnittswert des absoluten Minimums ist:', aMin, '°C')

    # Ausgabe der Ergebnisse der Ortsverteilung

    print('Ermittle die Koordinaten des Absoluten Minimums')
    x_min = ld['abs.Min'].idxmin(axis=0)
    y_min = ld['abs.Min'].min(axis=0)

    print('Die absolute Minimal Temperatur des Minimums ist am Standort', str(x_min), ' und beträgt', str(y_min), '°C')

    print('Ermittle die Koordinaten des Absoluten Maximums')
    x_max = ld['abs.Max'].idxmax(axis=0)

    y_max = ld['abs.Max'].max(axis=0)
    print('Die absolute Maximal Temperatur des Minimums ist am Standort', str(x_max), ' und beträgt', str(y_max), '°C')

    print(' Das Ergebniss der PA ', Orty_min)

    LocMean = ld.loc[str(Orty_min)]
    LocMin = ld.loc[str(x_min)]
    LocMax = ld.loc[str(x_max)]
    print(LocMax)
    Vis = pd.DataFrame()

    Vis[str(x_max)] = LocMax
    Vis[str(Orty_min)] = LocMean
    Vis[str(x_min)] = LocMin
    #Vis['Index'] = index_list
    print(Vis)

    Aname = 'Analyse' + str(location) + '.csv'

    Vis.to_csv(resultsdir / Aname)

    ''' Bereich zum Plotten der Ergebnisse'''

    #mt.boxplot() #gefällt mir aber besser, da man den Scheiß besser lesen und als Bilder verwenden kann
    #plt.show()

    # Boxplott Diagramm
    fig, axes = plt.subplots(1, 5, sharex=False, figsize=(10, 4) , constrained_layout=True)
    bib = str(location)
    fig.suptitle( str(location))
    aMax = round(results['abs.Max'], 1)
    box0 = sns.boxplot(ax=axes[0], data=aMax)
    axes[0].set_title('max. Temp')


    rMax = round(results['rel.Max'], 1)
    box1 = sns.boxplot(ax=axes[1], data=rMax)
    axes[1].set_title('0,75 Temp')

    Mean = round(results['Mean'], 1)
    box2 = sns.boxplot(ax=axes[2], data=Mean)
    axes[2].set_title('arith. Mittel Temp.')

    rMin = round(results['rel.Min'], 1)
    box3 = sns.boxplot(ax=axes[3], data=rMin)
    axes[3].set_title('0,25 Temp.')

    aMin = round(results['abs.Min'], 1)
    box4 = sns.boxplot(ax=axes[4], data=aMin)
    axes[4].set_title('min. Temp')




    print(bib)
    plt.savefig('Düsseldorf.png')

    plt.show()
    i += 1
    print( location, 'ist erfolgreich analysiert')
    print(i , '/', len(acab))
    if not os.path.exists(movefiles) :
        os.makedirs(movefiles)


print('Simulation Abgeschlossen')