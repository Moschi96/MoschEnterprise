from pandas import read_table, errors

# Die SkipNumbers zum lesen der Tabelle von verschiedenen TRY Versionen. Hier Hinzufügen oder entfernen
skipNumbersForTRYformats = {"TRY2010":17, "TRY2015":15, "TRY2045":16}


def loadWeatherData(pathToFile: object) -> object:
    """Lädt Wetter Daten aus. Bisher nur orginale TRY Datensätze mit der Endung .dat
    
    Parameters:
        pathToFile (Path): Pfad der Wetterdaten Datei mit Pathlib erstellt
        
    Return:
        df (pandasDataFrame): Pandas Data Frame Tabelle mit allen Wetterdaten"""
        
    # Anhand der Dateiendung richtige Funktion aufrufen
    if pathToFile.suffix == ".dat": # Überpruefe ob Dateiendung
        tryFormatKey = None
        for key in skipNumbersForTRYformats.keys(): # Bestimme TRY Version anhand des Dateinamen
            if key in pathToFile.name:
                tryFormatKey = key
                break
                
        if tryFormatKey is None: # Wenn TRY Version nicht in skipNumbersForTRYformats vorhanden -> Raise Error
            raise ValueError("Error detect TRY Format")
        
        # Führe Funktion aus und gebe die Resultate zurück    
        return _importData_TRY(pathToFile, skipNumbersForTRYformats[tryFormatKey])
            
    elif pathToFile.suffix == ".mos": # Wenn mos Datei (Umgewandelte TRY Dateien für Dymola) noch nicht hinzugefügt
        raise ValueError(".mos Files are not supported at the moment")
        

def _importData_TRY(pathToFile, skipHeaderRowsNumber):
    """Importiert aus TRY Dateien die Wetter Daten Tabelle in ein pandas Data Frame
    
    Parameters:
        pathToFile (Path): Pfad der TRY Datei mit Pathlib erstellt
        skipHeaderRowsNumber (int): Anzahl an überspringender Zeilen vom Header
        
    Return:
        df (pandasDataFrame): Pandas Frame Tabelle mit allen Wetterdaten"""
        
    # Überprüfen ob lesen der TRY Daten erfolgreich war
    skip_idx = [x for x in range(0, skipHeaderRowsNumber)] # Index der zu Überspringenden Zeilen im Header
    readTableSucessful = True
    try:
        # Lese Datei mit Pandas read_table
        df = read_table(filepath_or_buffer=pathToFile, header=skipHeaderRowsNumber, delim_whitespace=True, skiprows=skip_idx)
    except errors.ParserError: # ignoriere Fehler Parser Error
        readTableSucessful = False
        
    if not readTableSucessful: # Eigne Fehler Audgabe da bei dem Fehler nur skipHeaderRowsNumber falsch
        raise ValueError("Error Read TRY File: Header Skip Number to Low")
 
    # Kontrollieren ob auslesen Korrekt ist (Kann erweitert werden)
    if not "t" in df.columns.values:
        raise ValueError("Error Read TRY File: Header Skip Number to High")
    elif not "***" in df.head(1)[df.columns.values[0]].values:
        raise ValueError("Error Read TRY File: First Dummy Row is not correct -> Maybe other or unknown TRY Format")
        
    # Löscht erste Zeile im Panda Frame und giebt den Rest zurück
    return df.drop(0)