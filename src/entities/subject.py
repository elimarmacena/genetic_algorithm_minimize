import utils.constans as const
import math
class Subject:
    #every subject have a fixed sized list
    def __init__(self, bit_list=list([0]*16)):
        self.bit_list = bit_list
        self.value = self.__get_decimal_value()
        self.x_value = self.__get_x_value()
        self.fitness = self.__fitness()
    

    """
        Use the @bit_list to get the decimal representation
        @Return: decimal int
    """
    def __decimal_value(self):
        bit_string = ''.join(str(h) for h in self.bit_list)
        return int(bit_string,2)
    
    """
        Function used to calc the x value. function avaliable at resource\Especificacao.pdf on page 2
        @Return: float value
    """
    def __get_x_value(self):
        numerator = (const.MAX_INTERVAL - const.MIN_INTERVAL) * self.value
        denominator = pow(2,const.USED_BITS) - 1
        fraction = numerator / denominator
        x_value = const.MIN_INTERVAL + fraction
        return x_value
    
    """
        The fitness function used is the same function that we are trying to minimize.
        The function can be found at resource\Especificacao.pdf on page 1 (f(x)=cos(x)*x+2)
        @Return: float value
    """
    def __fitness(self):
        cos_value = math.cos(self.x_value)
        fitness_result = (cos_value * self.x_value) + 2
        return fitness_result

