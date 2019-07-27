import pygame

pygame.init()

(width, height) = (800, 600)
bg_color = (255, 255, 255)

character_bg_color = (0, 128, 255)
hpbra_color = (255, 0, 0)

font = pygame.font.SysFont("calibri", 20)



def init():
    screen = pygame.display.set_mode((width, height))
    screen.fill(bg_color)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        print_bg(screen)
        print_info(screen)


def print_bg(screen):
    #                                                   begging , w , h
    player1 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(50, 50, 100, 100))
    player2 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(50, 180, 100, 100))
    player3 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(50, 310, 100, 100))
    player4 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(150, 50, 100, 100))
    player5 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(150, 180, 100, 100))
    player6 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(150, 310, 100, 100))

    player1_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(50, 150, 100, 20))
    player2_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(50, 280, 100, 20))
    player3_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(50, 410, 100, 20))
    player4_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(150, 150, 100, 20))
    player5_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(150, 280, 100, 20))
    player6_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(150, 410, 100, 20))

    cpu1 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(450, 50, 100, 100))
    cpu2 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(450, 180, 100, 100))
    cpu3 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(450, 310, 100, 100))
    cpu4 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(550, 50, 100, 100))
    cpu5 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(550, 180, 100, 100))
    cpu6 = pygame.draw.rect(screen, character_bg_color, pygame.Rect(550, 310, 100, 100))

    cpu1_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(450, 150, 100, 20))
    cpu2_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(450, 280, 100, 20))
    cpu3_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(450, 410, 100, 20))
    cpu4_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(550, 150, 100, 20))
    cpu5_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(550, 280, 100, 20))
    cpu6_hpbar = pygame.draw.rect(screen, hpbra_color, pygame.Rect(550, 410, 100, 20))


# TODO: extend this method
# method prints information about character


def print_info(screen):
    pygame.draw.rect(screen, character_bg_color, pygame.Rect(50, 450, 100, 100))
    name = font.render("Name: ", False, (0, 0, 0))
    hp = font.render("HP: ", False, (0, 0, 0))
    attack = font.render("Attack: ", False, (0, 0, 0))
    deff = font.render("Defense: ", False, (0, 0, 0))
    init = font.render("Initiative: ", False, (0, 0, 0))
    screen.blit(name, (160, 450))
    screen.blit(hp, (160, 470))
    screen.blit(attack, (160, 490))
    screen.blit(deff, (160, 510))
    screen.blit(init, (160, 530))
