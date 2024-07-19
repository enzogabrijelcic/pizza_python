import tkinter as tk
from tkinter import messagebox
from controller.pizza_c import Controller

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.title("Pizzaria Delivery")
        self.geometry("400x600")
        self.show_login_window()

    def show_login_window(self):
        self.clear_window()
        tk.Label(self, text="Usuário:").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)
        tk.Label(self, text="Senha:").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)
        tk.Button(self, text="Login", command=self.login).pack(pady=20)
        tk.Button(self, text="Cadastrar", command=self.show_register_window).pack(pady=5)

    def show_register_window(self):
        self.clear_window()
        tk.Label(self, text="Novo Usuário:").pack(pady=5)
        self.new_username_entry = tk.Entry(self)
        self.new_username_entry.pack(pady=5)
        tk.Label(self, text="Nova Senha:").pack(pady=5)
        self.new_password_entry = tk.Entry(self, show='*')
        self.new_password_entry.pack(pady=5)
        tk.Button(self, text="Cadastrar", command=self.register).pack(pady=20)
        tk.Button(self, text="Voltar ao Login", command=self.show_login_window).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.controller.login(username, password)
        if user:
            self.user_id = user[0]
            self.show_menu_window()
        else:
            messagebox.showerror("Erro", "Login Inválido")

    def register(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        self.controller.register(username, password)
        messagebox.showinfo("OK!", "Usuário cadastrado corretamente!")
        self.show_login_window()

    def show_menu_window(self):
        self.clear_window()
        self.selected_items = []
        self.menu_items = self.controller.get_menu()

        tk.Label(self, text="Menu - Salgadas").pack(pady=5)
        self.salgadas = [
            {"name": "Marguerita", "valor": 25.0},
            {"name": "Calabresa", "valor": 28.0},
            {"name": "4 Queijos", "valor": 30.0},
            {"name": "Mussarela", "valor": 27.0},
            {"name": "Frango", "valor": 26.0}
        ]
        self.salgadas_vars = []

        for item in self.salgadas:
            var = tk.IntVar()
            tk.Checkbutton(self, text=f"{item['name']} - ${item['valor']}", variable=var).pack()
            self.salgadas_vars.append((item, var))

        tk.Label(self, text="Menu - Doces").pack(pady=5)
        self.doces = [
            {"name": "Chocolate", "valor": 20.0},
            {"name": "Morango com Chocolate", "valor": 22.0},
            {"name": "chocolate branco", "valor": 24.0},
            {"name": "Banana", "valor": 23.0}
        ]
        self.doces_vars = []

        for item in self.doces:
            var = tk.IntVar()
            tk.Checkbutton(self, text=f"{item['name']} - ${item['valor']}", variable=var).pack()
            self.doces_vars.append((item, var))

        tk.Label(self, text="Bebidas").pack(pady=5)
        self.bebidas = [
            {"name": "Suco", "valor": 5.0},
            {"name": "Agua", "valor": 3.0},
            {"name": "Pepsi", "valor": 6.0},
            {"name": "Guaraná", "valor": 6.0},
            {"name": "Heineken", "valor": 8.0},
            {"name": "Vinho", "valor": 15.0}
        ]
        self.bebidas_vars = []

        for item in self.bebidas:
            var = tk.IntVar()
            tk.Checkbutton(self, text=f"{item['name']} - ${item['valor']}", variable=var).pack()
            self.bebidas_vars.append((item, var))

        tk.Button(self, text="Adicionar ao Pedido", command=self.add_to_order).pack(pady=10)
        tk.Button(self, text="Ir ao Resumo do Pedido", command=self.show_summary_window).pack(pady=10)

    def add_to_order(self):
        for item, var in self.salgadas_vars + self.doces_vars + self.bebidas_vars:
            if var.get():
                self.selected_items.append(item)
        if not self.selected_items:
            messagebox.showwarning("Atenção!", "Selecione no mínimo um item antes de Ver o resumo do pedido.")
        else:
            messagebox.showinfo("iten(s) adicionado(s)", "Item(s) adicionados ao seu pedido.")

    def show_summary_window(self):
        if not self.selected_items:
            messagebox.showwarning("Atenção!", "Selecione no mínimo um item antes de Ver o resumo do pedido.")
            return
        
        self.clear_window()
        total_price = sum(item['valor'] for item in self.selected_items)
        self.payment_var = tk.StringVar(value='Dinheiro')

        tk.Label(self, text="Resumo do Pedido").pack(pady=5)
        tk.Label(self, text=f"Items: {', '.join(item['name'] for item in self.selected_items)}").pack(pady=5)
        tk.Label(self, text=f"Valor Total: ${total_price}").pack(pady=5)
        
        tk.Label(self, text="Selecione a forma de pagamento:").pack(pady=5)
        tk.Radiobutton(self, text="Dinheiro", variable=self.payment_var, value='Dinheiro').pack()
        tk.Radiobutton(self, text="Cartao de Credito", variable=self.payment_var, value='Cartao de Credito').pack()
        tk.Radiobutton(self, text="Pix", variable=self.payment_var, value='Pix').pack()

        tk.Button(self, text="Finalize o Pedido", command=lambda: self.show_address_window(total_price)).pack(pady=10)
        tk.Button(self, text="Voltar ao Cardapio", command=self.show_menu_window).pack(pady=10)

    def show_address_window(self, total_price):
        self.clear_window()
        self.delivery_var = tk.StringVar(value='Delivery')
        self.address_entry = tk.Entry(self)

        tk.Label(self, text="Endereço da Entrega( deixe em branco se for pegar na loja)").pack(pady=5)
        self.address_entry.pack(pady=5)
        tk.Label(self, text=f"Frete: $10").pack(pady=5)
        tk.Label(self, text=f"Valor Total: ${total_price + 10 if self.delivery_var.get() == 'Delivery' else total_price}").pack(pady=5)
        
        tk.Label(self, text="Selecione a Forma de entrega:").pack(pady=5)
        tk.Radiobutton(self, text="Delivery", variable=self.delivery_var, value='Delivery').pack()
        tk.Radiobutton(self, text="Retirar na Loja", variable=self.delivery_var, value='Retirar na Loja').pack()

        tk.Button(self, text="Finalize o Pedido", command=lambda: self.validate_and_confirm_order(total_price)).pack(pady=20)

    def validate_and_confirm_order(self, total_price):
        address = self.address_entry.get()
        delivery_type = self.delivery_var.get()
        payment_method = self.payment_var.get()
        final_price = total_price + 10 if delivery_type == 'Delivery' else total_price

        if delivery_type == 'Delivery' and not address:
            messagebox.showerror("Erro", "É necessario inserir o endereço para delivery.Por favor insira um endereço.")
            return
        
        items = ', '.join(item['name'] for item in self.selected_items)
        self.controller.place_order(self.user_id, items, final_price, payment_method, address, delivery_type)
        order_id = self.controller.get_last_order_id()
        messagebox.showinfo("Pedido Finalizado", f"Numero do seu pedido:{order_id}. Obrigado por comprar conosco!")
        self.destroy()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
