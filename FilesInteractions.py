from Character import *
import xml.etree.ElementTree as et


def import_character_from_xml(xml, character):
    tree = et.parse(xml)
    root = tree.getroot()
    if root.tag == "character":
        for child in root:
            if child.tag == "name":
                character.Name = child.text
            elif child.tag == "attack":
                character.Attack = child.text
            elif child.tag == "hp":
                character.HP = character.currentHP = child.text
            elif child.tag == "init":
                character.Init = child.text
            elif child.tag == "def":
                character.Deff = child.text
            elif child.tag == "class":
                if child.text in character.ClassEnumerate: # TODO check if it key or values from dict if so get this values
                    character.Class = child.text
                else:
                    warnings.warn("INVALID FORMAT: class name not recognised", UserWarning)
            elif child.tag == "size":
                character.Size = child.text
    else:
        warnings.warn("INVALID FORMAT: cannot parse xml. Xml root name '" + root.tag + "' not recognised", UserWarning)


x = Character()
x.print_properties()

# tree = et.parse('testChar.xml')
# root = tree.getroot()
# print(root.tag)
#
# for child in root:
#     if child.tag == "name":
#         x.Name = child.text

import_character_from_xml(xml="testChar.xml", character=x)
x.print_properties()
