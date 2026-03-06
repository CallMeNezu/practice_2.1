import csv
from random import choice

FILENAME = 'products.csv'

products = [{'name' : 'яблоки' , 'price' : 100 , 'quantity' : 50},
            {'name' : 'бананы' , 'price' : 80 , 'quantity' : 30},
            {'name' : 'молоко' , 'price' : 120 , 'quantity' : 20},
            {'name' : 'хлеб' , 'price' : 40 , 'quantity' : 100}]

def read_csvfile(FILENAME):
    try:
        with open(FILENAME, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("файл ненйден")
        return []

def add_product(data):
    name_new_product = input("введите название продукта: ")
    while True:
        try:
            price_new_product = int(input("введите цену продукта: "))
            quantity_new_product = int(input("введите количество продукта: "))
            break
        except ValueError:
            print("неверно")
    new_product = {'name' : name_new_product,
                   'price' : price_new_product,
                   'quantity' : quantity_new_product}
    data.append(new_product)
    print("товар добавлен\n")

def append_product(FILENAME, data):
    fieldnames = ['name', 'price', 'quantity']
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in data:
            writer.writerow(i)

def search_product(data):
    name = input("введи название товара который хотите найти: ").strip().lower()
    found_product = [i for i in data if i['name'].strip().lower() == name]
    if found_product:
        print("товар найден")
    else:
        print("товар ненайден")

def total_cost_all_items(data):
    total = sum(float(product['price']) * product['quantity'] for product in data)
    print("общая стоимость всех товаров: ",total)

with open(FILENAME, 'w', newline='') as file:
    columns = ['name', 'price', 'quantity']
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(products)
with open(FILENAME, 'r', newline = '') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['price'], row['quantity'])

while True:
    print('''введите:
    1 - показать список товаров
    2 - добавить новый товар
    3 - поиск товара по названию 
    4 - расчет общей стоимости всех товаров на складе
    5 - сохранить исменения
    0 - выйти''')
    choice = input(":")
    if choice == '1':
        for i in read_csvfile(FILENAME):
            print(i['name'], i['price'], i['quantity'])
    elif choice == '2':
        add_product(products)
        append_product(FILENAME, products)
    elif choice == '3':
        search_product(products)
    elif choice == '4':
        total_cost_all_items(products)
    elif choice == '5':
        append_product(FILENAME, products)
    elif choice == '0':
        break
    else:
        print("такого действия нет")
