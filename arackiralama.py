class GaleriSistemi:
    def __init__(self):
     
        self.araclar = {
            "Fiat Egea":      {"durum": "Musait", "fiyat": 1200},
            "Renault Clio":   {"durum": "Musait", "fiyat": 1300},
            "Toyota Corolla": {"durum": "Kirada", "fiyat": 1800},
            "Ford Focus":     {"durum": "Musait", "fiyat": 1900},
            "BMW 320i":       {"durum": "Musait", "fiyat": 3500}
        }

    def araclari_goster(self):
        print("\n--- 🚗 GUNCEL ARAC LISTESI ---")
        for model, detay in self.araclar.items():
            durum_isareti = "✅" if detay["durum"] == "Musait" else "❌"
            print(f"{durum_isareti} {model} \t| Fiyat: {detay['fiyat']} TL \t| Durum: {detay['durum']}")

    def arac_kirala(self):
        self.araclari_goster()
        secim = input("\nKiralamak istediginiz aracin tam adini yazin: ")
        
        if secim in self.araclar:
            if self.araclar[secim]["durum"] == "Musait":
                self.araclar[secim]["durum"] = "Kirada"
                print(f"\n>>> BASARILI! {secim} kiralandi. Iyi yolculuklar!")
            else:
                print(f"\n>>> HATA: {secim} su an zaten kirada!")
        else:
            print("\n>>> HATA: Boyle bir arac galerimizde yok.")

    def iade_al(self):
        secim = input("\nIade edilecek aracin adini yazin: ")
        
        if secim in self.araclar:
            if self.araclar[secim]["durum"] == "Kirada":
                self.araclar[secim]["durum"] = "Musait"
                print(f"\n>>> ISLEM TAMAM: {secim} galerimize geri alindi.")
            else:
                print(f"\n>>> BILGI: {secim} zaten bizde (Musait durumda).")
        else:
            print("\n>>> HATA: Bu arac bizim sistemimize kayitli degil.")

galeri = GaleriSistemi()

while True:
    print("\n" + "="*30)
    print("   OTO GALERI YONETIM SISTEMI")
    print("="*30)
    print("1. Araclari Listele")
    print("2. Arac Kirala")
    print("3. Arac Iade Al")
    print("4. Cikis")
    
    kullanici_secimi = input("Yapmak istediginiz islem (1-4): ")
    
    if kullanici_secimi == '1':
        galeri.araclari_goster()
    elif kullanici_secimi == '2':
        galeri.arac_kirala()
    elif kullanici_secimi == '3':
        galeri.iade_al()
    elif kullanici_secimi == '4':
        print("Sistemden cikiliyor... Iyi gunler!")
        break
    else:
        print("Gecersiz secim, lutfen tekrar deneyin.")
    
