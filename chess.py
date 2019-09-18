import tkinter as tk
from PIL import Image, ImageTk
import sys
import os


class BackgroundBoard(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self)
        self.master.title("Chess Python")
        self.background_image = Image.open(os.path.join(
            os.path.dirname(__file__)) + "/img/board.png")
        self.background_photo = ImageTk.PhotoImage(
            self.background_image)
        (backgroundWidth, backgroundHeight) = self.background_image.size
        self.canvas = tk.Canvas(self, width=backgroundWidth,
                                height=backgroundHeight)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo,
                                 anchor="nw")


class King:

    def __init__(self, color):
        self.color = color


class Queen:
    pass


class Bishop:
    pass


class Knight:
    pass


class Castle:
    pass


class Pawn:
    pass


root = tk.Tk()
root.geometry("720x720")
ui = BackgroundBoard(root)
ui.pack(side="top", fill="both", expand=True)
ui.mainloop()
