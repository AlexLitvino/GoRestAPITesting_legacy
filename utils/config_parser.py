import configparser

parser = configparser.ConfigParser()
parser.read("config.ini")

BASE_URL = parser.get("gorest", "url")
GOREST_AUTH_TOKEN = parser.get("gorest", "token")
