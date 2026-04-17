from FictionBook import FictionBook
from ScienceBook import ScienceBook
from ArtBook import ArtBook

class BookFactory:

    # Типы книг
    FICTION_BOOK = "fiction"
    SCIENCE_BOOK = "science"
    ART_BOOK = "art"

    def create_book(book_type, title, author, price):
        if book_type == BookFactory.FICTION_BOOK:
            return FictionBook(title, author, price)
        elif book_type == BookFactory.SCIENCE_BOOK:
            return ScienceBook(title, author, price)
        elif book_type == BookFactory.ART_BOOK:
            return ArtBook(title, author, price)
        else:
            raise ValueError("Неизвестный тип книги")
