import tkinter as tk

# Canvas size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
DEFAULT_ERASER_SIZE = 20
DEFAULT_DRAW_COLOR = "black"

class EraserCanvas:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser & Draw Tool 🎨")
        
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        self.create_grid()
        
        self.eraser_size = DEFAULT_ERASER_SIZE
        self.eraser = self.canvas.create_rectangle(0, 0, self.eraser_size, self.eraser_size, fill="pink", outline="black")
        self.draw_mode = False  # False = Eraser mode, True = Draw mode
        self.undo_stack = []

        self.root.bind("<Motion>", self.use_tool)
        self.root.bind("<Up>", self.increase_tool_size)
        self.root.bind("<Down>", self.decrease_tool_size)
        self.root.bind("<c>", self.clear_canvas)
        self.root.bind("<d>", self.toggle_draw_mode)
        self.root.bind("<z>", self.undo_action)

    def create_grid(self):
        """Creates a grid of blue squares"""
        self.cells = []
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="white")
                self.cells.append(cell)

    def use_tool(self, event):
        """Moves the eraser or draws, based on the mode"""
        x, y = event.x, event.y
        self.canvas.moveto(self.eraser, x, y)
        
        overlapping = self.canvas.find_overlapping(x, y, x + self.eraser_size, y + self.eraser_size)
        for obj in overlapping:
            if obj in self.cells:
                if self.draw_mode:
                    self.canvas.itemconfig(obj, fill=DEFAULT_DRAW_COLOR)  # Draw
                else:
                    self.canvas.itemconfig(obj, fill="white")  # Erase
                self.undo_stack.append((obj, self.canvas.itemcget(obj, "fill")))

    def increase_tool_size(self, event):
        """Increases eraser/draw tool size"""
        self.eraser_size = min(self.eraser_size + 5, 60)  # Max 60 pixels
        self.canvas.coords(self.eraser, 0, 0, self.eraser_size, self.eraser_size)

    def decrease_tool_size(self, event):
        """Decreases eraser/draw tool size"""
        self.eraser_size = max(self.eraser_size - 5, 10)  # Min 10 pixels
        self.canvas.coords(self.eraser, 0, 0, self.eraser_size, self.eraser_size)

    def toggle_draw_mode(self, event):
        """Toggles between draw mode and erase mode"""
        self.draw_mode = not self.draw_mode
        mode = "Draw Mode ✏️" if self.draw_mode else "Eraser Mode 🧽"
        print(f"Switched to {mode}")

    def undo_action(self, event):
        """Undoes the last action"""
        if self.undo_stack:
            obj, prev_color = self.undo_stack.pop()
            self.canvas.itemconfig(obj, fill=prev_color)

    def clear_canvas(self, event):
        """Resets the grid to blue"""
        for cell in self.cells:
            self.canvas.itemconfig(cell, fill="blue")

        self.undo_stack.clear()

        print("Canvas cleared! 🎨")


def main():
    root = tk.Tk()
    app = EraserCanvas(root)
    root.mainloop()

if __name__ == '__main__':
    main()
