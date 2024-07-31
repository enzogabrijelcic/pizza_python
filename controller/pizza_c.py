from model.pizza_m import Database
from tkinter import messagebox

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
    
    def update_quantity(self, item, var):
            item['quantidade'] = var.get()
    
    def clear_window(self,parent):
        for widget in parent.winfo_children():
            widget.destroy()
    
    def get_user_orders(self, user_id):
        return self.db.get_user_orders(user_id)
    
    def get_faqs(self):
        # Exemplo de FAQs estáticas
        faqs = [
            {"question": "Como faço para realizar um pedido?", "answer": "Você pode fazer um pedido através da nossa tela de menu. Selecione os itens desejados e siga o processo de checkout."},
            {"question": "Quais são os métodos de pagamento aceitos?", "answer": "Aceitamos Dinheiro, Cartão de Crédito e Pix."},
            {"question": "Qual é o horário de funcionamento?", "answer": "Estamos abertos todos os dias das 10h às 23h."},
            {"question": "Como posso alterar meu endereço de entrega?", "answer": "Você pode atualizar seu endereço na tela de perfil do usuário antes de finalizar um pedido."}
        ]
        return faqs

    def get_reviews(self):
        return self.db.get_reviews()

    def add_review(self, user_id, rating, comment):
        self.db.add_review(user_id, rating, comment)
    
