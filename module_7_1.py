from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name # название продукта (строка).
        self.weidht = weight # общий вес товара (дробное число)
        self.category = category # категория товара (строка)
    def __str__ (self): # возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.
        return f'{self.name}, {self.weidht}, {self.category} \n'
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt2'
    def get_products(self):
        file = open(self.__file_name, 'r')# считывает всю информацию из файла __file_name
        pprint(file.read())
        file.close()#закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        return self.__file_name

    def add(self, *products): # принимает неограниченное количество объектов класса Product.
        for product in products:
            if product.name in products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(product.__str__())
                file.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
"""
Spaghetti, 3.4, Groceries
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato, 50.5, Vegetables уже есть в магазине
Продукт Spaghetti, 3.4, Groceries уже есть в магазине
Продукт Potato, 5.5, Vegetables уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
"""
