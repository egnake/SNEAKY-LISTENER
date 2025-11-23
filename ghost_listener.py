import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time
from datetime import datetime
import os

# --- AYARLAR (HASSASİYETİ BURADAN YAP) ---
ESIK_DEGERI = 0.02  # Ses hassasiyeti (0.01 çok hassas, 0.1 bağırınca çalışır)
KAYIT_SURESI = 5    # Ses algılayınca kaç saniye kaydetsin?
SAMPLE_RATE = 44100 # Ses kalitesi (CD Kalitesi)

# Kayıtların tutulacağı klasör
KAYIT_KLASORU = "Gizli_Kayitlar"

def klasor_hazirla():
    if not os.path.exists(KAYIT_KLASORU):
        os.makedirs(KAYIT_KLASORU)

def ses_algilandi_mi(indata, frames, time, status):
    """Mikrofondan gelen veriyi analiz eder."""
    # Gelen ses verisinin (indata) matematiksel ortalamasını (RMS) al
    # Bu bize sesin "şiddetini" verir.
    volume_norm = np.linalg.norm(indata) * 10
    
    # Eğer ses şiddeti eşiği geçerse True döner (Global değişken kontrolü dışarıda yapılır)
    # Burası sadece stream callback içindir, asıl mantık aşağıda.
    pass 

def dinle_ve_kaydet():
    print("-" * 40)
    print("👂 GHOST LISTENER AKTİF - Ortam Dinleniyor...")
    print(f"[*] Hassasiyet: {ESIK_DEGERI}")
    print("Durdurmak için: CTRL + C")
    print("-" * 40)
    
    klasor_hazirla()

    while True:
        try:
            # 0.5 saniyelik kısa bir dinleme yap (Ortamı kokla)
            # sd.rec arka planda çalışır, o yüzden wait() ile bitmesini bekliyoruz
            kayit = sd.rec(int(0.5 * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
            sd.wait()
            
            # Sesin şiddetini (Volume) hesapla
            # np.linalg.norm vektörün büyüklüğünü verir (Ses dalgasının genliği)
            ses_siddeti = np.linalg.norm(kayit) * 10
            
            # Ekrana anlık ses seviyesini bas (Ayar yaparken işine yarar)
            # print(f"Ses Seviyesi: {ses_siddeti:.4f}") 

            # Eğer ses eşiği geçerse KAYDA BAŞLA
            if ses_siddeti > ESIK_DEGERI:
                zaman_damgasi = datetime.now().strftime("%Y%m%d_%H%M%S")
                print(f"\n[!] SES ALGILANDI! ({ses_siddeti:.2f}) -> Kayıt Başlıyor...")
                
                # Belirlenen süre kadar kayıt al
                uzun_kayit = sd.rec(int(KAYIT_SURESI * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
                sd.wait()
                
                # Dosyayı kaydet
                dosya_adi = os.path.join(KAYIT_KLASORU, f"REC_{zaman_damgasi}.wav")
                
                # Numpy array'i WAV formatına çevirip kaydet
                # (Veriyi normalize etmemiz gerekebilir ama scipy genelde halleder)
                wav.write(dosya_adi, SAMPLE_RATE, uzun_kayit)
                
                print(f"[+] Kaydedildi: {dosya_adi}")
                print("[*] Tekrar dinlemeye geçildi...")
                
        except KeyboardInterrupt:
            print("\nProgram kapatılıyor.")
            break
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    dinle_ve_kaydet()