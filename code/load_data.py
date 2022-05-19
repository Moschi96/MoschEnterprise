#Skrip Vorstellung

#Modul Importe
from pathlib import Path
from io import BytesIO
from datetime import datetime
import pandas as pd
import scipy.io
from scipy.io import loadmat
import warnings
import os
import glob



# WeatherData Pfade mit pathlib
dataFolder = Path(__file__).resolve().parent.parent # Absoluter Pfad zum Ordner dieser Datei, findet ihn automatisch heraus

# Füge Ordner zur Laufzeitumgebung damit die selbst erstellte Module gefunden werden
import sys; sys.path.append(str(dataFolder.parent))

data =dataFolder/ 'Input_Data'/'02_Quasistationär' # gibt möglichkeit die RawData mit dem Attribut data aufzugreifen.

#Lade die einzelnen Dateien in ein DataFrame ein
data_raw_R32 = data/'R32'/'meandata.mat' #Matlabdatei wird eingelesen. meandata da ich keinen Plan habe was wichtig ist

matdata = scipy.io.loadmat(data_raw_R32)
print(matdata)
#x = mat['None']
