"""
    Class with the main methods to perform a genetic behavior
"""

import utils.common as common
import utils.constants as const
from entities.subject import Subject
from random import seed
from random import choice #function used to get a randomic item from a list
from random import randint
from random import random


class Lab:
    def __init__(self):
        self.population_size = const.POPULATION_SIZE
        # the population are sorted by the fitness value
        self.init_population = self.__create_gen(population_size)
        # the current population will be used on every population manipulation
        self.current_population = self.init_population
        # selected population
        self.selected_population = list()
        # crossovered population
        self.crossover_population = list()

        self.mutated_population = list()
        seed(const.USED_SEED)
    # GET AREA
    def get_init_population(self):
        return self.init_population
    def get_current_population(self):
        return self.current_population
    def get_selected_population(self):
        return self.selected_population
    def get_crossover_population(self):
        return self.crossover_population
    def get_mutated_population(self):
        return self.mutated_population
    # END AREA

    """
        The asked selection was with 2  subjects, but the number of subjects can be
        send as parameter
        @Return: list of subject(class)
    """
    def championship(self):
        current_round = 0
        winner_list = list()
        while current_round < self.population_size:
            battle_subject = list()
            for i in range(const.CHAMPIONSHIP_PICK):
                battle_subject.append(choice(self.current_population))
            # Here we pick the winner of the round, in this case we are using a random
            # to simulate the alternation of the best and the best and the worst.
            round_winner = randint(0,const.CHAMPIONSHIP_PICK-1)
            winner_list.append(battle_subject[round_winner])
            current_round += 1
        winner_list.sort(key=lambda x:x.get_fitness())
        self.selected_population = winner_list
        return winner_list

    """
        The crossover work with a percentage of @CROSSOVER_RATE, when the necessary rate isn't achived
        are used the two parents as result. This way we can have subjects without 
        crossover as final result.
        @Return: list of subject(class)
    """
    def crossover(self):
        cross_populaltion = []
        while(len(cross_populaltion) < self.population_size):
            current_rate = random()
            picker_1 = choice(self.selected_population)
            picker_2 = choice(self.selected_population)
            if current_rate >= const.CROSSOVER_RATE:    
                dna_size = len(picker_1.get_bit_list())
                # In the current approach we are using the one point cross over, in our case
                # using half of the 'DNA' of each subject to create a new one
                cross_list = picker_1.get_bit_list()[:(dna_size)//2] + picker_2.get_bit_list()[(dna_size//2):dna_size]
                cross_subject = Subject(cross_list)
                cross_populaltion.append(cross_subject)
            else:
                cross_populaltion.append(picker_1)
                cross_populaltion.append(picker_2)
        cross_populaltion.sort(key=lambda x:x.get_fitness())
        self.crossover_population = cross_populaltion
        return cross_populaltion

    """
        Performs a avaliation bit-bit of each subject in the @crossover_population. Each bit from each subject
        have @mutation_rate to be transformed, in our scenario, inverted.
        @Return: list of subject(class)
    """
    def mutation(self):
        mutation_population = []
        for current_subject in self.crossover_population:
            new_bit_list = []
            for i in current_subject.get_bit_list():
                mutation_value = random()
                if(mutation_value <= const.MUTATION_RATE):
                    #inverting the bit value
                    new_bit_list.append(0 if i == 1 else 1)
                else:
                    new_bit_list.append(i)
            #End for i
            mutation_subject = Subject(new_bit_list)
            mutation_population.append(mutation_subject)
        # End for current_subject
        mutation_population.sort(key=lambda x:x.get_fitness())
        self.mutated_population = mutation_population
        return mutation_population
    
    """
        This function create a new generation based on information getted on previous steps
        (selection(championship), crossover and mutation) and make us of elitism, here are
        preserved @ELITE_PERCENT of the highest fitness of our population. This way we can void the miss.
        @Return: list of subject(class)
    """
    def create_new_gen(self):
        if self.crossover_population == [] or self.selected_population == [] or self.mutated_population == []:
            raise RuntimeError('previous steps not performed')
        new_gen = list()
        new_gen = self.current_population[:int(self.population_size * const.ELITE_PERCENT)]
        new_gen = new_gen + self.mutated_population[:-int(self.population_size * const.ELITE_PERCENT)]
        new_gen.sort(key=lambda x:x.get_fitness())
        self.current_population = new_gen
        return new_gen

    """
        Function that return the best fitness value available.
        In the problem, the minor value is the best value
        @Return: Subject
    """
    def get_best_fitness(self):
        return self.current_population[0]

    """
        function used to create a randomic population of @size_population subjects
        @Return: list of subject(class)
    """
    def __create_gen(self,size_population:int):
        population = list()
        for i in range(0, size_population, 1):
            bit_list = common.random_list()
            new_subject = Subject(bit_list=bit_list)
            population.append(new_subject)
        population.sort(key=lambda x:x.get_fitness())
        return population

