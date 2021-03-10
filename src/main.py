from entities.lab import Lab
from utils import constants as const
from utils import common
def main():
  # number of iterations in a population
  generation_life_list = [10,20]
  for lifetime in generation_life_list:
    generation_best_hist = dict()
    generation_hist = dict()
    print(f'THE LIFETIME {lifetime} GENERATION STARTED')
    # Note for my self: create a const at utils.constants EXECUTIONS
    # Every different lifetime generation must be executed @EXECUTIONS times
    for i in range(const.EXECUTIONS):
      print(f'* EXECUTION {i+1} STARTED')
      # starting a population
      # during our population creation the fitness is calculated
      population = Lab()
      fitness_population_text = ''.join(str(h.get_fitness())+'; ' for h in population.get_init_population())
      print(f'** INITIAL POPULATION FITNESS:{fitness_population_text}')
      generation_best_hist[(i,-1)]=population.get_best_fitness()
      generation_hist[(i,-1)]=population.get_init_population()
      current_lifetime = 0
      while current_lifetime < lifetime:
        print(f'** GENERATION {current_lifetime} ARE BEING CREATED')
        # Performing the selection
        print('*** Performing the Selection')
        population.championship()
        # Performing the crossover
        print('*** Performing the Crossover')
        population.crossover()
        # Performing the mutation
        print('*** Performing the Mutation')
        population.mutation()
        # Creating a new generation
        print('*** Finished the Generation Creation')
        new_gen = population.create_new_gen()
        generation_best_hist[(i,current_lifetime)]=population.get_best_fitness()
        generation_hist[(i,current_lifetime)]=population.get_current_population()
        print('========================')
        current_lifetime += 1
      # End While current_lifetime
    # End for I
    common.write_best(generation_best_hist,lifetime)
    common.write_history(generation_hist,lifetime)
  # End for lifetime
  print('=OVER=')




main()