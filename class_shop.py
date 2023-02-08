from abstract_class_storage import Storage


class Shop(Storage):

    def __init__(self, items, capacity=20):
        self.__items = items
        self.capacity = capacity

    def add(self, name, quantity):
        if self.get_free_space() < quantity:
            raise Exception('No space')
        elif self.get_unique_items_count() > 5:
            raise Exception('Too many unique items')
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

    @property
    def items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.items)

    @items.setter
    def items(self, value):
        self.__items = value
