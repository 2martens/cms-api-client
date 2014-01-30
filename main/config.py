import configparser

def get_git_dir():
    'Returns the configured git dir'
    config = read_config()
    return config['Git']['dir']

def set_git_dir(git_dir):
    'Sets the git dir in the config file'
    config = read_config()
    config['Git']['dir'] = git_dir
    write_config(config)

def get_api_key():
    'Returns the configured API key'
    config = read_config()
    return config['General']['apikey']

def set_api_key(apikey):
    'Sets the api key in the config file'
    config = read_config()
    config['General']['apikey'] = apikey
    write_config(config)

def read_config():
    'Returns the config parser for the config file'
    config = configparser.ConfigParser()
    with open('config.ini', 'r') as configfile:
        config.read_file(configfile)
    return config

def write_config(config):
    'Writes the config file for the given config'
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

