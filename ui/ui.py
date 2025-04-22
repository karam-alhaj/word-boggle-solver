import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)


def display_matrix(matrix:list):
    canvas.pack()
    cell_size = 50
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")
            canvas.create_text(x1 + cell_size / 2, y1 + cell_size / 2, text=char, font=("Arial", 16))


def draw_ball_at(row, col,color):
    cell_size = 50
    x = col * cell_size + cell_size / 2
    y = row * cell_size + cell_size / 2
    radius = 3
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline=color)


def draw_line_between_cells(start, end,color):
    cell_size = 50
    start_x = (start[1] * cell_size + cell_size / 2)
    start_y = (start[0] * cell_size + cell_size / 2) 
    end_x = (end[1] * cell_size + cell_size / 2)
    end_y = (end[0] * cell_size + cell_size / 2)
    canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=2)


def main():
    display_matrix([['a','b','c'],['d','f','g'],['h','g','k']])
    draw_line_between_cells((0, 0), (1, 1))
    
    root.mainloop()


if __name__ == '__main__':
    main()