import configparser

class Config:
    'Config accessor class'
    def __init__(self, configfile='config.ini'):
        self.__configfile = configfile

    def get(self, section, key):
        'Returns a config value'
        config = self.__read())
        return config[section][key]

    def set(self, section, key, value):
        'Sets a config value'
        config = self.__read()
        config[section][key] = value
        self.__write(config)

    def __read(self):
        'Returns the config parser for the config file'
        config = configparser.ConfigParser()
        with open(self.__configfile, 'r') as configfile:
            config.read_file(configfile)
        return config

    def __write(self, config):
        'Writes the config file for the given config'
        with open(self.__configfile, 'w') as configfile:
            config.write(configfile)

