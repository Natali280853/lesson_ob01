# Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями,
# адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар,
# обнови цену, убери товар и запрашивай цену.
# Store - магазин
# (name; address; items) - название магазина; адрес магазина;
# словарь, где ключ - название товара, а значение - его цена. Например,
# `{'apples': 0.5, 'bananas': 0.75}`

class Store:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"товар '{item_name}' добавлен в магазин {self.name}")

    def del_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"товар '{item_name}' удален из магазина {self.name}")

    def price_item(self, item_name):
        print(f"Цена на {item_name} равна {self.items.get(item_name)}.")

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '<{item_name}>' обновилась в {self.name} и составляет {self.items[item_name]}.")


store1 = Store("Гудвин",  "Советская, 122")

store1.add_item("Пальто",  11000)
store1.add_item("Платье",  9000)
store1.add_item("Костюм",  15000)
print()
store2 = Store("Метро",  "Мельникайте, 141")
store2.add_item("Сливочное масло",  950)
store2.add_item("Коньяк",  2500)
store2.add_item("Конфеты",  450)
store2.add_item("Чай 'Акбар'",  260)
print()
store3 = Store("Дикси", "Мельникайте, 62")
store3.add_item("Яблоки", 149)
store3.add_item("Хлеб", 62)
store3.add_item("Молоко", 98)
store3.add_item("Сметана", 102)

# Выбери один из созданных магазинов и протестируй все его методы: добавь товар,
# обнови цену, убери товар и запрашивай цену.
print()
store2.add_item("Кофе", 1200)
store2.price_item("Кофе")
store2.update_price("Кофе", 980)
store2.del_item("Кофе")
