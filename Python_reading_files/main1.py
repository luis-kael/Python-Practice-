import json


file_path = "C:\Users\DELL\OneDrive\Desktop\output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")