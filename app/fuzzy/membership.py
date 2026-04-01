def fuzzifikasi_penjualan(x):
    # Sedikit
    if x <= 10: p_sedikit = 1.0
    elif 10 < x < 100: p_sedikit = (100 - x) / 90.0
    else: p_sedikit = 0.0
    
    # Sedang
    if x <= 90 or x >= 570: p_sedang = 0.0
    elif 90 < x <= 330: p_sedang = (x - 90) / 240.0 
    elif 330 < x < 570: p_sedang = (570 - x) / 240.0
    p_sedang = max(0, (x - 90) / 480.0) if x < 570 else 0 

    # Banyak
    p_banyak = 1.0 if x >= 570 else 0.0 
    
    return p_sedikit, p_sedang, p_banyak

def fuzzifikasi_stok(y):
    # Sedikit
    if y <= 250: s_sedikit = 1.0
    elif 250 < y < 1500: s_sedikit = (1500 - y) / 1250.0
    else: s_sedikit = 0.0
    
    # Banyak
    if y <= 250: s_banyak = 0.0
    elif 250 < y < 1500: s_banyak = (y - 250) / 1250.0
    else: s_banyak = 1.0
    
    return s_sedikit, s_banyak