from pymongo import MongoClient
import app.settings as settings

client = MongoClient(settings.mongodb_uri, settings.port)
db = client['usersdata']