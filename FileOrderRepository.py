import json
import os.path

from OrderRepository import OrderRepository


class FileOrderRepository(OrderRepository):

    def __init__(self, filename="orders.json"):
        self.filename = filename

    def _load(self):
        if not os.path.exists(self.filename):
            return []
        else:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)

    def _save(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add(self, order):
        data = self._load()
        data.append(order.to_dict())
        self._save(data)

    def get_all(self):
        return self._load()

    def get_by_id(self, order_id):
        data = self._load()
        for order in data:
            if order["id"] == order_id:
                return order
