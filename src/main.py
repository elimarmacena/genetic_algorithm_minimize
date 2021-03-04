from entities.lab import Lab
def main():
    # number of iterations in a population
    generation_life_list = [10,20]
    for lifetime in generation_life_list:
        print(f'THE POPULATION WITH LIFETIME {lifetime} ARE BEING CREATED')
        # starting a population
        # during our population creation the fitness is calculated
        population = Lab()
        fitness_population_text = ''.join(str(h.get_fitness())+'; ' for h in population.get_init_population())
        print(f'INITIAL POPULATION FITNESS:{fitness_population_text}')
        print(f'INITIAL BEST FITNESS:{population.get_best_fitness().get_fitness()}')
        current_lifetime = 0
        while current_lifetime < lifetime:
            # Performing the selection
            population.championship()
            # Performing the crossover
            population.crossover()
            # Performing the mutation
            population.mutation()
            # Creating a new generation
            new_gen = population.create_new_gen()
            print(f'GENERATION {current_lifetime+1} - BEST FITNESS')
            print(population.get_best_fitness().get_fitness())
            print('========================')
            current_lifetime += 1




main()