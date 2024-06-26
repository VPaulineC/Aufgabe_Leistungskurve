import matplotlib.pyplot as plt
import numpy as np
from sort import bubble_sort
from load_data import load_data
import os 

# Daten laden
data = load_data("activity.csv")
PowerOriginal = data["PowerOriginal"]

# Daten sortieren
sorted_PowerOriginal = bubble_sort(PowerOriginal)

# Datensatz in Minuten umwandeln und Leistungskurve anzeigen
minuten_PowerOriginal=sorted_PowerOriginal[::60]
plt.plot(minuten_PowerOriginal[::-1])

# Plot beschriftung
plt.grid(True)
plt.ylabel("PowerOriginal")
plt.xlabel("Minuten")

# Ordner für Grafik erstellen und speichern der Grafik
# Hilfestellung: https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory

if not os.path.exists("figures"):
    os.makedirs("figures")

plt.savefig("figures/Leistungskurve.png")
