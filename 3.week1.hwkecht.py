#1.ODEV: HESAP OLUSTURMA
#   Kullanicidan, kullanici adi ve parola olusturarak hesap olusturmasini
#   isteyin. Bu aldiginiz bilgileri bir dosyaya yazdirin.
#   Her gırıste dosyadakı bılgıler sıfırlanmasın ((##w kullanma diyor) kayıt bılgılerı
#   dosyaya eklenmeye devam etsın. Kullanici daha once girilmis olan bir
#   kullanici adiyla hesap olusturmak isterse, bu kullanici adinin daha once
#   secildigini ve baska bir kullanici adiyla hesap olusturmasini isteyin.

f=open("Hesap_bilgileri.txt", "r+")
print(""" Giris: (1) Hesap olusturma,   
        (2) Cikis   """)
secim= int(input("Hangi islemi yapmak istediginizi seciniz."))
if secim==2:
    print("Program kapatiliyor...")

    
elif secim==1:
    while True:                                                                   #bunun icin bir dosya aciyoruz, yazdikca silinmesin yeniden eklensin diye w degil de
        kullanici_adi= str(input("Bir kullanici adi giriniz:"))#kullanicidan kullanici adi olusturmasini istiyoruz.
        parola=str(input("Parolaniz:"))

        with open("Hesap_bilgileri.txt", "r+") as f:
        veri= f.read()
        f.write(kullanici_adi\n + parola\n +veri)

        #f=open("Hesap_bilgileri.txt", "r")
        #data=f.read()
        if kullanici_adi in data:
            print("Bu kullanici adi zaten alinmis, lutfen yeni bir isim deneyiniz.")
        else:
            f==open("Hesap_bilgileri.txt", "a")
            data=kullanici_adi+parola
            f.write(data)
            f.close()
            print("Hesap olusturuldu.")
        break  
    else:
        print("Yanlis giris yaptiniz.")


 
#1. Kod calisiyor.
#2. Bug var. Hangi islemi yapmak istiyorsunuzu sorduktan sonra 1 veya 2yi secince devam etmiyor.
#3. Mantik hatasi olabilir, belki o yuzden dogru islemiyor 10'a gelince, ama ben goremiyorum su anda.
#4.Degisken isimleri acik.
#5.Anlasilir bir kod.
#6.Bilgim dahilinde olmasi gereken uzunlukta.
#7. Yorum eklenmis.
#8. Algoritma mantikli; ama mantiksiz bira tarafi var ki kod 10.da yanlis isliyor. 
#9.Kapsamli
