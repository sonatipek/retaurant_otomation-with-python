import tkinter as tk
import components.masalar as masalar
import components.pencereler as pencereler
from tkinter.font import Font

# Tüm Masaları Temizle
def clearAllTable():
    global MainWindow
    for i in range(1,11,1):
        f = open(f'./database/masa{i}/masa{i}Siparisler.txt', 'r', encoding="UTF-8")
        sonuc = f.read()
        f.close()
        
        f = open(f"./fisler/masa{i}Fis.txt", "w", encoding="UTF-8")
        f.write(str(sonuc))
        f.close()

        f = open(f'./database/masa{i}/masa{i}Siparisler.txt', 'w',encoding="UTF-8")
        f.write('Bu masanın siparişi yok! => 0TL')
        f.close()

        masaToplam = tk.Label(MainWindow, text="Masalar başarıyla kapatıldı ve fişleri 'fisler' klasörüne basıldı!").place(x=75, y=220)

# Main Window
global MainWindow

MainWindow = tk.Tk()
MainWindow.title("Bergama MYO | Restoran Yönetim Sistemi")
MainWindow.geometry("480x280+100+50")
MainWindow.resizable(False, False)

header = Font(family='Arial', 
              size=14, 
              weight='normal')

# Restoran Başlık
restoran_adi = tk.Label(MainWindow, text="Bergama MYO Lokantasına Hoş Geldiniz", font=header)
restoran_adi.pack()

# Masaların Butonları
masa1 = tk.Button(MainWindow, text="Masa #1", command=masalar.masa1) 
masa1.place(x=10, y=50)

masa2 = tk.Button(MainWindow, text="Masa #2", command=masalar.masa2) 
masa2.place(x=110, y=50)

masa3 = tk.Button(MainWindow, text="Masa #3", command=masalar.masa3) 
masa3.place(x=210, y=50)

masa4 = tk.Button(MainWindow, text="Masa #4", command=masalar.masa4) 
masa4.place(x=310, y=50)

masa5 = tk.Button(MainWindow, text="Masa #5", command=masalar.masa5) 
masa5.place(x=410, y=50)

masa6 = tk.Button(MainWindow, text="Masa #6", command=masalar.masa6) 
masa6.place(x=10, y=100)

masa7 = tk.Button(MainWindow, text="Masa #7", command=masalar.masa7) 
masa7.place(x=110, y=100)

masa8 = tk.Button(MainWindow, text="Masa #8", command=masalar.masa8) 
masa8.place(x=210, y=100)

masa9 = tk.Button(MainWindow, text="Masa #9", command=masalar.masa9) 
masa9.place(x=310, y=100)

masa10 = tk.Button(MainWindow, text="Masa #10", command=masalar.masa10) 
masa10.place(x=410, y=100)
# Masaların butonları bitişi


# Menü Button
menu_button = tk.Button(MainWindow, text="Menüyü Görüntüle", command=pencereler.menu_window)
menu_button.place(x=100, y=150)

# Siparisler Button
siparisler_button = tk.Button(MainWindow, text="Siparişleri Görüntüle", command=pencereler.siparis_window)
siparisler_button.place(x=250, y=150)

temizle_button = tk.Button(MainWindow, text="Tüm Siparişleri Temizle", command=clearAllTable)
temizle_button.place(x=170, y=190)

# Telif Footer
author_name = tk.Label(MainWindow, text="© Bergama Meslek Yüksekoulu | Sonat Saygın İpek - 90210000216")
author_name.place(x=0, y=260)



MainWindow.mainloop()