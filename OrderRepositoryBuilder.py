from FileOrderRepository import FileOrderRepository
from InMemoryOrderRepository import InMemoryOrderRepository


# Билдер для создания репозитория
class OrderRepositoryBuilder:
    # Тип создаваемого репозитория: в памяти
    IN_MEMORY = 0
    # Тип создаваемого репозитория: в json-файле
    JSON_FILE = 1

    def __init__(self):
        self.repository_type = OrderRepositoryBuilder.IN_MEMORY

    def set_repository_type(self, new_type):
        self.repository_type = new_type
        return self

    def build(self):
        if self.repository_type == OrderRepositoryBuilder.IN_MEMORY:
            return InMemoryOrderRepository()
        elif self.repository_type == OrderRepositoryBuilder.JSON_FILE:
            return FileOrderRepository()
        else:
            raise IOError("Неизвестный тип репозитория.")
