# SmartShopper AI Agent

Mini project AI Agent Personalized SmartShopper Assistant untuk menangani dua kebutuhan utama:

1. Product Recommendation
2. Common Information seperti pengiriman, pembelian, pembayaran, refund, dan retur

Project ini memakai Google ADK, Python, dan MongoDB Atlas.

## Cara Menjalankan

### 1. Buat virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 2. Install library

```bash
pip install -r requirements.txt
```

### 3. Buat file `.env`

Copy isi `.env.example`, lalu ubah nama file menjadi `.env`.

Isi API key Gemini dan connection string MongoDB Atlas.

### 4. Test koneksi MongoDB

```bash
python database/test_koneksi.py
```

### 5. Simpan dataset ke MongoDB Atlas

```bash
python database/storing_common_info.py
```

### 6. Test tools secara lokal

```bash
python test_agent.py
```

### 7. Jalankan agent ADK

```bash
adk web
```

## Struktur Project

```text
SmartShopper-AI-Agent/
├── data/
│   └── common_information.csv
├── database/
│   ├── __init__.py
│   ├── test_koneksi.py
│   └── storing_common_info.py
├── tools/
│   ├── __init__.py
│   ├── common_information_tool.py
│   └── product_recommendation_tool.py
├── agent.py
├── test_agent.py
├── test_common_tool.py
├── test_product_tool.py
├── requirements.txt
├── .gitignore
└── README.md
```
