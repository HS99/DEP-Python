import xml.etree.ElementTree as ET
import xmltodict
import json
tree = ET.parse('output.xml')
xml_data = tree.getroot()
xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')
data_dict = dict(xmltodict.parse(xmlstr))
print(data_dict)
with open('new_data5.json', 'w+') as json_file:
    json.dump(data_dict, json_file, indent=4, sort_keys=True)