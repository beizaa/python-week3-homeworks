#6.ODEV: ASAL SAYI MI?
#   Kullanicidan aldiginiz sayinin asal sayi olup olmadigini
#   sorgulayan bir program yazmanizi istiyoruz.



while True:                                            #Programin yeniden yeniden calismasi icin while dongusu kurduk.
      sayac=0                                          #Sayac adli bir degisken tanimlayip ona 0 degerini  veriyoruz.
      sayi=input("Bir sayi giriniz: ")                 #Kullanicidan bir sayi istedik.ama inputa cevap hep string olarak geldigi icin bunuintegera cevirdik. 
      if str.isdigit(sayi)!=1: 
          print ("Bu bir sayı değildir. Lütfen SAYI Giriniz. Örnek: 2, 15, 594")
          continue
                                                       #Burada inputun karakter mi yoksa sayi mi oldugu kontrol ediliyor.
      print("""Asal sayi olup olmadiginizi
      bilmek istediginiz pozitif tam sayi: """, sayi)
      for i in range(2,int(sayi)):                     #2den kullanicinin girdigi sayiya kadar olan aralikta: 
            if(int(sayi)%i==0):                        #eger kullanicin gird sayi, bu araliktan bir seye tam bolunuyorsa 
                  sayac+=1                             #sayaci bir arttir
                
      if(sayac!=0):                                    #Eger sayac 0a esit degilse(o zaman sayi 2 ile sayi arasi bir seye tam bolunuyor demektir)
            print(sayi, "bir asal sayi degildir.")     #asal sayi degil (cunku asal sayilar hicbir sayiya bolunemez sayilardir.)

      
      else:                                            #eger sayac 0a esitse (2den kullanicinin girdigi sayiya kadar olan aralikta, kullanicin gird sayi, bu araliktan bir seye tam bolunmedigi surece)
            print(sayi, "bir asal sayidir.")           #asal sayidir



#1. Kod calisiyor.
#2. Bug yok 
#3. Mantik hatasi yok.
#4.Degisken isimleri acik.
#5.Anlasilir bir kod.
#6.Bilgim dahilinde olmasi gereken uzunlukta.
#7. Yorum eklenmis.
#8. Algoritma mantikli.
#9.Kapsamli
