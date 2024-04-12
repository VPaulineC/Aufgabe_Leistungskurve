import matplotlib.pyplot as plt
import numpy as np
from sort import bubble_sort
from load_data import load_data
import os 

#Daten laden
data = load_data("activity.csv")
PowerOriginal = data["PowerOriginal"]

# Daten sortieren
sorted_PowerOriginal = bubble_sort(PowerOriginal)

# Leistungskurve anzeigen
plt.plot(PowerOriginal[::-1])
plt.show()


if not os.path.exists("figures"):
    os.makedirs("figures")

plt.savefig("figures/Leistungskurve.png")