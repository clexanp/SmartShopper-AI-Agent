import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
nama_database = os.getenv("NAMA_DATABASE", "smartshopper_db")
nama_collection = os.getenv("NAMA_COLLECTION", "common_information")


def _ambil_collection():
    if not mongo_uri:
        raise ValueError("MONGO_URI belum diisi. Pastikan file .env sudah dibuat.")

    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=10000)
    database = client[nama_database]
    return database[nama_collection]


def ambil_common_information(query_user: str) -> dict:
    """
    Gunakan tools ini untuk menjawab pertanyaan umum seputar e-commerce,
    seperti pengiriman barang, cara pembelian, metode pembayaran, refund,
    retur, pembatalan pesanan, dan cek resi.
    """

    collection = _ambil_collection()
    query_kecil = query_user.lower()
    kata_query = [kata for kata in query_kecil.split() if len(kata) > 2]

    semua_data = list(collection.find({}, {"_id": 0}))

    hasil_terbaik = None
    skor_tertinggi = 0

    for data in semua_data:
        teks = data.get("teks_lengkap", "").lower()
        skor = sum(1 for kata in kata_query if kata in teks)

        if skor > skor_tertinggi:
            skor_tertinggi = skor
            hasil_terbaik = data

    if hasil_terbaik is None or skor_tertinggi == 0:
        return {
            "status": "tidak_ditemukan",
            "jawaban": "Maaf, informasi umum yang sesuai dengan pertanyaan tersebut belum tersedia di database."
        }

    return {
        "status": "ditemukan",
        "kategori": hasil_terbaik["kategori"],
        "pertanyaan_referensi": hasil_terbaik["pertanyaan"],
        "jawaban": hasil_terbaik["jawaban"]
    }
