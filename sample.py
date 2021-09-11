import json

with open("sample.json") as jsonFile:
    data = json.load(jsonFile)
    jsonData = data["Employees"]
    for x in jsonData:
        keys = x.keys()
        print(keys)
