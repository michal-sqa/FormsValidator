from xml.etree import ElementTree

def extract_xml_elements_by_path(xml_root, xml_path):
    xml_tree = ElementTree.fromstring(xml_root)
    extracted_values_list = xml_tree.findall(xml_path)
    return extracted_values_list

def extract_attribute_value_of_xml_element(element, attribute_name):
    attribute_value = element.get(attribute_name)
    return attribute_value