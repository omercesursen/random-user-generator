import requests

sayi = int(input("Kaç adet kullanıcı oluşturulsun ?: "))
url = f"https://randomuser.me/api/?results={sayi}"

cevap = requests.get(url)
veri = cevap.json()

kullaniciverisi = veri["results"]

with open("kullaniciverisi.txt", "w" , encoding="utf-8" ) as dosya:
    sayac = 1
    for kullanici in kullaniciverisi:
        dosya.write(f"{sayac}. Kullanıcı\n")
        dosya.write(f"Adı: {kullanici['name']['first']}\n")
        dosya.write(f"Soyadı: {kullanici['name']['last']}\n")
        dosya.write(f"Email Adresi: {kullanici['email']}\n")
        dosya.write(f"Telefonu: {kullanici['phone']}\n")
        dosya.write("--------------------------------------\n")

        sayac = sayac + 1


