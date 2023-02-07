from abc import ABC, abstractmethod, abstractproperty


class Storage(ABC):

    @abstractmethod
    def add(self, name, quantity):
        pass

    @abstractmethod
    def remove(self, name, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
