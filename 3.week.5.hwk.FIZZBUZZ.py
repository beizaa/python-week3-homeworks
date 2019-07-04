#5.ODEV: FIZZ BUZZ
#   1'den 100'e kadar sayilari yazdirin.
#   Fakat 3'e tam bolunen sayilarin yerine FIZZ,
#   5'e tam bolunen sayilarin yerine BUZZ, hem 3'e hem de 5'e
#   tam bolunebilen sayilarin yerine FIZZBUZZ yazsin.

for i in range(1,101):       #1den 100e kadar olan sayilari yazdiralim.
    if i%3==0 and i%5!=0:    #Eger sayi 3e tam bolunuyor ve 5e tam bolunmuyorsa:
        print("FIZZ")        #sayi yerine FIZZ yaz
    elif i%5==0 and i%3!=0:  #Eger sayi 5e tam bolunuyor ve 3e tam bolunmuyorsa:
        print("BUZZ")        #sayi yerine BUZZ yaz
    elif i%3==0 and i%5==0:  #Eger sayi hem 5e hem de 3e tam bolunuyorsa:
        print("FIZZBUZZ")    #sayi yerine FIZZBUZZ yaz
    else:                    #Eger sayi ne 3e ne de 5e tam bolunmuyorsa 
        print(i)             #sayiyi yazdir


     
 
#1. Kod calisiyor.
#2. Bug yok 
#3. Mantik hatasi yok.
#4.Degisken isimleri acik.
#5.Anlasilir bir kod.
#6.Bilgim dahilinde olmasi gereken uzunlukta.
#7. Yorum eklenmis.
#8. Algoritma mantikli.
#9.Kapsamli
