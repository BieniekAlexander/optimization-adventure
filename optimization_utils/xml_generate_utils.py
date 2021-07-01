import xml.etree.ElementTree as ET
from copy import deepcopy

def render_xml(input_path, output_path, parameter_dict):
	"""
	Reads an XML tree from a file, finds the element containing variables to rewrite,
	and rewrites the values according to the parameter_dict

	Args:
		input_path (str): the path to the input XML, to be cloned
		output_path (str): the path to render the output XML
		parameter_dict (dict): A dictionary containing the variables to render,
		mapped to their output values (all values should be strings)

	"""
	if False in [type(v) == str for v in parameter_dict.values()]:
		raise ValueError("Not all parameter_dict values were strings")

	# parse tree
	tree = ET.parse(input_path)
	tree = tree.getroot()

	# write defines
	tree_group_define_elements = tree.findall('DEFINE')
	for element in tree_group_define_elements:
		if element.get('VAR_NAME') in parameter_dict:
			element.set('VALUE', parameter_dict[element.get('VAR_NAME')])
		else:
			print("{} not found in parameter_dict, using default value".format(element.get('VAR_NAME')))

	# write things to file
	with open(output_path, 'w', encoding='UTF-8') as f:
		f.write("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n""")
		f.write("""<!DOCTYPE MADYMO_INCLUDE SYSTEM "mtd_3d.dtd">\n""")
		f.write(ET.tostring(tree, encoding='unicode', method="xml"))

if __name__ == "__main__":
	DATA_PATH = "../data"
	parameter_dict = {"Friction_Headrest": "1.5", "Friction_Seat": "2"}

	render_xml(
		f"{DATA_PATH}/Defines.xml",
		f"{DATA_PATH}/sample_render.xml",
		parameter_dict)
