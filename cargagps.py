import subprocess
import os


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from PyQt4.QtGui import QInputDialog

 

mycrs = QgsCoordinateReferenceSystem(25830)
nombre = QInputDialog.getText(None, "NOMBRE DE LA CAPA","Introduce el nombre del archivo shp sin espacios")

shapefile=r'C:/sigmena/gps/'+nombre [0]+'.shp'
vectorLyr =QgsVectorLayer(shapefile, nombre [0], "ogr")
vectorLyr.setCrs(mycrs,True)
processing.runalg("qgis:reprojectlayer",shapefile, "epsg:4326",str(shapefile[:-4])+"_wgs84.shp")

iface.addVectorLayer(shapefile, nombre [0], "ogr")

dest_crs = QgsCoordinateReferenceSystem(4326)
QgsVectorFileWriter.writeAsVectorFormat(vectorLyr,str(shapefile[:-4])+"_wgs84","utf-8",dest_crs,"ESRI Shapefile")
vectorLyr2 =QgsVectorLayer(str(shapefile[:-4])+"_wgs84.shp", nombre [0]+"_wgs84", "ogr")
vectorLyr2.setCrs(dest_crs,True)
iface.addVectorLayer(str(shapefile[:-4])+"_wgs84.shp", str(nombre[0])+"_wgs84", "ogr")
if os.path.exists(str(shapefile[:-4])+".gpx"):
    os.remove(str(shapefile[:-4])+".gpx")
comando="ogr2ogr -f GPX "+str(shapefile[:-4])+".gpx "+str(shapefile[:-4])+"_wgs84.shp"# -sql SELECT nombre AS name"#ogr2ogr -f GPX output.gpx input.gpx waypoints routes tracks"
os.system(comando)

ruta =str(shapefile[:-4])+".gpx"
comando= "C:/Users/cargagps.bat"

os.system(comando+" "+ ruta)


