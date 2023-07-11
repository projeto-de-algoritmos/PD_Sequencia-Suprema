from PIL import Image, ImageTk, ImageDraw, ImageFont
import random
import tkinter as tk
import tkinter.font as tkfont
import os

player_1_window = None
player_2_window = None

def start_game(mode):
    if mode == "Player 1":
        start_game_player_1()
    elif mode == "Player 2":
        start_game_player_2()

def show_instructions():
    window.withdraw()

    instructions_window = tk.Toplevel()
    instructions_window.title("Instruções")
    instructions_window.geometry("800x350")

    title_font = tkfont.Font(family="Arial", size=18, weight="bold")
    text_font = tkfont.Font(family="Arial", size=12)

    title_label = tk.Label(instructions_window, text="Instruções do jogo Buraco Game", font=title_font)
    title_label.pack(pady=10)

    instructions_text = """
    Modalidade Player 1 e Player 2:

    1. Cada jogador receberá 11 cartas no início do jogo.
    2. Seu objetivo é formar sequências crescentes do mesmo naipe (canastas).
    3. Durante sua vez, você pode pegar uma carta da pilha de compra ou descartar uma carta.
    4. Some os pontos das cartas restantes na sua mão.
    5. O jogador que encontrar a maior subsequência crescente possível entre as cartas em sua mão, vence a partida.
    
    Pressione o botão abaixo para voltar à janela anterior.
    """

    instructions_label = tk.Label(instructions_window, text=instructions_text, justify=tk.LEFT, font=text_font)
    instructions_label.pack()

    menu_button = tk.Button(instructions_window, text="Menu Inicial", command=lambda: [instructions_window.destroy(), window.deiconify()])
    menu_button.pack(pady=20)

def open_player_1_window():
    global player_1_window
    window.withdraw()

    player_1_window = tk.Toplevel(window)
    player_1_window.title("Modo Player 1")
    player_1_window.geometry("400x300")

    start_button = tk.Button(player_1_window, text="Iniciar", command=lambda: start_game("Player 1"))
    start_button.pack()

def open_player_2_window():
    global player_2_window
    window.withdraw()

    player_2_window = tk.Toplevel(window)
    player_2_window.title("Modo Player 2")
    player_2_window.geometry("400x300")

    start_button = tk.Button(player_2_window, text="Iniciar", command=lambda: start_game("Player 2"))
    start_button.pack()

def start_game_player_1():
    suits = ["Paus", "Espadas", "Copas", "Ouros"]
    ranks = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]
    deck = [(rank, suit) for suit in suits for rank in ranks]

    random.shuffle(deck)
    player_hand = deck[:11]

    for i, card in enumerate(player_hand):
        image_path = os.path.join("assets", f"{card[0]}_{card[1]}.png")
        image = Image.open(image_path)
        image = image.resize((100, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(player_1_window, image=photo)
        label.image = photo
        label.pack(pady=5)

    print("Cartas do jogador 1:")
    for card in player_hand:
        print(card)

def start_game_player_2():
    suits = ["Paus", "Espadas", "Copas", "Ouros"]
    ranks = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]
    deck = [(rank, suit) for suit in suits for rank in ranks]

    random.shuffle(deck)
    player_hand = deck[:11]

    for i, card in enumerate(player_hand):
        image_path = os.path.join("assets", f"{card[0]}_{card[1]}.png")
        image = Image.open(image_path)
        image = image.resize((100, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(player_2_window, image=photo)
        label.image = photo
        label.pack(pady=5)

    print("Cartas do jogador 2:")
    for card in player_hand:
        print(card)

def resize_bg(event):
    global bg_image, bg_photo, bg_photo_with_title, canvas

    new_width = event.width
    new_height = event.height

    bg_image_resized = bg_image.resize((new_width, new_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image_resized)
    canvas.config(width=new_width, height=new_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

window = tk.Tk()
window.title("Buraco Game")
window.geometry("800x600")

bg_image = Image.open("assets/inicio.png")
bg_photo = ImageTk.PhotoImage(bg_image)

image_with_title = Image.new("RGB", (bg_image.width, bg_image.height + 50), color=(255, 255, 255))
image_with_title.paste(bg_image, (0, 50))
draw = ImageDraw.Draw(image_with_title)
font = ImageFont.truetype("arial.ttf", 24)
text_bbox = draw.textbbox((0, 0), "Buraco Game", font=font)
text_position = ((bg_image.width - text_bbox[2]) // 2, 10)
draw.text(text_position, "Buraco Game", font=font, fill=(0, 0, 0))

bg_photo_with_title = ImageTk.PhotoImage(image_with_title)
canvas = tk.Canvas(window, width=300, height=200)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo_with_title)

label_font = tkfont.Font(size=26, weight='bold')
label_text_1 = tk.Label(window, text="BURACO GAME", font=label_font, bg="white")
label_text_1.place(x=400, y=50, anchor=tk.CENTER)

label_font = tkfont.Font(size=26, weight='bold')
label_text_2 = tk.Label(window, text="Modo de Jogo:", font=label_font, bg="white")
label_text_2.place(x=225, y=450, anchor=tk.CENTER)

button_font = tkfont.Font(size=14, weight='bold')

player_1_button = tk.Button(window, text="Player 1", command=open_player_1_window, font=button_font)
player_1_button.place(x=200, y=500, anchor=tk.E)

player_2_button = tk.Button(window, text="Player 2", command=open_player_2_window, font=button_font)
player_2_button.place(x=210, y=500, anchor=tk.W)

instructions_button = tk.Button(window, text="Instruções", command=show_instructions, font=button_font)
instructions_button.place(x=200, y=550, anchor=tk.CENTER)

window.bind("<Configure>", resize_bg)

window.mainloop()
