import json

def main():
    # load books.json into a dictionary
    books = dict()
    with open("books.json", "r") as f:
        json_books = json.loads(f.read())
        for book in json_books["books"]:
            books[book["ISBN"]] = book
    
    def add_book(book):
        if book["ISBN"] in books:
            raise Exception("grāmata ar šo ISBN jau eksistē")
        books[book["ISBN"]] = book
    
    def find_book_by_isbn(isbn):
        if isbn not in books:
            raise Exception("grāmata ar norādīto ISBN neeksistē")
        return books[isbn]
    
    def find_books_by_name(name):
        books = []  
        for book in books.values():
            if name in book["title"]:
                books.append(book)
    
    def find_books_by_author(author):
        books = []
        for book in books.values():
            if author in book["author"]:
                books.append(book)
                
    def del_book_by_isbn(isbn):
        if isbn not in books:
            raise Exception("grāmata ar norādīto ISBN neeksistē")
        del books[isbn]
    

if __name__ == "__main__":
    main()