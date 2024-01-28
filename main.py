import json
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTextEdit, QLabel

class BookManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.books = dict()
        try:
            with open("books.json", "r") as f:
                json_books = json.loads(f.read())
                for book in json_books["books"]:
                    self.books[book["ISBN"]] = book
        except FileNotFoundError:
            self.display_area.setText("Failu books.json nevar atrast. Lūdzu, pārliecinieties, ka tas atrodas pareizajā direktorijā.")

    def initUI(self):
        layout = QVBoxLayout()

        # ievades lauki
        self.isbn_input = QLineEdit(self)
        self.isbn_input.setPlaceholderText("Ievadiet ISBN")
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Ievadiet Nosaukumu")
        self.author_input = QLineEdit(self)
        self.author_input.setPlaceholderText("Ievadiet Autoru")

        # pogas
        add_button = QPushButton("Pievienot Grāmatu", self)
        add_button.clicked.connect(self.add_book)
        find_isbn_button = QPushButton("Meklēt pēc ISBN", self)
        find_isbn_button.clicked.connect(self.find_book_by_isbn)
        find_name_button = QPushButton("Meklēt pēc Nosaukuma", self)
        find_name_button.clicked.connect(self.find_books_by_name)
        find_author_button = QPushButton("Meklēt pēc Autora", self)
        find_author_button.clicked.connect(self.find_books_by_author)
        delete_button = QPushButton("Dzēst pēc ISBN", self)
        delete_button.clicked.connect(self.del_book_by_isbn)

        # rezultātu logs
        self.display_area = QTextEdit(self)
        self.display_area.setReadOnly(True)

        # pievienojam laukus un pogas
        layout.addWidget(QLabel("ISBN:"))
        layout.addWidget(self.isbn_input)
        layout.addWidget(QLabel("Nosaukums:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Autors:"))
        layout.addWidget(self.author_input)
        layout.addWidget(add_button)
        layout.addWidget(find_isbn_button)
        layout.addWidget(find_name_button)
        layout.addWidget(find_author_button)
        layout.addWidget(delete_button)
        layout.addWidget(self.display_area)

        # izkārtojums
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Grāmatu Pārvaldnieks")

    def add_book(self):
        book = {
            "ISBN": self.isbn_input.text(),
            "title": self.title_input.text(),
            "author": self.author_input.text()
        }
        try:
            if book["ISBN"] in self.books:
                raise Exception("Grāmata ar šo ISBN jau eksistē")
            self.books[book["ISBN"]] = book
            self.display_area.setText(f"Grāmata pievienota: {book}")
        except Exception as e:
            self.display_area.setText(str(e))

    def find_book_by_isbn(self):
        isbn = self.isbn_input.text()
        try:
            if isbn not in self.books:
                raise Exception("Grāmata ar norādīto ISBN neeksistē")
            book = self.books[isbn]
            self.display_area.setText(f"Grāmata atrasta: {book}")
        except Exception as e:
            self.display_area.setText(str(e))

    def find_books_by_name(self):
        name = self.title_input.text()
        found_books = []
        for book in self.books.values():
            if name in book["title"]:
                found_books.append(book)
        if found_books:
            self.display_area.setText(f"Grāmatas atrastas: {found_books}")
        else:
            self.display_area.setText("Nav atrasta neviena grāmata ar šādu nosaukumu.")

    def find_books_by_author(self):
        author = self.author_input.text()
        found_books = []
        for book in self.books.values():
            if author in book["author"]:
                found_books.append(book)
        if found_books:
            self.display_area.setText(f"Grāmatas atrastas: {found_books}")
        else:
            self.display_area.setText("Nav atrasta neviena grāmata ar šādu autoru.")

    def del_book_by_isbn(self):
        isbn = self.isbn_input.text()
        try:
            if isbn not in self.books:
                raise Exception("Grāmata ar norādīto ISBN neeksistē")
            del self.books[isbn]
            self.display_area.setText(f"Grāmata ar ISBN {isbn} izdzēsta.")
        except Exception as e:
            self.display_area.setText(str(e))

def main():
    app = QApplication(sys.argv)
    ex = BookManager()
    ex.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
