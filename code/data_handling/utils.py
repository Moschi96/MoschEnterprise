from pathlib import Path

def createPathIfNotExist(path):
	"""Erstellt die Ordner wenn diese nicht existieren
	
	Parameters:
		path (Path): Pfad der über"""
		
	# path nach Path umwandeln wenn String
	tempPath = None
	if type(path) == str:
		tempPath = Path(path)
	else:
		tempPath = path
		
	#Prüfen ob Datei oder Pfad
	if tempPath.suffixes:
		tempPath = tempPath.parent
		
	# Ordner erstellen wenn nicht existiert
	if not tempPath.exists():
		tempPath.mkdir(parents=True)