#2.ODEV: SAYI TAHMIN OYUNU
#   Bir degiskene 0-100 arasinda bir deger atayin. Kullanicidan bu sayiyi tahmin etmesini isteyin. Kullaniciyi yaptigi tahminlere gore yonlendirin. Kacinci denemede bildigini soyleyin.
#   Ornek:
#       sayi = 76
#       kullanicinin tahmini = 5
#       cikti = cok dusuk tahminde bulundun daha yuksek bir sayi girmelisin.
#       kullanicinin tahmini = 95
#       cikti = fazla yukari ciktin biraz asagi in.
#       kullanicinin tahmini = 80
#       cikti = cok yaklastin biraz daha inmelisin
#       kullanicinin tahmini = 73
#       cikti = cok yaklastin biraz daha cikmalisin
#       kullanicinin tahmini = 76
#       cikti= tebrikler sayiyi 5.denemede buldunuz


######FOR ILE OLAN###

deneme = 10                                                                       #Programi 10 deneme hakki ile sinirladik.
sayi = 41                                                                         #Tuttugum sayi 41.

for deneme in range(deneme):                                                      #for dongusu belirlenmis sayida yinelenecek sekilde kurulur.Burada denemeye 10 dedigimiz ve range deneme dedigimiz icin tahmin bilinene kadar 10 kere yinelenecek.
    tahmin = int(input("Aklimdan bir sayi tuttum, hadi tahmin et: "))             #Kullanicidan bir tahmin istiyorum

    if  sayi-5>tahmin:                                                            #Tahmin tuttugum sayidan 5ten fazla eksikse
        print("Cok dusuk bir tahminde bulundun daha yuksek bir sayi girmelisin.") #dusuk tahminde bulundun artir diyorum.
    elif sayi+5<tahmin:                                                           #Tahmin tuttugum sayinin 5 fazlasindan da fazlaysa
        print("Fazla yukari ciktin biraz asagi in.")                              #yuksek tahminde bulundun azalt diyorum.
    elif tahmin-5<sayi<tahmin and tahmin!=sayi:                                   #Tahmin tuttugum sayinin maximum 5 fazlasindaysa
        print("Cok yaklastin biraz daha inmelisin.")                              #biraz daha in
    elif tahmin+5>sayi>tahmin and tahmin!=sayi:                                   #Tahmin tuttugum sayinin maximum 5 asagisindaysa
        print("Cok yaklastin biraz daha cikmalisin.")                             #biraz daha cik
    else:
        print()
        print("\nBildin! Tuttugum sayi " ,sayi, "idi.")                           #Bunlardan hicbiri degilse(zaten o zaman syi==tahmin, yani bildin
        print("Sayiyi ", deneme+1, ". denemende buldun!")                         #dongu denemenin her bir ogesi kadar yineleneceginden deneme+1 (range 0dan basladigi icin deneme+1)
                                                                                  #yinelemede buldun demek oluyor
        break                                                                     #Sayiyi buldun artik yineleme

if tahmin != sayi:                                                                #Eger deneme hakkini bitirdiysen yani for loopun range sona erdiyse
    print()                   
    print("\n Uzgunuz, maksimum deneme sayisini astiniz.")                        #Deneme hakkiniz bitti.
    print("Tuttugum sayi ",sayi, "idi.")                                          #En son tuttugum sayiyi soyluyorum.


#1. Kod calisiyor.
#2. Bug yok.
#3. Mantik hatasi yok.
#4.Degisken isimleri acik.
#5.Anlasilir bir kod.
#6.Bilgim dahilinde olmasi gereken uzunlukta.
#7. Yorum eklenmis.
#8. Algoritma mantikli. 
#9.Kapsamli



####WHILE ILE###

#Programi 10 deneme hakki ile sinirladik.

deneme = 1                                                                   #Kullanicinin her seferinde kacinci denmesini yaptigini 
sayi = 41                                                                    #bilmek icin deneme=degiskenine 1 atiyoruz
                                                                             #sayi degsikenimize de 41 atiyoruz. Bu kullancinin bilmeye calisacagi sayi.

tahmin = int(input("Aklimdan bir sayi tuttum, hadi tahmin et: "))

while sayi != tahmin and deneme < 11:

    if  sayi-5>tahmin:
        print("Cok dusuk bir tahminde bulundun daha yuksek bir sayi girmelisin.")
    elif sayi+5<tahmin:
        print("Fazla yukari ciktin biraz asagi in.")
    elif tahmin-5<sayi<tahmin and tahmin!=sayi:
        print("Cok yaklastin biraz daha inmelisin.")
    elif tahmin+5>sayi>tahmin and tahmin!=sayi:
        print("Cok yaklastin biraz daha cikmalisin.")
    tahmin = int(input("Bir tahminde bulun: "))
    deneme += 1

if deneme == 10:
    print("\n Uzgunuz, maksimum deneme sayisini astiniz.")
    print("Tuttugum sayi ",sayi, "idi.") 

else:
    print("\nBildin! Tuttugum sayi " ,sayi, "idi.")
    print("Sayiyi ", deneme, ". denemende buldun!")

input("\n\n Cikmak icin enter'a bas.") 




#1. Kod calisiyor.
#2. Bug var. 10. denemeye gelince deneme hakkiniz bitti diyecegi yere tebrikler bildiniz 11. denemenizde vs diyor.
#3. Mantik hatasi olabilir, belki o yuzden dogru islemiyor 10'a gelince, ama ben goremiyorum su anda.
#4.Degisken isimleri acik.
#5.Anlasilir bir kod.
#6.Bilgim dahilinde olmasi gereken uzunlukta.
#7. Yorum eklenmis.
#8. Algoritma mantikli; ama mantiksiz bira tarafi var ki kod 10.da yanlis isliyor. 
#9.Kapsamli
