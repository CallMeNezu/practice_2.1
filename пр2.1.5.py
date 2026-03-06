import json

FILENAME = "library.json"

#сохронить изменения
def save_library(FILENAME, books):
    try:
        with open(FILENAME, "w") as file:
            json.dump(books, file, indent=4)
    except FileNotFoundError:
        print("такого файла нет.")

#прочесть файл(посмотреть все книги)
def read_all_books(FILENAME):
    with open(FILENAME, "r") as f:
        book_read = json.load(f)
    for book in book_read:
        for key, value in book.items():
            print(f"{key}: {value}")
        print(" ")

#найти книгу по названию или автору
def search_book(books):
    name = input("введите название или автора книги: ")
    for i in books:
        for key, value in i.items():
            if name == i["title"] or name == i["author"]:
                print(f"{key}: {value}")

#добавить книгу
def add_book(books):
    while True:
        try:
            id_book = int(input("введите id книги: "))
            break
        except ValueError:
            print("неверно")
    title_book = input("введите название книги: ")
    author_book = input("введите автора книги: ")
    while True:
        try:
            year_book = int(input("введите год выпуска книги: "))
            available_book = bool(int(input("введите 1 - если книга есть или 0 - если книга взята: ")))
            break
        except ValueError:
            print("неверно")
    new_book = {"id": id_book,
            "title": title_book,
            "author": author_book,
            "year": year_book,
            "available": available_book}
    books.append(new_book)

#сменить статус книги(взята/возвращена)
def take_or_give_book(books):
    name1 = input("введите название книги: ")
    for i in books:
        if name1 == i["title"]:
            avail = bool(int(input("введите 1 - если вы хотите вернуть книгу или 0 - если хотите взять книгу: ")))
            i["available"] = avail
            print("значение изменено")

#удалить книгу по id
def delete_book(books):
    delete_id = int(input("введите id книги которую хотите удалить: "))
    for i in books:
        if i["id"] == delete_id:
            books.remove(i)
            print("книга удалена")

#экспорт в txt
def export_library(books):
    txt_name = input("введите новое название экспортируемого файла: ")
    txt_name += ".txt"
    with open(txt_name, "w") as file:
        for book in books:
            for key, value in book.items():
                file.write(f"{key}: {value}\n")
    '''
    with open(txt_name, "r") as file:
        books_txt = file.readlines()
        for i in books_txt:
            print(i)
    '''

books = [{"id" : 1,
         "title" : "Мастер и Маргарита",
         "author" : "Булгаков",
         "year" : 1967,
         "available" : True},
        {"id" : 2,
         "title" : "Преступление и наказание",
         "author" : "Достоевский",
         "year" : 1866,
         "available" : False}]

with open(FILENAME, "w") as f:
    json.dump(books, f, indent=4)

while True:
    print('''введите:
    1 - посмотреть все книги.
    2 - поиск книги.
    3 - добавление новой книги.
    4 - изменить статус доступа.
    5 - удаление книги.
    6 - экспорт в txt.
    0 - выйти.''')
    while True:
        try:
            variant = int(input(":"))
            break
        except ValueError:
            print("неверно.")
    if variant == 1:
        read_all_books(FILENAME, books)
    elif variant == 2:
        search_book(books)
    elif variant == 3:
        add_book(books)
        save_library(FILENAME, books)
    elif variant == 4:
        take_or_give_book(books)
        save_library(FILENAME, books)
    elif variant == 5:
        delete_book(books)
        save_library(FILENAME, books)
    elif variant == 6:
        export_library(books)
    elif variant == 0:
        save_library(FILENAME, books)
        break
    else:
        print("такого действия нет.")





