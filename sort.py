from main_c import data

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Daten aus der CSV-Datei in eine Liste laden
rows = []  # Hier sollten Ihre Daten stehen
sorted_rows = bubble_sort(rows)

# Sortierte Daten ausgeben
for data in sorted_rows:
    print(data)