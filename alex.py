import os
import time as t
import os as o
from datetime import datetime as dtm

print("Merhaba, ben Alex. Sizin sanal asistanınızım. Komutları öğrenmek için bilgi yazınız.")
while True:
    end = "İşlem sona erdi"

    prompt = input("")

    if prompt == "versiyon":
        print("Ben Alex 1.1")
        print("Yeni özellik : Uygulama yükleme")
        print(end)

    elif prompt == "aç":
        print("Açmak istediğiniz uygulamanın adını yazın")
        app = input("")
        o.system(app)
        print(end)

    elif prompt == "shell":
        howManyTimes = int(input("Kaç kez komut çalıştıracaksınız : "))
        for i in range (howManyTimes):
            directory = o.path.dirname(o.path.abspath(__file__))
            shell = input(f"bash {directory} > ")

            if shell == "sudo rm -rf /":
                print("Bu komut tehlikeli olduğu için çalıştıramam.")
                print("İşlem başarısız : 0x415 : UNSAFE_COMMAND (Güvenli olmayan komut)")

            o.system(f'bash -c "{shell}"')
        print(end)

    elif prompt == "bilgi":
        print("Versiyon isteme : versiyon")
        print("Uygulama açma : İlk olarak aç yazın. Bu sizi uygulama açıcıya götürecek. Sonra istediğiniz uygulamanın paket adını yazın (Konsolu açınca olduğunuz dizine gönderecek.)")
        print("Shell komutu yazdırma : İlk olarak shell yazın. Bu sizi shell komutu yazdırıcıya götürecek. Sonra istediğiniz shell komutunu yazın.")
        print("Asistandan çıkma : çık")
        print("Hava durumunu öğrenmek için : hava durumu yazın.")
        print("Saati öğrenmek için : saat yazın.")
        print("Uygulama yükleme : uygulama yazın, ardından paket yöneticinizi yazın daha sonra paket adını girin.")
        print("Bilgilendirme sona erdi.")

    elif prompt == "hava durumu":
        t.sleep(1)
        print("Sunucuya bağlanıyorum...")
        t.sleep(1)
        print("Maalesef hava durumuna erişemedim. Dışarıya bakabilirsiniz :D")

    elif prompt == "saat":
        zaman = dtm.now()
        saat = zaman.strftime("%H:%M")
        tarih = zaman.strftime("%d.%m.%Y")
        print(f"Bugün {tarih}, saat şu an {saat}.")
        print(end)

    elif prompt == "çık":
        print("Asistandan çıkıyor...")
        print(end)
        break

    elif prompt == "uygulama":
        print("Paket yöneticiniz nedir ? (yum, apt, pacman, dnf, flatpak, zypper, snap)")
        packageInstaller = input("").lower()

        if packageInstaller == "yum":
            print("Paket adını giriniz")
            packageName = input("")
            packageToInstall = f"sudo yum install {packageName}"
            os.system(packageToInstall)
            print(end)

        elif packageInstaller == "apt":
            print("Paket adını giriniz")
            packageName = input("")
            packageToInstall = f"sudo apt install {packageName}"
            os.system(packageToInstall)
            print(end)

        elif packageInstaller == "pacman":
            print("Paket adını giriniz")
            packageName = input("")
            packageToInstall = f"sudo pacman -S {packageName}"
            os.system(packageToInstall)
            print(end)

        elif packageInstaller == "dnf":
            print("Paket adını giriniz")
            packageName = input("")
            packageToInstall = f"sudo dnf install {packageName}"
            os.system(packageToInstall)
            print(end)

        elif packageInstaller == "snap":
            print("Paket adını giriniz")
            packageName = input("")
            packageToInstall = f"sudo snap install {packageName}"
            os.system(packageToInstall)
            print(end)

        elif packageInstaller == "zypper":
            print("Paket adını giriniz")
            packageName = input("")
            packageToInstall = f"sudo zypper install {packageName}"
            os.system(packageToInstall)
            print(end)

        elif packageInstaller == "flatpak":
            print("Paket adını giriniz (com.example.example)")
            packageName = input("")
            packageToInstall = f"flatpak install {packageName}"
            os.system(packageToInstall)
            print(end)

        else:
            print("İşlem başrısız : 0x438 : UNDEFINED_PACKAGE_INSTALLER (Tanımlanmamış paket yöneticisi)")

    else:
        print("İşlem başarısız : 0x654 : UNDEFINED_PROMPT (Tanımlanmamış istek)")