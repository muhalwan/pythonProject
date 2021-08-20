# Variable
character_name = "John"
character_age = "35"
print("suatu hari ada orang bernama " + character_name + ",")
print("ia berusia " + character_age + " tahun")
character_name = "mark"
character_age = "25"
print("suatu hari ada orang bernama " + character_name + ",")
print("ia berusia " + character_age + " tahun")

# String
makan = "Ayam Goreng"
kenyang = makan.upper()
print(kenyang)
print(makan.upper().isupper())
print(makan.lower() + " itu lemak")
print("ayam\ngoreng")
print("ayam\"goreng")
print("""ayam
goreng""")
print(len(makan))
print(makan[3])
print(makan.index("r"))
print(makan.replace("Ayam", "Bebek") + " dak lemak")

# Numbers
# from math import * (harus dipocok skali )
num = -5
print(num + 2)
print(str(abs(num)) + " yes")  # abs = ubah jadi plus
print(pow(3, 6))  # pow = pangkat
