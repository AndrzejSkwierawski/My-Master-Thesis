from Character import *
import xml.etree.ElementTree as ET


def import_character_from_xml(xml, character):
    tree = ET.parse(xml)
    root = tree.getroot()
    if root.tag == "character":
        for child in root:
            if child.tag == "name":
                character.Name = child.text.strip()
            elif child.tag == "attack":
                character.Attack = child.text.strip()
            elif child.tag == "hp":
                character.HP = character.currentHP = child.text.strip()
            elif child.tag == "init":
                character.Init = child.text.strip()
            elif child.tag == "def":
                character.Deff = child.text.strip()
            elif child.tag == "class":
                if child.text.strip() in character.ClassEnumerate:
                    character.Class = character.ClassEnumerate[child.text.strip()]
                else:
                    warnings.warn("INVALID FORMAT: class name not recognised", UserWarning)
            elif child.tag == "size":
                character.Size = child.text.strip()
    else:
        warnings.warn("INVALID FORMAT: cannot parse xml. Xml root name '" + root.tag + "' not recognised", UserWarning)


def export_character_to_xml(character, xml):
    root = ET.Element("character")
    ET.SubElement(root, "name").text = character.Name
    ET.SubElement(root, "attack").text = str(character.Attack)
    ET.SubElement(root, "hp").text = str(character.HP)
    ET.SubElement(root, "init").text = str(character.Init)
    ET.SubElement(root, "def").text = str(character.Deff)
    ET.SubElement(root, "class").text = str([key for (key, value) in character.ClassEnumerate.items() if value == 1][0])
    ET.SubElement(root, "size").text = str(character.Size)
    tree = ET.ElementTree(root)
    tree.write(xml)


y = Character(name="Błażej", attack=0)
export_character_to_xml(y, "export.xml")
x = Character()
import_character_from_xml("export.xml", x)
x.print_properties()
