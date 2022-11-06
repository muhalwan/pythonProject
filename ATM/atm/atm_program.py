import random
import datetime
from customer import Customer

atm = Customer(id)

while True:

    id = int(input("\nMasukkan pin Anda: "))
    trial = 0

    while (id != int(atm.checkPin()) and trial <3):
        id = int(input("Pin yang Anda masukkan salah, silahkan coba lagi: "))

        trial += 1

        if trial == 3:
            print("Anda telah salah memasukkan kata sandi sebanyak tiga kali, silahkan coba lagi.")
            exit()

    while True:
        print("""\nSelamat datang di atm
        \n1. Cek Saldo
        \n2. Debet
        \n3. Simpan
        \n4. Ganti Pin
        \n5. Keluar""")

        pilihmenu = int(input("\nSilakan pilih menu: "))

        if pilihmenu == 1:
            print("\nSaldo anda: Rp" + str(atm.checkBalance()) + "\n")
        elif pilihmenu == 2:
            nominal = float(input("\nMasukkan nominal saldo: "))
            verify_withdraw = input("Anda akan melakukan debet sebanyak: " + str(nominal) + " y/n: ")

            if verify_withdraw == "y" :
                print("Saldo awal Anda adalah: Rp" + str(atm.checkBalance()))
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi berhasil!")
                print("Saldo Anda sekarang adalah Rp" + str(atm.checkBalance()))
            else:
                print("Maaf, saldo Anda tidak cukup untuk melakukan transaksi!")
        elif pilihmenu == 3:
            nominal = float(input("\nMasukkan nominal saldo: "))
            verify_deposit = input("Anda akan menabung sejumlah Rp" + str(nominal) + " y/n: ")

            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print("Saldo Anda sekarang adalah Rp" + str(atm.checkBalance()) + "\n")
            else:
                break
        elif pilihmenu == 4:
            verify_pin = int(input("\nMasukkan pin lama Anda: "))

            while verify_pin != int(atm.checkPin()):
                print("Pin Anda salah, masukkan pin:")

            update_pin = int(input("Silahkan masukkan pin baru: "))
            print("Pin Anda berhasil diganti!")

            verify_newpin = int(input("Ulangi masukkan pin baru: "))

            if verify_newpin == update_pin:
                print("Pin baru Anda sukses!")
            else:
                print("Maaf, pin Anda salah!")
        elif pilihmenu == 5:
            print("""\nResi tercetak otomatis setelah melakukan transaksi. 
Harap simpan bukti transaksi ini. 
Sebagai bukti transaksi yang sah""")
            print("\nNo. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Terima kasih telah menggunakan ATM Alwan")
            exit()
        else:
            print("Error. Maaf, menu tidak tersedia.")