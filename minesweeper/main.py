import tkinter as tk
from tkinter import messagebox, simpledialog
from game_board.game_board import Board
from game_board.cell import Cell

class MinesweeperGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Minesweeper")
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.mines_label = tk.Label(self.top_frame, text="Mines: 0")
        self.mines_label.pack(side=tk.LEFT, padx=5, pady=5)

        self.new_game_button = tk.Button(self.top_frame, text="New Game", command=self.new_game)
        self.new_game_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

    def new_game(self):
        width = simpledialog.askinteger("Board Width", "Enter the board width:", initialvalue=8, minvalue=5, maxvalue=30)
        height = simpledialog.askinteger("Board Height", "Enter the board height:", initialvalue=8, minvalue=5, maxvalue=30)
        
        self.board = Board((width, height))
        self.buttons = []
        self.create_board_gui()
        self.mines_label.config(text=f"Mines: {len(self.board.mines)}")

    def create_board_gui(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        for i in range(self.board.x):
            button_row = []
            for j in range(self.board.y):
                button = tk.Button(self.board_frame, width=2, height=1)
                button.grid(row=i, column=j)
                button.bind('<Button-1>', lambda e, x=i, y=j: self.left_click(x, y))
                button.bind('<Button-3>', lambda e, x=i, y=j: self.right_click(x, y))
                button_row.append(button)
            self.buttons.append(button_row)

    def left_click(self, x, y):
        cell = self.board.board[x][y]
        if cell.is_mine:
            self.game_over()
        elif cell.neighbouring_mines > 0:
            self.reveal_cell(x, y)
        else:
            self.reveal_empty_cells(x, y)
        
        if self.check_win():
            messagebox.showinfo("Congratulations", "You won!")

    def right_click(self, x, y):
        button = self.buttons[x][y]
        if button['text'] == '🚩':
            button.config(text='')
        else:
            button.config(text='🚩')

    def reveal_cell(self, x, y):
        cell = self.board.board[x][y]
        button = self.buttons[x][y]
        cell.is_revealed = True
        if cell.is_mine:
            button.config(text='💣', bg='red')
        elif cell.neighbouring_mines > 0:
            button.config(text=str(cell.neighbouring_mines), relief=tk.SUNKEN)
        else:
            button.config(text='', relief=tk.SUNKEN)

    def reveal_empty_cells(self, x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if not (0 <= cx < self.board.x and 0 <= cy < self.board.y):
                continue
            cell = self.board.board[cx][cy]
            if cell.is_revealed:
                continue
            self.reveal_cell(cx, cy)
            if cell.neighbouring_mines == 0:
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    stack.append((cx + dx, cy + dy))

    def game_over(self):
        for x in range(self.board.x):
            for y in range(self.board.y):
                cell = self.board.board[x][y]
                if cell.is_mine:
                    self.buttons[x][y].config(text='💣', bg='red')
        messagebox.showinfo("Game Over", "You hit a mine!")

    def check_win(self):
        for x in range(self.board.x):
            for y in range(self.board.y):
                cell = self.board.board[x][y]
                if not cell.is_mine and not cell.is_revealed:
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    game = MinesweeperGUI(root)
    root.mainloop()