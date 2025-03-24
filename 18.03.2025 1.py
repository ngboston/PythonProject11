# Завдання 1
# Реалізуйте патерн Command. Протестуйте роботу створеного класу.

print("\nTask 1")

from abc import ABC, abstractmethod
import unittest

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def turn_on(self):
        return "Light is on"

    def turn_off(self):
        return "Light is off"

class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_on()

class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        if slot in self.commands:
            return self.commands[slot].execute()
        return "No command assigned to this slot"

class TestCommandPattern(unittest.TestCase):
    def setUp(self):
        self.light = Light()
        self.remote = RemoteControl()
        self.on_command = TurnOnLightCommand(self.light)
        self.off_command = TurnOffLightCommand(self.light)

    def test_turn_on_light(self):
        self.remote.set_command(1, self.on_command)
        self.assertEqual(self.remote.press_button(1), "Light is on")

    def test_turn_off_light(self):
        self.remote.set_command(2, self.off_command)
        self.assertEqual(self.remote.press_button(2), "Light is off")

    def test_no_command_assigned(self):
        self.assertEqual(self.remote.press_button(3), "No command assigned to this slot")

if __name__ == '__main__':
    unittest.main()

# Завдання 2
# Маємо клас, який надає доступ до набору чисел.Джерелом цього набору чисел є певний файл.З певною періодичністю
# дані у файлі мінюються (реалізуйте механізм оновлення).Додаток має отримувати доступ до цих даних та виконувати
# набір операцій над ними(сума, максимум, мінімум тощо).При кожній спробі доступу до цього набору вносіть
# запису лог - файл.При реалізації використовуйте патерн Proxy(для логування) та інші необхідні патерни.

print("\nTask 2")

import time
import threading
import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataProvider:
    """Клас, який надає доступ до даних з файлу."""

    def __init__(self, filename):
        self.filename = filename
        self.data = self._load_data()
        self._start_update_thread()

    def _load_data(self):
        """Завантажує дані з файлу."""
        try:
            with open(self.filename, 'r') as file:
                return [int(line.strip()) for line in file]
        except FileNotFoundError:
            return []

    def _update_data(self):
        """Періодично оновлює дані з файлу."""
        while True:
            time.sleep(10)  # Оновлюємо дані кожні 10 секунд
            self.data = self._load_data()
            logging.info("Дані оновлено.")

    def _start_update_thread(self):
        """Запускає потік для оновлення даних."""
        update_thread = threading.Thread(target=self._update_data)
        update_thread.daemon = True
        update_thread.start()

    def get_data(self):
        """Повертає поточні дані."""
        return self.data

class DataProviderProxy:
    """Проксі-клас для логування доступу до даних."""

    def __init__(self, data_provider):
        self.data_provider = data_provider

    def get_data(self):
        """Логує доступ до даних та повертає їх."""
        logging.info("Доступ до даних.")
        return self.data_provider.get_data()

class DataProcessor:
    """Клас для обробки даних."""

    def __init__(self, data_provider):
        self.data_provider = data_provider

    def calculate_sum(self):
        """Обчислює суму чисел."""
        data = self.data_provider.get_data()
        return sum(data)

    def find_max(self):
        """Знаходить максимальне число."""
        data = self.data_provider.get_data()
        return max(data) if data else None

    def find_min(self):
        """Знаходить мінімальне число."""
        data = self.data_provider.get_data()
        return min(data) if data else None

data_provider = DataProvider("data.txt")
data_provider_proxy = DataProviderProxy(data_provider)
data_processor = DataProcessor(data_provider_proxy)

print("Сума:", data_processor.calculate_sum())
print("Максимум:", data_processor.find_max())
print("Мінімум:", data_processor.find_min())

# Завдання 3
# Створіть додаток для бібліотекарів. Додаток має оперувати такими сутностями: Книга, Бібліотекар, Читач.
# Додаток має дозволяти вводити, видаляти, змінювати, зберігати у файл, завантажувати з файлу, логувати дії,
# шукати інформацію про сутності (результати пошуку виводяться на екран або у файл).  При реалізації використовуйте
# максимально можливу кількість патернів проєктування.

print("\nTask 3")

import json
import logging

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def __str__(self):
        return f"Назва: {self.title}, Автор: {self.author}, ISBN: {self.isbn}, Рік: {self.publication_year}"

class Librarian:
    def __init__(self, name, librarian_id):
        self.name = name
        self.librarian_id = librarian_id

    def __str__(self):
        return f"Ім'я: {self.name}, ID: {self.librarian_id}"

class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id

    def __str__(self):
        return f"Ім'я: {self.name}, ID: {self.reader_id}"

class EntityFactory:
    @staticmethod
    def create_entity(entity_type, **kwargs):
        if entity_type == 'book':
            return Book(**kwargs)
        elif entity_type == 'librarian':
            return Librarian(**kwargs)
        elif entity_type == 'reader':
            return Reader(**kwargs)
        else:
            raise ValueError("Невідомий тип сутності")

class SearchStrategy:
    def search(self, data, query):
        pass

class BookSearchStrategy(SearchStrategy):
    def search(self, books, query):
        results = []
        for book in books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        return results

class LibrarianSearchStrategy(SearchStrategy):
    def search(self, librarians, query):
        results = []
        for librarian in librarians:
            if query.lower() in librarian.name.lower():
                results.append(librarian)
        return results

class ReaderSearchStrategy(SearchStrategy):
    def search(self, readers, query):
        results = []
        for reader in readers:
            if query.lower() in reader.name.lower():
                results.append(reader)
        return results

class Logger:
    def log(self, message):
        logging.info(message)

class LibraryRepository:
    def __init__(self, filename):
        self.filename = filename
        self.data = {'books': [], 'librarians': [], 'readers': []}
        self.load_data()

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, default=lambda o: o.__dict__, indent=4)

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass

    def add_book(self, book):
        self.data['books'].append(book)
        self.save_data()

    def add_librarian(self, librarian):
        self.data['librarians'].append(librarian)
        self.save_data()

    def add_reader(self, reader):
        self.data['readers'].append(reader)
        self.save_data()

    def get_books(self):
        return [EntityFactory.create_entity('book', **book_data) for book_data in self.data['books']]

    def get_librarians(self):
        return [EntityFactory.create_entity('librarian', **librarian_data) for librarian_data in self.data['librarians']]

    def get_readers(self):
        return [EntityFactory.create_entity('reader', **reader_data) for reader_data in self.data['readers']]


class LibraryApp:
    def __init__(self, repository, logger):
        self.repository = repository
        self.logger = logger
        self.search_strategies = {
            'book': BookSearchStrategy(),
            'librarian': LibrarianSearchStrategy(),
            'reader': ReaderSearchStrategy()
        }

    def add_book(self, title, author, isbn, publication_year):
        book = EntityFactory.create_entity('book', title=title, author=author, isbn=isbn, publication_year=publication_year)
        self.repository.add_book(book)
        self.logger.log(f"Додано книгу: {book}")

    def add_librarian(self, name, librarian_id):
        librarian = EntityFactory.create_entity('librarian', name=name, librarian_id=librarian_id)
        self.repository.add_librarian(librarian)
        self.logger.log(f"Додано бібліотекаря: {librarian}")

    def add_reader(self, name, reader_id):
        reader = EntityFactory.create_entity('reader', name=name, reader_id=reader_id)
        self.repository.add_reader(reader)
        self.logger.log(f"Додано читача: {reader}")

    def search(self, entity_type, query):
        data = getattr(self.repository, f'get_{entity_type}s')()
        results = self.search_strategies[entity_type].search(data, query)
        for result in results:
            print(result)

repository = LibraryRepository('library_data.json')
logger = Logger()
app = LibraryApp(repository, logger)

app.add_book(title='Майстер і Маргарита', author='Михайло Булгаков', isbn='978-5-9268-1253-5', publication_year=1967)
app.add_librarian(name='Іван Петренко', librarian_id='L001')
app.add_reader(name='Олена Сидоренко', reader_id='R001')

app.search(entity_type='book', query='Майстер')
app.search(entity_type='librarian', query='Іван')
app.search(entity_type='reader', query='Олена')