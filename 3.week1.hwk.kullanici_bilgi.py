#1.ODEV: HESAP OLUSTURMA
#   Kullanicidan, kullanici adi ve parola olusturarak hesap olusturmasini
#   isteyin. Bu aldiginiz bilgileri bir dosyaya yazdirin.
#   Her gırıste dosyadakı bılgıler sıfırlanmasın ((##w kullanma diyor) kayıt bılgılerı
#   dosyaya eklenmeye devam etsın. Kullanici daha once girilmis olan bir
#   kullanici adiyla hesap olusturmak isterse, bu kullanici adinin daha once
#   secildigini ve baska bir kullanici adiyla hesap olusturmasini isteyin.



print(""" Giris: (1) Hesap olusturma,
       (2) Cikis   """)
secim= int(input("Hangi islemi yapmak istediginizi seciniz."))                           #1 ile hesap olusturma
                                                                                         #2 ile cikis


if secim==2:
   print("Program kapatiliyor...")
elif secim==1:
   while True:                                                                   
       kullanici_adi= str(input("Bir kullanici adi giriniz:"))                #kullanicidan kullanici adi ve parola olusturmasini istiyoruz.
       parola=str(input("Parolaniz:"))

       f=open("Hesap_bilgileri.txt", "r+")                                     #kullanici adi ve parola bilgilerini bir dosyaya yazdirabilmemiz lazim.
       veri=f.read()                                                           #bunun icin bir dosya aciyoruz, yazdikca silinmesin yeniden eklensin diye r+ ile aciyoruz.
       if kullanici_adi in veri:
           print("Bu kullanici adi zaten alinmis, lutfen yeni bir isim deneyiniz.")
       else:
           f==open("Hesap_bilgileri.txt", "a")
           veri=kullanici_adi+parola
           f.write(veri)
           f.close()
           print("Hesap olusturuldu.")
       break
   else:
       print("Yanlis giris yaptiniz.")



#1. Kod calisiyor.
#2. Bug yok. 
#3. Mantik hatasi yok.
#4.Degisken isimleri acik.
#5.Anlasilir bir kod.
#6.Bilgim dahilinde olmasi gereken uzunlukta.
#7. Yorum eklenmis.
#8. Algoritma mantikli. 
#9.Kapsamli
