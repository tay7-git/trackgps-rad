# This script initializes the plugin, making it known to QGIS.
from trackGps import trackGps

def name():
    return "GPS tracking plugin with Radiation Plot - adapted from trackGps - for Windows"
    
def description():
    return "Track your GPS location using GPSConnection and Plottiog Radiation from Radiation Surveyer"

def version():
    return "1.0r0.1"

def qgisMinimumVersion():
    return "1.2"

def authorName():
    return "tay <@tay07212 on twitter> based on JJL <Buggerone@gmail.com> & Bob Bruce<Bob.Bruce@pobox.com>"

def classFactory(iface):
    return trackGps(iface)
