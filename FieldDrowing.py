import pygame
import numpy as np
from TeamOrganization import *
pygame.init()

(width, height) = (800, 600)
char_height = 100
char_width = 100

char_height2 = 100
char_width2 = 200

hpbar_hight = 20
hpbar_width = 100
hpbar_width2 = 200
hpbar_diference = 100
player_start_pos = [(50, 50), (50, 180), (50, 310), (150, 50), (150, 180), (150, 310)]
cpu_start_pos = [(550, 50), (550, 180), (550, 310), (450, 50), (450, 180), (450, 310)]

bg_color = (255, 255, 255)
character_bg_color = (192, 192, 192)
hpbar_bgcolor = (255, 255, 0)
hpbar_color = (255, 0, 0)

font = pygame.font.SysFont("calibri", 20)

screen = pygame.display.set_mode((width, height))

(player, cpu) = ([], [])


def init(team1, team2):
    running = True
    screen.fill(bg_color)
    print_bg()
    print_player_team(team1)
    print_cpu_team(team2)
    print(player, cpu)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pos = pygame.mouse.get_pos()
        check_team(pos, player, team1)
        check_team(pos, cpu, team2)
        pygame.display.flip()


def check_team(cursor, team, matrix):
    for ch in team:
        if is_cursor_over(cursor, ch):
            character = Character()
            if ch[1] == 0:
                character = matrix[0][0]
            elif ch[1] == 1:
                character = matrix[0][1]
            elif ch[1] == 2:
                character = matrix[0][2]
            elif ch[1] == 3:
                character = matrix[1][0]
            elif ch[1] == 4:
                character = matrix[1][1]
            elif ch[1] == 5:
                character = matrix[1][2]
            if character.isTaken:
                print_info(character.Character)


def is_cursor_over(cursor, rect):
    left = rect[0][0]
    right = rect[0][0] + rect[0][2]
    up = rect[0][1]
    down = rect[0][1] + rect[0][3]
    if left <= cursor[0] <= right and up <= cursor[1] <= down:
        return True
    else:
        return False


def print_bg():
    for i in range(ROWS * COLUMNS):
        player.append((pygame.draw.rect(screen, character_bg_color, pygame.Rect(player_start_pos[i][0],
                                                                                player_start_pos[i][1],
                                                                                char_width, char_height)), i))

        pygame.draw.rect(screen, hpbar_bgcolor,
                         pygame.Rect(player_start_pos[i][0], player_start_pos[i][1] + hpbar_diference, hpbar_width,
                                     hpbar_hight))

        cpu.append((pygame.draw.rect(screen, character_bg_color, pygame.Rect(cpu_start_pos[i][0], cpu_start_pos[i][1],
                                                                             char_width, char_height)), i))
        pygame.draw.rect(screen, hpbar_bgcolor,
                         pygame.Rect(cpu_start_pos[i][0], cpu_start_pos[i][1] + hpbar_diference, hpbar_width,
                                     hpbar_hight))


def print_player_team(team):
    i = 0
    for column in range(COLUMNS):
        for row in range(ROWS):
            character = team[column][row].Character
            if team[column][row].is_taken and character.Alive:
                char_img = pygame.image.load(character.Image)
                if character.Size == 1:
                    char_img = pygame.transform.scale(char_img, (char_width, char_height))
                    screen.blit(char_img, (player_start_pos[i][0], player_start_pos[i][1]))

                    pygame.draw.rect(screen, hpbar_color,
                                     pygame.Rect(player_start_pos[i][0], player_start_pos[i][1] + hpbar_diference,
                                                 hpbar_width * (character.currentHP / character.HP), hpbar_hight))
                else:
                    if column != 1:
                        char_img = pygame.transform.scale(char_img, (char_width2, char_height2))
                        screen.blit(char_img, (player_start_pos[i][0], player_start_pos[i][1]))

                        pygame.draw.rect(screen, hpbar_color, pygame.Rect(player_start_pos[i][0], player_start_pos[i][1] + hpbar_diference,
                                                                          hpbar_width2 * (character.currentHP / character.HP), hpbar_hight))
            i += 1


def print_cpu_team(team):
    i = 0
    for column in range(COLUMNS):
        for row in range(ROWS):
            character = team[column][row].Character
            if character.Alive and team[column][row].is_taken:
                char_img = pygame.image.load(character.Image)
                if character.Size == 1:
                    char_img = pygame.transform.scale(char_img, (char_width, char_height))
                    char_img = pygame.transform.flip(char_img, True, False)
                    screen.blit(char_img, (cpu_start_pos[i][0], cpu_start_pos[i][1]))

                    pygame.draw.rect(screen, hpbar_color,
                                     pygame.Rect(cpu_start_pos[i][0], cpu_start_pos[i][1] + hpbar_diference,
                                                 hpbar_width * (character.currentHP / character.HP), hpbar_hight))

                else:
                    if column != 0:
                        char_img = pygame.transform.scale(char_img, (char_width2, char_height2))
                        char_img = pygame.transform.flip(char_img, True, False)
                        screen.blit(char_img, (cpu_start_pos[i][0], cpu_start_pos[i][1]))

                        pygame.draw.rect(screen, hpbar_color,
                                         pygame.Rect(cpu_start_pos[i][0], cpu_start_pos[i][1] + hpbar_diference,
                                                     hpbar_width2 * (character.currentHP / character.HP), hpbar_hight))

            i += 1


# TODO: extend this method
# method prints information about character


def print_info(character):
    pygame.draw.rect(screen, character_bg_color, pygame.Rect(50, 450, 500, 100))
    char_img = pygame.image.load(character.Image)
    if character.Size == 1:
        char_img = pygame.transform.scale(char_img, (char_width, char_height))
    else:
        char_img = pygame.transform.scale(char_img, (char_width2, char_height2))
    name = font.render(("Name: " + character.Name), False, (0, 0, 0))
    hp = font.render(("HP: " + str(character.currentHP) + " / " + str(character.HP)), False, (0, 0, 0))
    attack = font.render(("Attack: " + str(character.Attack)), False, (0, 0, 0))
    deff = font.render(("Defense: " + str(character.Deff)), False, (0, 0, 0))
    init = font.render(("Initiative: " + str(character.Init)), False, (0, 0, 0))
    screen.blit(char_img, (50, 450))
    screen.blit(name, (260, 450))
    screen.blit(hp, (260, 470))
    screen.blit(attack, (260, 490))
    screen.blit(deff, (260, 510))
    screen.blit(init, (260, 530))


