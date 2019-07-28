import pygame
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
player = [(50, 50), (50, 180), (50, 310), (150, 50), (150, 180), (150, 310)]
cpu = [(550, 50), (550, 180), (550, 310), (450, 50), (450, 180), (450, 310)]

bg_color = (255, 255, 255)
character_bg_color = (192, 192, 192)
hpbar_bgcolor = (255, 255, 0)
hpbar_color = (255, 0, 0)

font = pygame.font.SysFont("calibri", 20)

screen = pygame.display.set_mode((width, height))
screen.fill(bg_color)


def init(team1, team2):
    print_bg()
    print_info()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        print_player_team(team1)
        print_cpu_team(team2)


def print_bg():
    #                                                   begging , w , h
    player1 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(player[0][0], player[0][1], char_width, char_height))
    player2 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(player[1][0], player[1][1], char_width, char_height))
    player3 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(player[2][0], player[2][1], char_width, char_height))
    player4 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(player[3][0], player[3][1], char_width, char_height))
    player5 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(player[4][0], player[4][1], char_width, char_height))
    player6 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(player[5][0], player[5][1], char_width, char_height))

    player1_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(player[0][0], player[0][1] + hpbar_diference, hpbar_width, hpbar_hight))
    player2_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(player[1][0], player[1][1] + hpbar_diference, hpbar_width, hpbar_hight))
    player3_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(player[2][0], player[2][1] + hpbar_diference, hpbar_width, hpbar_hight))
    player4_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(player[3][0], player[3][1] + hpbar_diference, hpbar_width, hpbar_hight))
    player5_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(player[4][0], player[4][1] + hpbar_diference, hpbar_width, hpbar_hight))
    player6_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(player[5][0], player[5][1] + hpbar_diference, hpbar_width, hpbar_hight))

    cpu1 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(cpu[0][0], cpu[0][1], char_width, char_height))
    cpu2 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(cpu[1][0], cpu[1][1], char_width, char_height))
    cpu3 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(cpu[2][0], cpu[2][1], char_width, char_height))
    cpu4 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(cpu[3][0], cpu[3][1], char_width, char_height))
    cpu5 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(cpu[4][0], cpu[4][1], char_width, char_height))
    cpu6 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(cpu[5][0], cpu[5][1], char_width, char_height))

    cpu1_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(cpu[0][0], cpu[0][1] + hpbar_diference, hpbar_width, hpbar_hight))
    cpu2_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(cpu[1][0], cpu[1][1] + hpbar_diference, hpbar_width, hpbar_hight))
    cpu3_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(cpu[2][0], cpu[2][1] + hpbar_diference, hpbar_width, hpbar_hight))
    cpu4_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(cpu[3][0], cpu[3][1] + hpbar_diference, hpbar_width, hpbar_hight))
    cpu5_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(cpu[4][0], cpu[4][1] + hpbar_diference, hpbar_width, hpbar_hight))
    cpu6_hpbar = pygame.draw.rect(screen, hpbar_bgcolor, pygame.Rect(cpu[5][0], cpu[5][1] + hpbar_diference, hpbar_width, hpbar_hight))


def print_player_team(team):
    i = 0
    for column in range(COLUMNS):
        for row in range(ROWS):
            character = team[column][row].Character
            if character.Alive and team[column][row].is_taken:
                if character.Class == 1:
                    char_img = pygame.image.load('images/warrior.jpg')
                elif character.Class == 2:
                    char_img = pygame.image.load('images/archer.jpg')
                elif character.Class == 3:
                    char_img = pygame.image.load('images/mage.jpg')
                else:
                    warnings.warn("UNRECOGNIZED CLASS OF CHARACTER")
                if character.Size == 1:
                    char_img = pygame.transform.scale(char_img, (char_width, char_height))
                    screen.blit(char_img, (player[i][0], player[i][1]))

                    pygame.draw.rect(screen, hpbar_color,
                                     pygame.Rect(player[i][0], player[i][1] + hpbar_diference,
                                                 hpbar_width * (character.currentHP / character.HP), hpbar_hight))
                else:
                    if column != 1:
                        char_img = pygame.transform.scale(char_img, (char_width2, char_height2))
                        screen.blit(char_img, (player[i][0], player[i][1]))

                        pygame.draw.rect(screen, hpbar_color, pygame.Rect(player[i][0], player[i][1] + hpbar_diference,
                                                                          hpbar_width2 * (character.currentHP / character.HP), hpbar_hight))
            i += 1


def print_cpu_team(team):
    color = (0, 255, 0)
    i = 0
    for column in range(COLUMNS):
        for row in range(ROWS):
            character = team[column][row].Character
            if character.Alive and team[column][row].is_taken:
                if character.Class == 1:
                    char_img = pygame.image.load('images/warrior.jpg')
                elif character.Class == 2:
                    char_img = pygame.image.load('images/archer.jpg')
                elif character.Class == 3:
                    char_img = pygame.image.load('images/mage.jpg')
                else:
                    warnings.warn("UNRECOGNIZED CLASS OF CHARACTER")
                if character.Size == 1:
                    pygame.draw.rect(screen, color, pygame.Rect(cpu[i][0], cpu[i][1], 10, 10))
                    char_img = pygame.transform.scale(char_img, (char_width, char_height))
                    char_img = pygame.transform.flip(char_img, True, False)
                    screen.blit(char_img, (cpu[i][0], cpu[i][1]))

                    pygame.draw.rect(screen, hpbar_color,
                                     pygame.Rect(cpu[i][0], cpu[i][1] + hpbar_diference,
                                                 hpbar_width * (character.currentHP / character.HP), hpbar_hight))

                else:
                    if column != 0:
                        pygame.draw.rect(screen, color, pygame.Rect(cpu[i][0], cpu[i][1], 20, 10))
                        char_img = pygame.transform.scale(char_img, (char_width2, char_height2))
                        char_img = pygame.transform.flip(char_img, True, False)
                        screen.blit(char_img, (cpu[i][0], cpu[i][1]))

                        pygame.draw.rect(screen, hpbar_color,
                                         pygame.Rect(cpu[i][0], cpu[i][1] + hpbar_diference,
                                                     hpbar_width2 * (character.currentHP / character.HP), hpbar_hight))

            i += 1


# TODO: extend this method
# method prints information about character


def print_info():
    pygame.draw.rect(screen, character_bg_color, pygame.Rect(50, 450, 200, 100))
    name = font.render("Name: ", False, (0, 0, 0))
    hp = font.render("HP: ", False, (0, 0, 0))
    attack = font.render("Attack: ", False, (0, 0, 0))
    deff = font.render("Defense: ", False, (0, 0, 0))
    init = font.render("Initiative: ", False, (0, 0, 0))
    screen.blit(name, (260, 450))
    screen.blit(hp, (260, 470))
    screen.blit(attack, (260, 490))
    screen.blit(deff, (260, 510))
    screen.blit(init, (260, 530))
