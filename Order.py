import uuid
from datetime import datetime


# Заказ
class Order:
    def __init__(self, reader_id, items):
        # id заказа
        self.id = str(uuid.uuid4())
        # сохранение номера читателя
        self.reader_id = reader_id
        # Дата/время выдачи заказа
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        # Список книг
        self.items = items
        # Состояние заказ
        self.status = "Создан"

    def to_dict(self):
        return {
            "id": self.id,
            "reader_id": self.reader_id,
            "date": self.date,
            "status": self.status,
            "items": [item.get_info() for item in self.items]
        }
