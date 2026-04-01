
# Fuzzy Production System (Tsukamoto Method) 🧥

Aplikasi berbasis Web menggunakan **Flask** untuk menentukan jumlah produksi pakaian optimal berdasarkan data **Penjualan** dan **Stok** menggunakan Logika Fuzzy metode Tsukamoto.

## 📂 Struktur Proyek
```text
fuzzy-flask-app/
├── app/
│   ├── fuzzy/          # Logika Fuzzy (Membership, Rules, Inference, Defuzz)
│   ├── templates/      # File HTML (UI)
│   ├── static/         # Aset CSS/JS (Opsional)
│   ├── routes.py       # Pengatur URL/Endpoint
│   └── __init__.py     # Inisialisasi Flask
├── config.py           # Konfigurasi Aplikasi
├── run.py              # Entry point untuk menjalankan aplikasi
└── requirements.txt    # Daftar dependensi Python
````

## 🚀 Cara Menjalankan di Lokal

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di laptop:

### 1\. Clone Repositori

Buka terminal/command prompt dan clone folder ini:

```bash
git clone <url-repository-anda>
cd fuzzy-flask-app
```

### 2\. Buat Virtual Environment (Direkomendasikan)

Agar library tidak bentrok dengan proyek lain:

  - **Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
  - **macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3\. Instal Dependensi

Instal semua library yang dibutuhkan (terutama Flask):

```bash
pip install -r requirements.txt
```

### 4\. Jalankan Aplikasi

Jalankan file `run.py` sebagai pintu utama aplikasi:

```bash
python run.py
```

### 5\. Akses di Browser

Buka browser Anda dan akses alamat berikut:
[http://127.0.0.1:5000](https://www.google.com/search?q=http://127.0.0.1:5000)

-----

## 📊 Detail Kasus (Contoh Perhitungan)

Untuk mencoba apakah aplikasi berjalan akurat, Anda bisa menggunakan data uji dari laporan:

  - **Penjualan:** 95
  - **Stok:** 1200
  - **Hasil Produksi:** 1087.5 Unit

## 🛠️ Teknologi yang Digunakan

  * **Python 3.x**
  * **Flask** (Web Framework)
  * **Bootstrap 5** (UI Styling)
  * **FontAwesome** (Icons)
