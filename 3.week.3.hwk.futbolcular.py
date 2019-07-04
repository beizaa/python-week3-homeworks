#3.ODEV: LISTE AYIKLAMA
#   Ekte gonderilmis olan text dosyasinda 3 takimin futbolcularinin
#   isimleri ve takimlari yer almaktadir. Sizden 3 tane dosya olusturmanizi
#   ve bu 3 dosyaya futbolculari takimlarina gore ayirmanizi istiyoruz.

f=open("futbolcular.txt")                #burada close yapmamak icin  simdi yazacagim ile de yaapmaz miydik??   with open("futbolcular.txt", "r+") as f:
veri = f.readlines()
                                                               #dosyayi ac
                                                               # dosyadakileri veri degiskenine verdik
for i in veri:                                                 #Burada dosyadakileri tek tek gosterelim diye for dongusu
  if "Fenerbahçe" in i:                                        #listedeki herhangi bri degerin icinde fenerbahce geciyorsa
    ff=open("fenerbahce.txt","a")                           # fenerbahce.txt diye bir dosya ac ve bu tarz ogeleri oraya yaz.
    ff.write(i)                             
  elif "Galatasaray" in i:                                     # galatasaray yaziyorsa ona da dosya acip yaz
    fg=open("galatasaray.txt","a")
    fg.write(i)
  elif "Beþiktaþ" in i:                                        # besiktas yaziyorsa ona da aynisini
    fb=open("besiktas.txt","a")
    fb.write(i)

f.close()
ff.close()
fg.close()
fb.close()


#1. Kod calisiyor.
#2. Bug olabilir emin degilim. 
#3. Mantik hatasi yok gibi duruyor.
#4.Degisken isimleri acik.
#5.Anlasilir bir kod (sanirim).
#6.Bilgim dahilinde olmasi gereken uzunlukta.
#7. Yorum eklenmis.
#8. Algoritma mantikli.
#9.Kapsamli
