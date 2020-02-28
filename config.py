import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
MIDDLEWARE = []
NO_AUTH = []
PYTHON_TO_REGEX = {"int": "([0-9]+)", "str": "(.+)"}
URL = ""

DATABASE = {
    'user': '',
    'passwd': '',
    'host': '',
    'db': ''
}
