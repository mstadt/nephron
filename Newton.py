#from numba import jit
import equations
import math
import numpy as np

#@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def Jac(func,x,k):

    epsfcn = 1.0e-3
    epsmch = 1.0e-3
    eps = math.sqrt(max(epsfcn,epsmch))
    
    Jfun=[[0 for i in range(len(x))] for i in range (len(x))]
    
    
    wa1=func(x,k)
    for i in range(len(x)):
        temp=x[i]
        h=eps*abs(temp)
        if (h==0):
            h=eps
        x[i]=temp+h
        fvec=func(x,k)
        x[i]=temp
        for j in range(len(x)):
            Jfun[j][i]=(-wa1[j]+fvec[j])/h
    
    return Jfun
    
#@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit    
def newton(func,x,k,cell):#cell.segment,cell.humOrrat = 'rat',cell.sex = 'male',cell.type = 'sup',cell.diabete='Non',cell.inhib=None,cell.unx='Y'


    fun=equations.conservation_eqs
    f = np.matrix(fun(x,k))
    # print(np.linalg.norm(f))    
    TOLpcn = 1
    i = 1
    iter=0
    while(np.linalg.norm(f) > 0.0001) and (iter<150): #(iter<300): #male: (iter<300)  female: (iter<100)
#        print("Iteration Times: " + str(i) + " with TOL " + str(TOLpcn) + "%")
        i += 1
        J = np.matrix(Jac(fun,x,k))
        IJ = J.I
        F = np.matrix(fun(x,k))

        if cell.humOrrat == 'rat' and cell.inhib == None:
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17# sup: 0.5
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.5
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>5000: # sup: 100
                            amp = 0.5# sup: 0.5; saline: 0.5;
                        else:
                            amp=0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.3; 
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15 ncc: 0.05
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15 nhe80:0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.1 # saline: 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 1.0
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if np.linalg.norm(f)>1000:
                    if k == 0:
                        amp = 0.5#0.005 male:0.5 female:0.005
                    else:
                        amp = 0.1
                else:
                    amp = 0.8
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    amp = 0.8#0.8 #normal male/female: 1.0, diabetic male: 0.8
                else:
                    amp = 1.0# normal male: 1.0, diabetic male: 0.8
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1
        elif cell.humOrrat == 'rat' and cell.inhib == 'NHE3-50':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100:				
                            amp = 0.17
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.7
                            else:
                                amp = 0.7
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.7
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.7
                        else:
                            if k == 9:
                                amp = 0.1
                            else:
                                amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.7
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.7
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>5000:
                            amp = 0.5
                        else:
                            amp=0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13  
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: 
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if np.linalg.norm(f)>1000:
                    if k == 0:
                        amp = 1.0
                    else:
                        amp = 0.1
                else:
                    amp = 0.8
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    amp = 0.8
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1
        elif cell.humOrrat == 'rat' and cell.inhib == 'NHE3-80':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.17
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>5000: # sup: 100
                            amp = 0.5# sup: 0.5; saline: 0.5;
                        else:
                            amp=0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            amp = 0.3
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.15 # nhe50: 0.15 ncc: 0.05
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.15 # nhe50: 0.15
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.15 # nhe50: 0.15
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1 # nhe50: 0.15 nhe80:0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17 # saline: 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if np.linalg.norm(f)>1000:
                    if k == 0:
                        amp = 0.7#0.005 male:0.5 female:0.005
                    else:
                        amp = 0.1
                else:
                    amp = 0.8
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    amp = 0.8#0.8 #normal male/female: 1.0, diabetic male: 0.8
                else:
                    amp = 1.0# normal male: 1.0, diabetic male: 0.8
            elif cell.segment == 'cTAL' or type == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1        
        elif cell.humOrrat == 'rat' and cell.inhib == 'NKCC2-70':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17# sup: 0.5
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.13
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>5000: # sup: 100
                            amp = 0.5# sup: 0.5; saline: 0.5;
                        else:
                            amp=0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17 # saline: 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if np.linalg.norm(f)>1000:
                    if k == 0:
                        amp = 1.0#0.005 male:0.5 female:0.005
                    else:
                        amp = 0.1
                else:
                    amp = 0.8
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    amp = 0.8#0.8 #normal male/female: 1.0, diabetic male: 0.8
                else:
                    amp = 1.0# normal male: 1.0, diabetic male: 0.8
            elif cell.segment == 'cTAL' or type == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1        
        elif cell.humOrrat == 'rat' and cell.inhib == 'NKCC2-100':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17# sup: 0.5
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.2
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>5000: # sup: 100
                            amp = 0.17
                        else:
                            amp=0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            amp = 0.3 # nhe50: 0.3; 
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.3
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.3
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.3
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.3
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17 # saline: 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if np.linalg.norm(f)>1000:
                    if k == 0:
                        amp = 1.0#0.005 male:0.5 female:0.005
                    else:
                        amp = 0.1
                else:
                    amp = 0.8
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    amp = 0.8#0.8 #normal male/female: 1.0, diabetic male: 0.8
                else:
                    amp = 1.0# normal male: 1.0, diabetic male: 0.8
            elif cell.segment == 'cTAL' or type == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1        
        elif cell.humOrrat == 'rat' and cell.inhib == 'NCC-70':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17# sup: 0.5
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>5000:
                            amp = 0.17
                        else:
                            amp=0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17 # saline: 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if np.linalg.norm(f)>1000:
                    if k == 0:
                        amp = 1.0#0.005 male:0.5 female:0.005
                    else:
                        amp = 0.1
                else:
                    amp = 0.8
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    amp = 0.8#0.8 #normal male/female: 1.0, diabetic male: 0.8
                else:
                    amp = 1.0# normal male: 1.0, diabetic male: 0.8
            elif cell.segment == 'cTAL' or type == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1        
        elif cell.humOrrat == 'rat' and cell.inhib == 'NCC-100':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.05
                            else:
                                amp = 1.0
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            if k==0:
                                amp = 0.05
                            else:
                                amp =0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            if k==0:
                                amp = 0.05
                            else:
                                amp =0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            if k==0:
                                amp = 0.05
                            else:
                                amp =0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            if k==0:
                                amp = 0.05
                            else:
                                amp =0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if np.linalg.norm(f)>1000:
                    if k == 0:
                        amp = 1.0#0.005 male:0.5 female:0.005
                    else:
                        amp = 0.1
                else:
                    amp = 0.8
            elif cell.segment == 'OMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        amp = 0.8#0.8 #normal male/female: 1.0, diabetic male: 0.8
                    else:
                        amp = 1.0# normal male: 1.0, diabetic male: 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp = 1.0
            elif cell.segment == 'cTAL' or type == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1        
        elif cell.humOrrat == 'rat' and cell.inhib == 'ENaC-70':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17# sup: 0.5
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.05
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>5000: # sup: 100
                            amp = 0.5# sup: 0.5; saline: 0.5;
                        else:
                            amp=0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.3; 
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15 ncc: 0.05
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15 nhe80:0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17 # saline: 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if np.linalg.norm(f)>1000:
                    if k == 0:
                        amp = 1.0#0.005 male:0.5 female:0.005
                    else:
                        amp = 0.1
                else:
                    amp = 0.8
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    amp = 0.8#0.8 #normal male/female: 1.0, diabetic male: 0.8
                else:
                    amp = 1.0# normal male: 1.0, diabetic male: 0.8
            elif cell.segment == 'cTAL' or type == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1        
        elif cell.humOrrat == 'rat' and cell.inhib == 'ENaC-100':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17# sup: 0.5
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.17
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.05
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.05
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>5000: # sup: 100
                            amp = 0.5# sup: 0.5; saline: 0.5;
                        else:
                            amp=0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.3; 
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15 ncc: 0.05
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17 # saline: 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>1000:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.1
                    else:
                        amp = 1.0
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>1000:
                        if k == 0:
                            amp = 1.0
                        else:
                            amp = 0.1
                    else:
                        amp = 1.0
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    if cell.sex == 'male':
                        amp = 0.5
                    elif cell.sex == 'female':
                        amp = 0.7
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or type == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1
        elif cell.humOrrat == 'rat' and cell.inhib == 'SNB-70':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17# sup: 0.5
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.05
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.05
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.05
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>1000: # sup: 100
                            amp = 0.1# sup: 0.5; saline: 0.5;
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            amp = 0.13 # nhe50: 0.3; 
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15 ncc: 0.05
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17 # saline: 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>1000:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.1
                    else:
                        amp = 1.0
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>1000:
                        if k == 0:
                            amp = 1.0
                        else:
                            amp = 0.1
                    else:
                        amp = 1.0
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    if cell.sex == 'male':
                        amp = 0.5
                    elif cell.sex == 'female':
                        amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or type == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1		        
        elif cell.humOrrat == 'rat' and cell.inhib == 'SNB-100':
            if cell.segment=='DCT':
                amp = 1
            elif cell.segment == 'CNT':
                if cell.sex =='female':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>100: # sup: 100							
                            amp = 0.17# sup: 0.5
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>5000:
                            if k == 0:
                                amp = 0.05
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.05
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.05
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
                elif cell.sex =='male':
                    if cell.type =='sup':
                        if np.linalg.norm(f)>1000: # sup: 100
                            amp = 0.1# sup: 0.5; saline: 0.5;
                        else:
                            amp=1.0
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            amp = 0.13 # nhe50: 0.3; 
                        else:
                            amp = 1.0
                    elif cell.type == 'jux2': 
                        if np.linalg.norm(f)>5000:
                            amp = 0.13 # nhe50: 0.15 ncc: 0.05
                        else:
                            amp = 1.0
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>5000:
                            amp = 0.1
                        else:
                            amp = 1.0
                    else:
                        if np.linalg.norm(f)>5000:
                            amp = 0.15
                        else:
                            amp = 1.0
            elif cell.segment == 'SDL':
                amp = 0.2
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>1000: # 100
                        if k==0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8#1.0 male:0.7 female:0.8
                        else:
                            amp = 0.8
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>5000:
                        if k==0:
                            amp = 0.17 # saline: 0.17
                        else:
                            amp = 0.2
                    else:
                        if k==0:
                            amp = 0.8
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>1000:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.1
                    else:
                        amp = 1.0
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>1000:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.1
                    else:
                        amp = 1.0
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    if cell.sex == 'male':
                        amp = 0.5
                    elif cell.sex == 'female':
                        amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or type == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8 # normal male: 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2 #0.2
                else:
                    amp = 1.0
            elif cell.segment == 'LDL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            elif cell.segment == 'LAL':
                if np.linalg.norm(f)>5000:
                    amp = 0.5
                else:
                    amp = 1.0
            else:
                amp = 1		        
        elif cell.humOrrat == 'hum' and cell.inhib == 'ACE':
            if cell.segment == 'S3':
                amp = 1.0 
            elif cell.segment == 'SDL':
                amp = 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8             
            elif cell.segment=='DCT':
                if cell.sex == 'male':
                    amp = 0.5
                elif cell.sex == 'female':
                    amp = 1.0
            elif cell.segment == 'CNT':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp=0.8
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        if np.linalg.norm(f)>100:
                            amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.09
                            else:
                                amp = 0.13
                        else:
                            amp = 0.8
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.8 
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.4
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
            elif cell.segment == 'OMCD':
                if np.linalg.norm(f)>100:
                    amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                else:
                    amp = 0.8#male:0.8 female:
            elif cell.segment == 'IMCD':
                if np.linalg.norm(f)>100:
                    if k==0:
                        amp = 0.2 # male:0.1 female:0.2
                    else:
                        amp = 0.1 # male:0.2 female:0.2
                else:
                    if k==0:
                        amp = 1.5# male:0.5 female:0.5
                    else:
                        amp = 0.9 # male:0.5 female:0.5      
            else:
                amp = 1.0
        elif cell.humOrrat == 'hum' and cell.diabete == 'Non' and cell.inhib !='SGLT2' and cell.unx == 'N':
            if cell.segment == 'S3':
                amp = 1.0 
            elif cell.segment == 'SDL':
                amp = 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8             
            elif cell.segment=='DCT':
                if cell.sex == 'female' and cell.type == 'jux1':
                    amp = 0.9
                elif cell.sex == 'female' and cell.type == 'jux3':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'jux2':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'sup':
                    if np.linalg.norm(f)>2000:
                        amp = 0.5
                    else:
                        amp = 0.5
                else:
                    amp = 0.5
            elif cell.segment == 'CNT':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp=0.8
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        if np.linalg.norm(f)>100:
                            amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.13
                        else:
                            amp = 0.8
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.3
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
            elif cell.segment == 'OMCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.2 # male:0.1 female:0.2
                        else:
                            amp = 0.1 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.5# male:0.5 female:0.5
                        else:
                            amp = 0.5 # male:0.5 female:0.5      
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.27#0.19 # male:0.1 female:0.2
                        else:
                            amp = 0.2 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.8# male:0.5 female:0.5
                        else:
                            amp = 0.8 # male:0.5 female:0.5   
            else:
                amp = 1.0
        elif cell.humOrrat == 'hum' and cell.diabete == 'Non' and cell.inhib == 'SGLT2' and cell.unx == 'N':
            if cell.segment == 'S3':
                amp = 1.0 
            elif cell.segment == 'SDL':
                amp = 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8             
            elif cell.segment=='DCT':
                if cell.sex == 'female' and cell.type == 'jux1':
                    amp = 0.9
                elif cell.sex == 'female' and cell.type == 'jux3':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'jux2':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'sup':
                    if np.linalg.norm(f)>2000:
                        amp = 0.5
                    else:
                        amp = 0.5
                else:
                    amp = 0.5
            elif cell.segment == 'CNT':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp=0.8
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        if np.linalg.norm(f)>100:
                            amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.13
                        else:
                            amp = 0.8
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.3
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.8
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.8
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
            elif cell.segment == 'OMCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.2 # male:0.1 female:0.2
                        else:
                            amp = 0.1 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.5# male:0.5 female:0.5
                        else:
                            amp = 0.5 # male:0.5 female:0.5      
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.27#0.19 # male:0.1 female:0.2
                        else:
                            amp = 0.2 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.8# male:0.5 female:0.5
                        else:
                            amp = 0.8 # male:0.5 female:0.5   
            else:
                amp = 1.0        
        elif cell.humOrrat == 'hum' and cell.diabete == 'Non' and cell.inhib == 'SGLT2' and cell.unx == 'Y':
            if cell.segment == 'S3':
                amp = 1.0 
            elif cell.segment == 'SDL':
                amp = 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8             
            elif cell.segment=='DCT':
                if cell.sex == 'female' and cell.type == 'jux1':
                    amp = 0.9
                elif cell.sex == 'female' and cell.type == 'jux3':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'jux2':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'sup':
                    if np.linalg.norm(f)>2000:
                        amp = 0.8
                    else:
                        amp = 0.5
                else:
                    amp = 0.5
            elif cell.segment == 'CNT':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp=0.8
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        if np.linalg.norm(f)>100:
                            amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.13
                        else:
                            amp = 0.8
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.3
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
            elif cell.segment == 'OMCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.2 # male:0.1 female:0.2
                        else:
                            amp = 0.1 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.5# male:0.5 female:0.5
                        else:
                            amp = 0.5 # male:0.5 female:0.5      
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.23#0.19 # male:0.1 female:0.2
                        else:
                            amp = 0.2 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.8# male:0.5 female:0.5
                        else:
                            amp = 0.8 # male:0.5 female:0.5   
            else:
                amp = 1.0                
        elif cell.humOrrat == 'hum' and cell.diabete == 'Moderate' and cell.inhib != 'SGLT2':
            if cell.segment == 'S3':
                amp = 1.0 
            elif cell.segment == 'SDL':
                amp = 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8             
            elif cell.segment=='DCT':
                if cell.sex == 'female' and cell.type == 'jux1':
                    amp = 0.9
                elif cell.sex == 'female' and cell.type == 'jux3':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'jux2':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'sup':
                    if np.linalg.norm(f)>2000:
                        amp = 0.5
                    else:
                        amp = 0.5
                else:
                    amp = 0.5
            elif cell.segment == 'CNT':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp=0.8
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        if np.linalg.norm(f)>100:
                            amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.13
                        else:
                            amp = 0.8
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.3
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
            elif cell.segment == 'OMCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.2 # male:0.1 female:0.2
                        else:
                            amp = 0.1 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.5# male:0.5 female:0.5
                        else:
                            amp = 0.5 # male:0.5 female:0.5      
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.19#0.19 # male:0.1 female:0.2
                        else:
                            amp = 0.17 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.8# male:0.5 female:0.5
                        else:
                            amp = 0.8 # male:0.5 female:0.5   
            else:
                amp = 1.0
        elif cell.humOrrat == 'hum' and cell.diabete == 'Moderate' and cell.inhib == 'SGLT2':
            if cell.segment == 'S3':
                amp = 1.0 
            elif cell.segment == 'SDL':
                amp = 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8             
            elif cell.segment=='DCT':
                if cell.sex == 'female' and cell.type == 'jux1':
                    amp = 0.9
                elif cell.sex == 'female' and cell.type == 'jux3':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'jux2':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'sup':
                    if np.linalg.norm(f)>2000:
                        amp = 0.7
                    else:
                        amp = 0.5
                else:
                    amp = 0.5
            elif cell.segment == 'CNT':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp=0.8
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        if np.linalg.norm(f)>100:
                            amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.3
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.7
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
            elif cell.segment == 'OMCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.2 # male:0.1 female:0.2
                        else:
                            amp = 0.1 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.5# male:0.5 female:0.5
                        else:
                            amp = 0.5 # male:0.5 female:0.5      
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.27#0.19 # male:0.1 female:0.2
                        else:
                            amp = 0.17 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.8# male:0.5 female:0.5
                        else:
                            amp = 0.8 # male:0.5 female:0.5   
            else:
                amp = 1.0        
        elif cell.humOrrat == 'hum' and cell.diabete == 'Severe' and cell.inhib !='SGLT2':
            if cell.segment == 'S3':
                amp = 1.0 
            elif cell.segment == 'SDL':
                amp = 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8             
            elif cell.segment=='DCT':
                if cell.sex == 'female' and cell.type == 'jux1':
                    amp = 0.9
                elif cell.sex == 'female' and cell.type == 'jux3':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'jux2':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'sup':
                    if np.linalg.norm(f)>2000:
                        amp = 0.5
                    else:
                        amp = 0.5
                else:
                    amp = 0.5
            elif cell.segment == 'CNT':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp=0.8
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        if np.linalg.norm(f)>100:
                            amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.13
                        else:
                            amp = 0.8
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.3
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.2
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
            elif cell.segment == 'OMCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.2 # male:0.1 female:0.2
                        else:
                            amp = 0.1 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.5# male:0.5 female:0.5
                        else:
                            amp = 0.5 # male:0.5 female:0.5      
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.13 # male:0.1 female:0.2
                        else:
                            amp = 0.17 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.8# male:0.5 female:0.5
                        else:
                            amp = 0.8 # male:0.5 female:0.5   
            else:
                amp = 1.0        
        elif cell.humOrrat == 'hum' and cell.diabete == 'Severe' and cell.inhib == 'SGLT2':
            if cell.segment == 'S3':
                amp = 1.0 
            elif cell.segment == 'SDL':
                amp = 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8             
            elif cell.segment=='DCT':
                if cell.sex == 'female' and cell.type == 'jux1':
                    amp = 0.9
                elif cell.sex == 'female' and cell.type == 'jux3':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'jux2':
                    amp = 0.7
                elif cell.sex == 'female' and cell.type == 'sup':
                    if np.linalg.norm(f)>2000:
                        amp = 0.7#0.5
                    else:
                        amp = 0.5
                else:
                    amp = 0.5
            elif cell.segment == 'CNT':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp=0.8
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        if np.linalg.norm(f)>100:
                            amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.13
                        else:
                            amp = 0.8
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.3
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.5
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.47
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
            elif cell.segment == 'OMCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.2 # male:0.1 female:0.2
                        else:
                            amp = 0.1 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.5# male:0.5 female:0.5
                        else:
                            amp = 0.5 # male:0.5 female:0.5      
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.23 # male:0.1 female:0.2
                        else:
                            amp = 0.17 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.8# male:0.5 female:0.5
                        else:
                            amp = 0.8 # male:0.5 female:0.5   
            else:
                amp = 1.0                

        elif cell.humOrrat == 'hum' and cell.diabete == 'Non' and cell.inhib !='SGLT2' and cell.unx == 'Y':
            if cell.segment == 'S3':
                if cell.sex == 'male':
                    amp = 1.0
                elif cell.sex == 'female':
                    amp = 0.6
            elif cell.segment == 'SDL':
                if cell.sex == 'male':
                    amp = 1.0
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        amp = 1.0
                    else:
                        amp = 1.0
            elif cell.segment == 'mTAL':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 1.0
            elif cell.segment == 'cTAL' or cell.segment == 'MD':
                if np.linalg.norm(f)>100:
                    amp = 0.2
                else:
                    amp = 0.8             
            elif cell.segment=='DCT':
                if cell.sex == 'female' and cell.type == 'jux1':
                    amp = 1.0
                elif cell.sex == 'female' and cell.type == 'jux3':
                    amp = 1.0
                elif cell.sex == 'female' and cell.type == 'jux2':
                    amp = 1.0
                elif cell.sex == 'female' and cell.type == 'sup':
                    if np.linalg.norm(f)>2000:
                        amp = 1.0
                    else:
                        amp = 1.0
                else:
                    amp = 1.0
            elif cell.segment == 'CNT':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5
                    else:
                        amp=0.8
                elif cell.sex == 'female':
                    if cell.type == 'sup':
                        if np.linalg.norm(f)>100:
                            amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux1':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.13
                        else:
                            amp = 0.8
                    elif cell.type == 'jux2':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.5
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux3':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.3
                            else:
                                amp = 0.5
                        else:
                            amp = 1.0
                    elif cell.type == 'jux4':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.3
                            else:
                                amp = 0.5
                        else:
                            amp = 0.8
                    elif cell.type == 'jux5':
                        if np.linalg.norm(f)>1000:
                            if k==0:
                                amp = 0.1
                            else:
                                amp = 0.17
                        else:
                            amp = 1.0
            elif cell.segment == 'CCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.6
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k == 0:
                            amp = 0.8
                        else:
                            amp = 0.2
                    else:
                        amp = 0.8
            elif cell.segment == 'OMCD':
                if cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
                elif cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        amp = 0.5 #male: 0.5 female:0.8 (0.5 works for male and female)  
                    else:
                        amp = 0.8#male:0.8 female:
            elif cell.segment == 'IMCD':
                if cell.sex == 'female':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.33 # male:0.1 female:0.2
                        else:
                            amp = 0.8 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.8# male:0.5 female:0.5
                        else:
                            amp = 0.8 # male:0.5 female:0.5      
                elif cell.sex == 'male':
                    if np.linalg.norm(f)>100:
                        if k==0:
                            amp = 0.27#0.19 # male:0.1 female:0.2
                        else:
                            amp = 0.2 # male:0.2 female:0.2
                    else:
                        if k==0:
                            amp = 0.8# male:0.5 female:0.5
                        else:
                            amp = 0.8 # male:0.5 female:0.5   
            else:
                amp = 1.0
        delta = amp*np.array(F * IJ.T)[0]
        x -= delta
        f = np.matrix(fun(x,k))
        iter+=1
        print(iter,np.linalg.norm(f))
        TOLpcn = np.max(delta / x)
        #print(i)
        
         # Pause: Added by Dania
#        input("Pausing! Press Enter to continue...")
#    print("Iteration Times: " + str(i) + " with TOL " + str(TOLpcn) + "%")
    
    return x

#@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit       
def broyden(func,x,k,type):
    fun=equations.conservation_eqs
    f=np.matrix(fun(x,k))
    J=np.matrix(Jac(fun,x,k))
#    IJ=np.linalg.inv(J)
    IJ=J.I
    dx=np.ones(x.shape)
    i=0
    iter=0
    #while(np.max(dx)>0.0001):
    while(np.linalg.norm(f)>0.0001) and (iter<500):
        
        f_previous=f
        x_previous=x
        
        x=x-np.array(f*IJ.T)[0]
        
        f=np.matrix(fun(x,k))
#                print('x',x)
#                print('f',f)

        df=f-f_previous
        dx=x-x_previous
        # #
        # #-------------------------------------------------------
        # #using good broyden
        # dx=np.array([dx])
        # df=np.array([df])
        # dx=dx.T
        # df=df.T

        # IJ = IJ+(dx-IJ*df)*(dx.T*IJ)/np.inner(dx.T*IJ,df)
        # #-------------------------------------------------------

        IJ=IJ-np.outer(IJ*f.T,dx)*IJ/np.inner(dx,dx+(IJ*f.T).T)
        #print(i)
        iter+=1
        print(iter,np.linalg.norm(f))
        
        #Pause: Added by Dania
#        input("Pausing! Press Enter to continue...")
        #J=J+np.outer((df-dx*J.T),dx)/np.linalg.norm(x)**2
        #IJ=J.I

    return x
