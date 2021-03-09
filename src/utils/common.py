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
