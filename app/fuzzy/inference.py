from .membership import fuzzifikasi_penjualan, fuzzifikasi_stok
from .rules import evaluate_rules
from .defuzz import hitung_rata_rata_terpusat

def process_fuzzy_tsukamoto(penjualan, stok):
    # 1. Proses Fuzzifikasi
    p_sedikit, p_sedang, p_banyak = fuzzifikasi_penjualan(penjualan)
    s_sedikit, s_banyak = fuzzifikasi_stok(stok)
    
    # 2. Evaluasi Rules (Mendapatkan Alpha)
    rules_evaluated = evaluate_rules(p_sedikit, p_sedang, p_banyak, s_sedikit, s_banyak)
    
    # 3. Hitung Nilai Z (Inversi Tsukamoto)
    alpha_z_list = []
    for alpha, jenis in rules_evaluated:
        if alpha > 0:
            if jenis == "tambah":
                z = 300 + (alpha * 900)
            else:
                z = 1200 - (alpha * 900)
            
            alpha_z_list.append((alpha, z))
            
    # 4. Proses Defuzzifikasi
    hasil_akhir = hitung_rata_rata_terpusat(alpha_z_list)
    
    return hasil_akhir