import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# =============================================================================
# Needs work, data is random at the moment
# Not fully functional at the moment
# =============================================================================

df = pd.read_csv("mydata.csv")
mydata = pd.read_csv("mydata.csv")

pm10 = mydata.pm10
o3 = mydata.o3
ws = mydata.ws
wd = mydata.wd
nox = mydata.nox
no2 = mydata.no2
pm25 = mydata.pm25


theta = np.linspace(0, 2 * np.pi)
r = np.linspace(2, 15, 16)

Theta, R = np.meshgrid(theta, r)
C = np.sinc(Theta - 2) + (5 - np.sqrt(R)) + np.random.rand(len(r), len(theta))
C = np.ma.masked_less_equal(C, 2)
# print(C)
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={"projection": "polar"})

ax.pcolormesh(Theta, R, C, vmin=2, vmax=5, cmap="Spectral_r")

plt.show()
# print(Theta)
# print(r)
