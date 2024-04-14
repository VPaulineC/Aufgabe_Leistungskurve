# Aufgabe_Leistungskurve
Gruppe: Pauline Voigtsberger & Carina Tilg

# Vorbereitung
## Virtual Environment anlegen

- Öffne ein neues Terminal (in VSCode) und gib **python -m venv .venv** ein
- Aktiviere die Virtuelle Umgebung mit dem Befehl **.\ .venv\Scripts\Activate**

## Pakete installieren 
Für die Ausführung der main.py müssen folgende Pakete mit 
**pip install < Paketname >** (Beispiel: pip install numpy) installiert werden:

- matplotlib.pyplot (oder nur matplotlib)
- numpy
 
 Der **bubble_sort** algorithmus steht in sort.py und wird mit **from sort import bubble_sort** in die main.py importiert.
 Die Daten aus der CSV-Datei werden in load_data.py geladen und in main.py mit **from load_data import load_data** importiert.

# Verwendung
Aus einer CSV_Datei hier **activity.csv** wird der Datensatz "PowerOriginal" geladen und nach main.py importiert. Im Hauptprogramm wird der Datensatz gelesen, in Minuten dargestellt, mit matplotlib ein Plot erstellt, mit OS ein Ordner "figures" erstellt und die Grafik als .png abgespeichert.
