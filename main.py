import tkinter as tk
import tkinter.font as tkfont
from PIL import Image, ImageTk, ImageDraw, ImageFont

def start_game(mode):
    # Função para iniciar o jogo com base no modo selecionado
    # Coloque aqui a lógica para iniciar o jogo no modo individual ou em dupla
    pass

def show_instructions():
    # Função para exibir as instruções do jogo
    window.withdraw()  # Oculta a janela principal

    # Cria a nova janela para as instruções
    instructions_window = tk.Toplevel()
    instructions_window.title("Instruções")
    instructions_window.geometry("800x600")

    # Definir a fonte para o texto das instruções
    instructions_font = tkfont.Font(family="Arial", size=12)

    # Crie um label para exibir as instruções
    instructions_text = """
    Instruções do jogo "Buraco Game"

    Modalidade Player 1 e Player 2:
    1. Cada jogador receberá 11 cartas no início do jogo.
    2. Seu objetivo é formar sequências crescentes do mesmo naipe (canastas).
    3. Durante sua vez, você pode pegar uma carta da pilha de compra ou descartar uma carta.
    4. Some os pontos das cartas restantes na sua mão.
    5. O jogador que encontrar a maior subsequência crescente possível entre as cartas em sua
    mão, vence a partida.
    
    Pressione o botão "Menu Inicial" para voltar a janela anterior.
    """

    instructions_label = tk.Label(instructions_window, text=instructions_text, justify=tk.LEFT, font=instructions_font)
    instructions_label.pack()

    # Definir a fonte para o título
    title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")

    # Cria o botão "Menu Inicial" para voltar ao menu principal
    menu_button = tk.Button(instructions_window, text="Menu Inicial", command=lambda: [instructions_window.destroy(), window.deiconify()])
    menu_button.pack()

    instructions_window.mainloop()

def resize_bg(event):
    # Função para redimensionar a imagem de fundo quando a janela é redimensionada
    global bg_image, bg_photo

    new_width = event.width
    new_height = event.height

    bg_image_resized = bg_image.resize((new_width, new_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image_resized)
    canvas.config(width=new_width, height=new_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

# Criar a janela principal
window = tk.Tk()
window.title("Buraco Game")
window.geometry("800x600")

# Carregar a imagem de fundo
bg_image = Image.open("assets/inicio.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Adicionar o título na imagem
image_with_title = Image.new("RGB", (bg_image.width, bg_image.height + 50), color=(255, 255, 255))
image_with_title.paste(bg_image, (0, 50))
draw = ImageDraw.Draw(image_with_title)
font = ImageFont.truetype("arial.ttf", 24)
text_bbox = draw.textbbox((0, 0), "Buraco Game", font=font)
text_position = ((bg_image.width - text_bbox[2]) // 2, 10)
draw.text(text_position, "Buraco Game", font=font, fill=(0, 0, 0))

bg_photo_with_title = ImageTk.PhotoImage(image_with_title)

# Criar um Canvas para exibir a imagem de fundo com título
canvas = tk.Canvas(window, width=300, height=200)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo_with_title)

# Criar labels para exibir os textos acima dos botões
label_font = tkfont.Font(size=26, weight='bold')  # Define a fonte do label
label_text_1 = tk.Label(window, text="BURACO GAME", font=label_font, bg="white")
label_text_1.place(x=400, y=50, anchor=tk.CENTER)

label_font = tkfont.Font(size=26, weight='bold')  # Define a fonte do label
label_text_1 = tk.Label(window, text="Modo de Jogo:", font=label_font, bg="white")
label_text_1.place(x=225, y=450, anchor=tk.CENTER)

# Criar os botões
button_font = tkfont.Font(size=14, weight='bold')  # Define a fonte dos botões

player_1_button = tk.Button(window, text="Player 1", command=lambda: start_game("Player 1"), font=button_font)
player_1_button.place(x=200, y=500, anchor=tk.E)

player_2_button = tk.Button(window, text="Player 2", command=lambda: start_game("Player 2"), font=button_font)
player_2_button.place(x=210, y=500, anchor=tk.W)

instructions_button = tk.Button(window, text="Instruções", command=show_instructions, font=button_font)
instructions_button.place(x=200, y=550, anchor=tk.CENTER)

# Registrar a função resize_bg para ser chamada quando a janela for redimensionada
window.bind("<Configure>", resize_bg)

# Iniciar a interface gráfica
window.mainloop()