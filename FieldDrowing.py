import pygame
from Order import *
pygame.init()

graphic = True

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
hpbar_bgcolor = (232, 232, 111)
hpbar_color = (255, 0, 0)
current_char_clolor = (116, 32, 169)

reachable_char_color = (85, 226, 41)

button_color1 = (85, 226, 41)
button_color2 = (109, 249, 66)

font = pygame.font.SysFont("calibri", 20)

screen = pygame.display.set_mode((width, height))

(player, cpu) = ([], [])

fitness = 0


def change_fitness(value):
    global fitness
    fitness += value


def refresh():
    if graphic:
        screen.fill(bg_color)
        print_bg()
        print_player_team(pteam)
        print_cpu_team(cteam)


def init(team1, team2, genome, net, index, generation, graphical=True):
    global graphic
    graphic = graphical
    global pteam
    global cteam
    global fitness
    window_title = "Generation: " + str(generation) + "; Genome: " + str(index)
    pygame.display.set_caption(window_title)
    fitness = 0
    pteam = team1
    cteam = team2
    running = True
    refresh()
    set_move_order(pteam, cteam)
    match = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pos = pygame.mouse.get_pos()
        if len(characters) != 0:
            if characters[0].flee:
                for column in range(COLUMNS):
                    for row in range(ROWS):
                        for team in pteam, cteam:
                            if len(characters) != 0:
                                if team[column][row].Character == characters[0] and characters[0].flee:
                                    if characters[0].Size == 1:
                                        team[column][row].isTaken = False
                                        # print(team[column][row].Character.Name, "fled")
                                    else:
                                        team[0][row].isTaken = False
                                        team[1][row].isTaken = False
                                        # print(team[column][row].Character.Name, "fled")
                                    characters.__delitem__(0)
                                    refresh()

            if not check_win() == 0:
                match = False
                # screen.fill(bg_color)
                if check_win() == 1:
                    screen.blit(font.render("WIN", True, (0, 0, 0)), (0, 0))
                    change_fitness(1000)
                    running = False
                elif check_win() == -1:
                    screen.blit(font.render("LOST", True, (0, 0, 0)), (0, 0))
                    change_fitness(-500)
                    running = False

            if match and len(characters) != 0:
                characters[0].cancel_defence()
                mark_current_character()
                mark_reachable(characters[0])

                if characters[0].OpponentTeam:
                    cpu_algorithm()
                else:
                    AI_algorithm(net)
                if len(characters) == 0:
                    set_move_order(pteam, cteam)

                check_team(pos, player, pteam)
                check_team(pos, cpu, cteam)
                if graphic:
                    button("Defense", (300, 100, 100, 45), button_color1, button_color2, "def")
                    button("   Wait", (300, 150, 100, 45), button_color1, button_color2, "wait")
                    button("   Flee", (300, 200, 100, 45), button_color1, button_color2, "flee")
        else:
            running = False
        pygame.display.flip()

    genome.fitness += fitness


def AI_algorithm(net):
    if len(characters) != 0 and not characters[0].OpponentTeam:
        target_character = Character(name="Dave", attack=0, hp=100000000000, init=0, deff=100)

        targets = []
        team_mates = []
        for column in range(COLUMNS):
            for row in range(ROWS):
                targets.append(cteam[column][row].Character)
                team_mates.append(pteam[column][row].Character)

        nn_input = [characters[0].Attack] + [characters[0].Class] + [characters[0].Spot[0], characters[0].Spot[1]] +\
                   [char.currentHP for char in targets] + [char.HP for char in targets] +\
                   [char.currentHP for char in team_mates] + [char.HP for char in team_mates]
        output = net.activate(nn_input)
        outcome = output.index(max(output))
        # print("\noutput:", output)
        # print("outcome:", outcome)
        if outcome == 0:
            characters[0].defence()
            characters.__delitem__(0)
        elif outcome == 1:
            characters[0].defence()
            #characters.append(characters[0])
            # characters[0].wait()
            characters.__delitem__(0)
        elif outcome == 2:
            characters[0].start_flee()
            characters[0].flee = True
            characters.__delitem__(0)
        else:
            if outcome == 3:
                target_character = cteam[0, 0].Character
            elif outcome == 4:
                target_character = cteam[0, 1].Character
            elif outcome == 5:
                target_character = cteam[0, 2].Character
            elif outcome == 6:
                target_character = cteam[1, 0].Character
            elif outcome == 7:
                target_character = cteam[1, 1].Character
            elif outcome == 8:
                target_character = cteam[1, 2].Character

            taken_points = attack(target_character)
            if taken_points <= 0:
                change_fitness(-10)
            else:
                change_fitness(taken_points)


def cpu_algorithm():
    if len(characters) != 0 and  characters[0].OpponentTeam:
        target_character = Character(name="Dave", attack=0, hp=100000000000, init=0, deff=100)
        prev_t_current_hp = target_character.currentHP
        prev_t_deff = target_character.Deff
        prev_t_current_deff = target_character.currentDeff
        certain = []
        for column in range(COLUMNS):
            for row in range(ROWS):
                if pteam[column][row].Character.CanBeReached:
                    t_current_hp = pteam[column][row].Character.currentHP
                    t_Deff = pteam[column][row].Character.Deff
                    t_current_deff = pteam[column][row].Character.currentDeff

                    if t_current_hp - characters[0].Attack * ((100 * (100 - t_current_deff) / 100) - t_Deff) / 100 <= 0:
                        certain.append(pteam[column][row].Character)

                    if t_current_hp - characters[0].Attack * (
                            (100 * (100 - t_current_deff) / 100) - t_Deff) / 100 < prev_t_current_hp - characters[
                        0].Attack * ((100 * (100 - prev_t_current_deff) / 100) - prev_t_deff) / 100:
                        target_character = pteam[column][row].Character

                        prev_t_current_hp = t_current_hp
                        prev_t_deff = t_Deff
                        prev_t_current_deff = t_current_deff
        if len(certain) == 0:
            takien_points = attack(target_character)
            change_fitness(-takien_points)
        else:
            prev_t_current_hp = 0
            prev_t_deff = 0
            prev_t_current_deff = 0
            for target in certain:
                if target.currentHP - characters[0].Attack * ((100 * (100 - target.currentDeff) / 100) - target.Deff) /\
                        100 > prev_t_current_hp - characters[0].Attack * ((100 * (100 - prev_t_current_deff) / 100) -
                                                                          prev_t_deff) / 100:
                    prev_t_current_hp = target.currentHP
                    prev_t_deff = target.Deff
                    prev_t_current_deff = target.currentDeff
                    target_character = target
            takien_points = attack(target_character)
            change_fitness(-takien_points)


def cpu_algorithm0():
    if any(any(item.Character == characters[0] for item in items) for items in cteam):
        target_character = Character(name="Dave", attack=0, hp=100000000000, init=0, deff=100)
        prev_t_current_hp = target_character.currentHP
        prev_t_deff = target_character.Deff
        prev_t_current_deff = target_character.currentDeff
        for column in range(COLUMNS):
            for row in range(ROWS):
                if pteam[column][row].Character.CanBeReached:
                    if pteam[column][row].Character.currentHP <= target_character.currentHP:
                        target_character = pteam[column][row].Character
        attack(target_character)


def cpu_algorithm1():
    if any(any(item.Character == characters[0] for item in items) for items in cteam):
        target_character = Character(name="Dave", attack=0, hp=100000000000, init=0, deff=100)
        prev_t_current_hp = target_character.currentHP
        prev_t_deff = target_character.Deff
        prev_t_current_deff = target_character.currentDeff
        for column in range(COLUMNS):
            for row in range(ROWS):
                if pteam[column][row].Character.CanBeReached:
                    t_current_hp = pteam[column][row].Character.currentHP
                    t_Deff = pteam[column][row].Character.Deff
                    t_current_deff = pteam[column][row].Character.currentDeff

                    if t_current_hp - characters[0].Attack * (
                            (100 * (100 - t_current_deff) / 100) - t_Deff) / 100 < prev_t_current_hp - characters[
                        0].Attack * ((100 * (100 - prev_t_current_deff) / 100) - prev_t_deff) / 100:
                        target_character = pteam[column][row].Character

                        prev_t_current_hp = t_current_hp
                        prev_t_deff = t_Deff
                        prev_t_current_deff = t_Deff
        attack(target_character)


# checks if mouse is over character
def check_team(cursor, team, matrix):
    for ch in team:
        if is_cursor_over(cursor, ch[0]):
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

                event = pygame.event.get()
                for event in event:
                    if event.type == pygame.MOUSEBUTTONUP and character.isTaken:
                        attack(character.Character)


def button(text, rect, color1, color2, action="none"):

    if is_cursor_over(pygame.mouse.get_pos(), rect):
        pygame.draw.rect(screen, color2, pygame.Rect(rect))
        mouse = pygame.mouse.get_pressed()[0]
        if mouse:
            if action == "def":
                characters[0].defence()
            elif action == "wait":
                characters.append(characters[0])
                characters[0].wait()
            elif action == "flee":
                characters[0].start_flee()
                characters[0].flee = True
            characters.__delitem__(0)
            if len(characters) == 0:
                set_move_order(pteam, cteam)
            refresh()

    else:
        pygame.draw.rect(screen, color1, pygame.Rect(rect))

    message = font.render(text, True, (0, 0, 0))
    screen.blit(message, ((rect[0] + rect[2]/6), (rect[1]) + rect[3]/3))


def is_cursor_over(cursor, rect):
    left = rect[0]
    right = rect[0] + rect[2]
    up = rect[1]
    down = rect[1] + rect[3]
    if left <= cursor[0] <= right and up <= cursor[1] <= down:
        return True
    else:
        return False


def attack(character):
    taken_points = 0
    if character.CanBeReached:
        if characters[0].Class == 1 or characters[0].Class == 2:
            taken_points = characters[0].attack_character(character)
        elif characters[0].Class == 3:
            for column in range(COLUMNS):
                for row in range(ROWS):
                    for team in pteam, cteam:
                        if team[column][row].Character.CanBeReached and team[column][row].Character.Alive and not \
                                (team[column][row].Character.Size == 2 and column == 1):
                            taken_points += characters[0].attack_character(team[column][row].Character)

    for each in characters:
        if not each.Alive:
            characters.remove(each)
    if len(characters) == 0:
        set_move_order(pteam, cteam)
    refresh()
    characters.__delitem__(0)
    return taken_points


def check_win():
    if all(all(not item.Character.Alive or not item.isTaken for item in items) for items in cteam):
        return 1
    if all(all(not item.Character.Alive or not item.isTaken for item in items) for items in pteam):
        return -1
    else:
        return 0


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
                    if character.flee:
                        char_img = pygame.transform.flip(char_img, True, False)
                    screen.blit(char_img, (player_start_pos[i][0], player_start_pos[i][1]))
                    character.Position = player_start_pos[i]

                    pygame.draw.rect(screen, hpbar_color,
                                     pygame.Rect(player_start_pos[i][0], player_start_pos[i][1] + hpbar_diference,
                                                 hpbar_width * (character.currentHP / character.HP), hpbar_hight))
                else:
                    if column != 1:
                        char_img = pygame.transform.scale(char_img, (char_width2, char_height2))
                        if character.flee:
                            char_img = pygame.transform.flip(char_img, True, False)
                        screen.blit(char_img, (player_start_pos[i][0], player_start_pos[i][1]))
                        character.Position = player_start_pos[i]

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
                    if not character.flee:
                        char_img = pygame.transform.flip(char_img, True, False)
                    screen.blit(char_img, (cpu_start_pos[i][0], cpu_start_pos[i][1]))
                    character.Position = cpu_start_pos[i]

                    pygame.draw.rect(screen, hpbar_color,
                                     pygame.Rect(cpu_start_pos[i][0], cpu_start_pos[i][1] + hpbar_diference,
                                                 hpbar_width * (character.currentHP / character.HP), hpbar_hight))

                else:
                    if column != 0:
                        char_img = pygame.transform.scale(char_img, (char_width2, char_height2))
                        if not character.flee:
                            char_img = pygame.transform.flip(char_img, True, False)
                        screen.blit(char_img, (cpu_start_pos[i][0], cpu_start_pos[i][1]))
                        character.Position = cpu_start_pos[i]

                        pygame.draw.rect(screen, hpbar_color,
                                         pygame.Rect(cpu_start_pos[i][0], cpu_start_pos[i][1] + hpbar_diference,
                                                     hpbar_width2 * (character.currentHP / character.HP), hpbar_hight))

            i += 1


def print_info(character):
    pygame.draw.rect(screen, character_bg_color, pygame.Rect(50, 450, 500, 120))
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
    char_class = font.render(("Class: " + str([key for (key, value) in
                                               character.ClassEnumerate.items() if value == character.Class][0])), False
                             , (0, 0, 0))
    screen.blit(char_img, (50, 450))
    screen.blit(name, (260, 450))
    screen.blit(hp, (260, 470))
    screen.blit(attack, (260, 490))
    screen.blit(deff, (260, 510))
    screen.blit(init, (260, 530))
    screen.blit(char_class, (260, 550))


def mark_current_character():
    if graphic:
        if not len(characters) == 0:
            if characters[0].Size == 1:
                pygame.draw.rect(screen, current_char_clolor, pygame.Rect(characters[0].Position, (char_width, 10)))
            else:
                pygame.draw.rect(screen, current_char_clolor, pygame.Rect(characters[0].Position, (char_width2, 10)))


def mark_reachable(character):
    if any(any(item.Character == character for item in items) for items in pteam):
        char_team = pteam
        oponent_team = cteam
    else:
        char_team = cteam
        oponent_team = pteam

    for column in range(COLUMNS):
        for row in range(ROWS):
            oponent_team[column][row].Character.CanBeReached = False
            char_team[column][row].Character.CanBeReached = False

    current_position = character.Spot
    if character.Class == 3 or character.Class == 2:
        for column in range(COLUMNS):
            for row in range(ROWS):
                if oponent_team[column][row].isTaken and oponent_team[column][row].Character.Alive:
                    oponent_team[column][row].Character.CanBeReached = True

    elif character.Class == 1:
        if current_position[0] == 0 and any(item.isTaken and item.Character.Alive for item in char_team[1]):
            print(character.Name, ", a Short Distance character is blocked by own teammate")
            # TODO: issue #6
        else:
            if any(item.isTaken and item.Character.Alive for item in oponent_team[1]):
                line = 1
            else:
                line = 0

            if current_position[1] == 0:
                if oponent_team[line][0].isTaken and oponent_team[line][0].Character.Alive:
                    oponent_team[line][0].Character.CanBeReached = True
                if oponent_team[line][1].isTaken and oponent_team[line][1].Character.Alive:
                    oponent_team[line][1].Character.CanBeReached = True
                if oponent_team[line][2].isTaken and oponent_team[line][2].Character.Alive and not \
                        (oponent_team[line][1].isTaken and oponent_team[line][1].Character.Alive) and not \
                        (oponent_team[line][0].isTaken and oponent_team[line][0].Character.Alive):
                    oponent_team[line][2].Character.CanBeReached = True

            elif current_position[1] == 1:
                for rows in range(ROWS):
                    if oponent_team[line][rows].Character.Alive and oponent_team[line][rows].isTaken:
                        oponent_team[line][rows].Character.CanBeReached = True

            elif current_position[1] == 2:
                if oponent_team[line][2].isTaken and oponent_team[line][2].Character.Alive:
                    oponent_team[line][2].Character.CanBeReached = True
                if oponent_team[line][1].isTaken and oponent_team[line][1].Character.Alive:
                    oponent_team[line][1].Character.CanBeReached = True
                if oponent_team[line][0].isTaken and oponent_team[line][0].Character.Alive and not \
                        (oponent_team[line][1].isTaken and oponent_team[line][1].Character.Alive) and not \
                        (oponent_team[line][2].isTaken and oponent_team[line][2].Character.Alive):
                    oponent_team[line][0].Character.CanBeReached = True
    if graphic:
        for column in range(COLUMNS):
            for row in range(ROWS):
                if oponent_team[column][row].Character.CanBeReached:
                    if oponent_team[column][row].Character.Size == 1:
                        pygame.draw.rect(screen, reachable_char_color, pygame.Rect(oponent_team[column][row].Character.
                                                                                   Position, (char_width, 10)))
                    else:
                        pygame.draw.rect(screen, reachable_char_color, pygame.Rect(oponent_team[column][row].Character.
                                                                                   Position, (char_width2, 10)))
