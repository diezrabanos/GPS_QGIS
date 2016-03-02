set parametro=%1
"C:/archivos de programa/QGIS Lyon/bin/gpsbabel.exe" -w -r -t -i garmin -f usb: -o gpx -F %parametro%
"C:/archivos de programa/QGIS Lyon/bin/gpsbabel.exe" -w -r -t -i garmin -f COM1 -o gpx -F %parametro%
"C:/archivos de programa/QGIS Lyon/bin/gpsbabel.exe" -w -r -t -i garmin -f COM2 -o gpx -F %parametro%
"C:/archivos de programa/QGIS Lyon/bin/gpsbabel.exe" -w -r -t -i garmin -f COM3 -o gpx -F %parametro%
"C:/archivos de programa/QGIS Lyon/bin/gpsbabel.exe" -w -r -t -i garmin -f COM4 -o gpx -F %parametro%
"C:/archivos de programa/QGIS Lyon/bin/gpsbabel.exe" -w -r -t -i garmin -f COM5 -o gpx -F %parametro%
"C:/archivos de programa/QGIS Lyon/bin/gpsbabel.exe" -w -r -t -i garmin -f COM6 -o gpx -F %parametro%
"C:/archivos de programa/QGIS Lyon/bin/gpsbabel.exe" -w -r -t -i garmin -f COM7 -o gpx -F %parametro%
