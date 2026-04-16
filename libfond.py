import sys
from BookCollectionBuilder import BookCollectionBuilder
from BookCollection import BookCollection
from ArtBook import ArtBook
from FictionBook import FictionBook
from ScienceBook import ScienceBook
from BookFactory import BookFactory

def main():
    # print("Управление библиотечным фондом")
    # print("Аргументы командной строки:")
    # print("memory - Хранить в памяти")
    # print("file - Хранить в файле")
    # book = BookFactory.create_book("xdvfsdv", "Буратино", "Носов", 1000)
    # print(book.get_info())
    # bookCol = BookCollection("Научная фантастика")
    # print(bookCol.get_info())
    builder = BookCollectionBuilder()
    builder.set_price(999)
    builder.set_theme("Детективы")
    builder.add_book(ArtBook("Десять негритят", "Агата Кристи", 100))
    builder.add_book(FictionBook("Как управлять миром, что бы не заметили санитары", "Шизик", 666))
    bookCol = builder.build()
    print(bookCol.get_info())

if __name__ == "__main__":
    main()