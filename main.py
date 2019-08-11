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

print_team_matrix(Spots)
print_oponent_team(OponentSpots)
