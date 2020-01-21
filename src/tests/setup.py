import configparser

setup = configparser.ConfigParser()
setup.read("../env.ini")

print(setup['TFNSW_DETAILS']['API_KEY'])