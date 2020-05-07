from screen import *

# run options window
app = mainWindow()
app.mainloop()

row = (800, 40)
col = (800, 40)

# pull data from options window
startX = app.gameOptions["startX"].get()
startY = app.gameOptions["startY"].get()
endX = app.gameOptions["endX"].get()
endY = app.gameOptions["endY"].get()

print("Sayohn", startX, startY, endX, endY)