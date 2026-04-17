from BookCollectionBuilder import BookCollectionBuilder
from BookFactory import BookFactory
from Order import Order
from OrderRepositoryBuilder import OrderRepositoryBuilder
from OrderService import OrderService


def main():
    order_repository = (
        OrderRepositoryBuilder()
        # .set_repository_type(OrderRepositoryBuilder.IN_MEMORY)
        .set_repository_type(OrderRepositoryBuilder.JSON_FILE)
        .build()
    )
    # Сервис упарвления заказами
    service = OrderService(order_repository)

    # Книги
    book1 = BookFactory.create_book(BookFactory.FICTION_BOOK, "1984", "Оруэл", 150)
    book2 = BookFactory.create_book(BookFactory.SCIENCE_BOOK, "Наполеон", "Е. Тарле", 355)
    book3 = BookFactory.create_book(BookFactory.ART_BOOK, "Незнайка на Луне", "Н. Носов", 999)

    catalog = [book1, book2, book3]

    # Создание коллекции книг
    book_col = (
        BookCollectionBuilder()
        .set_theme("Книги нашей библиотеки")
        .add_book(book1)
        .add_book(book2)
        .add_book(book3)
        .set_price(5000)
        .build()
    )
    print(f"Коллекция книг: {book_col.get_info()}")

    # Заказ
    order = Order(9999, [book2])
    service.add(order)
    order = Order(1, catalog)
    service.add(order)

    # Получение заказа по id
    # zakaz = service.get_by_id("1c342f10-ba2f-4510-880b-ba331043dfd4")
    zakaz = service.get_by_id("a5c0fb81-5248-4279-a586-31b8355cbccf")
    print(zakaz)

    # Получение истории заказов
    print("=== История заказов ===")
    orders = service.get_all()
    for order in orders:
        print(order)

if __name__ == "__main__":
    main()
