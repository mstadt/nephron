import equations
import math
import numpy as np
from Newton import Jac

def newton_preg_rat(func,x,k,cell):
    if cell.humOrrat != 'rat':
        print('humOrrat:' + cell.humOrrat)
        raise Exception('newton_preg_rat only for rat model')
    if cell.sex.lower() != 'female':
        print('sex: ' + cell.sex)
        raise Exception('newton_preg only for pregnant female rat')
    fun=equations.conservation_eqs
    f=np.matrix(fun(x,k))
    TOLpcn = 1
    i = 1
    iter = 0
    while(np.linalg.norm(f) > 0.0001) and (iter<150): 
        if np.linalg.norm(f)>1e12:
            print('segment: ' + cell.segment)
            raise Exception('Newton solver diverged')

        i += 1
        J = np.matrix(Jac(fun,x,k))
        IJ = J.I
        F = np.matrix(fun(x,k))
        # PCT
        if cell.segment == 'PT':
            amp = 1.0
        # S3
        elif cell.segment == 'S3':
            amp = 1.0 
        # SDL
        elif cell.segment == 'SDL':
            amp = 1.0 #0.2
        # LDL
        elif cell.segment == 'LDL':
            if np.linalg.norm(f)>5000:
                amp = 0.5
            else:
                amp = 1.0
        # LAL
        elif cell.segment == 'LAL':
            if np.linalg.norm(f)>5000:
                amp = 0.5
            else:
                amp = 1.0
        # mTAL
        elif cell.segment == 'mTAL':
            if np.linalg.norm(f)>5000:
                amp = 0.5 #0.2
            else:
                amp = 1.0 #0.9
        # cTAL
        elif cell.segment == 'cTAL':
            if np.linalg.norm(f)>5000:
                amp = 0.5 #0.2
            else:
                amp = 1.0 #0.8
        # DCT
        elif cell.segment == 'DCT':
            amp = 1.0
            # if iter < 100:
            #     amp = 1.0
            # else:
            #     amp = 0.7
        # CNT
        elif cell.segment == 'CNT':
            if cell.sex == 'female':
                if cell.type == 'sup':
                    if np.linalg.norm(f)>1000:
                        amp = 1.0 #0.17
                    elif np.linalg.norm(f)>100:
                        amp = 1.0 #0.6
                    else:
                        amp = 1.0 #0.9
                elif cell.type == 'jux1':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17
                        else:
                            amp = 0.3
                    else:
                        amp = 1.0 #0.8
                elif cell.type == 'jux2':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17
                        else:
                            amp = 0.3
                    else:
                        amp = 1.0 #0.8
                elif cell.type == 'jux3':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17
                        else:
                            amp = 0.3
                    else:
                        amp = 1.0 #0.8
                elif cell.type == 'jux4':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17
                        else:
                            amp = 0.3
                    else:
                        amp = 1.0 #0.8
                elif cell.type == 'jux5':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17
                        else:
                            amp = 0.3
                    else:
                        amp =1.0 # 0.8
                else:
                    if np.linalg.norm(f) > 5000:
                        amp = 0.13
                    else:
                        amp = 1.0 #0.81
            elif cell.sex == 'male':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0 #0.8
        # CCD     
        elif cell.segment == 'CCD':
            if cell.preg == 'mid':
                if np.linalg.norm(f)>5000:
                    if k==0:
                        amp = 0.1 
                    else:
                        amp = 0.5
                elif np.linalg.norm(f)>1000:
                    amp = 1.0   
                elif iter > 75:
                    if np.linalg.norm(f)>1:
                        amp = 0.8
                    else:
                        amp = 0.95
                else:
                    amp = 1.0
            elif cell.preg == 'late':
                if np.linalg.norm(f)>1000:
                    if k==0:
                        amp = 0.1
                    else:
                        amp = 1.0 #0.8
                else:
                    amp = 1.0 #0.8
        # OMCD
        elif cell.segment == 'OMCD':
            amp = 1.0
        # IMCD
        elif cell.segment == 'IMCD':
            if cell.preg == 'mid':
                if np.linalg.norm(f)>5000:
                    if k==0:
                        amp = 0.25 
                    else:
                        amp = 0.5 
                elif np.linalg.norm(f)>1000:
                    amp = 1.0 #0.5
                elif iter>75:
                    amp = 0.95
                else:
                    amp = 1.0
            elif cell.preg == 'late':
                if np.linalg.norm(f)>5000:
                    if k==0:
                        amp = 1.0 #0.1 
                    else:
                        amp = 1.0 #0.5 
                elif np.linalg.norm(f)>1000:
                    amp =1.0 # 0.5
                else:
                    amp = 1.0
        else:
            print('What is this segment?', cell.segment)
            raise Exception('cell.segment is not characterized')
        delta = amp*np.array(F*IJ.T)[0]
        x-= delta
        f = np.matrix(fun(x,k))
        iter+=1
        print(iter, np.linalg.norm(f))
        TOLpcn = np.max(delta/x)
    return x
        
