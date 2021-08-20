while True:
    barang = {"apel": 2, "pisang": 4, "pepaya": 3}
    uang = 20
    for x in barang:
        print("-----------------")
        print("Anda memiliki uang sebanyak " + str(uang) + " ribu")
        print("Harga " + x + " adalah " + str(barang[x]) + " ribu")
        input_barang = input("Mau beli berapa " + x + "? ")
        print("Anda akan membeli " + input_barang + " " + x)
        print("Seharga " + str(int(input_barang) * barang[x]) + " ribu")
        uang -= int(input_barang) * barang[x]
        if uang < 0:
            print("Uang Anda tidak cukup untuk membeli " + x + " sebanyak itu")
        else:
            print("Uang Anda tersisa " + str(uang) + " ribu")
        if uang <= 0:
            break