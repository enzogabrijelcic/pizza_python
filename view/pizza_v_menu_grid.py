import tkinter as tk
from tkinter import ttk
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
        self.controller.clear_window(self)
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia/Pizzaria stories para Instagram escuro (1).png")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

       
        tk.Button(self, text="Entrar", command=self.show_login_window, width=20,bg= "pink", height=2, font=("Arial", 16)).pack(pady=260)

    def show_login_window(self):
        self.controller.clear_window(self)
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia/login_cadastro.png")
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
        self.controller.clear_window(self)
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia/login_cadastro.png")
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
            messagebox.showinfo("Login!", "Seja bem vindo!")
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
        self.controller.clear_window(self)
        
        
        # Criar uma Label como título da janela Menu
        #tk.Label(menu_frame, text='CARDÁPIO', font=('Arial', 30)).pack(pady=10)

        # Carregar a imagem de fundo
        self.background_image = Image.open("midia\Estamos abertos story chamativo vermelho.png")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.selected_items = []
        self.menu_items = self.controller.get_menu()

        # Cria um frame para a tabela
        table_frame = tk.Frame(self)
        table_frame.pack(pady=20)

        # Configura as colunas para expandirem uniformemente
        for i in range(3):
            table_frame.grid_columnconfigure(i, weight=1)

        # Títulos das categorias
        tk.Label(table_frame, text="Salgadas", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        tk.Label(table_frame, text="Doces", font=("Arial", 14)).grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        tk.Label(table_frame, text="Bebidas", font=("Arial", 14)).grid(row=0, column=2, padx=10, pady=5, sticky="ew")

        # Dados das categorias
        self.salgadas = [
            {"name": "Marguerita", "valor": 25.0, "quantidade": 0},
            {"name": "Calabresa", "valor": 28.0, "quantidade": 0},
            {"name": "4 Queijos", "valor": 30.0, "quantidade": 0},
            {"name": "Mussarela", "valor": 27.0, "quantidade": 0},
            {"name": "Frango", "valor": 26.0, "quantidade": 0}
        ]
        self.doces = [
            {"name": "Chocolate", "valor": 20.0, "quantidade": 0},
            {"name": "Morango com Chocolate", "valor": 22.0, "quantidade": 0},
            {"name": "Chocolate Branco", "valor": 24.0, "quantidade": 0},
            {"name": "Banana", "valor": 23.0, "quantidade": 0}
        ]
        self.bebidas = [
            {"name": "Suco", "valor": 5.0, "quantidade": 0},
            {"name": "Agua", "valor": 3.0, "quantidade": 0},
            {"name": "Pepsi", "valor": 6.0, "quantidade": 0},
            {"name": "Guaraná", "valor": 6.0, "quantidade": 0},
            {"name": "Heineken", "valor": 8.0, "quantidade": 0},
            {"name": "Vinho", "valor": 15.0, "quantidade": 0}
        ]

        self.item_vars = {"Salgadas": [], "Doces": [], "Bebidas": []}

        def create_item_widgets(items, category):
            column = column_mapping[category]
            for row, item in enumerate(items, start=1):
                frame = tk.Frame(table_frame)
                frame.grid(row=row, column=column, padx=10, pady=5, sticky="w")
                tk.Label(frame, text=f'{item["name"]} - R${item["valor"]}').pack(side=tk.LEFT)
                var = tk.IntVar(value=0)
                var.trace_add('write', lambda _, __, ___, item=item, var=var: self.controller.update_quantity(item, var))
                spinbox = tk.Spinbox(frame, from_=0, to=100, textvariable=var, width=3)
                spinbox.pack(side=tk.RIGHT)
                self.item_vars[category].append((item, var))

        # Mapeia as colunas para inteiros
        column_mapping = {"Salgadas": 0, "Doces": 1, "Bebidas": 2}

        create_item_widgets(self.salgadas, "Salgadas")
        create_item_widgets(self.doces, "Doces")
        create_item_widgets(self.bebidas, "Bebidas")

        tk.Button(self, font=("Arial", 13), text="Adicionar ao Pedido", command=self.add_to_order).pack(pady=10)
        tk.Button(self, font=("Arial", 13), text="Ir ao Resumo do Pedido", command=self.show_summary_window).pack(pady=10)

    def add_to_order(self):
        for category in self.item_vars:
            for item, var in self.item_vars[category]:
                if var.get() > 0:
                    item['quantidade'] = var.get()
                    self.selected_items.append(item)
        if not self.selected_items:
            messagebox.showwarning("Atenção!", "Selecione no mínimo um item antes de Ver o resumo do pedido.")
        else:
            messagebox.showinfo("iten(s) adicionado(s)", "Item(s) adicionados ao seu pedido.")

    def show_summary_window(self):
        if not self.selected_items:
            messagebox.showwarning("Atenção!", "Selecione no mínimo um item antes de ver o resumo do pedido.")
            return
        
        self.controller.clear_window(self)
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia\pngtree-delicious-nutritious-pizza-background-material-image_140939.jpg")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        total_price = sum(item['valor'] for item in self.selected_items)
        self.payment_var = tk.StringVar(value='Dinheiro')

        
        tk.Label(self, font=("Arial", 15),text=f"Items: {', '.join(f"{item['name']} (x{item['quantidade']})"for item in self.selected_items)}").pack(pady=5)
        tk.Label(self,font=("Arial", 15), text="Resumo do Pedido").pack(pady=30)
        tk.Label(self,font=("Arial", 15), text=f"Valor Total: ${total_price}").pack(pady=5)
        
        tk.Label(self,font=("Arial", 14), text="Selecione a forma de pagamento:").pack(pady=5)
        tk.Radiobutton(self,font=("Arial", 13), text="Dinheiro", variable=self.payment_var, value='Dinheiro').pack()
        tk.Radiobutton(self,font=("Arial", 13), text="Cartao de Credito", variable=self.payment_var, value='Cartao de Credito').pack()
        tk.Radiobutton(self,font=("Arial", 13), text="Pix", variable=self.payment_var, value='Pix').pack()

        tk.Button(self,font=("Arial", 14), text="Finalize o Pedido", command=lambda: self.show_address_window(total_price)).pack(pady=10)
        tk.Button(self,font=("Arial", 14), text="Voltar ao Cardapio", command=self.show_menu_window).pack(pady=10)

               
    def show_address_window(self, total_price):
        self.controller.clear_window(self)

        # Carregar a imagem de fundo
        self.background_image = Image.open("midia\pngtree-delicious-nutritious-pizza-background-material-image_140939.jpg")
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
        final_price = total_price + 10 if delivery_type == 'Tele-Entrega' else total_price

        if delivery_type == 'Tele-Entrega' and not address:
            messagebox.showerror("Erro", "É necessario inserir o endereço para tele-entrega.Por favor insira um endereço.")
            return
        
        items = ', '.join(item['name'] for item in self.selected_items)
        self.controller.place_order(self.user_id, items, final_price, payment_method, address, delivery_type)
        order_id = self.controller.get_last_order_id()
        messagebox.showinfo("Pedido Finalizado", f"Numero do seu pedido:{order_id}. Obrigado por comprar conosco!")
        self.controller.clear_window(self)
        self.criar_tela_inicio()

