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
    
    fun=equations.conservation_eqs
    f=np.matrix(fun(x,k))
    TOLpcn = 1
    i = 1
    iter = 0
    while(np.linalg.norm(f) > 0.0001) and (iter<150): #(iter<300)
        i += 1
        J = np.matrix(Jac(fun,x,k))
        IJ = J.I
        F = np.matrix(fun(x,k))
        if cell.segment == 'PT':
            amp = 1
        elif cell.segment == 'S3':
            amp = 1
        elif cell.segment == 'SDL':
            amp = 1
        elif cell.segment == 'LDL':
            amp = 1
        elif cell.segment == 'LAL':
            amp = 1
        elif cell.segment == 'mTAL':
            amp = 1
        elif cell.segment == 'cTAL':
            amp = 1
        elif cell.segment == 'DCT':
            amp = 1
        elif cell.segment == 'CNT':
            amp = 1
        elif cell.segment == 'CCD':
            amp = 1
        elif cell.segment == 'OMCD':
            amp = 1
        elif cell.segment == 'IMCD':
            amp = 1
        else:
            print('What is this segment?', cell.segment)
            raise Exception('cell.segment is not characterized')
        