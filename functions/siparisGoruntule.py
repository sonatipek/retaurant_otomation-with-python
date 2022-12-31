import tkinter as tk
import functions.txtIslemleri as txt

def siparisGoruntule(frameName, masaNo):
    toplam = 0
    sonuc = txt.txtBaglanti(masaNo)
    siparisler = sonuc[0]
    fiyatlar = sonuc[1]

    # Tüm siparişleri ekleyen döngü
    for i in range(0, len(siparisler),1):
        masaSiparis = tk.Label(frameName, text=siparisler[i]).pack(anchor=tk.W)

    sep = tk.Label(frameName, text="______________").pack(anchor=tk.W)
    # Toplamı hesaplayan döngü
    for i in range(0, len(fiyatlar),1):
        toplam = toplam + int(fiyatlar[i])
        
    masaToplam = tk.Label(frameName, text=f"Toplam: {toplam} TL").pack(anchor=tk.W)