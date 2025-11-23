# 👂 Ghost Listener - Noise Activated Audio Recorder

![Python](https://img.shields.io/badge/Language-Python_3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **⚠️ YASAL UYARI:** Bu yazılım tamamen **eğitim ve kişisel otomasyon** amacıyla geliştirilmiştir. Bulunduğunuz bölgedeki ses kaydı ve gizlilik yasalarına (KVKK/GDPR) uymak kullanıcının sorumluluğundadır. Başkalarının gizliliğini ihlal etmek için kullanılamaz.

## 📖 Proje Hakkında

**Ghost Listener**, bilgisayar mikrofonunu kullanarak ortamı sürekli izleyen ancak sadece **belirli bir ses seviyesi aşıldığında** kayıt yapan akıllı bir Python aracıdır.

Geleneksel ses kayıt cihazlarının aksine, saatlerce süren "boş sessizliği" kaydetmez. Sadece aksiyon anını yakalar. Bu özellik, disk alanından tasarruf sağlar ve kayıtların analiz edilmesini kolaylaştırır.

### 🎯 Neden Kullanılır?
* **Akıllı Depolama:** Gereksiz sessizlikleri diskte tutmaz.
* **Otomasyon:** Belirli bir gürültü eşiği (Threshold) aşıldığında otomatik tetiklenir.
* **Güvenlik:** Ortam güvenliği veya bebek telsizi mantığıyla kullanılabilir.

## 🚀 Özellikler

* 🎛️ **Ayarlanabilir Hassasiyet:** Ortam gürültüsüne göre tetiklenme eşiğini değiştirebilirsiniz.
* 📂 **Otomatik Arşivleme:** Kayıtları tarih ve saat etiketiyle (`REC_YYYYMMDD_HHMMSS.wav`) klasörler.
* ⚡ **Düşük Kaynak Tüketimi:** Arka planda CPU'yu yormadan çalışır.
* 📊 **RMS Analizi:** Ses şiddetini matematiksel (Root Mean Square) yöntemle analiz eder.

## 🛠️ Kurulum

Projenin çalışması için Python 3.x ve aşağıdaki kütüphanelerin yüklü olması gerekir.

1. Projeyi indirin veya klonlayın.
2. Gerekli kütüphaneleri kurun:

    ```bash
         pip install sounddevice numpy scipy
        💻 Kullanım
         Terminal veya komut satırını proje klasöründe açarak şu komutu girin:

    python ghost_listener.py

       Program çalışmaya başladığında:

       Gizli_Kayitlar klasörünü otomatik oluşturur.

         Ortamı dinlemeye başlar.

      ses algılandığında konsolda [!] SES ALGILANDI! uyarısı verir ve kayda başlar.

       Durdurmak için CTRL + C kombinasyonunu kullanabilirsiniz.
##⚙️ Konfigürasyon
ghost_listener.py dosyasının başındaki şu değişkenleri değiştirerek programı ortamınıza göre özelleştirebilirsiniz:

Python

# Tetiklenme Hassasiyeti (Düşük sayı = Daha Hassas)
# Örnek: 0.01 çok hassas, 0.1 sadece yüksek sesler
ESIK_DEGERI = 0.02  

# Ses algılandığında yapılacak kaydın süresi (saniye)
KAYIT_SURESI = 5    

# Ses Kalitesi (44100 = CD Kalitesi)
SAMPLE_RATE = 44100 
🗺️ Yol Haritası (To-Do)
[x] Temel ses algılama ve WAV kayıt

[ ] MP3 formatında sıkıştırma desteği

[ ] Ses algılandığında e-posta bildirimi (SMTP)

[ ] Konuşmayı yazıya dökme (Speech-to-Text)

🤝 İletişim & Katkı
Bu proje açık kaynaklıdır. Hata bildirmek veya özellik eklemek için Pull Request gönderebilirsiniz.

Geliştirici: egnake
