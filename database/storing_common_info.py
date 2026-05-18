import csv
import os
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
nama_database = os.getenv("NAMA_DATABASE", "smartshopper_db")
nama_collection = os.getenv("NAMA_COLLECTION", "common_information")

if not mongo_uri:
    raise ValueError("MONGO_URI belum diisi. Buat file .env dulu dari .env.example")

lokasi_file = Path(__file__).resolve().parents[1] / "data" / "common_information.csv"

client = MongoClient(mongo_uri, serverSelectionTimeoutMS=10000)
client.admin.command("ping")

database = client[nama_database]
collection = database[nama_collection]

data_common_info = []

with open(lokasi_file, mode="r", encoding="utf-8-sig", newline="") as file:
    df = csv.DictReader(file)

    for baris in df:
        dokumen = {
            "kategori": baris["kategori"].strip(),
            "pertanyaan": baris["pertanyaan"].strip(),
            "jawaban": baris["jawaban"].strip(),
            "teks_lengkap": f"{baris['kategori']} {baris['pertanyaan']} {baris['jawaban']}".lower()
        }
        data_common_info.append(dokumen)

collection.delete_many({})

if data_common_info:
    collection.insert_many(data_common_info)

print("Data Common Information berhasil disimpan ke MongoDB Atlas.")
print(f"Database   : {nama_database}")
print(f"Collection : {nama_collection}")
print(f"Jumlah data tersimpan: {len(data_common_info)}")
