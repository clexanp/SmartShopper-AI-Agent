from tools.common_information_tool import ambil_common_information
from tools.product_recommendation_tool import rekomendasi_produk

kata_common_info = [
    "kirim", "pengiriman", "resi", "refund", "retur", "bayar", "pembayaran",
    "batal", "pembatalan", "checkout", "beli", "pembelian"
]

pertanyaan_uji = [
    "Berapa lama pengiriman barang?",
    "Bagaimana cara mengajukan refund?",
    "Metode pembayaran apa saja yang tersedia?",
    "Saya mau beli mouse wireless yang murah",
    "Rekomendasikan produk audio untuk saya"
]

for pertanyaan in pertanyaan_uji:
    print("=" * 70)
    print("Pertanyaan:", pertanyaan)

    pertanyaan_kecil = pertanyaan.lower()

    if any(kata in pertanyaan_kecil for kata in kata_common_info):
        hasil = ambil_common_information(pertanyaan)
        nama_tool = "Common Information Tool"
    else:
        hasil = rekomendasi_produk(pertanyaan)
        nama_tool = "Product Recommendation Tool"

    print("Tool yang dipilih:", nama_tool)
    print("Hasil:", hasil)
