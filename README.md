# Yıldız Avcısı - Kabus Modu 🌟💀

Web tarayıcınızda oynayabileceğiniz, kurulum gerektirmeyen, süper dinamik ve giderek zorlaşan bir 15x15 bulmaca-arcade oyunudur. 

## 🎮 Nasıl Oynanır?
1. Ekranda gördüğünüz sarı parlayan **Yıldızları (🌟)** toplayarak skorunuzu artırın.
2. Haritanın uçlarından çıktığınızda karşı uçtan girersiniz (Pac-Man mekaniği).

## ⚠️ Kabus Mekanikleri (Zorluklar)
*   **Yapay Zeka Kuralları:** Yıldız yediğinizde ekranın üstünde rastgele bir **"Yasak Kural"** türer (Örn: "Sağa Gitmek Yasak"). 
*   **Zamanlı İptaller:** Bu kurallar sonsuza kadar sürmez. Her kuralın 8 hamlelik ömrü vardır. 8 kere adım attığınızda kural silinir.
*   **Dondurma Cezası:** Bir kuralı ihlal ederseniz oyun ekranı kararır ve **2 Saniye boyunca donarsınız**. Oksederseniz sadece zaman kaybedersiniz!
*   **Ölümcül Bombalar (💣):** Siz yıldızları topladıkça (Her 2 skorda 1 adet) rastgele yerlerde bombalar türer. İstediğiniz kadar bekleyin, o bombalar oradan hiç gitmez. Bastığınız an oyun anında biter!

## 🚀 Nasıl Çalıştırılır?
* Hiçbir dil, "node.js" ya da framework yüklemenize gerek YOKTUR!
* İndirdiğiniz klasördeki **`index.html`** dosyasına iki kere tıklayın ve anında oyuna başlayın.
* GitHub Pages, Vercel, Netlify gibi her şeyde direkt yayınlanmaya uygundur.

Geliştiriciler: Tamamen "Vanilla JavaScript, HTML5 ve TailwindCSS (CDN)" kullanılarak inşa edilmiştir.

### Ekran Görüntüleri
Sanal zeka, glassmorphism (bulanık arka plan), CSS ile üretilmiş gridler ve hareketli arka plan tasarımları bulunmaktadır. Müzikler saf `AudioContext` 8-Bit sinyal sentezlemeyle üretilmiştir.
