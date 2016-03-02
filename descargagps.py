import subprocess
import os


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from PyQt4.QtGui import QInputDialog

 

 
nombre = QInputDialog.getText(None, "NOMBRE DE LA CAPA","Introduce el nombre del archivo sin espacios")
 


ruta = r'C:/sigmena/gps/'+nombre [0]+'.gpx'
comando= "C:/Users/descargagps.bat"

os.system(comando+" "+ ruta)


names =["waypoint", "track", "route"]#["waypoint", "route", "track", "route_point", "track_point"]  # ["waypoint"]
path=ruta
dest_crs = QgsCoordinateReferenceSystem(25830)
for name in names:
    #iface.addVectorLayer(ruta+"?type="+name, name, "gpx")
    vectorLyr =QgsVectorLayer(ruta+"?type="+name, name, "gpx")
    QgsVectorFileWriter.writeAsVectorFormat(vectorLyr,str(ruta[:-4])+"_"+name,"utf-8",dest_crs,"ESRI Shapefile")
    iface.addVectorLayer(str(ruta[:-4])+"_"+name+".shp", str(nombre[0])+"_"+name, "ogr")
