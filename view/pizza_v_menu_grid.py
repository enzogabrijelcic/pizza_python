import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controller.pizza_c import Controller
from PIL import Image, ImageTk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.title("Pizza Python")
        self.geometry("600x600")
        self.resizable(False,False)
        self.app_no_centro_da_tela(600,600)
        self.criar_tela_inicio()
    
    def app_no_centro_da_tela(self, width, height):
        largura_da_tela = self.winfo_screenwidth()
        altura_da_tela = self.winfo_screenheight()
        x = (largura_da_tela // 2) - (width // 2)
        y = (altura_da_tela // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        
    def fechar_programa(self):
        # Função para fechar o programa
        if messagebox.askokcancel("Fechar programa", "Deseja fechar o programa?"):
            self.destroy()  # Fecha a janela principal e finaliza o programa


    def criar_tela_inicio(self):
        self.controller.clear_window(self)
        # Carregar a imagem de fundo
        self.background_image = Image.open("midia/Pizzaria stories para Instagram escuro (1).png")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

       
        botao_entrar = tk.Button(self, text="Entrar", command=self.show_login_window, width=15,bg= "pink", height=1, font=("Arial", 16))
        botao_entrar.pack(pady=(240, 0), side=tk.TOP)
        botao_sair = tk.Button(self, text="Sair", command=self.fechar_programa, width=15,bg= "pink", height=1, font=("Arial", 16))
        botao_sair.pack(pady=(0, 240), side=tk.TOP)

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
        tk.Button(self, text="Voltar Para Tela Inicial",font=("Arial", 16), command=self.criar_tela_inicio).pack(pady=5)

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
    
    def show_order_history(self):
        self.controller.clear_window(self)

        self.background_image = Image.open("midia/papiro.jpg")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        orders = self.controller.get_user_orders(self.user_id)
        
        tk.Label(self, text="Histórico de Pedidos", font=("Arial", 16)).pack(pady=10)
        
        if not orders:
            tk.Label(self, text="Nenhum pedido encontrado.").pack(pady=10)
        else:
            for order in orders:
                tk.Label(self, text=f"Pedido ID: {order[0]}, Itens: {order[2]}, Total: R${order[3]}").pack(pady=5)
        
        tk.Button(self, text="Voltar ao Menu", command=self.show_menu_window).pack(pady=10)

    def show_faq_window(self):
        self.controller.clear_window(self)
        faqs = self.controller.get_faqs()

        tk.Label(self, text="Perguntas Frequentes", font=("Arial", 16)).pack(pady=20)

        for faq in faqs:
            tk.Label(self, text=f"Pergunta: {faq['question']}", font=("Arial", 14, 'bold')).pack(pady=5)
            tk.Label(self, text=f"Resposta: {faq['answer']}", font=("Arial", 14)).pack(pady=10)

        tk.Button(self, text="Voltar ao Menu", command=self.show_menu_window).pack(pady=20)
    
    def show_reviews_window(self):
        self.controller.clear_window(self)
        
        # Create a frame for the entire content
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Create a frame for recent reviews with a scrollbar
        self.reviews_canvas = tk.Canvas(self.content_frame)
        self.reviews_scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical", command=self.reviews_canvas.yview)
        self.reviews_frame = tk.Frame(self.reviews_canvas)

        # Create a window inside the canvas for the reviews_frame
        self.reviews_canvas.create_window((0, 0), window=self.reviews_frame, anchor="nw")
        self.reviews_canvas.configure(yscrollcommand=self.reviews_scrollbar.set)

        # Pack the canvas and scrollbar
        self.reviews_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.reviews_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind the configure event to update scroll region
        self.reviews_frame.bind("<Configure>", self.on_frame_configure)

        # Frame for adding new review
        self.add_review_frame = tk.Frame(self.content_frame)
        self.add_review_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

        # Load reviews
        self.load_reviews()

        # Add the section for adding new reviews
        self.add_review_section()

    def on_frame_configure(self, event):
        self.reviews_canvas.configure(scrollregion=self.reviews_canvas.bbox("all"))

    def load_reviews(self):
        reviews = self.controller.get_reviews()

        if reviews:
            tk.Label(self.reviews_frame, text="Avaliações Recentes:", font=("Arial", 14)).pack(pady=10)
            for review in reviews:
                username, rating, comment, created_at = review
                review_frame = tk.Frame(self.reviews_frame, borderwidth=1, relief="solid")
                review_frame.pack(pady=10, padx=10, fill=tk.X)

                tk.Label(review_frame, text=f"{username} ({created_at}):", font=("Arial", 12)).pack(anchor=tk.W)
                tk.Label(review_frame, text=f"Rating: {rating}", font=("Arial", 12)).pack(anchor=tk.W)
                tk.Label(review_frame, text=f"Comment: {comment}", font=("Arial", 12)).pack(anchor=tk.W)
        else:
            tk.Label(self.reviews_frame, text="Ainda não há avaliações.", font=("Arial", 14)).pack(pady=10)

    def add_review_section(self):
        tk.Label(self.add_review_frame, text="Adicionar Nova Avaliação", font=("Arial", 14)).pack(pady=20)

        self.rating_var = tk.IntVar(value=1)
        tk.Label(self.add_review_frame, text="Nota (1 a 5):", font=("Arial", 12)).pack(pady=5)
        tk.Spinbox(self.add_review_frame, from_=1, to=5, textvariable=self.rating_var, width=3, font=("Arial", 12)).pack(pady=10)

        tk.Label(self.add_review_frame, text="Comentário:", font=("Arial", 12)).pack(pady=5)
        self.comment_entry = tk.Entry(self.add_review_frame, width=50, font=("Arial", 12))
        self.comment_entry.pack(pady=10)

        tk.Button(self.add_review_frame, text="Enviar Avaliação", font=("Arial", 14), command=self.submit_review).pack(pady=20)
        tk.Button(self.add_review_frame, text="Voltar ao Menu", font=("Arial", 14), command=self.show_menu_window).pack(pady=10)

    def submit_review(self):
        rating = self.rating_var.get()
        comment = self.comment_entry.get()

        if not comment.strip():
            messagebox.showwarning("Atenção", "O comentário não pode estar vazio.")
            return

        # Call controller to save review
        self.controller.add_review(self.user_id, rating, comment)
        messagebox.showinfo("Sucesso", "Avaliação enviada com sucesso!")

        # Reload reviews
        self.show_reviews_window()

        # Clear the entry fields
        self.comment_entry.delete(0, tk.END)
        self.rating_var.set(1)
        
    def show_menu_window(self):
        self.controller.clear_window(self)
        

        # Carregar a imagem de fundo
        self.background_image = Image.open("midia\Estamos abertos story chamativo vermelho (1).png")
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
            {"name": "Água", "valor": 3.0, "quantidade": 0},
            {"name": "Pepsi", "valor": 6.0, "quantidade": 0},
            {"name": "Guaraná", "valor": 6.0, "quantidade": 0},
            {"name": "Heineken", "valor": 8.0, "quantidade": 0},
            {"name": "Vinho", "valor": 15.0, "quantidade": 0}
        ]

        self.item_vars = {"Salgadas": [], "Doces": [], "Bebidas": []}

        # Função que cria os widgets (label e spinbox) para os itens de uma categoria e os organiza em colunas.  
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
        tk.Button(self, font=("Arial", 13), text="Voltar a tela de login", command=self.show_login_window).pack(pady=10)
        tk.Button(self, font=("Arial", 13), text="Historico de pedidos", command=self.show_order_history).pack(pady=10)
        tk.Button(self, font=("Arial", 13), text="Tela de perguntas", command=self.show_faq_window).pack(pady=10)
        tk.Button(self, font=("Arial", 13), text="Tela de Avaliaçoes", command=self.show_reviews_window).pack(pady=10)

    def add_to_order(self):
        for category in self.item_vars:
            for item, var in self.item_vars[category]:
                if var.get() > 0:
                    item['quantidade'] = var.get()
                    self.selected_items.append(item)
        if not self.selected_items:
            messagebox.showwarning("Atenção!", "Selecione no mínimo um item antes de Ver o resumo do pedido.")
        else:
            messagebox.showinfo("item(s) adicionado(s)", "Item(s) adicionado(s) ao seu pedido.")

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

        total_price = sum(item['quantidade'] * item['valor'] for item in self.selected_items)
        self.payment_var = tk.StringVar(value='Dinheiro')

        
        tk.Label(self, font=("Arial", 15),text=f"Items: {', '.join(f"{item['name']} (x{item['quantidade']})"for item in self.selected_items)}").pack(pady=5)
        tk.Label(self,font=("Arial", 15), text="Resumo do Pedido").pack(pady=30)
        tk.Label(self,font=("Arial", 15), text=f"Valor Total: ${total_price}").pack(pady=5)
        
        tk.Label(self,font=("Arial", 14), text="Selecione a forma de pagamento:").pack(pady=5)
        tk.Radiobutton(self,font=("Arial", 13), text="Dinheiro", variable=self.payment_var, value='Dinheiro').pack()
        tk.Radiobutton(self,font=("Arial", 13), text="Cartao de Crédito", variable=self.payment_var, value='Cartao de Credito').pack()
        tk.Radiobutton(self,font=("Arial", 13), text="Pix", variable=self.payment_var, value='Pix').pack()

        tk.Button(self,font=("Arial", 14), text="ir à Tela de Endereço", command=lambda: self.show_address_window(total_price)).pack(pady=10)
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

        self.delivery_var = tk.StringVar(value='Tele-Entrega')
        self.address_entry = tk.Entry(self)

        tk.Label(self,font=("Arial", 16), text="Endereço (deixe em branco se for pegar na loja):").pack(pady=5)
        self.address_entry.pack(pady=5)
        
        self.frete_label = tk.Label(self, font=("Arial", 14), text=f"Frete: R$10")
        self.frete_label.pack(pady=15)

        self.total_com_frete_label = tk.Label(self, font=("Arial", 14), text=f"Valor Total com Frete: R${total_price + 10}")
        self.total_com_frete_label.pack(pady=5)

        self.total_sem_frete_label = tk.Label(self, font=("Arial", 14), text=f"Valor Total: R${total_price}")
        self.total_sem_frete_label.pack(pady=5)
        self.total_sem_frete_label.pack_forget()  # Esconde inicialmente

        self.forma_entrega=tk.Label(self,font=("Arial", 16), text="Selecione a Forma de entrega:")
        self.forma_entrega.pack(pady=5)
        
        self.tele_entrega=tk.Radiobutton(self,font=("Arial", 14), text="Tele-Entrega", variable=self.delivery_var, value='Tele-Entrega', command=self.update_labels)
        self.tele_entrega.pack()
        
        self.retirar_loja= tk.Radiobutton(self,font=("Arial", 14), text="Retirar na Loja", variable=self.delivery_var, value='Retirar na Loja', command=self.update_labels)
        self.retirar_loja.pack()

        self.finaliza_botao=tk.Button(self,font=("Arial", 16), text="Finalize o Pedido", command=lambda: self.validate_and_confirm_order(total_price))
        self.finaliza_botao.place(x=200, y=350)
        
        self.volta_botao=tk.Button(self,font=("Arial", 14), text="Voltar à Tela de Resumo", command=self.show_summary_window)
        self.volta_botao.place(x=175, y=400)
    
    
    def update_labels(self):
        if self.delivery_var.get() == 'Retirar na Loja':
            self.frete_label.pack_forget()
            self.total_com_frete_label.pack_forget()
            self.total_sem_frete_label.pack()
           
        else:
            self.frete_label.pack(pady=15)
            self.total_com_frete_label.pack(pady=5)
            self.total_sem_frete_label.pack_forget()
        
    def validate_and_confirm_order(self, total_price):
        address = self.address_entry.get()
        delivery_type = self.delivery_var.get()
        payment_method = self.payment_var.get()
        final_price = total_price + 10 if delivery_type == 'Tele-Entrega' else total_price

        if delivery_type == 'Tele-Entrega' and not address:
            messagebox.showerror("Erro", "É necessario inserir o endereço para tele-entrega. Por favor, insira um endereço.")
            return
        
        items = ', '.join(item['name'] for item in self.selected_items)
        self.controller.place_order(self.user_id, items, final_price, payment_method, address, delivery_type)
        order_id = self.controller.get_last_order_id()
        messagebox.showinfo("Pedido Finalizado", f"Número do seu pedido:{order_id}. Obrigado por comprar conosco!")
        self.controller.clear_window(self)
        self.criar_tela_inicio()

