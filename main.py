from FilesInteractions import *
from FieldDrowing import *
import numpy as np
import os
import neat

# Creating new table of spots
Spots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
OponentSpots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
# making each spot free
create_spots(Spots)
create_spots(OponentSpots)
# importing team from xml
import_team_from_xml("testTeam.xml", Spots)
import_team_from_xml("testTeamOP.xml", OponentSpots)

# init(Spots, OponentSpots, 0)

# export_team_to_xml(Spots, "exportTeam.xml")
# export_character_to_xml(Spots[0][0].Character, "export.xml")
#
# print_team_matrix(Spots)
# print_oponent_team(OponentSpots)


def eval_genoms(genomes, config):

    nets = []
    ge = []
    for genome_id, genome in enumerate(genomes):
        genome[1].fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome[1], config)
        nets.append(net)
        ge.append(genome[1])

        # Creating new table of spots
        Spots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
        OponentSpots = np.empty(shape=(COLUMNS, ROWS), dtype=object)
        # making each spot free
        create_spots(Spots)
        create_spots(OponentSpots)
        # importing team from xml
        import_team_from_xml("testTeam.xml", Spots)
        import_team_from_xml("testTeamOP.xml", OponentSpots)

        print("Genome: ", genome_id)
        init(Spots, OponentSpots, genome[1], nets, genome_id-1)

def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genoms, 10)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)