import json

def readJson():
    
    # Lendo o arquivo JSON
    with open('data.json') as json_data:
        constants = json.load(json_data)
        json_data.close()
    
    return constants