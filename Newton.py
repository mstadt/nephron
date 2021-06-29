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

#=====================================================
# newton solvers, separate for human and rat models
#=====================================================
# rat newton solver
def newton_rat(func,x,k,cell):
    print('to do')
    if cell.humOrrat != 'rat':
        raise Exception('newton_rat only for rat model')


# human newton solver
def newton_human(func,x,k,cell):
    print('to do')
    if cell.humOrrat != 'hum':
        raise Exception('newton_human only for human model')
