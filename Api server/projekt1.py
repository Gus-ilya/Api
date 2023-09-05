
menu = []
client = []
sklad = []
class Product:

  def __init__(self, name, price):
      self.name = name
      self.price = price

  def add_product(self):
      name = input("Введите название товара, который хотите добавить:")
      price = float(input("Введите цену товара:"))
      new_product = Product(name, price)
      menu.append(new_product)
      return menu

  def delete_product(self):
      delete = input("Введите название позиции, которую хотите удалить:")
      for product in menu:
          if product.name == delete:
              menu.remove(product)
      return menu

class Sklad:
    def __init__(self, name, nums):
        self.name = name
        self.nums = nums

    def add_sklad(self):
        name = input("Введите название товара, который хотите добавить:")
        nums = int(input("Введите кол-во товара:"))
        new_product = Sklad(name, nums)
        sklad.append(new_product)
        return sklad

    def delete_product(self):
        delete = input("Введите название позиции, которую хотите удалить:")
        for product in sklad:
            if product.name == delete:
                sklad.remove(product)
        return sklad


class Clients:
    def __init__(self, name, number, point):
        self.name = name
        self.number = number
        self.point = point

    def add_client(self):
        name = input("Введите имя нового клиента:")
        number = int(input("Введите номер телефона:"))
        point = 0
        new_client = Clients(name, number, point)
        client.append(new_client)
        return client

    def delete_client(self):
        delete = input("Введите телефон клиента, который хотите удалить:")
        for numb in client:
            if numb.numbers == delete:
                client.remove(numb)
        return client

    def found_add_subtract(self):
        found = int(input("Введите номер телефона клиента:"))
        for numb in client:
            if numb.numbers == found:
                info = (f"{numb.name}, {numb.numbers}, {numb.points}")
                print(info)
                add = input("Введите + для начисления бонусов и - для списания")
                if add == "+":
                    numb.points = numb.points + (int(input("Введите сумму покупки:"))* 0.04)
                    return
                elif add == "-":
                    numb.points = numb.points - (int(input("Введите сумму для списания :")))
                    return




class Sale:
    def __init__(self, name , price):
        self.name = name
        self.price = price

    def new_sale(self):
        while True:
            choise = input("Введите название товара:")
            num = int(input("Введите кол-во:"))
            orders = []
            for prod in menu:
                if prod.name == choise:
                    sale = prod.price * num
                    orders.append(f"{choise} {num}, {sale}")
                    add = input("Введите + для выбоа добавки и - для отказа:")
                    dop = input("Выберете добавку:")
                    num_dop = int(input("Кол-во порций добавки:"))
                    if add == "+":
                        for i in menu:
                            if i.name == dop:
                                total_dop = i.price + num_dop
                                total = sale + total_dop
                                orders.append(f"{choise} {num}, {sale}\n"
                                              f"{dop}, {num_dop}, {total_dop}\n"
                                              f"{total} руб.")
                                next = (input("Введите + если хотите добавить , что то в заказ и - для завершения:"))
                                if next != "+":
                                    break


f
















