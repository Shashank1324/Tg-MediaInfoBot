import json
from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

 API_ID = environ.get('API_ID',"11760418") 
 API_HASH = environ.get('API_HASH',"1087bd9fc871216be0e86287e5c50ac3") 
 BOT_TOKEN = environ.get('BOT_TOKEN',"6525864792:AAHoeiRNOQmdRD4GFyRo4Ht0vZtccEOWk10")

SUDO_USERID = json.loads(getenv("SUDO_USERID","6561715152"))
AUTHORIZED_CHATS = json.loads(getenv("AUTHORIZED_CHATS","6561715152"))
