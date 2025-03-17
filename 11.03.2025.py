#   Завдання 3
# Створіть додаток для бібліотекарів. Додаток має оперувати такими сутностями:
# Книга, Бібліотекар, Читач. Додаток має дозволяти вводити, видаляти, змінювати,
# зберігати у файл, завантажувати з файлу, логувати дії, шукати інформацію про сутності
# (результати пошуку виводяться на екран або у файл).  При реалізації використовуйте
# максимально можливу кількість патернів проєктування.

print("\nTask 1")


import json
import logging
from abc import ABC, abstractmethod

class EntityFactory(ABC):
    @abstractmethod
    def create_entity(self, data):
        pass

class BookFactory(EntityFactory):
    def create_entity(self, data):
        return Book(**data)

class LibrarianFactory(EntityFactory):
    def create_entity(self, data):
        return Librarian(**data)

class ReaderFactory(EntityFactory):
    def create_entity(self, data):
        return Reader(**data)

class EntityPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Book(EntityPrototype):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def clone(self):
        return Book(self.title, self.author, self.isbn)

    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}, ISBN: {self.isbn}"

class Librarian(EntityPrototype):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def clone(self):
        return Librarian(self.name, self.employee_id)

    def __str__(self):
        return f"Бібліотекар: {self.name}, ID: {self.employee_id}"

class Reader(EntityPrototype):
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id

    def clone(self):
        return Reader(self.name, self.reader_id)

    def __str__(self):
        return f"Читач: {self.name}, ID: {self.reader_id}"

class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
            cls._instance.librarians = []
            cls._instance.readers = []
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.INFO)
            handler = logging.FileHandler('library.log')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls._instance.logger.addHandler(handler)
        return cls._instance

    def add_book(self, book):
        self.books.append(book)
        self.logger.info(f"Додано книгу: {book}")

    def add_librarian(self, librarian):
        self.librarians.append(librarian)
        self.logger.info(f"Додано бібліотекаря: {librarian}")

    def add_reader(self, reader):
        self.readers.append(reader)
        self.logger.info(f"Додано читача: {reader}")

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.logger.info(f"Видалено книгу з ISBN: {isbn}")

    def remove_librarian(self, employee_id):
        self.librarians = [librarian for librarian in self.librarians if librarian.employee_id != employee_id]
        self.logger.info(f"Видалено бібліотекаря з ID: {employee_id}")

    def remove_reader(self, reader_id):
        self.readers = [reader for reader in self.readers if reader.reader_id != reader_id]
        self.logger.info(f"Видалено читача з ID: {reader_id}")

    def find_books(self, query):
        results = [book for book in self.books if query.lower() in str(book).lower()]
        return results

    def find_librarians(self, query):
        results = [librarian for librarian in self.librarians if query.lower() in str(librarian).lower()]
        return results

    def find_readers(self, query):
        results = [reader for reader in self.readers if query.lower() in str(reader).lower()]
        return results

    def save_to_file(self, filename):
        data = {
            "books": [{"title": book.title, "author": book.author, "isbn": book.isbn} for book in self.books],
            "librarians": [{"name": librarian.name, "employee_id": librarian.employee_id} for librarian in self.librarians],
            "readers": [{"name": reader.name, "reader_id": reader.reader_id} for reader in self.readers]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        self.logger.info(f"Дані збережено у файл: {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            book_factory = BookFactory()
            librarian_factory = LibrarianFactory()
            reader_factory = ReaderFactory()
            self.books = [book_factory.create_entity(book_data) for book_data in data.get("books", [])]
            self.librarians = [librarian_factory.create_entity(librarian_data) for librarian_data in data.get("librarians", [])]
            self.readers = [reader_factory.create_entity(reader_data) for reader_data in data.get("readers", [])]
            self.logger.info(f"Дані завантажено з файлу: {filename}")
        except FileNotFoundError:
            self.logger.warning(f"Файл не знайдено: {filename}")


if __name__ == "__main__":
    library = Library()

    book1 = Book("Майстер і Маргарита", "Михайло Булгаков", "978-5-389-00955-6")
    book2 = Book("1984", "Джордж Орвелл", "978-0-14-103614-4")
    librarian1 = Librarian("Іван Петров", "123")
    reader1 = Reader("Олена Сидорова", "456")

    library.add_book(book1)
    library.add_book(book2)
    library.add_librarian(librarian1)
    library.add_reader(reader1)

    print(library.find_books("Майстер"))
    print(library.find_librarians("Іван"))

    library.save_to_file("library.json")
    library2 = Library()
    library2.load_from_file("library.json")
    print(library2.find_books("1984"))