from UFOsWindow import UFOsWindow

class SandboxApp:
    def __init__(self):
        # create window
        self.UFOsWindow = UFOsWindow("WEEOOEEOOEEOOEEOO", 800, 600)

        # create UFOs
        self.UFOsWindow.add_object(20, 20, 80, 100, "RED")  # red circle
        self.UFOsWindow.add_object(180, 180, 80, 100, "BLUE")  # blue circle

        # animate
        self.UFOsWindow.animate(20)

    def run(self):
        self.UFOsWindow.run()
