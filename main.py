from class_shop import Shop
from class_store import Store
from class_request import Request
from class_courier import Courier

store = Store(items={})

shop = Shop(items={})

store.items = {
    'печеньки': 5,
    'собачки': 5,
    'коробки': 5,
}
shop.items = {
    'печеньки': 1,
    'собачки': 2,
    'коробки': 3,
}


storages = {
    'магазин': shop,
    'склад': store
}


def main_app():
    print('Здравствуйте!\n')

    while True:

        for storage in storages:
            print(f'В {storage} находится {storages[storage].items}.\n')


        user_input = input('''
        Введите запрос в формате "Доставить 3 печеньки из склад в магазин".
        Введите стоп или stop, чтобы закончить программу.
        ''')

        if user_input.lower() in ['стоп', 'stop']:
            break

        try:
            request = Request(request=user_input, storages=storages)
        except Exception as e:
            print(e)
            continue

        courier = Courier(request=request, storages=storages)

        courier.move()


if __name__ == '__main__':
    main_app()
