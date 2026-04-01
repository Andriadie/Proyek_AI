from flask import render_template, request
from app import app
from app.fuzzy.inference import process_fuzzy_tsukamoto

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    if request.method == 'POST':
        val_p = float(request.form['penjualan'])
        val_s = float(request.form['stok'])
        # Panggil fungsi orkestrator dari modul fuzzy
        hasil = process_fuzzy_tsukamoto(val_p, val_s)
        
    return render_template('index.html', hasil=hasil)