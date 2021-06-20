# imports
import subprocess 
import os

# variables
FILE_LOCATION = r'C:/Users/ILLINI/Desktop/optimization-adventure/data'
MADYMO_XML_PATH = "sample_render0.xml"


# script
os.chdir(FILE_LOCATION)
subprocess.call(['madymo20201', '-3d', MADYMO_XML_PATH])	# TODO is this a correct sample of calling madymo?
#%%