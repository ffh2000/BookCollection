from FictionBook import FictionBook
from ScienceBook import ScienceBook
from ArtBook import ArtBook

class BookFactory:
    def create_book(book_type, title, author, price):
        if book_type == "fiction":
            return FictionBook(title, author, price)
        elif book_type == "science":
            return ScienceBook(title, author, price)
        elif book_type == "art":
            return ArtBook(title, author, price)
        else:
            raise ValueError("Неизвестный тип книги")
