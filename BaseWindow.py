import tkinter as tk

# class to handle basic window attributes and fuctions
class BaseWindow:
    def __init__(self, title, width, height):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.configure(bg="white")
        self.root.attributes("-topmost", True)

        # init canvas
        self.canvas = None

    
    # setup transparent window
    def set_transparent(self):
        # set transparency color
        self.root.attributes("-transparentcolor", "white")
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)


    def run(self):
        self.root.mainloop()
