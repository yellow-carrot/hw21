class Courier:
    def __init__(self, request, storages):
        self.request = request
        if self.request.departure in storages:
            self._from = storages[self.request.departure]

        if self.request.destination in storages:
            self._to = storages[self.request.destination]

    def move(self):
        self._from.remove(name=self.request.item, quantity=self.request.quantity)
        print(f'Курьер забрал {self.request.quantity} {self.request.item} из {self.request.departure}')

        self._to.add(name=self.request.item, quantity=self.request.quantity)
        print(f'Курьер доставил {self.request.quantity} {self.request.item} в {self.request.destination}')



