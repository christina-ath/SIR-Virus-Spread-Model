import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import math
from sklearn.metrics import mean_squared_error
import scipy.optimize as spo
from scipy.optimize import least_squares
from scipy.optimize import fmin

#classic Runge-Kutta method
def dydt(t, a, y, e):  #1st DE
    return -a * y * e


def dedt(t, a, b, y, e):   #2nd DE
    return a * y * e - b * e


def dtdt(t, b, e):  #3rd DE
    return b * e


def rungeKutta(t, a, b, h, t0, E0, Y0, T0):
    # iterations
    n = int((t - t0) / h)

    for i in range(1, n + 1):

        kY1 = h * dydt(t0, a, Y0, E0)
        kE1 = h * dedt(t0, a, b, Y0, E0)
        #kT1 = h * dtdt(t0, b, E0)

        kY2 = h * dydt(t0 + h / 2, a, Y0 + kY1 / 2, E0 + kE1 / 2)
        kE2 = h * dedt(t0 + h / 2, a, b, Y0 + kY1 / 2, E0 + kE1 / 2)
        #kT2 = h * dtdt(t0 + h / 2, b, E0 + kE1 / 2)

        kY3 = h * dydt(t0 + h / 2, a, Y0 + kY2 / 2, E0 + kE2 / 2)
        kE3 = h * dedt(t0 + h / 2, a,b , Y0 + kY2 / 2, E0 + kE2 / 2)
        #kT3 = h * dtdt(t0 + h / 2, b, E0 + kE2 / 2)

        kY4 = h * dydt(t0 + h / 2, a, Y0 + kY3 / 2, E0 + kE3 / 2)
        kE4 = h * dedt(t0 + h / 2, a, b, Y0 + kY3 / 2, E0 + kE3 / 2)
        #kT4 = h * dtdt(t0 + h / 2, b, E0 + kE3 / 2)

        Y0 = Y0 + 1 / 6 * (kY1 + 2 * kY2 + 2 * kY3 + kY4)
        E0 = E0 + 1 / 6 * (kE1 + 2 * kE2 + 2 * kE3 + kE4)
        #T0 = T0 + 1 / 6 * (kT1 + 2 * kT2 + 2 * kT3 + kT4)
        t0 = t0 + h

    results = [Y0, E0]
    np.array(results)
    return results