from abstract_class_storage import Storage, abstractproperty


class Store(Storage):

    def __init__(self, items, capacity=100):
        self.__items = items
        self.capacity = capacity

    def add(self, name, quantity):
        if self.get_free_space() < quantity:
            raise Exception('No space')
        else:
            if name in self.items:
                self.items[name] += quantity
            else:
                self.items[name] = quantity

    def remove(self, name, quantity):
        if name not in self.items:
            raise Exception('No item')
        elif self.items[name] < quantity:
            raise Exception('Not enough items')

        self.items[name] -= quantity
        if self.items[name] == 0:
            del self.items[name]

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_unique_items_count(self):
        return len(self.items)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value
