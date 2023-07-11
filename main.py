from PIL import Image, ImageTk, ImageDraw, ImageFont
import random
import tkinter as tk
import tkinter.font as tkfont
import os

player_1_window = None
subsequence_window = None

def start_game(mode):
    if mode == "Player 1":
        start_game_player_1()

def show_instructions():
    window.withdraw()

    instructions_window = tk.Toplevel()
    instructions_window.title("Instruções")
    instructions_window.geometry("600x300")

    title_font = tkfont.Font(family="Arial", size=18, weight="bold")
    text_font = tkfont.Font(family="Arial", size=12)

    title_label = tk.Label(instructions_window, text="Instruções do jogo Sequência Suprema", font=title_font)
    title_label.pack(pady=10)

    instructions_text = """
    Modalidade Player 1:

    1. Ao clicar no botão "Iniciar", o jogador receberá 11 cartas.
    2. Se o jogador clicar em "Resposta", irá obter a Maior Subsequência Crescente.
    
    Pressione o botão abaixo para voltar à janela anterior.
    """

    instructions_label = tk.Label(instructions_window, text=instructions_text, justify=tk.LEFT, font=text_font)
    instructions_label.pack()

    menu_button = tk.Button(instructions_window, text="Menu Inicial", font=("Arial", 14, "bold") , command=lambda: [instructions_window.destroy(), window.deiconify()])
    menu_button.pack(pady=20)

def open_player_1_window():
    global player_1_window
    window.withdraw()

    player_1_window = tk.Toplevel(window)
    player_1_window.title("Modo Player 1")
    player_1_window.geometry("700x550")

    instruction_label = tk.Label(player_1_window, text="Para receber as suas cartas, clique no botão abaixo:", font=("Arial", 14))
    instruction_label.pack(pady=10)

    start_button = tk.Button(player_1_window, text="Iniciar", font=("Arial", 14, "bold"), command=lambda: start_game("Player 1"))
    start_button.pack(pady=1)

def start_game_player_1():
    suits = ["Paus", "Espadas", "Copas", "Ouros"]
    ranks = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]
    deck = [(rank, suit) for suit in suits for rank in ranks]

    random.shuffle(deck)
    player_hand = deck[:11]

    # Criar um frame para exibir as cartas recebidas
    frame_received = tk.Frame(player_1_window)
    frame_received.pack()

    # Exibir as cartas recebidas em duas linhas
    for i in range(6):
        card = player_hand[i]
        image_path = os.path.join("assets", f"{card[0]}_{card[1]}.png")
        image = Image.open(image_path)
        image = image.resize((100, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(frame_received, image=photo)
        label.image = photo
        label.grid(row=0, column=i, padx=5, pady=10) 

    for i in range(5):
        card = player_hand[i+6]
        image_path = os.path.join("assets", f"{card[0]}_{card[1]}.png")
        image = Image.open(image_path)
        image = image.resize((100, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(frame_received, image=photo)
        label.image = photo
        label.grid(row=1, column=i, padx=5, pady=5)

    print("Cartas do jogador 1:")
    for card in player_hand:
        print(card)

    instruction_label = tk.Label(player_1_window, text="Para visualizar a Maior Subsequência Crescente, clique no botão abaixo:", font=("Arial", 14))
    instruction_label.pack(pady=10)

    # Botão para encontrar a maior subsequência crescente
    find_subsequence_button = tk.Button(player_1_window, text="Resposta", font=("Arial", 14, "bold"), command=lambda: find_and_display_subsequence(player_hand))
    find_subsequence_button.pack(pady=1)


def find_and_display_subsequence(cards):
    # Ordenar as cartas por naipe e classificá-las em ordem crescente
    cards.sort(key=lambda card: (card[1], card[0]))

    # Inicializar uma matriz para armazenar os comprimentos das subsequências
    lengths = [1] * len(cards)

    # Inicializar uma matriz para armazenar os índices dos predecessores
    predecessors = [-1] * len(cards)

    # Encontrar a maior subsequência crescente
    for i in range(1, len(cards)):
        for j in range(i):
            if cards[i][0] > cards[j][0] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                predecessors[i] = j

    # Encontrar o comprimento máximo da subsequência
    max_length = max(lengths)

    # Encontrar o índice do último elemento da subsequência máxima
    max_index = lengths.index(max_length)

    # Reconstruir a subsequência máxima
    subsequence = []
    while max_index != -1:
        subsequence.append(cards[max_index])
        max_index = predecessors[max_index]
    subsequence.reverse()

    display_subsequence(subsequence)

def play_again():
    subsequence_window.destroy()
    player_1_window.deiconify()

# Limpar a janela "Modo Player 1"
    for widget in player_1_window.winfo_children():
        widget.destroy()

    instruction_label = tk.Label(player_1_window, text="Para receber as suas cartas, clique no botão abaixo:", font=("Arial", 14))
    instruction_label.pack(pady=10)

    start_button = tk.Button(player_1_window, text="Iniciar", font=("Arial", 14, "bold"), command=lambda: start_game("Player 1"))
    start_button.pack(pady=1)

def display_subsequence(subsequence):
    global subsequence_window

    if subsequence_window is not None:
        subsequence_window.destroy()

    subsequence_window = tk.Toplevel(player_1_window)
    subsequence_window.title("Maior Subsequência Crescente")
    subsequence_window.geometry("700x400")

    # Criar um frame para exibir as cartas da subsequência
    frame_subsequence = tk.Frame(subsequence_window)
    frame_subsequence.pack()

    # Exibir as cartas da subsequência em uma grade de 5 colunas por 2 linhas
    for i, card in enumerate(subsequence):
        image_path = os.path.join("assets", f"{card[0]}_{card[1]}.png")
        image = Image.open(image_path)
        image = image.resize((100, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(frame_subsequence, image=photo)
        label.image = photo
        label.grid(row=i // 5, column=i % 5, padx=5, pady=5)

    play_again_button = tk.Button(subsequence_window, text="Jogar novamente", font=("Arial", 14, "bold"), command=play_again)
    play_again_button.pack(pady=20)

def resize_bg(event):
    global bg_image, bg_photo, bg_photo_with_title, canvas

    new_width = event.width
    new_height = event.height

    bg_image_resized = bg_image.resize((new_width, new_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image_resized)
    canvas.config(width=new_width, height=new_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

window = tk.Tk()
window.title("Sequência Suprema")
window.geometry("800x600")

bg_image = Image.open("assets/inicio.png")
bg_photo = ImageTk.PhotoImage(bg_image)

image_with_title = Image.new("RGB", (bg_image.width, bg_image.height + 50), color=(255, 255, 255))
image_with_title.paste(bg_image, (0, 50))
draw = ImageDraw.Draw(image_with_title)
font = ImageFont.truetype("arial.ttf", 24)
text_bbox = draw.textbbox((0, 0), "Sequência Suprema", font=font)
text_position = ((bg_image.width - text_bbox[2]) // 2, 10)
draw.text(text_position, "Sequência Suprema", font=font, fill=(0, 0, 0))

bg_photo_with_title = ImageTk.PhotoImage(image_with_title)
canvas = tk.Canvas(window, width=300, height=200)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo_with_title)

label_font = tkfont.Font(size=26, weight='bold')
label_text_1 = tk.Label(window, text="SEQUÊNCIA SUPREMA", font=label_font, bg="white")
label_text_1.place(x=400, y=50, anchor=tk.CENTER)

label_font = tkfont.Font(size=26, weight='bold')
label_text_2 = tk.Label(window, text="Modo de Jogo:", font=label_font, bg="white")
label_text_2.place(x=225, y=450, anchor=tk.CENTER)

button_font = tkfont.Font(size=14, weight='bold')

player_1_button = tk.Button(window, text="Player 1", command=open_player_1_window, font=button_font)
player_1_button.place(x=200, y=500, anchor=tk.CENTER)

instructions_button = tk.Button(window, text="Instruções", command=show_instructions, font=button_font)
instructions_button.place(x=200, y=550, anchor=tk.CENTER)

window.bind("<Configure>", resize_bg)

window.mainloop()