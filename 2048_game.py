from tkinter import *
from tkinter import messagebox
import random


class GamePlay():
    def __init__(self):
        #colours
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

    def win_game(self):
        new_tile_label = tk.Label(master = self.window, bg = "#000000", fg = "#ff0051", text = str(highest) + " TILE CREATED", font = self.game_font)
        new_tile_label.pack(fill = tk.BOTH, expand = True)
        new_tile_label.after(750, new_tile_label.destroy)
        self.game_over()

    def game_over(self):
        self.window.after(50, self.remove_board_widgets)
        self.window.after(50, self.remove_game_widgets)
        game_over_label = tk.Label(master = self.window, text = "GAME OVER!!", font = self.home_game_font, fg = self.board_frame_colour, bg = self.top_frame_colour, width = 20, height = 5)
        game_over_label.pack()
        game_over_label.after(2000, game_over_label.destroy)
        self.window.after(2100, self.dashboard)

    def dashboard(self):
        self.nav_widgets = []
        background_frame = tk.Frame(master = self.window, bg = self.top_frame_colour, width = 435, height = 580)
        background_frame.pack()

        game_label = tk.Label(master = background_frame, text = "2048", font = self.home_game_font, fg = self.board_frame_colour, bg = self.top_frame_colour, width = 10, height = 2)
        game_label.pack()

        instruction_label = tk.Label(master = background_frame, text = "Use arrow keys or WASD to move tiles\nUse U to undo your last move", fg = self.board_frame_colour, bg = self.top_frame_colour, font = self.board_font)
        instruction_label.pack()

        new_game_button = tk.Button(master = background_frame, text = "New Game", width = 10, height = 3, bg = self.board_frame_colour, fg = "#ffffff", command = self.dashboard_start)
        new_game_button.pack()

        exit_button = tk.Button(master = background_frame, text = "Exit", width = 10, height = 3, bg = self.board_frame_colour, fg = "#ffffff", command = self.close_window)
        exit_button.pack()

        self.nav_widgets.append(background_frame)
        self.nav_widgets.append(game_label)
        self.nav_widgets.append(instruction_label)
        self.nav_widgets.append(new_game_button)
        self.nav_widgets.append(exit_button)
        self.window.mainloop()

    def remove_nav_widgets(self):
        for i in self.nav_widgets:
            i.destroy()

    def dashboard_start(self):
        self.remove_nav_widgets()
        self.start_game()

    def remove_game_widgets(self):
        self.top_frame.destroy()
        self.game_label.destroy()
        self.new_game_button.destroy()
        self.exit_button.destroy()
        self.score_label.destroy()

    def remove_board_widgets(self):
        for i in self.widgets:
            for j in i:
                j[0].destroy()
                j[1].destroy()
        self.board_frame.destroy()

    def end_start_game(self):
        self.remove_board_widgets()
        self.remove_game_widgets()
        self.start_game()

    def start_game(self):
        self.initialize_board()
        self.top_frame = tk.Frame(master = self.window, bg = self.top_frame_colour)
        self.top_frame.pack(fill = tk.BOTH, expand = True)

        self.game_label = tk.Label(master = self.top_frame, text = "2048", font = self.game_font, fg = self.board_frame_colour, bg = self.top_frame_colour, width = 4, height = 3)
        self.game_label.grid(row = 0, column = 0, padx = 3, pady = 3)


        self.new_game_button = tk.Button(master = self.top_frame, text = "New Game", width = 9, height = 4, bg = self.board_frame_colour, fg = "#ffffff", command = self.end_start_game)
        self.new_game_button.grid(row = 0, column = 1, padx = 3, pady = 3)

        self.exit_button = tk.Button(master = self.top_frame, text = "Exit", width = 8, height = 4, bg = self.board_frame_colour, fg = "#ffffff", command = self.close_window)
        self.exit_button.grid(row = 0, column = 2, padx = 3, pady = 3)

        self.score_label = tk.Label(master = self.top_frame, text = "Score\n" + str(score), font = self.score_font, fg = "#ffffff", bg = self.board_frame_colour, width = 10, height = 3)
        self.score_label.grid(row = 0, column = 3, padx = 3, pady = 3)

        self.board_frame = tk.Frame(master = self.window, bg = self.board_frame_colour)
        self.board_frame.pack(fill = tk.BOTH, expand = True)

        self.create_gridboard()

        self.window.bind("<Key>", self.key_press)

    def close_window(self):
        exit(0)

    def create_gridboard(self):
        self.widgets = []
        for i in range(size):
            self.widgets.append([])
            for j in range(size):
                frame = tk.Frame(master = self.board_frame, borderwidth = 1, relief = tk.RAISED)
                frame.grid(row = i, column = j, padx = 3, pady = 3)
                label = tk.Label(master = frame, text = str(board[i][j]), font = self.board_font, fg = self.foreground_colours[board[i][j]], bg = self.background_colours[board[i][j]], width = 6, height = 3)
                label.pack(fill = tk.BOTH, expand = True)
                self.widgets[i].append((frame, label))

    def key_press(self, event):
        global highest
        g = highest
        key = event.keysym
        update_gridboard(self, key)
        self.update_gridboard()

    def update_gridboard(self):
        global board
        global next_board
        global score
        self.score_label.config(text = "Score\n" + str(score))
        for i in range(size):
            for j in range(size):
                self.widgets[i][j][1].config(text = str(board[i][j]), fg = self.foreground_colours[board[i][j]], bg = self.background_colours[board[i][j]])

    def initialize_board(self):
        global board
        global next_board
        global prev_board
        global highest
        global score
        board = []
        highest = 32
        score = 0
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append(0)
        spawn(size, board)
        spawn(size, board)
        next_board = copy.deepcopy(board)
        prev_board = copy.deepcopy(board)
        
    

if __name__ == "__main__":
    size = 4
    gamepanel = GamePlay()
    gamepanel.dashboard()