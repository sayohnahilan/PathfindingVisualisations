import tkinter as tk
from tkinter import ttk


# A controller window for other frames
class mainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(False, False)
        self.title("Visualizing Pathfinding Algorithms")

        # Variables to pass onto runner
        self.gameOptions = {
            "alg": tk.StringVar(),
            "startX": tk.IntVar(),
            "startY": tk.IntVar(),
            "endX": tk.IntVar(),
            "endY": tk.IntVar(),
        }

        controller = tk.Frame(self)
        controller.grid(column=0, row=0)
        controller.grid_rowconfigure(0, weight=1)
        controller.grid_columnconfigure(0, weight=1)

        # My frame
        self.frames = {}
        windowName = Options.__name__
        frame = Options(parent=controller, controller=self)
        self.frames[windowName] = frame
        frame.grid(column=0, row=0, sticky="nsew")

        # Immediately show options frame
        self.bringToFront("Options")

    # Bring myFrame to front
    def bringToFront(self, myFrame):
        frame = self.frames[myFrame]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")

    def endGame(self):
        self.destroy()


# Options the user can choose from
class Options(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        algLabel = ttk.Label(self, text="Select an algorithm: ")
        startLabel = ttk.Label(self, text="Select a start location, (x, y): ")
        endLabel = ttk.Label(self, text="Select a end location, (x, y): ")

        options = [i for i in range(40)]

        # Checkboxes for options
        algBox = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.gameOptions["alg"],
            values=("Breadth First Search", "Depth First Search"),
        )
        algBox.current(0)
        startXBox = ttk.Combobox(
            self,
            state="readonly",
            values=options,
            textvariable=self.controller.gameOptions["startX"],
            width="5",
        )
        startYBox = ttk.Combobox(
            self,
            state="readonly",
            values=options,
            textvariable=self.controller.gameOptions["startY"],
            width="5",
        )
        endXBox = ttk.Combobox(
            self,
            state="readonly",
            values=options,
            textvariable=self.controller.gameOptions["endX"],
            width="5",
        )
        endYBox = ttk.Combobox(
            self,
            state="readyonly",
            values=options,
            textvariable=self.controller.gameOptions["endY"],
            width="5",
        )

        confirmLabel = ttk.Label(
            self,
            text="Place walls with mouse and then press spacebar to begin visualizing.",
        )

        startButton = ttk.Button(
            self, text="Start", command=lambda: controller.endGame()
        )
        algLabel.grid(column=0, row=0, sticky=("nw"))
        startLabel.grid(column=0, row=1, sticky=("nw"))
        endLabel.grid(column=0, row=2, sticky=("nw"))
        algBox.grid(column=1, row=0)
        startXBox.grid(column=1, row=1)
        startYBox.grid(column=2, row=1)
        endXBox.grid(column=1, row=2)
        endYBox.grid(column=2, row=2)
        confirmLabel.grid(column=0, row=5, columnspan=2, rowspan=2)
        startButton.grid(column=1, row=7, pady=10)
