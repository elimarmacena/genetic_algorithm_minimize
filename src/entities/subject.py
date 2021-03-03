import constans as const
class Subject:
    #every subject have a fixed sized list
    def __init__(self, bit_list=list([0]*16)):
        self.bit_list = bit_list
        self.value = self.__get_decimal_value()
        self.x_value = self.__get_x_value()
    

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
