import utils.constants as const
from random import seed
from random import randint

seed(const.USED_SEED)
"""
    function used to create a randomic N bits list
    @Return: list of 0's and 1's
"""
def random_list():
    random_list = list([None] * const.USED_BITS)
    for i in range(len(random_list)):
        random_list[i] = randint(0,1)
    return random_list


def write_best(best_history:dict,lifetime:int):
    output_file = open('outputs/lifetime'+str(lifetime)+'_best_entities.txt','w')
    for i in range(const.EXECUTIONS):
        best_result = get_lowerst_best_iteration(best_history,i)
        output_file.write(f'ITERATION({i}) GEN({best_result[1]}): {best_result[0]} \n')
    output_file.close()

def get_lowerst_best_iteration(best_history, iteration):
    data_iteration = []
    for dict_keys in best_history.keys():
        if (dict_keys[0] == iteration):
            data_iteration.append([best_history[dict_keys],dict_keys[1]])
    data_iteration.sort(key=lambda x:x[0].get_fitness())
    return data_iteration[0]

def write_history(generation_hist:dict,lifetime:int):
    for i in range(const.EXECUTIONS):
        output_file = open('outputs/iteration'+str(i)+'_lifetime'+str(lifetime)+'_historic.txt','w')
        for dict_keys in generation_hist.keys():
            if dict_keys[0] == i:
                for current_value in generation_hist[dict_keys]:
                    output_file.write(f'[GEN({dict_keys[1]})] {current_value}\n')
                # End for current_value
            # End if
        # End for dict_keys
        output_file.close()
    # End for i

def write_mean_bests(best_history:dict,lifetime:int):
  output_file = open('outputs/lifetime'+str(lifetime)+'_mean.txt','w')
  mean_results = dict()
  for i in range(lifetime):
    generation_sum = 0
    for dict_keys in best_history.keys():
      if(dict_keys[1] == i):
        generation_sum += best_history[dict_keys].get_fitness()
      # End IF
    # End FOR dict_keys
    output_file.write(f'GENERATION[{i}]: {generation_sum/const.EXECUTIONS}\n')
  # End FOR i
  output_file.close
