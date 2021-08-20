import random

while True:

    def tangan_player(tangan, nama="random"):
        tangans = ['batu', 'kertas', ' gunting']
        print(nama_player + " memilih " + tangans[tangan])

    def tangan_komputer(komputer, nama="Komputer"):
        tangans = ['batu', 'kertas', ' gunting']
        print(nama + " memilih " + tangans[komputer])

    nama_player = input("Masukkan nama: ")
    tangan = int(input("Plih tangan: "))

    def valid():
        if tangan < 0 or tangan > 2:
            return True
        return False

    if valid():
        print("Masukkan nomor yang sesuai: ")
        break

    komputer = random.randint(0, 2)
    tangan_komputer(komputer)
    tangan_player(tangan, nama_player)

    if tangan == 0 and komputer == 1:
        print("Kalah")
    elif tangan == 0 and komputer == 0:
        print("seri")
    elif tangan == 1 and komputer == 1:
        print("seri")
    elif tangan == 2 and komputer == 2:
        print("seri")
    elif tangan == 1 and komputer == 2:
        print("kalah")
    elif tangan == 2 and komputer == 0:
        print("kalah")
    else:
        print("menang")
