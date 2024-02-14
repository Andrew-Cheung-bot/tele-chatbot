import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print(config['TELEGRAM']['ACCESS_TOKEN'])
#Notice: Do not track and push this configuration file to public r