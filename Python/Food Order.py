while True:
    class MenuItem:
        def __init__(self, item, price):
            self.item = item
            self.price = price

        def info(self):
            return "Harga " + self.item + ": Rp" + str(self.price)

        def total_item_price(self, count):
            total_price = self.price * count

            if count >= 10:
                total_price *= 0.9

            return round(total_price)

    menu_item1 = MenuItem("Ayam", 5000)
    menu_item2 = MenuItem("Bebek", 4000)
    menu_item3 = MenuItem("Ikan", 3000)
    menu_item4 = MenuItem("Sapi", 7000)

    menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]
    index = 1
    for menus in menu_items:
        print(str(index) + ". " + menus.info())
        index += 1

    order = int(input("Masukkan nomor menu yang akan dipesan: "))
    selected_menu = menu_items[order - 1]
    print("Anda akan membeli: " + str(selected_menu.item))

    count = int(input("Berapa banyak? (pembelian diatas 9 dapat diskon 10 persen): "))

    result = selected_menu.total_item_price(count)

    print ("Anda akan membeli: " + str(selected_menu) + " seharga Rp" + str(result))






