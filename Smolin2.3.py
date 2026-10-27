class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} — {self.price} грн (В наявності: {self.stock} шт.)"
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        if product.stock >= quantity:
            for item in self.items:
                if item["product"] == product:
                    item["quantity"] += quantity
                    product.stock -= quantity
                    return
            self.items.append({"product": product, "quantity": quantity})
            product.stock -= quantity
        else:
            print(f"Недостатньо товару '{product.name}' на складі.")

    def remove_product(self, product_name):
        for item in self.items:
            if item["product"].name.lower() == product_name.lower():
                item["product"].stock += item["quantity"]
                self.items.remove(item)
                print(f"Товар '{product_name}' видалено з кошика.")
                return
        print(f"Товар '{product_name}' не знайдено в кошику.")

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total
    def display_cart(self):
        if not self.items:
            print("Кошик порожній.")
            return
        print("\n--- КОШИК ---")
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity
            print(f"{product.name} | Ціна: {product.price} грн | Кількість: {quantity} | Сума: {subtotal} грн")
        print(f"Загальна вартість: {self.calculate_total()} грн")
        print("-------------\n")


product1 = Product("Ноутбук", 25000, 5)
product2 = Product("Мишка", 800, 15)
product3 = Product("Клавіатура", 1500, 10)
cart = Cart()
cart.add_product(product1, 1)
cart.add_product(product2, 2)
cart.add_product(product3, 1)
cart.display_cart()
cart.remove_product("Мишка")
cart.display_cart()