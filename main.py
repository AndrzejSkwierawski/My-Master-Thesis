from FilesInteractions import *
from FieldDrowing import *
import numpy as np


# Creating new table of spots
Spots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
OponentSpots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
# making each spot free
create_spots(Spots)
create_spots(OponentSpots)
# importing team from xml
import_team_from_xml("testTeam.xml", Spots)
import_team_from_xml("testTeam.xml", OponentSpots)

init(Spots, OponentSpots)

export_team_to_xml(Spots, "exportTeam.xml")
export_character_to_xml(Spots[0][0].Character, "export.xml")


x = Character(name="Bary", hp=100)
y = Character(name="Adison", hp=90, deff=50)
# place_character_in_spot(Spots, [1, 1], x)
# place_character_in_spot(OponentSpots, [1, 1], y)
# place_character_in_spot(Spots, [0, 0], y)


print_team_matrix(Spots)
print_oponent_team(OponentSpots)


# x.attack_character(Spots[1][2].Character)

# x.attack_character(OponentSpots[0][1].Character)


# TODO: method for checking if the characters is reachable for current character
