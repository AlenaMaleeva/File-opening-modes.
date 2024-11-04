from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name # название продукта (строка).
        self.weight = weight # общий вес товара (дробное число)
        self.category = category # категория товара (строка)
    def __str__ (self): # возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.
        return f'{self.name}, {self.weight}, {self.category} \n'
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt4'
    def get_products(self):
        __file_name = open('products.txt', 'r')
        name_product = __file_name.read()
        __file_name.close()

        return name_product
    def add(self, *products):
        for product in products:
            if str(product) not in self.get_products():
                file = open('products.txt4', 'a+')
                file.write(f'{str(product)}\n')
                file.close()
            
            else:
                print(f'Продукт {product} уже есть в магазине')



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
