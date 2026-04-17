from OrderRepository import OrderRepository;

# Репозиторий для хранения заказов в памяти
class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = []

    def add(self, order):
        self.orders.append(order)

    def get_all(self):
        return self.orders

    def get_by_id(self, order_id):
        for order in self.orders:
            if order_id == order.id:
                return order
