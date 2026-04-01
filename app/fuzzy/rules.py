def evaluate_rules(p_sedikit, p_sedang, p_banyak, s_sedikit, s_banyak):
    """
    Mengevaluasi kombinasi himpunan fuzzy berdasarkan Rule 1-6.
    Mengembalikan list berisi tuple: (nilai_alpha, "jenis_output")
    """
    rules = [
        (min(p_banyak, s_banyak), "tambah"),    # R1
        (min(p_banyak, s_sedikit), "tambah"),   # R2
        (min(p_sedang, s_banyak), "kurang"),    # R3
        (min(p_sedang, s_sedikit), "tambah"),   # R4
        (min(p_sedikit, s_banyak), "kurang"),   # R5
        (min(p_sedikit, s_sedikit), "kurang")   # R6
    ]
    return rules