import pymongo
import certifi

con_str = "mongodb+srv://Aerkadia:aerkadia123@cluster0.hedru.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("Aerkadia")
