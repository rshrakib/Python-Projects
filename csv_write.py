import csv
data = [
    ["Name", "Age", "City"],
    ["Rakib", 24, "Bogura"],
    ["Mubassir", 26, "Gaibandha"],
    ["Tuhin", 27, "Dinajpur"]
]
with open("file.csv", "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

with open("file.csv", "r", newline='') as csv_file:
    content = csv.reader(csv_file)
    for row in content:
        print(row)