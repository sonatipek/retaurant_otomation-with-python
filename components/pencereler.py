import tkinter as tk
from tkinter.font import Font
from tkinter import ttk

import components.masalar as masalar
import functions.siparisAyirici as spa
import functions.txtIslemleri as txt
import functions.siparisGoruntule as spg


# bu fonksiyon menü penceresini içerir
def menu_window():
    header = Font(family='Arial', 
              size=14, 
              weight='normal')
    menuWindow = tk.Tk()
    menuWindow.title("Bergama MYO | Restoran Menüsü")
    menuWindow.geometry("480x600+100+50")
    menuWindow.resizable(False, False)

    mainHeader = tk.Label(menuWindow, text="BERGAMA MYO RESTORAN MENÜSÜ", font=header)
    mainHeader.grid(row=0, column=0, pady=30, padx=75)

    # Kahvaltılıklar
    sonuc = spa.siparisFiyatAyirici("kahvaltilar")
    siparisler = sonuc[0]
    fiyatlar = sonuc[1]

    kahvaltiliklar = tk.LabelFrame(menuWindow, text="Kahvaltılıklar", labelanchor="n")
    kahvaltiliklar.grid(row=10, column=0, padx=75)

    for i in range(0, len(sonuc[0]),1):
        menuItems = tk.Label(kahvaltiliklar, text=f"{siparisler[i]} => {fiyatlar[i]} TL").pack(anchor=tk.W)
        

    # Ana Yemekler
    sonuc = spa.siparisFiyatAyirici("anaYemekler")
    siparisler = sonuc[0]
    fiyatlar = sonuc[1]

    anayemekler = tk.LabelFrame(menuWindow, text="Ana Yemekler", labelanchor="n")
    anayemekler.grid(row=20, column=0, padx=75)

    for i in range(0, len(sonuc[0]),1):
        menuItems = tk.Label(kahvaltiliklar, text=f"{siparisler[i]} => {fiyatlar[i]} TL").pack(anchor=tk.W)

    # Tatlilar
    sonuc = spa.siparisFiyatAyirici("tatlilar")
    siparisler = sonuc[0]
    fiyatlar = sonuc[1]

    tatlilar = tk.LabelFrame(menuWindow, text="Tatlilar", labelanchor="n")
    tatlilar.grid(row=30, column=0, padx=75)

    for i in range(0, len(sonuc[0]),1):
        menuItems = tk.Label(tatlilar, text=f"{siparisler[i]} => {fiyatlar[i]} TL").pack(anchor=tk.W)

    # İçecekler
    sonuc = spa.siparisFiyatAyirici("icecekler")
    siparisler = sonuc[0]
    fiyatlar = sonuc[1]

    icecekler = tk.LabelFrame(menuWindow, text="İçecekler", labelanchor="n")
    icecekler.grid(row=40, column=0, padx=75)

    for i in range(0, len(sonuc[0]),1):
        menuItems = tk.Label(icecekler, text=f"{siparisler[i]} => {fiyatlar[i]} TL").pack(anchor=tk.W)



# bu fonksiyon siparis penceresini içerir
def siparis_window():
    siparisWindow = tk.Tk()
    siparisWindow.title("Bergama MYO | Restoran Siparisler")
    siparisWindow.resizable(False, False)
    
    # Masaların Göstergeleri
    # Masa -1
    masa1 = tk.LabelFrame(siparisWindow, text="Masa #1", labelanchor="n")
    masa1.grid(row=0, column=0, padx=10)


    # Bu fonksiyon ile  masadaki siparisleri ve toplamı masanın siparis görüntüleme kısmına yazıyoruz
    spg.siparisGoruntule(masa1,"masa1")
    

    #Masa -2
    masa2 = tk.LabelFrame(siparisWindow, text="Masa #2", labelanchor="n")
    masa2.grid(row=0, column=10, padx=10)

    spg.siparisGoruntule(masa2,"masa2")


    #Masa -3
    masa3 = tk.LabelFrame(siparisWindow, text="Masa #3", labelanchor="n")
    masa3.grid(row=0, column=20, padx=10)

    spg.siparisGoruntule(masa3,"masa3")


    #Masa -4
    masa4 = tk.LabelFrame(siparisWindow, text="Masa #4", labelanchor="n")
    masa4.grid(row=0, column=30, padx=10)

    spg.siparisGoruntule(masa4,"masa4")


    #Masa -5
    masa5 = tk.LabelFrame(siparisWindow, text="Masa #5", labelanchor="n")
    masa5.grid(row=0, column=40, padx=10)

    spg.siparisGoruntule(masa5,"masa5")


    #Masa -6
    masa6 = tk.LabelFrame(siparisWindow, text="Masa #6", labelanchor="n")
    masa6.grid(row=150, column=0, pady=5, padx=10)

    spg.siparisGoruntule(masa6,"masa6")


    #Masa-7
    masa7 = tk.LabelFrame(siparisWindow, text="Masa #7", labelanchor="n")
    masa7.grid(row=150, column=10, padx=10)

    spg.siparisGoruntule(masa7,"masa7")


    #Masa -8
    masa8 = tk.LabelFrame(siparisWindow, text="Masa #8", labelanchor="n")
    masa8.grid(row=150, column=20, padx=10)

    spg.siparisGoruntule(masa8,"masa8")


    #Masa -9
    masa9 = tk.LabelFrame(siparisWindow, text="Masa #9", labelanchor="n")
    masa9.grid(row=150, column=30, padx=10)

    spg.siparisGoruntule(masa9,"masa9")


    #Masa -10
    masa10 = tk.LabelFrame(siparisWindow, text="Masa #10", labelanchor="n")
    masa10.grid(row=150, column=40, pady=100, padx=10)
    
    spg.siparisGoruntule(masa10,"masa10")

    
def siparisEkle():
    siparis_ekleWindow = tk.Tk()
    siparis_ekleWindow.title("Bergama MYO | Restoran Siparisler")
    siparis_ekleWindow.geometry("820x480+100+50")
    siparis_ekleWindow.resizable(False, False)

    # Yemekleri Ekle Fonksiyonları
    def ekleKuymak():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.write("Kuymak              =>  5TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a", encoding="UTF-8")
            f.write("\nKuymak              =>  5TL")
            f.close()

    def ekleMenemen():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.write("Menemen             =>  3TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a", encoding="UTF-8")
            f.write("\nMenemen             =>  3TL")
            f.close()

    def ekleCakalli():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.write("Cakalli Menemeni    =>  5TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a", encoding="UTF-8")
            f.write("\nCakalli Menemeni    =>  5TL")
            f.close()

    def ekleSerpme():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Serpme Kahvalti     =>  8TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nSerpme Kahvalti     =>  8TL")
            f.close()

    def ekleSamsun():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Samsun Pidesi               =>  8TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nSamsun Pidesi               =>  8TL")
            f.close()

    def ekleTavuk():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Tavuk Sis                   =>  5TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nTavuk Sis                   =>  5TL")
            f.close()

    def ekleKebap():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Kebap                       =>  8TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nKebap                       =>  8TL")
            f.close()

    def ekleIskender():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Iskender                    =>  9TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nIskender                    =>  9TL")
            f.close()

    def ekleOrdek():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Portakalli Pekin Ordegi     => 11TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nPortakalli Pekin Ordegi     => 11TL")
            f.close()

    def ekleAyran():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Ayran       =>  3TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nAyran       =>  3TL")
            f.close()

    def ekleKola():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Kola        =>  5TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nKola        =>  5TL")
            f.close()

    def ekleMeyve():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Meyve Suyu  =>  3TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nMeyve Suyu  =>  3TL")
            f.close()

    def ekleSu():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Su          =>  1TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nSu          =>  1TL")
            f.close()

    def ekleKunefe():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Kunefe              =>  5TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nKunefe              =>  5TL")
            f.close()

    def ekleKazan():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Kazandibi           =>  3TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nKazandibi           =>  3TL")
            f.close()

    def ekleSutlac():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Sutlac              =>  3TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nSutlac              =>  3TL")
            f.close()

    def ekleHamsikoy():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.writelines("Hamsikoy Sutlaci    =>  6TL")
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("\nHamsikoy Sutlaci    =>  6TL")
            f.close()

    def silHamsi():
        masaNo= masalar.get()
        f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "r+", encoding="UTF-8")
        okunan  = f.read()
        lines = f.readlines()

        if (okunan == "Bu masanın siparişi yok! => 0TL"):
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        
            f.close()
        else:
            f = open(f"./database/{masaNo}/{masaNo}Siparisler.txt", "a+", encoding="UTF-8")
            f.writelines("")
            f.close()


    header = Font(family='Arial', 
              size=14, 
              weight='normal')

    siparisEkleHeader = tk.Label(siparis_ekleWindow, text="Sipariş Ekle", font=header)
    siparisEkleHeader.grid(row=0, column=0, pady=30, padx=75)

    siparisEkleHeader = tk.Label(siparis_ekleWindow, text="Sipariş Ekleyeceğiniz Masayı Seçiniz: ")
    siparisEkleHeader.grid(row=20, column=0, pady=10)

    secilen_masa = tk.StringVar()
    masalar = ttk.Combobox(siparis_ekleWindow, textvariable=secilen_masa, state='readonly')
    masalar['values'] = ["masa1", "masa2", "masa3","masa4", "masa5", "masa6","masa7", "masa8", "masa9", "masa10"]
    masalar.current(0)
    masalar.grid(row=20, column=40)


    kuymak = tk.Label(siparis_ekleWindow, text="Kuymak").grid(row=30, column=0)
    tk.Button(siparis_ekleWindow, text="+", command=ekleKuymak).grid(row=30, column=10)

    menemen = tk.Label(siparis_ekleWindow, text="Menemen").grid(row=40, column=0)
    tk.Button(siparis_ekleWindow, text="+", command=ekleMenemen).grid(row=40, column=10)

    cakalli = tk.Label(siparis_ekleWindow, text="Çakallı Menemeni").grid(row=50, column=0)
    tk.Button(siparis_ekleWindow, text="+", command=ekleCakalli).grid(row=50, column=10)

    serpme = tk.Label(siparis_ekleWindow, text="Serpme Kahvaltı").grid(row=60, column=0)
    tk.Button(siparis_ekleWindow, text="+", command=ekleSerpme).grid(row=60, column=10)

    samsun = tk.Label(siparis_ekleWindow, text="Samsun Pidesi").grid(row=70, column=0)
    tk.Button(siparis_ekleWindow, text="+", command=ekleSamsun).grid(row=70, column=30)

    tavuk = tk.Label(siparis_ekleWindow, text="Tavuk Şiş").grid(row=80, column=0)
    tk.Button(siparis_ekleWindow, text="+", command=ekleTavuk).grid(row=80, column=30)

    kebap = tk.Label(siparis_ekleWindow, text="Kebap").grid(row=90, column=0)
    tk.Button(siparis_ekleWindow, text="+", command=ekleKebap).grid(row=90, column=30)

    iskender = tk.Label(siparis_ekleWindow, text="İskender").grid(row=100, column=0)
    tk.Button(siparis_ekleWindow, text="+", command=ekleIskender).grid(row=100, column=30)

    ordek = tk.Label(siparis_ekleWindow, text="Portakallı Pekin Ördeği").grid(row=110, column=0)
    tk.Button(siparis_ekleWindow, text="+", command=ekleOrdek).grid(row=110, column=30)

    ayran = tk.Label(siparis_ekleWindow, text="Ayran").grid(row=30, column=100)
    tk.Button(siparis_ekleWindow, text="+", command=ekleAyran).grid(row=30, column=130)

    kola = tk.Label(siparis_ekleWindow, text="Kola").grid(row=40, column=100)
    tk.Button(siparis_ekleWindow, text="+", command=ekleKola).grid(row=40, column=130)

    meyve = tk.Label(siparis_ekleWindow, text="Meyve Suyu").grid(row=50, column=100)
    tk.Button(siparis_ekleWindow, text="+", command=ekleMeyve).grid(row=50, column=130)

    su = tk.Label(siparis_ekleWindow, text="Su").grid(row=60, column=100)
    tk.Button(siparis_ekleWindow, text="+", command=ekleSu).grid(row=60, column=130)

    kunefe = tk.Label(siparis_ekleWindow, text="Künefe").grid(row=70, column=100)
    tk.Button(siparis_ekleWindow, text="+", command=ekleKunefe).grid(row=70, column=130)

    kazan = tk.Label(siparis_ekleWindow, text="Kazandibi").grid(row=80, column=100)
    tk.Button(siparis_ekleWindow, text="+", command=ekleKazan).grid(row=80, column=130)

    sutlac = tk.Label(siparis_ekleWindow, text="Sütlaç").grid(row=90, column=100)
    tk.Button(siparis_ekleWindow, text="+", command=ekleSutlac).grid(row=90, column=130)

    hamsikoy = tk.Label(siparis_ekleWindow, text="Hamsiköy Sütlacı").grid(row=100, column=100)
    tk.Button(siparis_ekleWindow, text="+", command=ekleHamsikoy).grid(row=100, column=130)