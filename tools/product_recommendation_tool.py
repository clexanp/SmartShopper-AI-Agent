def rekomendasi_produk(query_user: str) -> dict:
    """
    Gunakan tools ini jika user bertanya tentang rekomendasi produk,
    pencarian produk, produk terbaik, harga produk, kategori produk,
    atau produk yang cocok dibeli.
    """

    daftar_produk = [
        {
            "nama_produk": "Wireless Mouse Pro",
            "kategori": "aksesoris komputer",
            "harga": 125000,
            "deskripsi": "Mouse wireless ringan untuk kerja harian dan belajar."
        },
        {
            "nama_produk": "Keyboard Mechanical Lite",
            "kategori": "aksesoris komputer",
            "harga": 350000,
            "deskripsi": "Keyboard mechanical entry-level untuk mengetik dan gaming ringan."
        },
        {
            "nama_produk": "TWS ClearSound Mini",
            "kategori": "audio",
            "harga": 199000,
            "deskripsi": "Earbuds wireless dengan suara jernih dan baterai tahan lama."
        },
        {
            "nama_produk": "Laptop Stand Foldable",
            "kategori": "aksesoris laptop",
            "harga": 89000,
            "deskripsi": "Stand laptop lipat untuk membuat posisi kerja lebih nyaman."
        }
    ]

    query_kecil = query_user.lower()
    kata_query = [kata for kata in query_kecil.split() if len(kata) > 2]
    hasil_produk = []

    for produk in daftar_produk:
        teks_produk = f"{produk['nama_produk']} {produk['kategori']} {produk['deskripsi']}".lower()
        if any(kata in teks_produk for kata in kata_query):
            hasil_produk.append(produk)

    if not hasil_produk:
        hasil_produk = daftar_produk[:2]

    return {
        "status": "berhasil",
        "jumlah_produk": len(hasil_produk),
        "rekomendasi": hasil_produk
    }
