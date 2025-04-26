import tkinter as tk
from tkinter import simpledialog

# Theme constants
BG_COLOR = "#2e2e2e" # dark background color
CELL_BG_COLOR_A = "#3e3e4e" # light cell background color
CELL_BG_COLOR_B = "#4e4e5e" # dark cell background color
GRID_LINE_COLOR = "#5e5e6e" # grid line color
TEXT_COLOR = "#e0e0e0" # text color
BALL_COLOR = "#ffa500"   # default ball color
LINE_COLOR = "#1e90ff"   # default line color

CELL_SIZE = 50
BALL_RADIUS = 5

# Initialize main window
root = tk.Tk() 
root.title("Word Search UI")
root.configure(bg=BG_COLOR)

# Initialize canvas
canvas = tk.Canvas(
    root,
    width=400,
    height=400,
    bg=BG_COLOR,
    highlightthickness=0
)
canvas.pack(padx=10, pady=10)


def display_matrix(matrix: list):
    """
    Display a matrix in a themed Tkinter canvas.
    """
    canvas.delete("all")  # clear previous drawings

    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            # Alternate cell background for checkerboard effect
            fill = CELL_BG_COLOR_A if (i + j) % 2 == 0 else CELL_BG_COLOR_B

            canvas.create_rectangle(
                x1, y1, x2, y2,
                outline=GRID_LINE_COLOR,
                fill=fill,
                width=1
            )
            canvas.create_text(
                x1 + CELL_SIZE / 2,
                y1 + CELL_SIZE / 2,
                text=char,
                fill=TEXT_COLOR,
                font=("Helvetica", 18, "bold")
            )


def draw_ball_at(row, col, color=BALL_COLOR):
    """
    Draws a ball at the given row and column in the themed canvas.
    """
    x = col * CELL_SIZE + CELL_SIZE / 2
    y = row * CELL_SIZE + CELL_SIZE / 2
    r = BALL_RADIUS
    canvas.create_oval(
        x - r, y - r, x + r, y + r,
        fill=color,
        outline=""
    )


def draw_line_between_cells(start, end, color=LINE_COLOR):
    """
    Draws a smooth line between two cells in the themed canvas.
    """
    x1 = start[1] * CELL_SIZE + CELL_SIZE / 2
    y1 = start[0] * CELL_SIZE + CELL_SIZE / 2
    x2 = end[1] * CELL_SIZE + CELL_SIZE / 2
    y2 = end[0] * CELL_SIZE + CELL_SIZE / 2
    canvas.create_line(
        x1, y1, x2, y2,
        fill=color,
        width=3,
        capstyle=tk.ROUND,
        joinstyle=tk.ROUND
    )


def main():
    # Hide window while prompting
    root.withdraw()
    rows = simpledialog.askinteger("Grid Size", "Enter number of rows:", minvalue=1, parent=root)
    cols = simpledialog.askinteger("Grid Size", "Enter number of columns:", minvalue=1, parent=root)
    if rows is None or cols is None:
        root.destroy()
        return

    # Build matrix through user input
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            letter = simpledialog.askstring(
                "Input Letter",
                f"Enter letter at (row {i+1}, col {j+1}):",
                parent=root
            )
            row.append(letter[0] if letter else " ")
        matrix.append(row)

    # Show window and display
    root.deiconify()
    display_matrix(matrix)
    draw_line_between_cells((0, 0), (2, 2))
    draw_ball_at(2, 2)
    root.mainloop()


if __name__ == '__main__':
    main()
    