import json

class Configuration:
    
    def __init__(self):
        with open("config.json", "r") as config_f:
            config = json.load(config_f)
        self.config = config