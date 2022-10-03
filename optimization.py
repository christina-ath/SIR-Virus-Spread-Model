import rungeKutta
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import math
from sklearn.metrics import mean_squared_error
import scipy.optimize as spo
from scipy.optimize import least_squares
from scipy.optimize import fmin


#Gaussian template

def Gauss(x, A, B,cen):
    y = A * np.exp(-1 * B * (np.array(x)+cen) ** 2)
    return y

#constant data
a0 = 0.0005
b0 = 0.079
v0 = [a0,b0]
np.array(v0)
time = []
np.array(time)


for i in range(130):
    time.append(i)

tdata = [0, 16, 31, 47, 62, 78, 109]
ydata = [235, 201, 153, 121, 108, 97, 83]
edata = [14, 22, 29, 21, 8, 8, 0]

np.array(tdata)
np.array(ydata)
np.array(edata)


#This Function Takes as an input a vector v with the parameters a and b and outputs the root mean squared error
def func(v):
    RKDe = []
    np.array(RKDe)
    for i in range(130):
        RKDe.append(rungeKutta(i, v[0], v[1], 0.1, 0, 14, 235, 0)[1])
    eprd = []
    np.array(eprd)
    for i in tdata:
        if(i == 0 or i == 16 or i == 31 or i == 47 or i == 62 or i == 78 or i == 109):
            eprd.append(rungeKutta(i, v[0], v[1], 0.1, 0, 14, 235, 0)[1])
    return  math.sqrt(mean_squared_error(edata,eprd))
print("The initial RMSE (using the guesses) before the optimization is: ",func(v0))


#Minimization of the previous functions given constraints
bnds = ((0, 1), (0, 1))
res= spo.minimize(func,v0,bounds=bnds)
print(res)
