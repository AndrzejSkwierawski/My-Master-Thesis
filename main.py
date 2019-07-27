from FilesInteractions import *
import numpy as np

x = Character(name="Bary", hp=100)
y = Character(name="Adison", hp=90, deff=50)
z = Character(name="gruby", size=2)

# 1 2     2 1
# 3 4     4 3
# 5 6     6 5
# if the index is devided by 2 the character stands in first line

# 1 4    4 1
# 2 5    5 2
# 3 6    6 3
# if the index of character is from 4 to 6 it stands in first line

# the second model is more useful, while we check for reachable characters we just have to solve difference between indexes

# Creating new table of spots
Spots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
OponentSpots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
# making each spot free
create_spots(Spots)
create_spots(OponentSpots)

import_team_from_xml("testTeam.xml", Spots)
import_team_from_xml("testTeam.xml", OponentSpots)

# place_character_in_spot(Spots, [1, 1], x)
# place_character_in_spot(OponentSpots, [1, 1], y)
# place_character_in_spot(Spots, [0, 0], y)
# place_character_in_spot(Spots, [1, 2], z)
# place_character_in_spot(Spots, [1, 1], z) # this should create warinig



print_team_matrix(Spots)
print_oponent_team(OponentSpots)

z.print_properties()

# x.attack_character(Spots[1][2].Character)

# x.attack_character(OponentSpots[0][1].Character)


# TODO: method for checking if the characters is reachable for current character
