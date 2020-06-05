from FilesInteractions import *
from FieldDrowing import *
import numpy as np
import os
import neat

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
        OponentSpots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
        # making each spot free
        create_spots(Spots)
        create_spots(OponentSpots)
        # importing team from xml
        import_team_from_xml("testTeam.xml", Spots)
        import_team_from_xml("testTeamOP2.xml", OponentSpots, True)

        # print("Genome: ", genome_id)
        # print_team_matrix(Spots)
        # print_oponent_team(OponentSpots)
        init(Spots, OponentSpots, genome, net, genome_of_generation, generation)

        # print_team_matrix(Spots)
        # print_oponent_team(OponentSpots)
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

    winner = p.run(eval_genoms, 10)

    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)