import datetime                                # Fişte saat ve tarihin görünmesini istediğimiz için datetime modülünü kullandık.

Envanter = {'kuşkonmaz': [10, 5],              # Hocamızın istemiş olduğu Envanter adlı sözlüğü kopyalayıp yapıştırdık.
            'brokoli': [15, 6],
            'havuç': [18, 7],
            'elmalar': [20, 5],
            'muz': [10, 8],
            'meyve': [30, 3],
            'yumurta': [50, 2],
            'karışık meyve suyu': [0, 18],
            'balık çubukları': [25, 12],
            'dondurma': [32, 6],
            'elma suyu': [40, 7],
            'portakal suyu': [30, 8],
            'üzüm suyu': [10, 9]
            }
envanter_arama = ','.join(Envanter.keys())                       # Envanter'in keys(değer) kısmını her virgülden sonrasını içine yazacak şekilde envanter_arama adlı değişkenin içine atadık.
a_list = []                                                      # a_list diye boş bir liste oluşturduk.
dictionary_copy = Envanter.copy()                                # Envanterin kopyasını .copy metoduyla dictionary_copy adlı değişkene atadık.
a_list.append(dictionary_copy)                                   # dictionary_copy'i a_list in içine ekledik.
x = str(a_list)                                                  # a_list'in class'ını string yaptık ve x değişkenine atadık.
kullanici_bilgileri = {"Ahmet": "istinye123", "Meryem": "4444"}  # Kayıtlı kullanıcılarımızın adını ve şifresini kullanici_bilgileri değişkenine atadık.
kullanici = ""                                                   # kullanici adlı boş bir str oluşturduk
sepet = {"Ahmet": {},                                            # sepet adlı bir sözlük oluşturduk.(Kullanıcıların sepetleri)
         "Meryem": {}
         }

def menu():                                                           # menu() adlı bir fonksiyon tasarladık
    while True:                                                       # while döngüsünü başlattık.
                                                                      # print komutu ile ana menüyü yazdırdık.
        print('''                                                     
                    Lütfen aşağıdaki hizmetlerden birini seçiniz:
                    1. Ürün ara
                    2. Sepete git
                    3. Satın al                                          
                    4. Oturum Kapat
                    5. Çıkış yap
                    '''
              )
        secim = input("Seçiminiz: ")                                  # Bir input kullanıcı girdisi açtık. secim değişkenine atadık.

        if secim == "1":                                              # input kullanıcı girdisine girilen sayı 1 ise if bloğunun içine girecek.
            arama = input("Ne aramak istiyorsunuz: ")                 # Bir input kullanıcı girdisi açtık. arama değişkenine atadık.
            key = True                                                # key diye bir değişken atadım ve bunu boolean bir ifadeye eşitledim. Bunu yapmamın sebebi menu fonksiyonunu kurduğumda şartlara göre
                                                                      # döngüden çıkmayı ya da döngüye devam etmeyi sağlamak. True ise döngü devam edecek. False ise döngü duracak.
            while key:                                                # while döngüsünü başlattık.
                if arama in envanter_arama:                           # Eğer arama, envanter_arama'nın içindeyse if bloğunun içine girecek.
                    envanter_oge = envanter_arama.split(',')          # envanter_arama stringinin arasına virgül koyarak envanter_oge'nin içine atadık.
                    bulunan_ogeler = []                               # bulunan_ogeler adlı boş bir liste oluşturduk.
                    sayi = 0                                          # sayi değişkenini sıfıra atadık.
                    for i in range(len(envanter_oge)):                # envanter_oge'nin uzunluğu kadar for döngüsünde döndüreceğiz. Bu for döngüsü
                        if arama in envanter_oge[i] and Envanter.get(envanter_oge[i])[0] > 0:                      # Bir örnekle açıklayalım "i" değişkeni kuşkonmaz olsun, envanter_oge[i] dediğimiz zaman envanter_oge içerisinden kuşkonmazı çağırmış oluruz.
                            bulunan_ogeler.append(envanter_oge[i])                                                 # Arama değişkenimiz Kuşkonmaz ise True değerini döndürür.
                            sayi += 1                                                                              #"Envanter.get(envanter_oge[i])[0]>0" burada ise stok miktarını kontrol ediyoruz. Envanterden envanter_oge[i]'yi
                                                                                                                   # örneğin kuşkonmazı, envanterden çağırıyoruz ve onun [0] indeksini yani stok miktarını 0'dan büyük mü diye kontrol ediyoruz.
                    index = 1                                                                                      # index değişkenini 1'e eşitledim
                    print("\n" + str(sayi), "ürün bulundu !\n")
                    for i in range(len(bulunan_ogeler)):                                                           # bulunan_ogeler'in uzulunluğu kadar for döngüsü döner.
                        if Envanter.get(bulunan_ogeler[i])[0] > 0:                                                 #"Envanter.get(bulunan_ogeler[i])[0]>0" burada arattığımız ürün sıfırdan büyükse if bloğunun içine giriyor.
                            print(str(index) + "-)", bulunan_ogeler[i], Envanter.get(bulunan_ogeler[i])[1], "$")
                            index += 1
                    print("Sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin): ")
                    urun_secim = int(input())                                                                      # urun_secim adında integer bir input kullanıcı girdisi açtım.
                    while True:                                                                                    # while döngüsü başlattık.
                        if 0 < urun_secim <= len(bulunan_ogeler):                                                  # Eğer urun_secım 0 dan büyük, bulunan_ogeler'in uzunluğundan küçükse if bloğunun içine girer.
                            break                                                                                  # break komutuyla while döngüsünden çıkardık.
                        elif urun_secim > len(bulunan_ogeler):                                                     # Eğer urun_secim bulunan_ogeler'in uzunluğundan büyükse elif bloğunun içine girer.
                            print("Hatalı tuşlama yaptınız. Ana menüye yönlendiriliyorsunuz!")
                            return menu()                                                                          # menu fonksiyonun döndürmesini istedim.
                        elif urun_secim == 0:                                                                      # Eğer urun_secim 0 a eşitse,menu fonksiyonunu döndürür.
                            return menu()

                    print(bulunan_ogeler[urun_secim - 1], "ekleniyor")
                    while True:
                        print("Kaç tane istiyorsunuz?")
                        miktar = int(input())                                                                      # miktar adlı integer bir input kullanıcı girdisi açtım.
                        if Envanter.get(bulunan_ogeler[urun_secim - 1])[0] >= miktar:                              # Eğer girdiğimiz miktar seçtiğimiz ürünün stoğuna eşit veya stoğundan küçükse girilen değer kadar sepete seçilen ürünü ekler.
                            sepet.get(kullanici)[bulunan_ogeler[urun_secim - 1]] = miktar
                            print("Sepetinize", miktar, "adet", bulunan_ogeler[urun_secim - 1], "eklendi.")
                            print("Ana menüye dönülüyor...")
                            key = False
                            break
                        else:                                                                                      # Eğer girdiğimiz miktar seçtiğimiz ürünün stoğundan büyükse while döngüsü key = False ile devam eder.
                            key = False
                            print("Ürünün stok miktarından fazla giremezsiniz !")
                else:                                                                                              # Eğer arama, envanter_arama'nın içinde değilse else bloğunun içine girecek.
                    eslesmedi = input("Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin):")
                    if eslesmedi == '0':                                                                           # Kullanıcı 0'ı tuşlarsa if bloğunun içine girer.
                        return menu()                                                                              # menu fonksiyonunu döndürür.
                    else:                                                                                          # Kullanıcı 0'ı tuşlamazsa da farklı bir ürün arayabilmesi için menuye yönlendirilecektir.
                        return menu()

        if secim == "2":                                                                                           # input kullanıcı girdisine girilen sayı 2 ise if bloğunun içine girecek.
            sepete_git()                                                                                           # sepete_git fonksiyonunu çağırdık.
        if secim == "3":                                                                                           # input kullanıcı girdisine girilen sayı 3 ise if bloğunun içine girecek.
            satin_al()                                                                                             # satin_al fonksiyonunu çağırdık.
        if secim == "4":                                                                                           # input kullanıcı girdisine girilen sayı 4 ise if bloğunun içine girecek.
            print("Oturum kapanıyor...")
            return kullanici_giris()                                                                               # kullanici_giris fonksiyonunu geri dönüş değeri olarak döndürür.
        if secim == "5":                                                                                           # input kullanıcı girdisine girilen sayı 5 ise if bloğunun içine girecek.
            print("Çıkış yapıyorsunuz...")
            while True:

                tekrar_girme_istegi = input("Çıkmak istediğinize emin misiniz? : ").lower()                        # tekrar_girme_istegi adında input kullanıcı girdisi alan bir değişken atadık.  .lower(inputa girilenlerin hepsini küçük harfe dönüştürür.)
                if tekrar_girme_istegi == "hayır":                                                                 # tekrar_girme_istegi hayır ise if bloğuna girer.
                    return menu()                                                                                  # menu fonksiyonunu döndürür.
                elif tekrar_girme_istegi == "evet":                                                                # tekrar_girme_istegi evet ise elif bloğuna girer.
                    print("Çıkış yapıyorsunuz...")
                    break                                                                                          # break komutu ile while döngüsünden çıkar.
                else:                                                                                              # evet, hayır dışında bir şey girilirse altındaki print komutunu yazdırır.
                    print("Lütfen evet ya da hayır giriniz!")

        else:
            print("Lütfen 1 ile 5 arasında bir numara tuşlayınız!")                                                # secim inputuna 1-2-3-4-5 dışında bir değer girilirse else bloğuna girer ve altındaki printi yazdırır.


def satin_al():                                                                                                    # satin_al adında bir fonksiyon tasarladık.
    print("Makbuzunuz işleniyor ...\n**** Istine Online Market ****\n" + "*" * 40)
    print("\t\t 0850 283 6000\n \t\t istinye.edu.tr")
    toplam = 0.0                                                                                                   # toplam değişkenini 0.0 (float) atadık.
    for i in sepet.get(kullanici).keys():                                                                          #
        fiyat = float(Envanter.get(i)[1])
        miktar = int(sepet.get(kullanici).get(i))
        toplam = toplam + miktar * fiyat
        Envanter.get(i)[0] -= sepet.get(kullanici).get(i)
        print(i + " : " + str(fiyat) + "$ \tMiktar : " + str(miktar) + " \tToplam : " + str(miktar * fiyat) + " $")
    print("-" * 30 + "\nToplam : " + str(toplam) + "$\n" + "-" * 30)
    print(datetime.datetime.now())
    print("-" * 30)
    print("***** Online Marketimizi kullandığınız için teşekkür ederiz! *****")
    menu()                                                                                                         # menu fonksiyonunu çağırdık.


def sepete_git():                                                                                                  # sepete_git adında bir fonksiyon tasarladık.
    if len(sepet.get(kullanici)) == 0:                                                                             # sepet'in uzunluğu sıfıra eşitse altındaki printi yazdırır.
        print("Sepetiniz boş!")
    else:                                                                                                          # sepet boş değilse else bloğuna girer
        print("Sepetiniz şunları içeriyor : ")
        anahtar = list(sepet.get(kullanici).keys())                                                                ############################
        for i in range(len(anahtar)):                                                                              # anahtarın uzunluğu kadar for döngüsünü döndürürüz.
            fiyat = float(Envanter.get(anahtar[i])[1])
            miktar = int(sepet.get(kullanici).get(anahtar[i]))
            print(str(i + 1) + ". " + anahtar[i] + '\t|'" \tFiyat : " + str(fiyat) + "$ \t| \tMiktar : " + str(
                miktar) + '\t|' " \tToplam : " + str(miktar * fiyat) + " $")
        while True:                                                                                                # while döngüsünü başlattık.(break komutu ile döngüden çıkarız.)
            print("\n")
            print("1. Miktarı Güncelle")
            print("2. Ürün Sil")                                                                                   # sepet menüsünü printerle oluşturduk.
            print("3. Satın Al")
            print("4. Ana Menüye Dön")
            secim = int(input("Seçiminiz : "))                                                                     # integer(tam sayı) input(kullanıcı girdisi) ile değer girmesini istedik. secim değişkenine atadık.
            if secim > 4 or secim < 1:                                                                             # girilen secim 4 ten büyük birden küçükse if bloğuna girer ve altındaki printi yazdırır.
                print("Hatalı seçim!")
            else:                                                                                                  # girilen değer 1 ve 4 arasında ise else bloğunun içine girer.
                if secim == 1:                                                                                     # input kullanıcı girdisine girilen sayı 1 ise if bloğunun içine girecek.
                    while True:
                        secim1 = int(input("Güncellemek istediğiniz ürünü seçiniz : "))                            # while döngüsü içinde secim1 adında input kullanıcı girdisi oluşturdum. (integer)
                        if 1 > secim1 > len(anahtar):                                                              # secim 1 den küçük, anahtar'ın uzunluğundan büyükse if bloğunun içine girer.
                            print("Hatalı seçim!")
                        else:                                                                                      # secim 1 den küçük, anahtar'ın uzunluğundan büyük değil ise else bloğunun içine girer.
                            while True:                                                                            #
                                miktar1 = int(input("Yeni miktarı giriniz : "))                                    # miktar1 adında bir kullanıcı girdisi açtık.
                                if Envanter.get(anahtar[secim1 - 1])[0] < miktar1:                                 # miktar1 stoktan (Envanter.get(anahtar[secim1 - 1])[0]) fazla ise if bloğunun içine girer.
                                    print("Üzgünüm... Miktar yeterli değil!")
                                else:                                                                              # miktar1 stoktan fazla değil ise else bloğunun içine girer.
                                    sepet.get(kullanici)[anahtar[secim1 - 1]] = miktar1                            # tutarı güncelledik.
                                    print("<<<--- Ürün başarıyla güncellendi! --->>>")
                                    break                                                                          # Döngüden çıkarız(break)
                            break
                elif secim == 2:                                                                                   # input kullanıcı girdisine girilen sayı 2 ise elif bloğunun içine girecek.
                    while True:
                        select = int(input("Lütfen silmek istediğiniz ürünü seçiniz :  "))                         # select adında integer input kullanıcı girdisi oluşturduk.
                        if 0 < select < len(anahtar) + 1:                                                          # select 0 dan büyük, anahtarın uzunluğunun bir fazlasından küçük ise if bloğunun içine girer.
                            sepet.get(kullanici).pop(anahtar[select - 1])                                          # pop komutu ile sepette seçilen ürünü sileriz.
                            break                                                                                  # while döngüsünden break komutu ile çıkarız.
                        else:                                                                                      # select 0 dan büyük, anahtarın uzunluğunun bir fazlasından küçük değil ise else bloğunun içine girer.
                            print("Hata! \nLütfen tekrar deneyin!")
                    print("Ürün başarıyla silindi!!")
                elif secim == 3:                                                                                   # input kullanıcı girdisine girilen sayı 3 ise elif bloğunun içine girecek.
                    print("\n")
                    satin_al()                                                                                     # satin_al fonksiyonunu çağırdık.
                    break
                elif secim == 4:                                                                                   # input kullanıcı girdisine girilen sayı 4 ise elif bloğunun içine girecek.
                    break
                sepete_git ()                                                                                      # sepete_git fonksiyonunu çağırdık.
                break


def kullanici_giris():                                                                                             # kullanici_giris adlı bir fonksiyon tasarladık.
    global kullanici
    success = False
    while not success:
        kullanici_adi = input("Kullanıcı Adı : ").capitalize()                                                     # .capitalize inputa girilenin ilk harfi büyük sonraki harfleri küçük yapar.
        parola = input("Parola : ")
        if kullanici_adi in kullanici_bilgileri and kullanici_bilgileri.get(kullanici_adi) == parola:              # kullanici_adi'na girilen input kullanici_bilgileri sözlüğünün içindeyse ve kullanici_bilgileri için kullanici_adi'ndaki anahtar
                                                                                                                   # bilgileri parolaya eşitse if bloğunun içine girer.
            success = True
            kullanici = kullanici_adi
        else:                                                                                                      # if bloğunun şartlarını sağlamıyorsa else bloğunun altındaki print'i yazdırır.

            print("Kullanıcı adı ve/veya parola hatalı!! \nLütfen yeniden deneyin...")
    print("<<<--- Başarıyla giriş yapıldı --->>>")
    print("Hoşgeldiniz {}! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.".format(kullanici_adi))
    print("\n")
    menu()                                                                                                         # menu fonksiyonunu döndürdüm.


kullanici_giris()                                                                                                  #kullanici_giris adlı fonksiyonu çağırdım.

#KAYNAKÇA
"""https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3"""
"""https://docs.python.org/3/library/datetime.html"""
"""https://stackoverflow.com/questions/5244810/python-appending-a-dictionary-to-a-list-i-see-a-pointer-like-behavior"""
"""https://www.sadikturan.com/python-objeleri-ve-veri-yapilari/python-liste-metotlari/1376"""
"""https://www.programiz.com/python-programming/dictionary"""
"""https://realpython.com/python-dicts/#dgetkey-default"""
"""https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3"""
"""https://www.kite.com/python/answers/how-to-check-if-a-dictionary-is-empty-in-python#:~:text=Use%20bool()%20to%20check,one%20entry%20evaluate%20to%20True%20."""
"""Youtube"""