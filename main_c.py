import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("activity.csv")

y_ax = data["PowerOriginal"]
x_ax = np.arange(0, len(data), 1) # time in seconds 



#x_ax_min = np.arange(0, )
plt.xticks()
plt.plot(x_ax, y_ax)

plt.grid()
plt.show()

