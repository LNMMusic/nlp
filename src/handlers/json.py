import json

def loadJson(filename:str, keys=list) -> dict:
    with open(filename, mode="r") as json_file:
        data = json.load(json_file)
        for k in keys:
            data = data[k]
    
    return data

def loadTxt(filename:str) -> str:
    with open(filename, mode="r") as f:
        data = f.read()
    return data