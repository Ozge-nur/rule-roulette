import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='.', static_url_path='')

# 1. SQL Veritabanı ve Tablo Kurulumu
def init_db():
    conn = sqlite3.connect('oyun_veritabani.db') # SQLite dosyası oluşturur
    c = conn.cursor()
    # skor_tablosu adında bir SQL tablosu oluşturuyoruz
    c.execute('''CREATE TABLE IF NOT EXISTS skor_tablosu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    oyuncu TEXT DEFAULT 'Misafir',
                    skor INTEGER NOT NULL,
                    tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )''')
    conn.commit()
    conn.close()

# 2. Ana Sayfayı (index.html) Sunma
@app.route('/')
def index():
    return app.send_static_file('index.html')

# 3. SQL Veritabanı API Uç Noktası (Backend Service)
@app.route('/api/skor', methods=['GET', 'POST'])
def skor_islemleri():
    conn = sqlite3.connect('oyun_veritabani.db')
    c = conn.cursor()
    
    if request.method == 'POST':
        # Yeni rekor geldiğinde SQL veritabanına INSERT yap
        veri = request.json
        yeni_skor = veri.get('skor', 0)
        c.execute("INSERT INTO skor_tablosu (skor) VALUES (?)", (yeni_skor,))
        conn.commit()
        conn.close()
        return jsonify({"durum": "basarili", "mesaj": "Veritabanına kaydedildi"})
    
    else:
        # Oyun açıldığında SQL veritabanından en yüksek skoru SELECT ile getir
        c.execute("SELECT MAX(skor) FROM skor_tablosu")
        max_skor = c.fetchone()[0]
        conn.close()
        return jsonify({"en_yuksek_skor": max_skor if max_skor is not None else 0})

if __name__ == '__main__':
    init_db() # Başlarken tabloyu kur
    print("=======================================")
    print(" SQL VERİTABANLI OYUN SUNUCUSU AKTİF!  ")
    print(" Lütfen tarayıcınızdan şu adrese gidin:")
    print(" http://127.0.0.1:5000                 ")
    print("=======================================")
    app.run(port=5000)
