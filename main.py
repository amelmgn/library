class Book:
    """Класс для представления книги в библиотеке"""
    def __init__(self, title, author, year=None):
        self.id = None  # ID книги (присваивается библиотекой)
        self.title = title  # Название книги
        self.author = author  # Автор книги
        self.year = year  # Год издания (необязательно)
    
    def __str__(self):
        """Возвращает строковое представление книги"""
        year_str = f" ({self.year})" if self.year else ""
        return f"ID: {self.id}, '{self.title}' - {self.author}{year_str}"


class Library:
    """Класс для управления коллекцией книг"""
    def __init__(self):
        self.books = {}  # Словарь для хранения книг {id: Book}
        self.next_id = 1  # Счетчик для генерации уникальных ID
    
    def add_book(self, title, author, year=None):
        """Добавляет новую книгу в библиотеку"""
        book = Book(title, author, year)
        book.id = self.next_id
        self.books[self.next_id] = book
        self.next_id += 1
        return book.id
    
    def get_all_books(self):
        """Возвращает список всех книг в библиотеке"""
        return list(self.books.values())
    
    def get_book_by_id(self, book_id):
        """Возвращает книгу по ID или None, если не найдена"""
        return self.books.get(book_id)
    
    def delete_book(self, book_id):
        """Удаляет книгу по ID, возвращает удаленную книгу или None"""
        if book_id in self.books:
            deleted_book = self.books.pop(book_id)
            return deleted_book
        return None


def main():
    """Главная функция программы - консольный интерфейс библиотеки"""
    library = Library()  # Создаем экземпляр библиотеки
    
    while True:
        # Выводим главное меню
        print("\n=== Library Management System ===")
        print("1. Add book")
        print("2. Show all books")
        print("3. Find book by ID")
        print("4. Delete book")
        print("5. Exit")
        
        choice = input("\nChoose action (1-5): ")
        
        if choice == "1":
            # Добавление новой книги
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year_input = input("Enter publication year (or press Enter to skip): ")
            year = int(year_input) if year_input.strip() else None
            
            book_id = library.add_book(title, author, year)
            print(f"Book added with ID: {book_id}")
        
        elif choice == "2":
            # Показать все книги
            books = library.get_all_books()
            if books:
                print("\nList of all books:")
                for book in books:
                    print(book)
            else:
                print("Library is empty")
        
        elif choice == "3":
            # Поиск книги по ID
            try:
                book_id = int(input("Enter book ID: "))
                book = library.get_book_by_id(book_id)
                if book:
                    print(f"Found book: {book}")
                else:
                    print("Book with this ID not found")
            except ValueError:
                print("Error: enter valid ID (number)")
        
        elif choice == "4":
            # Удаление книги по ID
            try:
                book_id = int(input("Enter book ID to delete: "))
                deleted_book = library.delete_book(book_id)
                if deleted_book:
                    print(f"Book deleted: {deleted_book}")
                else:
                    print("Book with this ID not found")
            except ValueError:
                print("Error: enter valid ID (number)")
        
        elif choice == "5":
            # Выход из программы
            print("Goodbye!")
            break
        
        else:
            # Обработка неверного выбора
            print("Invalid choice. Please try again.")


# Точка входа в программу
if __name__ == "__main__":
    main()