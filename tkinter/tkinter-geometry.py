try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World!")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello World!")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', fill=tkinter.Y, expand=True)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='left', fill=tkinter.X, expand=True)
# canvas.pack(side='top', fill=tkinter.X)
# canvas.pack(side='top', fill=tkinter.BOTH)

canvas.pack(side='left', anchor='n')
canvas.pack(side='right', anchor='n')

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()
