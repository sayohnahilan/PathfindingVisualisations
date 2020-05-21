import tkinter as tk
from tkinter import ttk
import sys

# A controller window for other frames
class mainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(False, False)
        self.title("Visualizing Pathfinding Algorithms")

        # Variables to pass onto runner
        self.gameOptions = {
            "size": tk.IntVar(),
            "fps": tk.IntVar(),
            "maze": tk.StringVar(),
            "alg": tk.StringVar(),
            "startX": tk.IntVar(),
            "startY": tk.IntVar(),
            "endX": tk.IntVar(),
            "endY": tk.IntVar(),
        }

        # Centers the tkinter window
        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry("+%d+%d" % (x, y))

        controller = tk.Frame(self)
        controller.grid(column=0, row=0)
        controller.grid_rowconfigure(0, weight=1)
        controller.grid_columnconfigure(0, weight=1)

        # My frame
        self.frames = {}
        for fr in (Size, Options):
            windowName = fr.__name__
            frame = fr(parent=controller, controller=self)
            self.frames[windowName] = frame
            frame.grid(column=0, row=0, sticky="nsew")

        # Immediately show options frame
        self.bringToFront("Size")

    # Bring myFrame to front
    def bringToFront(self, myFrame):
        frame = self.frames[myFrame]
        frame.tkraise()
        frame.event_generate("<<BringToFront>>")

    def endGame(self):
        self.destroy()

# initial window with the size box
class Size(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        sizeValues = [i for i in range(10, 41)]
        sizeLabel = ttk.Label(self, text="Select a size for the grid, (x, y): ")
        sizeBox = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.gameOptions["size"],
            values=sizeValues,
        )
        sizeBox.current(len(sizeValues) - 1)
        speedLabel = ttk.Label(self, text="Select a speed: ")
        speedBox = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.gameOptions["fps"],
            values=[30, 60, 120, 240, 540],
        )
        speedBox.current(1)
        mazeLabel = ttk.Label(self, text="Select a maze: ")
        mazeBox = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.gameOptions["maze"],
            values=["No Maze", "Random Maze"]
        )
        mazeBox.current(0)
        nextBtn = ttk.Button(
            self, text="Next", command=lambda: controller.bringToFront("Options")
        )
        quitBtn = ttk.Button(
            self, text="Quit", command=lambda: sys.exit()
        )
        sizeLabel.grid(column=0, row=0, sticky=("nw"))
        speedLabel.grid(column=0, row=1, sticky=("nw"))
        mazeLabel.grid(column=0, row=2, sticky=("nw"))
        sizeBox.grid(column=1, row=0)
        speedBox.grid(column=1, row=1)
        mazeBox.grid(column=1, row=2)
        quitBtn.grid(column=1, row=3, pady=10)
        nextBtn.grid(column=2, row=3, pady=10)

# Options the user can choose from
class Options(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<BringToFront>>", self.bringToFront)

        algLabel = ttk.Label(self, text="Select an algorithm: ")
        startLabel = ttk.Label(self, text="Select a start location, (x, y): ")
        endLabel = ttk.Label(self, text="Select a end location, (x, y): ")

        # Checkboxes for options
        algBox = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.gameOptions["alg"],
            values=("Best First Search", "Dijkstra's Algorithm", "A Star Search", "Breadth First Search", "Depth First Search"),
        )
        algBox.current(0)
        self.startXBox = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.gameOptions["startX"],
            width="5",
        )
        self.startYBox = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.gameOptions["startY"],
            width="5",
        )
        self.endXBox = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.gameOptions["endX"],
            width="5",
        )
        self.endYBox = ttk.Combobox(
            self,
            state="readyonly",
            textvariable=self.controller.gameOptions["endY"],
            width="5",
        )
        confirmLabel = ttk.Label(
            self,
            text="Place walls with mouse left.\nRemove walls with mouse right.\nPress spacebar to begin visualizing.",
        )

        backButton = ttk.Button(
            self, text="Back", command=lambda: controller.bringToFront("Size")
        )
        startButton = ttk.Button(
            self, text="Start", command=lambda: controller.endGame()
        )
        quitBtn = ttk.Button(
            self, text="Quit", command=lambda: sys.exit()
        )

        algLabel.grid(column=0, row=0, sticky=("nw"))
        startLabel.grid(column=0, row=1, sticky=("nw"))
        endLabel.grid(column=0, row=2, sticky=("nw"))
        algBox.grid(column=1, row=0)
        self.startXBox.grid(column=1, row=1)
        self.startYBox.grid(column=2, row=1)
        self.endXBox.grid(column=1, row=2)
        self.endYBox.grid(column=2, row=2)
        confirmLabel.grid(column=0, row=5)
        backButton.grid(column=1, row=7)
        startButton.grid(column=2, row=7)
        quitBtn.grid(column=0, row=7)

    def bringToFront(self, event):
        size = self.controller.gameOptions["size"].get()
        dim = [i for i in range(size)]
        self.startXBox["values"] = dim
        self.startYBox["values"] = dim
        self.endXBox["values"] = dim
        self.endYBox["values"] = dim
        self.endXBox.current(len(dim) - 1)
        self.endYBox.current(len(dim) - 1)