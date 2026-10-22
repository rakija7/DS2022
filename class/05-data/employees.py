import json

with open("data/employees.json", "r") as f:
    data = json.load(f)

for emp in data["employees"]:
    print(f"{emp['name']}: {emp['position']}")

