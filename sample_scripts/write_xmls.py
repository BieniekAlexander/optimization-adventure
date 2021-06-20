# imports
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from optimization_utils.xml_generate_utils import render_xml



# variables
DATA_PATH = "../data"
TEMPLATE_PATH = "../data/Defines.xml"
parameter_dicts = [
	{"Friction_Headrest": "1.5", "Friction_Seat": "2"},
	{"Friction_Headrest": "1.5", "Friction_Seat": "1.5"},
	{"Friction_Headrest": "1.5"},
]


# script
for i, parameter_dict in enumerate(parameter_dicts):
	render_xml(
		TEMPLATE_PATH,
		"{path}/sample_render{n}.xml".format(path=DATA_PATH, n=i),
		parameter_dict)
