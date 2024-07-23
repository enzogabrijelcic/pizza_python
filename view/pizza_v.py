import tkinter as tk
from tkinter import messagebox
from controller.pizza_c import Controller
from PIL import Image, ImageTk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.title("Pizzaria Delivery")
        self.geometry("600x600")
        self.criar_tela_inicio()
    
    def criar_tela_inicio(self):
        self.clear_window()
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia\Pizzaria stories para Instagram escuro (1).png")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

       
        tk.Button(self, text="Entrar", command=self.show_login_window, width=20,bg= "pink", height=2, font=("Arial", 16)).pack(pady=260)

    def show_login_window(self):
        self.clear_window()
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia\login_cadastro.png")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self, text="Usuário:",font=("Arial", 16)).pack(pady=20)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=10)
        tk.Label(self, text="Senha:",font=("Arial", 16)).pack(pady=20)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=10)
        tk.Button(self, text="Login",font=("Arial", 16), command=self.login).pack(pady=30)
        tk.Button(self, text="Cadastrar",font=("Arial", 16), command=self.show_register_window).pack(pady=5)

    def show_register_window(self):
        self.clear_window()
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia\login_cadastro.png")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self, text="Novo Usuário:",font=("Arial", 16)).pack(pady=20)
        self.new_username_entry = tk.Entry(self)
        self.new_username_entry.pack(pady=15)
        tk.Label(self, text="Nova Senha:",font=("Arial", 16)).pack(pady=20)
        self.new_password_entry = tk.Entry(self, show='*')
        self.new_password_entry.pack(pady=15)
        tk.Button(self, text="Cadastrar",font=("Arial", 16), command=self.register).pack(pady=20)
        tk.Button(self, text="Voltar ao Login",font=("Arial", 16), command=self.show_login_window).pack(pady=5)

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
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia\pizza_bg.jpg")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

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
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia/tela_pedidos_carrinho.jpeg")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        total_price = sum(item['valor'] for item in self.selected_items)
        self.payment_var = tk.StringVar(value='Dinheiro')

        tk.Label(self,font=("Arial", 15), text="Resumo do Pedido").pack(pady=30)
        tk.Label(self,font=("Arial", 15), text=f"Itens: {', '.join(item['name'] for item in self.selected_items)}").pack(pady=5)
        tk.Label(self,font=("Arial", 15), text=f"Valor Total: ${total_price}").pack(pady=5)
        
        tk.Label(self,font=("Arial", 14), text="Selecione a forma de pagamento:").pack(pady=5)
        tk.Radiobutton(self,font=("Arial", 13), text="Dinheiro", variable=self.payment_var, value='Dinheiro').pack()
        tk.Radiobutton(self,font=("Arial", 13), text="Cartao de Credito", variable=self.payment_var, value='Cartao de Credito').pack()
        tk.Radiobutton(self,font=("Arial", 13), text="Pix", variable=self.payment_var, value='Pix').pack()

        tk.Button(self,font=("Arial", 14), text="Finalize o Pedido", command=lambda: self.show_address_window(total_price)).pack(pady=10)
        tk.Button(self,font=("Arial", 14), text="Voltar ao Cardapio", command=self.show_menu_window).pack(pady=10)

    def show_address_window(self, total_price):
        self.clear_window()

        # Carregar a imagem de fundo
        self.background_image = Image.open("midia/tela_pedidos_carrinho.jpeg")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.delivery_var = tk.StringVar(value='Delivery')
        self.address_entry = tk.Entry(self)

        tk.Label(self,font=("Arial", 16), text="Endereço da Entrega( deixe em branco se for pegar na loja)").pack(pady=5)
        self.address_entry.pack(pady=5)
        tk.Label(self,font=("Arial", 14), text=f"Frete: $10").pack(pady=15)
        tk.Label(self,font=("Arial", 14), text=f"Valor Total: ${total_price + 10 if self.delivery_var.get() == 'Delivery' else total_price}").pack(pady=5)
        
        tk.Label(self,font=("Arial", 16), text="Selecione a Forma de entrega:").pack(pady=5)
        tk.Radiobutton(self,font=("Arial", 14), text="Delivery", variable=self.delivery_var, value='Delivery').pack()
        tk.Radiobutton(self,font=("Arial", 14), text="Retirar na Loja", variable=self.delivery_var, value='Retirar na Loja').pack()

        tk.Button(self,font=("Arial", 16), text="Finalize o Pedido", command=lambda: self.validate_and_confirm_order(total_price)).pack(pady=20)

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
