def siparisFiyatAyirici(kategori):
        
    f = open(f'./database/menu/{kategori}.txt', 'r')
    okunanDeger = f.read()
    f.close()

    # Burada okuduğum değerdeki yeni satırları silip, bir listeye çeviriyorum.
    siparisList = okunanDeger.split('\n')

    # Bu döngü sonrasında Her bir siparisin içeriğini ve fiyatını icerikFiyat listesinde topluyorum. Toplama işlemim ve siparişleri yazdırma işlemim kolaylaşacak.
    icerikFiyatList = []
    for i in range(0, len(siparisList), 1):
        sonuc = siparisList[i].split('=>')  
        icerikFiyatList.append(sonuc)


    # bu döngü sonunda her bir siparis fiyatsız olarak "siparislerList" listesinde, her bir siparisin sadece fiyatını ise "fiyatlarList" listesinde topluyorum
    siparislerList = []
    fiyatlarList = []
    for i in range(0, len(icerikFiyatList), 1):
        sonuc = icerikFiyatList[i][0].strip()
        siparislerList.append(sonuc)

        sonuc = icerikFiyatList[i][1].split('TL')
        sonuc = sonuc[0].strip()
        fiyatlarList.append(sonuc)

    # bu değerleri döndürüyorum
    return siparislerList, fiyatlarList