import tkinter as tk
import functions.txtIslemleri as txt
import components.pencereler as pencereler

# Masanın siparislerini kapatan fonksiyon
def txtMasaKapat():
    global masa_no
    global pencere_ad

    f = open(f'./database/{masa_no}/{masa_no}Siparisler.txt', 'r', encoding="UTF-8")
    sonuc = f.read()
    f.close()
    
    f = open(f"./fisler/{masa_no}Fis.txt", "w", encoding="UTF-8")
    f.write(str(sonuc))
    f.close()


    f = open(f'./database/{masa_no}/{masa_no}Siparisler.txt', 'w', encoding="UTF-8")
    f.write('Bu masanın siparişi yok! => 0TL')
    f.close()

    masaToplam = tk.Label(pencere_ad, text="Masa başarıyla kapatıldı ve fiş 'fisler' klasörüne basıldı!").place(x=20, y=455)


def icerikOlustur(masaNo, pencereAd):
    global pencere_ad

    pencere_ad = pencereAd
    toplam = 0
    sonuc = txt.txtBaglanti(masaNo)
    siparisler = sonuc[0]
    fiyatlar = sonuc[1]
    

    labelframe = tk.LabelFrame(pencereAd, text="Siparişler", labelanchor="n")
    labelframe.pack(expand="yes", side="left")

    # Tüm siparişleri ekleyen döngü
    for i in range(0, len(siparisler),1):
        masaSiparis = tk.Label(labelframe, text=siparisler[i]).pack(anchor=tk.W)
    


    sep = tk.Label(labelframe, text="______________").pack(anchor=tk.W)
    # Toplamı hesaplayan döngü
    for i in range(0, len(fiyatlar),1):
        toplam = toplam + int(fiyatlar[i])
    masaToplam = tk.Label(labelframe, text=f"Toplam: {toplam} TL").pack(anchor=tk.W)


    global masa_no
    masa_no=masaNo
    masaTemizle = tk.Button(pencereAd, text="Masayı Kapat", command=txtMasaKapat)
    masaTemizle.place(x=20,y=430)

    siparisEkle = tk.Button(pencereAd, text="Masaya Sipariş Ekle", command=pencereler.siparisEkle)
    siparisEkle.place(x=190, y=430)