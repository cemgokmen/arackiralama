#Bu proje git hub üzerinden güncellendi
class GaleriSistemi:
    def __init__(self):
        self.araclar = {
            "Fiat Egea":      {"durum": "Musait", "fiyat": 1200},
            "Renault Clio":   {"durum": "Musait", "fiyat": 1300},
            "Toyota Corolla": {"durum": "Kirada", "fiyat": 1800},
            "Ford Focus":     {"durum": "Musait", "fiyat": 1900},
            "BMW 320i":       {"durum": "Musait", "fiyat": 3500}
        }
        # YENI: Müşteri listesi
        self.musteriler = []

    def araclari_goster(self):
        print("\n--- 🚗 GUNCEL ARAC LISTESI ---")
        for model, detay in self.araclar.items():
            durum_isareti = "✅" if detay["durum"] == "Musait" else "❌"
            print(f"{durum_isareti} {model} \t| Fiyat: {detay['fiyat']} TL \t| Durum: {detay['durum']}")

    def arac_kirala(self):
        self.araclari_goster()
        secim = input("\nKiralamak istediginiz aracin tam adini yazin: ")
        if secim in self.araclar and self.araclar[secim]["durum"] == "Musait":
            self.araclar[secim]["durum"] = "Kirada"
            print(f"\n>>> BASARILI! {secim} kiralandi.")
        else:
            print("\n>>> HATA: Arac yok veya zaten kirada.")

    def iade_al(self):
        secim = input("\nIade edilecek aracin adini yazin: ")
        if secim in self.araclar:
            self.araclar[secim]["durum"] = "Musait"
            print(f"\n>>> ISLEM TAMAM: {secim} geri alindi.")

    # YENI: Müşteri ekleme fonksiyonu
    def musteri_ekle(self):
        isim = input("\nMusteri Adi Soyadi: ")
        self.musteriler.append(isim)
        print(f">>> {isim} sisteme eklendi.")
        print("Guncel Musteriler:", self.musteriler)

# --- PROGRAM DONGUSU ---
galeri = GaleriSistemi()

while True:
    print("\n=== OTO GALERI V3 ===")
    print("1. Araclari Listele")
    print("2. Arac Kirala")
    print("3. Arac Iade Al")
    print("4. Musteri Ekle (YENI)")
    print("5. Cikis")
    
    secim = input("Seciminiz: ")
    
    if secim == '1': galeri.araclari_goster()
    elif secim == '2': galeri.arac_kirala()
    elif secim == '3': galeri.iade_al()
    elif secim == '4': galeri.musteri_ekle()
    elif secim == '5': break
