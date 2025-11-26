import os
import time as t
import os as o
from datetime import datetime as dtm

unsafeCommands = ["sudo rm -rf /", "rm -rf / home/user", "rm -rf $PWD", "dd if=/dev/zero of=dev/sda", ":(){ :|:& };:", "mv ~/* /dev/null", "mv ~/* /dev/null", "chmod -R 777 /", "chmod -R 000 /", "chown -R nobody:nogroup /", "mkfs.ext4 /dev/sda", "> /etc/passwd", "> /etc/shadow", "kill -9 1", "kill -9 -1"]
commandsCanBeUnsafe = ["rm", "dd", "mkfs", "fdisk", "parted", "chmod", "chown", ":(){", "fork", "wget", "curl", "nc", "netcat", "shred", "kill", "reboot", "shutdown", "poweroff", "init", "sysrq", "> /", ">/", "/dev/null", "/dev/zero", "/dev/sda"
]

print("Merhaba, ben Alex. Sizin sanal asistanınızım. Komutları öğrenmek için bilgi yazınız.")
while True:
    end = "İşlem sona erdi"

    prompt = input("")

    if prompt == "versiyon":
        print("Ben Alex 1.2")
        print("Yeni özellik : Güvenli olmayan komutları engelleme")
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

            if shell in unsafeCommands:
                #İşleme devam ettiği için direkt break attım.
                print("Bu komut tehlikeli olduğu olduğu için çalıştıramam.")
                print("0x415 : UNSAFE_COMMAND (Tehlikeli komut)")
                break

            elif shell in commandsCanBeUnsafe:
                print("UYARI : Lütfen bu komudu kullanırken dikkatli olun, dikkatsiz bir şekilde kullanmak sisteminize zarar verebilir.")
                areYouSure = input("Emin misiniz E/H : ").upper()
                if areYouSure == "E":
                    print("İşleme kullanıcı isteği üzerine devam ediliyor.")

                elif areYouSure == "H":
                    #İşleme devam ettiği için direkt break attım.
                    print("İşlem iptal ediliyor.")

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
