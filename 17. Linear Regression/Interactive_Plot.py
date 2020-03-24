import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X = pd.read_csv("Training Data/Linear_X_Train.csv").values
Y = pd.read_csv("Training Data/Linear_Y_Train.csv").values
theta = np.load("ThetaList.npy")

T0 = theta[:,0]
T1 = theta[:,1]

plt.style.use('seaborn')
plt.ion()
for i in range(0,50,3):
    Y_ = T1[i]*X + T0[i]
    plt.scatter(X,Y) # Training points
    plt.plot(X,Y_,'red') # Line
    plt.draw()
    plt.pause(1)
    plt.clf()
