from FilesInteractions import *
from FieldDrowing import *
import numpy as np
import os
import neat
import sys
import argparse
# # Creating new table of spots
# Spots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
# OponentSpots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
# # making each spot free
# create_spots(Spots)
# create_spots(OponentSpots)
# # importing team from xml
# import_team_from_xml("testTeam.xml", Spots)
# import_team_from_xml("testTeamOP.xml", OponentSpots)

# init(Spots, OponentSpots, 0)

# export_team_to_xml(Spots, "exportTeam.xml")
# export_character_to_xml(Spots[0][0].Character, "export.xml")
#
# print_team_matrix(Spots)
# print_oponent_team(OponentSpots)
generation = 0
number_of_generations = 10
teamP = 'testTeam.xml'
teamO = 'testTeamOP.xml'
graphic = False


def eval_genoms(genomes, config):
    global generation
    generation += 1
    genome_of_generation = 0
    for genome_id, genome in genomes:
        genome_of_generation += 1
        genome.fitness = 2000
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        # Creating new table of spots
        Spots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
        OpponentSpots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
        # making each spot free
        create_spots(Spots)
        create_spots(OpponentSpots)
        # importing team from xml
        import_team_from_xml(teamP, Spots)
        import_team_from_xml(teamO, OpponentSpots, True)

        # print_team_matrix(Spots)
        # print_oponent_team(OpponentSpots)
        init(Spots, OpponentSpots, genome, net, genome_of_generation, generation, graphic)

        # print_team_matrix(Spots)
        # print_oponent_team(OpponentSpots)
        print("Genome", genome_id, "fitness:", genome.fitness, "\t1/fitness:", 1.0 / genome.fitness)
        genome.fitness = 1.0 / genome.fitness


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genoms, number_of_generations)

    print('\nBest genome:\n{!s}'.format(winner))


def parse_args():
    print('Argument List:', str(sys.argv))
    parser = argparse.ArgumentParser()

    parser.add_argument('--gens', '-g', type=int, default=10, help='Number of generations')
    parser.add_argument('--teamp', '-p', type=str, default='testTeam.xml', help='File with player team')
    parser.add_argument('--teamo', '-o', type=str, default='testTeamOP.xml', help='File with opponent team')
    parser.add_argument('--image', '-i', action='store_true', help='If set, graphic interface will be shown')

    args = parser.parse_args()
    if args.gens:
        print("number of generations:", args.gens)
        global number_of_generations
        number_of_generations = args.gens
    if args.teamp:
        print("Player team:", args.teamp)
        global teamP
        teamP = args.teamp
    if args.teamo:
        print("Player team:", args.teamo)
        global teamO
        teamO = args.teamo
    if args.image:
        print("Graphic interface?:", args.image)
        global graphic
        graphic = args.image


if __name__ == '__main__':
    parse_args()
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
