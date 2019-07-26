from Character import *
import warnings

ROWS = 3
COLUMNS = 2


def create_spots(table):
    for column in range(COLUMNS):
        for row in range(ROWS):
            table[column][row] = Spot()


def place_character_in_spot(spot, character):
    if spot.is_taken:
        warnings.warn("CANNOT PLACE THIS CHARACTER HERE")
    elif not spot.is_taken:
        spot.Character = character
        spot.isTaken = True


def print_team_matrix(matrix):
    print("----------------------------")
    for row in range(ROWS):
        print("| ", end="")
        for column in range(COLUMNS):
            if matrix[column][row].is_taken:
                print(matrix[column][row].character.Name, end="")
            else:
                print("xxx", end="")
            print(" |", end="")
        print()
    print("----------------------------")


def print_oponent_team(matrix):
    print("----------------------------")
    for row in range(ROWS):
        print("| ", end="")
        for column in range(COLUMNS-1, -1, -1):
            if matrix[column][row].is_taken:
                print(matrix[column][row].character.Name, end="")
            else:
                print("xxx", end="")
            print(" |", end="")
        print()
    print("----------------------------")


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

# TODO: make loading characters from file
# TODO: make placing characters in field from file
