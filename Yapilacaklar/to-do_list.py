from datetime import date
to_do = []

def ekle(to_do):

    gorev = input("Görev ekle:")
    to_do.append("Görevin verildiği tarih:"+str(date.today())+" - Görev:"+gorev)

def listele(to_do):

    for i, gorevler in enumerate(to_do, start=1):
        print(f"{i}. {gorevler}")

def guncelle(to_do):
    listele(to_do)
    guncelleme = int(input("Güncellenecek Görevin id numarasını giriniz:"))

    if guncelleme > 0 and guncelleme <= len(to_do):
        yeni_guncelle = input("Yeni Görev:")
        to_do[guncelleme - 1] = yeni_guncelle  
        print("Görev başarıyla güncellendi.")
    else:
        print("Geçersiz ID numarası. Lütfen geçerli bir ID girin.")

def sil(to_do):
    listele(to_do)
    silme = int(input("Silinecek görevin id numarası:"))

    if silme > 0 and silme <= len(to_do):
        del to_do[silme - 1] 
        print("Görev başarıyla silindi.")
    else:
        print("Geçersiz ID numarası. Lütfen geçerli bir ID girin.")

while True:

    secim = input("1.Ekle\n2.Listele\n3.Güncelle\n4.Sil\nSeçim Yapınız:\n")

    if secim == "1":
        ekle(to_do)
    elif secim == "2":
        listele(to_do)
    elif secim == "3":
        guncelle(to_do)
    elif secim == "4":
        sil(to_do)

    