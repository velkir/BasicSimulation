import configparser

class Settings():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.grass = int(config.get("Settings","grass"))
        self.rocks = int(config.get("Settings","rocks"))
        self.trees = int(config.get("Settings","trees"))
        self.pigs = int(config.get("Settings","pigs"))
        self.pig_speed = int(config.get("Settings","pig_speed"))
        self.pig_hp = int(config.get("Settings","pig_hp"))
        self.wolves = int(config.get("Settings","wolves"))
        self.wolf_speed = int(config.get("Settings","wolf_speed"))
        self.wolf_hp = int(config.get("Settings","wolf_hp"))
        self.width = int(config.get("Settings","width"))
        self.height = int(config.get("Settings","height"))

