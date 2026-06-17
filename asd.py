books = [
]

def add_book():
    title = input("Введите название книги: ")
    author = input("Введите имя автора: ")
    book = {
        "title": title,
        "author": author
    }
    books.append(book)


def show_books():
    counter = 1
    for book in books:
        print(f"Книга {counter}:")
        print(f"Название: {book["title"]}")
        print(f"Автор: {book["author"]}\n")
        counter += 1


def save_books():
    file = open("books.txt", "w", encoding="utf-8")
    for book in books:
        file.write(f"{book["title"]};{book["author"]}\n")
    file.close()

def load_books():
    try:
        with open("books.txt", "r", encoding="utf-8") as file:
            for line in file:
                # ["Гарри потер", "Джоана Роулинг"]
                data = line.strip().split(";")
                book = {
                    "title": data[0],
                    "author": data[1]
                }
                books.append(book)
    except:
        print("Ошибка, повторите позже!")



while True:
    print("\n1. Добавить книгу")
    print("2. Показать книги")
    print("3. Сохранить")
    print("4. Выгрузить")
    print("0. Выход")
    
    choice = input("Выбор: ")
    match choice:
        case "1":
            add_book()
            print(books)
        case "2":
            show_books()
        case "3":
            save_books()
        case "4":
            load_books()
        case "0":
            break
        case _:
            print("Повторите попытку!")