# 🌟 Yıldız Avcısı (SQL Sürümü)

Yıldızları topladıkça Yapay Zeka'nın size anlık yasaklar koyduğu, SQL veritabanı destekli, sınırları zorlayan refleks ve bulmaca oyunudur.

## 🎮 Nasıl Oynanır?
*   **Amaç:** Haritadaki Yıldızları (🌟) toplayarak skoru artırmak. Hareket etmek için **WASD** veya **Ok Tuşlarını** kullanın.
*   **Yapay Zeka Kuralları:** Her yıldız aldığınızda ekrana süreli bir yasak gelir (Örn: Sola gitmek yasak). Yasağı delerseniz **2 saniye donma cezası** yersiniz.
*   **Bombalar:** Skor arttıkça haritada ölümcül bombalar (💣) belirir. Bastığınız an ölürsünüz ve skorunuz SQL veritabanına kaydedilir.
*   *İpucu: Ekranın sağından çıkarsanız solundan girersiniz!*

---

## 🛠️ Sistem Mimarisi (Backend & Veritabanı)

Bu proje, oyuncu verilerini güvenli ve kalıcı bir şekilde saklamak için gerçek bir Backend (Sunucu) ve SQL İlişkisel Veritabanı mimarisi üzerine kurulmuştur.

### 1. Veritabanı (Database) Tabloları
Proje veritabanı olarak hafif ve hızlı bir SQL motoru olan **SQLite** kullanmaktadır. Sistem çalıştığında otomatik olarak `oyun_veritabani.db` dosyası oluşur.
*   **Tablo Adı:** `skor_tablosu`
*   **Sütunlar:** 
    * `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
    * `oyuncu` (TEXT DEFAULT 'Misafir')
    * `skor` (INTEGER NOT NULL) - En yüksek rekorları barındırır.
    * `tarih` (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)

### 2. Backend Servisleri (Python Flask)
Oyunun sunucu tarafı (Backend) **Python Flask** framework'ü ile yazılmıştır. İstemci (Frontend) ve Sunucu, `JSON` formatında veri alışverişi (API) yapar.
*   **`GET /api/skor`:** Oyun (Lobby) yüklendiği an çalışır. Veritabanındaki `skor_tablosu` tablosuna `SELECT MAX(skor)` sorgusu atarak tüm zamanların en yüksek rekorunu çeker ve arayüze yansıtır.
*   **`POST /api/skor`:** Oyuncu öldüğünde ve yeni bir rekor kırdığında çalışır. Gelen JSON formatındaki skoru alarak `INSERT INTO` sorgusu ile SQL veritabanına yeni bir satır olarak ekler.

### 3. Frontend Fonksiyonları
*   `startGame()`: Oyun motorunu başlatır.
*   `movePlayer(dir)`: Grid tabanlı matris hareketlerini ve Pac-Man sınır geçişlerini hesaplar.
*   `addAiRule()`: Skorla eşzamanlı zorluk seviyesini artırarak yapay zeka kurallarını zamanlayıcıya (Timer) ekler.
*   `triggerError(msg)`: Asenkron (setTimeout) çalışarak kural ihlalinde thread'i kilitler (Cezalandırma sistemi).

## 🚀 Oyunu Başlatma (Kurulum)
Sunucuyu ve SQL veritabanını başlatmak için klasördeki **`baslat.bat`** dosyasına iki kere tıklamanız yeterlidir. Gerekli Python sunucusu otomatik ayaklanacak ve oyunu `http://127.0.0.1:5000` adresinde tarayıcınızda açacaktır.
