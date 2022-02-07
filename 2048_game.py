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