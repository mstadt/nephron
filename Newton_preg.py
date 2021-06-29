import equations
import math
import numpy as np
from Newton import Jac

def newton_preg_rat(func,x,k,cell):
    print('to do')
    if cell.humOrrat != 'rat':
        raise Exception('newton_preg_rat only for preg rat model')
    if cell.preg == 'non':
        raise Exception('newton_preg_rat for pregnant model')
        