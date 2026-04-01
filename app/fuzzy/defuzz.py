def hitung_rata_rata_terpusat(alpha_z_list):
    """
    Menerima list of tuple (alpha, z) dan melakukan perhitungan defuzzifikasi.
    """
    total_alpha_z = 0.0
    total_alpha = 0.0
    
    for alpha, z in alpha_z_list:
        total_alpha_z += alpha * z
        total_alpha += alpha

    if total_alpha == 0: 
        return 0
        
    return round(total_alpha_z / total_alpha, 2)