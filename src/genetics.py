"""
    File used to perform the all genetic logic.
"""
import utils.common as common
def start_evolution():
    first_gen = __create_gen(10)

"""
    function used to create a randomic population of @size_population subjects
    @Return: list of subject(class)
"""
def __create_gen(size_population:int):
    population = list()
    for(i in range(0, size_population, 1)):
        new_subject = common.random_list()
        population.append(new_subject)
    return population

