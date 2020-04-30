from Character import *
import warnings

ROWS = 3
COLUMNS = 2


def create_spots(table):
    for column in range(COLUMNS):
        for row in range(ROWS):
            table[column][row] = Spot()


def place_character_in_spot(team, spot, character):
    if character.Size == 1:
        if team[spot[0]][spot[1]].is_taken:
            warnings.warn("CANNOT PLACE THIS CHARACTER HERE")
        else:
            team[spot[0]][spot[1]].Character = character
            team[spot[0]][spot[1]].isTaken = True
    else:
        if any([x.is_taken for x in team[:, spot[1]]]):
            warnings.warn("CANNOT PLACE THIS CHARACTER HERE")
        else:
            team[0][spot[1]].Character = character
            team[1][spot[1]].Character = character
            team[0][spot[1]].isTaken = True
            team[1][spot[1]].isTaken = True


def print_team_matrix(matrix):
    print("--------------------------------------------------------")
    for row in range(ROWS):
        print("|", end="")
        for column in range(COLUMNS):
            if matrix[column][row].is_taken and matrix[column][row].character.Alive:
                print(matrix[column][row].character.Name, matrix[column][row].character.currentHP, "/",
                      matrix[column][row].character.HP, end="")
            else:
                print("xxx", end="")
            print("\t| ", end="")
        print()
    print("--------------------------------------------------------")


def print_oponent_team(matrix):
    print("--------------------------------------------------------")
    for row in range(ROWS):
        print("|", end="")
        for column in range(COLUMNS-1, -1, -1):
            if matrix[column][row].is_taken and matrix[column][row].character.Alive:
                print(matrix[column][row].character.Name, matrix[column][row].character.currentHP, "/",
                      matrix[column][row].character.HP, end="")
            else:
                print("xxx", end="")
            print("\t|", end="")
        print()
    print("--------------------------------------------------------")


class Spot:

    isTaken = False
    Character = Character()

    @property
    def is_taken(self):
        return self.isTaken

    @property
    def character(self):
        return self.Character

    def __init__(self):
        self.isTaken = False

    def print_status(self):
        print(self.is_taken)
