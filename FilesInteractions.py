from Character import *
from TeamOrganization import *
import xml.etree.ElementTree as ET


def import_character_from_xml(xml, character):
    tree = ET.parse(xml)
    root = tree.getroot()
    if root.tag == "character":
        for child in root:
            if child.tag == "name":
                character.Name = child.text.strip()
            elif child.tag == "attack":
                character.Attack = int(child.text.strip())
            elif child.tag == "hp":
                character.HP = character.currentHP = int(child.text.strip())
            elif child.tag == "init":
                character.Init = int(child.text.strip())
            elif child.tag == "def":
                character.Deff = int(child.text.strip())
            elif child.tag == "class":
                if child.text.strip() in character.ClassEnumerate:
                    character.Class = character.ClassEnumerate[child.text.strip()]
                else:
                    warnings.warn("INVALID FORMAT: class name not recognised", UserWarning)
            elif child.tag == "size":
                character.Size = int(child.text.strip())
    else:
        warnings.warn("INVALID FORMAT: cannot parse xml. Xml root name not recognised.", UserWarning)


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


def import_team_from_xml(xml, team):
    tree = ET.parse(xml)
    root = tree.getroot()
    if root.tag == "team":
        for child in root:
            character = Character()
            for option in child:
                if option.tag == "name":
                    character.Name = option.text.strip()
                elif option.tag == "attack":
                    character.Attack = int(option.text.strip())
                elif option.tag == "hp":
                    character.HP = character.currentHP = int(option.text.strip())
                elif option.tag == "init":
                    character.Init = int(option.text.strip())
                elif option.tag == "def":
                    character.Deff = int(option.text.strip())
                elif option.tag == "class":
                    if option.text.strip() in character.ClassEnumerate:
                        character.Class = character.ClassEnumerate[option.text.strip()]
                    else:
                        warnings.warn("INVALID FORMAT: class name not recognised", UserWarning)
                elif option.tag == "size":
                    character.Size = int(option.text.strip())
            if child.tag == "tl":
                place_character_in_spot(team, [0, 0], character)
            elif child.tag == "tr":
                place_character_in_spot(team, [1, 0], character)
            elif child.tag == "cl":
                place_character_in_spot(team, [0, 1], character)
            elif child.tag == "cr":
                place_character_in_spot(team, [1, 1], character)
            elif child.tag == "bl":
                place_character_in_spot(team, [0, 2], character)
            elif child.tag == "br":
                place_character_in_spot(team, [1, 2], character)
    else:
        warnings.warn("INVALID FORMAT: cannot parse xml. Xml root name not recognised.", UserWarning)


