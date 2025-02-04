from BaseWindow import BaseWindow
import tkinter as tk

class UFOsWindow(BaseWindow):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        
        # setup transparency
        self.set_transparent()
        
        # list to store animated objects
        self.objects = []


    def add_object(self, x, y, sizeX, sizeY, color):
        """Add a simple object to the canvas."""
        if self.canvas:
            # create a new circular shape on canvas at given pos and size with given color
            obj = self.canvas.create_oval(x, y, sizeX, sizeY, fill = color, outline = "")
            
            # add created object to list of objects
            self.objects.append(obj)


    def animate(self, ms):
        """Move all objects slightly each set time"""
        for obj in self.objects:
            # update pos of the object
            self.canvas.move(obj, 1, 1)
        
        # schedule next animation frame after given delay (in milliseconds)
        self.root.after(ms, lambda: self.animate(ms))
