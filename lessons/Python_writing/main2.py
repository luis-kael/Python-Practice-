# csv

import json
import csv

employees = [["Name", "Age", "Job"],
            ["Spongbob", 30, "Cook"],
            ["Patrick", 37, "Unomployed"],
            ["Sandy", 27, "Scientist"]]

file_path = "C:\\Users\\DELL\\OneDrive\\Desktopoutput.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path} was created")
except FileExistsError:
    print("That file already exists")