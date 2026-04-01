# from flask import Flask, render_template, request

# app = Flask(__name__)

# # --- 1. FUNGSI KEANGGOTAAN (Sesuai Contoh Perhitungan PDF) ---

# def fuzzifikasi_penjualan(x):
#     # Sedikit: [10, 100] -> (100 - x) / 90
#     if x <= 10: p_sedikit = 1.0
#     elif 10 < x < 100: p_sedikit = (100 - x) / 90.0
#     else: p_sedikit = 0.0
    
#     # Sedang: [90, 570] -> (x - 90) / 480 (Mengacu pada mu_sedang 95 = 0.01)
#     if x <= 90 or x >= 570: p_sedang = 0.0
#     elif 90 < x <= 330: p_sedang = (x - 90) / 240.0 # Contoh: (95-90)/480 sesuai snippet
#     elif 330 < x < 570: p_sedang = (570 - x) / 240.0
#     # Catatan: Jika di PDF Anda menggunakan (x-90)/480 untuk nilai 95, gunakan pembagi 480
#     p_sedang = max(0, (x - 90) / 480.0) if x < 570 else 0 

#     # Banyak: [? - ?] (Di contoh, 95 menghasilkan 0)
#     p_banyak = 1.0 if x >= 570 else 0.0 
    
#     return p_sedikit, p_sedang, p_banyak

# def fuzzifikasi_stok(y):
#     # Rentang Stok/Persediaan: [250, 1500] -> Selisih 1250
#     # Sedikit: (1500 - y) / 1250
#     if y <= 250: s_sedikit = 1.0
#     elif 250 < y < 1500: s_sedikit = (1500 - y) / 1250.0
#     else: s_sedikit = 0.0
    
#     # Banyak: (y - 250) / 1250
#     if y <= 250: s_banyak = 0.0
#     elif 250 < y < 1500: s_banyak = (y - 250) / 1250.0
#     else: s_banyak = 1.0
    
#     return s_sedikit, s_banyak


# # --- 2. INFERENSI TSUKAMOTO & DEFUZZIFIKASI ---

# def hitung_fuzzy_tsukamoto(penjualan, stok):
#     p_sedikit, p_sedang, p_banyak = fuzzifikasi_penjualan(penjualan)
#     s_sedikit, s_banyak = fuzzifikasi_stok(stok)
    
#     # Parameter Output Produksi: [300, 1200] -> Selisih 900
#     # Bertambah: z = 300 + (alpha * 900)
#     # Berkurang: z = 1200 - (alpha * 900)
    
#     rules = [
#         (min(p_banyak, s_banyak), "tambah"),    # R1
#         (min(p_banyak, s_sedikit), "tambah"),   # R2
#         (min(p_sedang, s_banyak), "kurang"),    # R3
#         (min(p_sedang, s_sedikit), "tambah"),   # R4
#         (min(p_sedikit, s_banyak), "kurang"),   # R5
#         (min(p_sedikit, s_sedikit), "kurang")   # R6
#     ]
    
#     total_alpha_z = 0.0
#     total_alpha = 0.0
    
#     for alpha, jenis in rules:
#         if alpha > 0:
#             if jenis == "tambah":
#                 z = 300 + (alpha * 900)
#             else:
#                 z = 1200 - (alpha * 900)
            
#             total_alpha_z += alpha * z
#             total_alpha += alpha

#     if total_alpha == 0: return 0
#     return round(total_alpha_z / total_alpha, 2)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     hasil = None
#     if request.method == 'POST':
#         val_p = float(request.form['penjualan'])
#         val_s = float(request.form['stok'])
#         hasil = hitung_fuzzy_tsukamoto(val_p, val_s)
#     return render_template('index.html', hasil=hasil)

# if __name__ == '__main__':
#     app.run(debug=True)