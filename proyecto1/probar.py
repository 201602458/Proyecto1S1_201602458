import xml.etree.ElementTree as ET



for event, elem in ET.iterparse("ejemplo.xml",events=("matrices", "dato")):
    print(event,elem,elem.tag,elem.attrib)
