# imports
import subprocess


# variables
MADYMO_XML_PATH = "Madymo.xml"


# script
subprocess.call('madymo20201', MADYMO_XML_PATH, shell=True)	# TODO is this a correct sample of calling madymo?
