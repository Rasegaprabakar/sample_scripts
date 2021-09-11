import json

with open("data10.json") as jsonFile:
    data = json.load(jsonFile)
    jsonData = data["results"]
    for x in jsonData:
        keys = x.keys()
    print(keys)
