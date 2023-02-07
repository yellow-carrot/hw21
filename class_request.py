from typing import Dict

from abstract_class_storage import Storage


class Request:

    def __init__(self, request, storages):
        splitted_req = request.lower().split(' ')
        if len(splitted_req) != 7:
            raise Exception('Неверный запрос')

        self.quantity = int(splitted_req[1])
        self.item = splitted_req[2]
        self.departure = splitted_req[4]
        self.destination = splitted_req[6]

        if self.departure not in storages or self.destination not in storages:
            raise Exception('Неправильное название места')

