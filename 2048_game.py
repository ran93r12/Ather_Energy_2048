from tkinter import *
from tkinter import messagebox
import random


class GamePlay():
    Frame_Color = "#faf8ef"
    Board_Color = "#bbada0"
    ForeGround_Color = {0: "#d6cdc4", 2:"#464646", 4:"#464646", 8:"#ffffff", 16:"#ffffff", 32:"#ffffff", 64:"#ffffff", 128:"#ffffff", 256:"#ffffff", 512:"#ffffff", 1024:"#ffffff", 2048:"#ffffff", 4096:"#ffffff", 8192:"#ffffff", 16384:"#ffffff", 32768:"#ffffff", 65536:"#ffffff", 131072:"#ffffff"}
    BackGround_Color = {0: "#d6cdc4", 2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", 32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", 512:"#edc850", 1024:"#edc53f", 2048:"#edc22e", 4096:"#464646", 8192:"#3d3d3d", 16384:"#19191a", 32768:"#111111", 65536:"#09090a", 131072:"#000000"}

    def __init__(self):
        global score
        self.top_frame_colour = Frame_Color
        self.board_frame_colour = Board_Color
        self.foreground_colours = ForeGround_Color
        self.background_colours = BackGround_Color
        self.board_font = ("Courier", 15, "bold")
        self.game_font = ("Courier", 25, "bold")
        self.home_game_font = ("Courier", 35, "bold")
        self.score_font = ("Promesh", 10, "bold")
        self.window = tk.Tk()

    def winGame(self):
        title_label = tk.Label(master = self.window, bg ="#000000", fg = "#ff0051", text = str(highest) + " TILE CREATED", font = self.game_font)
        title_label.pack(fill = tk.BOTH, expand = True)
        title_label.after(750,title_label.destory)
        self.game_Over()

    def gameOver(self):
        self.window.after(50, self.remove_board_widgets)
        self.window.after(50, self.remove_game_widgets)
        game_over = tk.Label(master = self.window, text = "GAME OVER!!", font = self.home_game_font, fg = self.board_frame_colour, bg = self.top_frame_colour, width = 20, height = 5)
        game_over.pack()
        game_over.after(2000, game_over.destroy)
        self.window.after(2100, self.dashboard)

    def dashboard(self):
        self.nav_widgets = []
        background_frame = tk.Frame(master = self.window, bg = self.top_frame_colour, width = 435, height = 580)
        background_frame.pack()

        game_label = tk.Label(master = background_frame, text = "2048", font = self.home_game_font, fg = self.board_frame_colour, bg = self.top_frame_colour, width = 10, height = 2)
        game_label.pack()

        instruction_label = tk.Label(master = background_frame, text = "Use arrow keys or WASD to move tiles\nUse U to undo your last move", fg = self.board_frame_colour, bg = self.top_frame_colour, font = self.board_font)
        instruction_label.pack()

        new_game_button = tk.Button(master = background_frame, text = "New Game", width = 10, height = 3, bg = self.board_frame_colour, fg = "#ffffff", command = self.home_start_game)
        new_game_button.pack()

        exit_button = tk.Button(master = background_frame, text = "Exit", width = 10, height = 3, bg = self.board_frame_colour, fg = "#ffffff", command = self.close_window)
        exit_button.pack()

        self.nav_widgets.append(background_frame)
        self.nav_widgets.append(game_label)
        self.nav_widgets.append(instruction_label)
        self.nav_widgets.append(new_game_button)
        self.nav_widgets.append(exit_button)
        self.window.mainloop()

    def remove_game_widgets(self):
        for widgets in self.nav_widgets:
            widgets.destroy()

    def starGame(self):
        self.remove_game_widgets()
        self.start_game()