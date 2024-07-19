from model.pizza_m import Database

class Controller:
    def __init__(self):
        self.db = Database()

    def login(self, username, password):
        return self.db.login_user(username, password)

    def register(self, username, password):
        self.db.register_user(username, password)

    def get_menu(self):
        return self.db.get_menu_items()

    def place_order(self, user_id, items, total_price, payment_method, address, delivery_type):
        order_details = (user_id, items, total_price, payment_method, address, delivery_type)
        self.db.save_order(order_details)

    def get_last_order_id(self):
        return self.db.get_last_order_id()
