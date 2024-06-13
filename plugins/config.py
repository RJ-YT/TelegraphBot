import os
import logging


class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7156263353:AAHtKpMffztd34WxG2rTsafrnT3T_8-ni7A")
    
    API_ID = int(os.environ.get("API_ID", "29478734"))
    
    API_HASH = os.environ.get("API_HASH", "8bd53e36eceada3329fbe46d9b961d1f")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://nikzgod:nikzgod@cluster0.lqn4wau.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "Romaancham_Premium_BoT")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "6807518752"))
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Romaancham_Premium_BoT")
                                  
