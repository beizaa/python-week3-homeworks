#4.ODEV: ALAN-HACIM HESAPLAMA
#   Karenin, ucgenin ve diktortgenin alanlarini hesaplayan,
#   kup,kure ve koni seklinde olan cisimlerin hacmini hesaplayan
#   bir program yazmanizi istiyoruz. Kullanicidan hangi seklin
#   alanini veya hangi sekildeki cismin hacmini hesaplamak istedigini
#   sormalisiniz ve o islem icin gereken verileri isteyip hesaplamayi yapmalisiniz.

while True:                                                                #Islem yapildiktan sonra sorular yinelesin diye buradan bir while dongusu baslatiyoruz. 
    hesap=input("Alan mi hacim mi hesaplamak istiyorsunuz?")               #Once kullaniciya alan mi yoksa hacim hesabi mi yapmak istedigini soruyoruz.
                                                           
    if hesap=="hacim":                                                     #eger hacimse, o zaman (Burada aslinda dongu icinde donguye girdik) hangi cismin hacmi?
        cisim=input("Hacmini hesaplayacaginiz cisim  nedir?")
        if cisim=="kup":                                                   #Kupun hacim formulu kenar uzunluklarinin kupunun alinmasidir veriyi alip bunu uyguluyoruz.
            kup_kenar=int(input("Kenar uzunlugunu giriniz."))
            print(pow(kup_kenar,3))
        elif cisim=="kure":                                                #Kurenin hacim formulu 4/3.pi.r.r.r   Yaricapi alip bunu uyguluyoruz.
            kure_yaricap=int(input("Kurenin yaricapini giriniz.")) 
            print(4/3*3.14*pow(kure_yaricap, 3))                           #Buradaki 3.14 degeri pi sayisidir.
        elif cisim=="koni":                                                #Koni hacim formulu 1/3.pi.r.r.h Yani 1/3 ile pi sayisi yukseklik ve yaricapin karesinin carpimi
            koni_yaricap=int(input("Koninin yaricapini giriniz."))
            koni_yukseklik=int(input("Koninin yuksekligini giriniz."))
            print((1/3)*3.14*pow(koni_yaricap, 2)*koni_yukseklik)          #Buradaki 3.14 degeri pi sayisidir.

    elif hesap=="alan":                                                    #Eger hesaplanmak istenen alansa o zaman kare ucgen ve dikdortgen var hepsinin verileri alip hesapliyoruz.
        cisim=input("Alanini hesaplayacaginiz cisim  nedir?")
        if cisim=="kare":                                                  #Karenin alani icin kenar uzunlugu yeterli. Bir kenarinin karesi alanini verir.
            kare_kenar=int(input("Kenar uzunlugunu giriniz."))
            print(pow(kare_kenar,2))
        elif cisim=="ucgen":                                               #Ucgen icin yukseklik ve dik kenar uzunlugunu bilmeliyiz. Sonra bunlari carpip ikiye bolecegiz.
            ucgen_ilkdik_kenar=int(input("Ilk dik kenar uzunlugunu giriniz."))
            ucgen_ikincidik_kenar=int(input("Ikinci dik kenar uzunlugunu giriniz."))
            print((ucgen_ilkdik_kenar*ucgen_ikincidik_kenar)/2)
        elif cisim=="dikdortgen":                                          #Burada kisa kenarn uzun kenardan kisa olmasi gerektigini sistemsel olarak soylememiz belki hos olabilridi.
            kisa_kenar=int(input("Kisa kenar uzunlugunu giriniz."))        #Dikdortgende kisa ve uzun kenar uzunluklarini carparak alani buluruz.
            uzun_kenar=int(input("Uzun kenar uzunlugunu giriniz."))
            print(kisa_kenar*uzun_kenar)
        else:
            print("Bu cisim sistemimizde tanimli degil, baska bir cisim deneyin.")
            continue


#1. Kod calisiyor.
#2. Bug ben goremedim ama olabilir.
#3. Mantik hatasi olabilir.
#4.Degisken isimleri acik, belki biraz uzun.
#5.Anlasilir bir kod.
#6.Gerekenden kisa gibi.
#7. Yorum eklenmis.
#8. Algoritma mantikli, ama mantiga ters aciklari olduguna neredeyse emeinim cunku sanirim uzerine gerekenden biraz az zaman harcadim. 
#9.Daha kapsamli yapilabilir.Mesela eskenar ucgen, cesitkenar ucgen icin ayri ayri vs.
    #Kullanici int yerine str girince uyarilabilir.

 









#Buradaki bir problem istenen islem gerceklestikten sonra en basa donmemesi yani tekrar alan mi hacim mi diye sormuyor da hacmi hesaplanmak istenen eleman hangisi vs diyor.
