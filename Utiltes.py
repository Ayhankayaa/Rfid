import json

class Utiltes:
    def Json_converter(kart):

        jsonStr = json.dumps(kart.__dict__)  
        print(jsonStr) 
        return jsonStr
