import numpy as np
import matplotlib.pyplot as plt

def culcCurvature1(x,y):
    dif_y = np.gradient(y,x)
    dif2_y = np.gradient(dif_y,x)
    curvature = np.abs(dif2_y) / (1 + (dif_y)**2)**1.5
    return curvature

def culcCurvature2(x,y):
    dif_x = np.gradient(x)
    dif_y = np.gradient(y)
    dif2_x = np.gradient(dif_x)
    dif2_y = np.gradient(dif_y)
    curvature = np.abs(dif2_x * dif_y - dif_x * dif2_y) / (dif_x **2 + dif_y **2)**1.5
    return curvature

if __name__ == '__main__':
    x = np.arange(-10,10,0.001)
    y = x ** 3

    cuv1 = culcCurvature1(x,y)
    cuv2 = culcCurvature2(x,y)