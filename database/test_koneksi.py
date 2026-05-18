import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise ValueError("MONGO_URI belum diisi. Buat file .env dulu dari .env.example")

client = MongoClient(mongo_uri, serverSelectionTimeoutMS=10000)
client.admin.command("ping")

print("Berhasil terhubung ke MongoDB Atlas")
