from bot.oauth import authenticate
from pprint import pprint

auth_info = {}

authenticate(auth_info)

pprint(auth_info)
