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

	tree = ET.parse(input_path)
	tree_group_define_elements = tree.find('GROUP_DEFINE').findall('DEFINE')
	for element in tree_group_define_elements:
		if element.get('VAR_NAME') in parameter_dict:
			element.set('VALUE', parameter_dict[element.get('VAR_NAME')])
		else:
			print("{} not found in parameter_dict, using default value".format(element.get('VAR_NAME')))

	tree.write(output_path)
