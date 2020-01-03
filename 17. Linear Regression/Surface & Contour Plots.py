#!/usr/bin/env python
# coding: utf-8

# ### Surface Plots

# In[19]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# In[28]:


#a = np.array([1,2,3])
#b = np.array([4,5,6,7])

a = np.arange(-1,1,0.02)
b = a

a,b = np.meshgrid(a,b)


# In[29]:


plt.style.use('seaborn')
fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap="rainbow")
plt.show()


# ### Contour Plots

# In[35]:


fig  = plt.figure()
axes = fig.gca(projection='3d')
axes.contour(a,b,a**2+b**2,cmap="rainbow")
plt.title("Contour")
plt.show()


# In[ ]:




