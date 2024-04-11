import csv
with open('activity.csv')as csv_file:
  data = csv.reader(csv_file)
  for row in data:
        print(row)