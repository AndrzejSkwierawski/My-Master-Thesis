import random
from TeamOrganization import *

characters = []


def set_move_order(team1, team2):
    for column in range(COLUMNS):
        for row in range(ROWS):
            if team1[column][row].Character.Size == 1 or (team1[column][row].Character.Size == 2 and column != 0):
                if team1[column][row].is_taken and team1[column][row].Character.Alive:
                    characters.append(team1[column][row].Character)
            if team2[column][row].Character.Size == 1 or (team2[column][row].Character.Size == 2 and column != 0):
                if team2[column][row].is_taken and team2[column][row].Character.Alive:
                    characters.append(team2[column][row].Character)

    random.shuffle(characters)
    characters.sort(key=lambda char: char.Init, reverse=True)

    for character in characters:
        print(character.Name, character.Init, character.Position)

