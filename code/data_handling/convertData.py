from datetime import datetime
from pandas import to_datetime, DatetimeIndex, DataFrame, concat
from geopy import Nominatim # OpenStreet
from warnings import warn
from calendar import leapdays
from code.data_handling.loadData import loadWeatherData
from code.data_handling.utils import createPathIfNotExist
from pathlib import Path
from numpy import radians, sin, degrees, pi, arcsin, cos
	
def createMosWeatherFile(pathToTryFile, pathToFolderForMosFiles, locationBuilding=None, startAtZero = False):
	"""Wandelt TRY Datein in mos Dateien um. mos Dateien werden für die Dymola Simulation benötigt.
		Quelle vom Code: https://git.rwth-aachen.de/EBC/EBC_all/WeatherDataConverter/-/blob/master/Functions/weatherconverter.py
		Es gibt aber auch eine Online Anwendung zum Manuellen umwandeln (nur aus dem ebc Netz): http://137.226.248.85:9000/converter/simpleupload/	
			Parameters:
				pathToTryFile (Path): Pfad zur TRY Datei. Path mit Pathlib erstellt
				pathToFolderForMosFiles (Path): Pfad zum Ordner wo die mos Datei abgespeichert werden soll. der Dateiname wird im Code automatisch erstellt
				locationBuilding (String): None (Default), Name vom Ort des Gebäudes. Wenn None, wird dann automatisch erstellt anhand der Koordinaten im TRY Datei Namen
				startAtZero (Boolean): False (Default), Aus anderem Code übernommen -> überprüfe Quelle
				
			Return:
				mosFilePath (Path): Path zur erstellten mos datei
				locationBuilding (String): Name vom Ort"""
	
	# Datei Format Einstellungen
	Format_PickleTRY = {
						'Name': [
							'timeOfYear', 'RG', 'IS', 'MM', 'DD', 'HH', 'N', 'WR', 'WG', 't', 'p',
							'x', 'RF', 'W', 'B', 'D', 'IK', 'A', 'E', 'IL'],
						'UnitOfMeas': [
							's', 'None', 'None', 'None', 'None', 'None', 'eighth', 'degree',
							'm/s', 'degC', 'hPa', 'g/kg', 'percent', 'None', 'W/m2', 'W/m2',
							'None', 'W/m2', 'W/m2', 'None']}
							
	Format_ModelicaTMY3 = {
		'Name': [
			'timeOfYear', 'DryBulbTemp', 'DewPointTemp', 'RelHum', 'AtmPressure',
			'ExtHorRad', 'ExtDirNormRad', 'HorInfra', 'GlobHorRad', 'DirNormRad',
			'DiffHorRad', 'GlobHorIll', 'DirecNormIll', 'DiffuseHorIll',
			'ZenithLum', 'WindDir', 'WindSpeed', 'TotalSkyCover',
			'OpaqueSkyCover', 'Visibility', 'CeilingH', 'WeatherObs',
			'WeatherCode', 'PrecWater', 'Aerosol', 'Snow', 'DaysSinceSnow',
			'Albedo', 'LiquidPrecD', 'LiquidPrepQuant'],
		'UnitOfMeas': [
			's', 'degC', 'degC', 'percent', 'Pa', 'Wh/m2', 'Wh/m2', 'Wh/m2',
			'Wh/m2', 'Wh/m2', 'Wh/m2', 'lux', 'lux', 'lux', 'Cd/m2', 'deg',
			'm/s', '1tenth', '1tenth', 'km', 'm', 'None', 'None', 'mm', 'None',
			'cm', 'days', 'None', 'mm', 'None']}
	
	# Lade Try Datei
	df_tryData = loadWeatherData(pathToTryFile)
	
	# Zeitangabe in Datetime Format umwandeln
	df_tryData['MM'] = df_tryData['MM'].astype(int)
	df_tryData['DD'] = df_tryData['DD'].astype(int)
	df_tryData['HH'] = df_tryData['HH'].astype(int)
	df_tryData['Timestamp'] = df_tryData.apply(
		lambda row: datetime(
			int(2017),
			row.MM,
			row.DD,
			row.HH - int(1.0)), axis=1)
			
	# hours in pandas only between 0 and 23, in TRY between 1 and 24
	# converts to pandas timestamps if desired
	df_tryData['Timestamp'] = to_datetime(df_tryData.Timestamp)
	# Create a DatetimeIndex and assign it to the dataframe.
	df_tryData.index = DatetimeIndex(df_tryData.Timestamp)
	df_tryData = df_tryData.drop('Timestamp', axis=1)
	# shift with one hour as values at 01:00 are the values for the passed hour
	df_tryData = df_tryData.shift(periods=1, freq='H', axis=0)
	
	# create data frame for missing weather data
	dataCalculatedWeather = DataFrame(index=df_tryData.index)
	
	# start calculation of relevant sun angles
	# calculate latitude and longitude sun
	try:
		corrdinates = pathToTryFile.name.replace(pathToTryFile.suffix, "").split("_")[1]
		latitude = float(corrdinates[:2] + "." + corrdinates[2:6])
		longitude = float(corrdinates[6:8] + "." + corrdinates[6:])
		tempLocation = _getAdressFromLatitudeAndLongitude(latitude, longitude, zoom=10)
		adressElementsDict = tempLocation["address"]
		adressElements = adressElementsDict.values()
		element_iterator = iter(adressElements)
		firstElement = next(element_iterator)
		tempLocationName = "%s %s" % (firstElement, adressElementsDict["state"])
	except KeyError:
		tempLocationName = "Unknown"
		corrdinates = pathToTryFile.name.replace(pathToTryFile.suffix, "").split("_")[1]
		latitude = float(corrdinates[:2] + "." + corrdinates[2:6])
		longitude = float(corrdinates[6:8] + "." + corrdinates[6:])
		warn("Adresse konnte gefunden werden jedoch kein String erstellt werden: unbekannter Key")
	except:
		tempLocationName = None
		
	if tempLocationName is None:
		if locationBuilding is None:
			# Setze Standard Koordinaten
			warn("Koordinaten können nicht aus der Try gefunden werden sowie keine Ort angabe -> nutze Default Koordinaten Aachen")
			locationBuilding = "Unknown"
			latitude = 50.7755
			longitude = 6.0854
		else:
			latitude, longitude = _getLatitudeAndLongitudeOfLocation(locationBuilding)
	else:
		if locationBuilding is None:
			locationBuilding = tempLocationName
			
	# calculate hour angle and declination angle sun
	dataCalculatedWeather = _calculateHourAngleDeclinationSun_VDI3789(dataCalculatedWeather, latitude, longitude)
	# calculate sin elevation angle
	dataCalculatedWeather = _calculateSolarAltitude(dataCalculatedWeather, latitude)
	dataCalculatedWeather = _calculateDirectNormalRadiation(dataCalculatedWeather, df_tryData)
		
	minYear = min(df_tryData.index.year)
	df_MW = DataFrame(index=df_tryData.index, columns=Format_ModelicaTMY3['Name'])

	df_MW['DryBulbTemp'] = df_tryData['st']
	df_MW['RelHum'] = df_tryData['RF']
	df_MW['DewPointTemp'] = df_MW['DryBulbTemp'] - (100 - df_MW['RelHum']) / 5
	# simple approximation, according to https://en.wikipedia.org/wiki/Dew_point
	df_MW['AtmPressure'] = df_tryData['p'] * 100
	df_MW['HorInfra'] = df_tryData['A']
	df_MW['GlobHorRad'] = df_tryData['B'] + df_tryData['D']
	df_MW['DirNormRad'] = dataCalculatedWeather['DirectNormalCloudySky']
	df_MW['DiffHorRad'] = df_tryData['D']
	df_MW['WindDir'] = df_tryData['WR']
	df_MW['WindSpeed'] = df_tryData['WG']
	df_MW['TotalSkyCover'] = df_tryData['N'] * (10.0 / 8.0)   # scaling from 0 to 10
	
	# create index needed by weather file in modelica format time in seconds from
	# beginning of the first year of provided measured data
	# take leap years into account
	index_df = (df_tryData.index.year - minYear) * 365 * 24 * 3600 + leapdays(minYear, df_tryData.index.year) * 24 * 3600 +(df_tryData.index.dayofyear - 1) * 24 * 3600 + df_tryData.index.hour * 3600
	df_MW = df_MW.set_index(index_df)
	df_MW = df_MW.drop('timeOfYear', axis=1)     # drop old index column
	
	# fill NaNs
	df_MW = df_MW.fillna(99999.9)

	# remove duplicated index - somehow data with the same timestamp exists.
	# remove it
	df_MW = df_MW[~df_MW.index.duplicated(keep='first')]

	# if data has to start at zero
	if startAtZero:
		newFirstRow = DataFrame(index=['0.0'], columns=df_MW.columns)
		newFirstRow.iloc[0] = df_MW.iloc[0]
		df_MW = concat([newFirstRow, df_MW])
		df_MW = df_MW[:-1]
		
	# Write to file
	mosFileName = pathToTryFile.name.replace(pathToTryFile.suffix, "") + "_" + locationBuilding + ".mos"
	mosFilePath = pathToFolderForMosFiles / removeUnsurportedCharsFromPathForDymola(mosFileName)
	
	createPathIfNotExist(mosFilePath)
	df_MW.to_csv(mosFilePath, sep='\t', float_format='%.3f', header=False)
	
	# add header
	# Create header
	headerOF = '#1' + '\ndouble tab1(' + str(int(df_MW.index.size)) + ',' +\
		str(int(df_MW.columns.size) + 1) + ')'
	# location in header
	diffGMT = longitude // 15.0 + 1.0
	headerOF = headerOF + '\n#LOCATION,' + locationBuilding +\
		",State,Country,TMY3,Something," + str(latitude) + ',' + str(longitude) +\
		',' + str(diffGMT) + ',Something'
	# a lot of non important header for Modelica
	headerOF = headerOF +\
		'\n#DESIGN CONDITIONS,BlaBla' +\
		'\n#TYPICAL/EXTREME PERIODS,BlabBla' +\
		'\n#GROUND TEMPERATURES, BlaBla' +\
		'\n#HOLIDAYS/DAYLIGHT SAVINGS,BlaBla' +\
		'\n#COMMENTS BlaBla' +\
		'\n#DATA PERIODS,BlaBla' +\
		'\n#C1 Time in seconds. Beginning of a year is 0s.' +\
		'\n#C2 Dry bulb temperature in Celsius at indicated time' +\
		'\n#C3 Dew point temperature in Celsius at indicated time' +\
		'\n#C4 Relative humidity in percent at indicated time' +\
		'\n#C5 Atmospheric station pressure in Pa at indicated time' +\
		'\n#C6 Extraterrestrial horizontal radiation in Wh/m2' +\
		'\n#C7 Extraterrestrial direct normal radiation in Wh/m2' +\
		'\n#C8 Horizontal infrared radiation intensity in Wh/m2' +\
		'\n#C9 Global horizontal radiation in Wh/m2' +\
		'\n#C10 Direct normal radiation in Wh/m2' +\
		'\n#C11 Diffuse horizontal radiation in Wh/m2' +\
		'\n#C12 Averaged global horizontal illuminance in lux during minutes ' +\
		'preceding the indicated time' +\
		'\n#C13 Direct normal illuminance in lux during minutes preceding the ' +\
		'indicated time' +\
		'\n#C14 Diffuse horizontal illuminance in lux  during minutes ' +\
		'preceding the indicated time' +\
		'\n#C15 Zenith luminance in Cd/m2 during minutes preceding the ' +\
		'indicated time' +\
		'\n#C16 Wind direction at indicated time. N=0, E=90, S=180, W=270' \
		'\n#C17 Wind speed in m/s at indicated time' +\
		'\n#C18 Total sky cover at indicated time' +\
		'\n#C19 Opaque sky cover at indicated time' +\
		'\n#C20 Visibility in km at indicated time' +\
		'\n#C21 Ceiling height in m' +\
		'\n#C22 Present weather observation' +\
		'\n#C23 Present weather codes' +\
		'\n#C24 Precipitable water in mm' +\
		'\n#C25 Aerosol optical depth' +\
		'\n#C26 Snow depth in cm' +\
		'\n#C27 Days since last snowfall' +\
		'\n#C28 Albedo' +\
		'\n#C29 Liquid precipitation depth in mm at indicated time' +\
		'\n#C30 Liquid precipitation quantity'
	headerOF.strip()
	
	with mosFilePath.open(mode="r+") as f:
		content = f.read()
		f.seek(0, 0)
		f.write(headerOF + '\n' + content)
		f.close()
		
	return mosFilePath, locationBuilding
	
def _getLatitudeAndLongitudeOfLocation(location):
	"""Gibt Latitude und Longitude von einem Ort
			Parameters:
				location (String): Name vom Ort
				
			Return:
				latitude (float): Koordinaten
				longitude (float): Koordinaten"""
			
	geolocator = Nominatim(user_agent="Converter")
	try:
		location = geolocator.geocode(location, timeout=10)
		latitude = location.latitude
		longitude = location.longitude
	except:
		warn("Koordinaten können nicht vom Ort gefunden werden nutze Default Koordinaten Aachen")
		latitude = 50.7755
		longitude = 6.0854
	return latitude, longitude
	
def _getAdressFromLatitudeAndLongitude(latitude, longitude, zoom=18):
	"""Gibt Adress Information von Koordinaten zurück
			Parameters:
				latitude (float): Koordinaten
				longitude (float): Koordinaten
				zoom (int): Auflösung der Adressdaten default (18) für max Auflösung. für create Mos nutze ich 10 um Stadt herauszufinden da der Key je nach Standort ändert
				
			Return:
				#locationName (String): Name vom Ort oder None wenn nicht gefunden
				location (geopy Adress Dict): Dict mit allen Adressinformationen"""
				
	geolocator = Nominatim(user_agent="Converter")
	try:
		location = geolocator.reverse("%f, %f" % (latitude, longitude), timeout=10, zoom=zoom)
	except:
		warn("Adresse konnte nicht anhand der TRY Korrdinaten gefunden werden: Latitude: %f  Longitude: %f" % (latitude, longitude))
		return None
	
	#locationName = "%s %s" % (location.raw["address"]["city"], location.raw["address"]["road"])
	return location.raw
		
def _calculateHourAngleDeclinationSun_VDI3789(data, Latitude, Longitude):
	"""calculateHourAngleDeclinationSun_VDI3789
			Parameters:
				data (pandasDataFrame): Tabelle mit Wetterdaten für mos knvertierung
				Latitude (float): Koordinaten
				Longitude (float): Koordinaten
				
			Return:
				data (pandasDataFrame): Umgewandelte Daten"""
					
	data['DayAngleSun'] = radians(
		0.9856 * (data.index.dayofyear) - 2.72)
	# x according to VDI 3789-2:1994 equation 13
	data['TimeEquation'] = -7.66 * sin(data['DayAngleSun']) - 9.87 * sin(radians(2 * degrees(data['DayAngleSun']) + 24.99 +3.83 * sin(data['DayAngleSun'])))
	# Equation of time in minutes, according VDI 3789-2:1994 equation C2
	# (page 34)
	data['SolarTime'] = data.index.hour - 0.5 + (data['TimeEquation'] / 60.0)
	# TLT according to VDI 3789-2:1994 equation C1 (page 34) - correction 0.5
	# assuming the solar value is calculated for the middle of the hour passed
	data['HourAngleSun'] = (data['SolarTime'] - 12) * pi / 12
	# hour angle according to VDI 3789-2:1994 equation D4 (page 35)
	data['DeclinationSun'] = arcsin(0.3978 * sin(radians(degrees(data['DayAngleSun']) - 77.51 + 1.92 * sin(data['DayAngleSun']))))
	# declination of sun according to VDI 3789-2:1994 equation D3 (page 35),
	# value constant over day
	return data
	
def _calculateSolarAltitude(data, Latitude):
	"""calculateSolarAltitude
			Parameters:
				data (pandasDataFrame): Tabelle mit Wetterdaten für mos knvertierung
				Latitude (float): Koordinaten
				
			Return:
				data (pandasDataFrame): Umgewandelte Daten"""
						
	data['AltitudeAngleSun'] = arcsin(
		sin(radians(Latitude)) *
		sin(data['DeclinationSun']) +
		cos(radians(Latitude)) *
		cos(data['DeclinationSun']) *
		cos(data['HourAngleSun']))
	# altitude angle of sun according to VDI 3789-2:1994 equation D1 (page 35)
	return data
	
def _calculateDirectNormalRadiation(data, df_tryData):
	"""calculateDirectNormalRadiation
			Parameters:
				data (pandasDataFrame): Tabelle mit Wetterdaten für mos knvertierung
				df_tryData (pandasDataFrame): TRY Daten in pandasDataFrame
				
			Return:
				data (pandasDataFrame): Umgewandelte Daten"""
							
	data['DirectNormalCloudySky'] = 0.0
	data['DirectNormalCloudySky'][(data['AltitudeAngleSun'] >= 0.087) & (data['AltitudeAngleSun'] <= 3.054)] = df_tryData['B'] / sin(data['AltitudeAngleSun'])
	# positive altitude angles, higher than 5° and lower than 175°
	return data

def removeUnsurportedCharsFromPathForDymola(path):
	"""Entferne nicht kompatible Zeichen aus dem Path Name. Dymola ist sehr empfindlich was Umlaute oder leerzeichen angeht. Wenn noch andere Zeichen dazu kommen hier einfügen damit es überall ausgeführt wird der diese Funktion aufruft.
			Parameters:
				path (Path): Pfad im pathlib Format
								
			Return:
				path (Path): Umgewandelte Chars im Path"""
								
	stringData = str(path)
	for charVar in stringData:
		if charVar == "ö":
			stringData = stringData.replace("ö", "oe")
		elif charVar == "Ö":
			stringData = stringData.replace("Ö", "Oe")
		elif charVar == "ä":
			stringData = stringData.replace("ä", "ae")
		elif charVar == "Ä":
			stringData = stringData.replace("Ä", "Ae")
		elif charVar == "ü":
			stringData = stringData.replace("ü", "ue")
		elif charVar == "Ü":
			stringData = stringData.replace("Ü", "Ue")
		elif charVar == "ß":
			stringData = stringData.replace("ß", "ss")
		elif charVar == " ":
			stringData = stringData.replace(" ", "_")
		elif charVar == "-":
			stringData = stringData.replace("-", "_")
		else:
			continue
	return Path(stringData)

