import json


def readJson(jsonFilePath):
    with open(jsonFilePath) as f:
        jsonFile = json.load(f)
        f.close()
    return jsonFile
