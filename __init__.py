# This script initializes the plugin, making it known to QGIS.
from trackGps import trackGps

def name():
    return "GPS tracking plugin - adapted from trackGps - for Windows"

def description():
    return "Track your GPS location using GPSConnection"

def version():
    return "1.0"

def qgisMinimumVersion():
    return "1.2"

def authorName():
    return "JJL <Buggerone@gmail.com> & Bob Bruce<Bob.Bruce@pobox.com>"

def classFactory(iface):
    return trackGps(iface)
