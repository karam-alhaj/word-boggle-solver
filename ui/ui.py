import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)


def display_matrix(matrix:list):
    '''
        Display a matrix in a Tkinter canvas.

        Parameters:
            matrix: list: The input matrix to be displayed.

        Returns:
            None
    '''
    canvas.pack()
    cell_size = 50
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")
            canvas.create_text(x1 + cell_size / 2, y1 + cell_size / 2, text=char, font=("Arial", 16))


def draw_ball_at(row, col,color='red'):# used instead of an arrow because it's easier to draw
    '''
        draws a ball at the given row and column in the Tkinter canvas.

        Parameters:
            row: int: The row index of the cell where the ball will be drawn.
            col: int: The column index of the cell where the ball will be drawn.
            color: str: The color of the ball.
        Returns:
            None
        Example:
            >>> draw_ball_at(1, 2, 'red')
            Draws a red ball at the cell (1, 2) in the Tkinter canvas.
    '''
    cell_size = 50
    x = col * cell_size + cell_size / 2
    y = row * cell_size + cell_size / 2
    radius = 3
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline=color)


def draw_line_between_cells(start, end,color='blue'):# used to connect the letters
    '''
        draws a line between two cells in the Tkinter canvas.

        Parameters:
            start: tuple: The starting cell coordinates (row, column).
            end: tuple: The ending cell coordinates (row, column).
            color: str: The color of the line.
        Returns:
            None
        Example:
            >>> draw_line_between_cells((0, 0), (1, 1), 'blue')
            Draws a blue line between the cells (0, 0) and (1, 1) in the Tkinter canvas.

    '''
    cell_size = 50
    start_x = (start[1] * cell_size + cell_size / 2)
    start_y = (start[0] * cell_size + cell_size / 2) 
    end_x = (end[1] * cell_size + cell_size / 2)
    end_y = (end[0] * cell_size + cell_size / 2)
    canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=2)


def main():# only for testing

    display_matrix([['a','b','c'],['d','f','g'],['h','g','k']])
    draw_line_between_cells((0, 0), (1, 1))
    root.mainloop()


if __name__ == '__main__':
    main()