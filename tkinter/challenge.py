# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter

mainWindow = tkinter.Tk()
mainWindow.geometry("240x320")
mainWindow.title("Calculator")
mainWindow['padx'] = 8
mainWindow.minsize(width=180, height=240)

buttons = (
    {
        "name": "C",
        "row": 1,
        "column": 0,
        "columnspan": 1
    },
    {
        "name": "CE",
        "row": 1,
        "column": 1,
        "columnspan": 1
    },
    {
        "name": "7",
        "row": 2,
        "column": 0,
        "columnspan": 1
    },
    {
        "name": "8",
        "row": 2,
        "column": 1,
        "columnspan": 1
    },
    {
        "name": "9",
        "row": 2,
        "column": 2,
        "columnspan": 1
    },
    {
        "name": "+",
        "row": 2,
        "column": 3,
        "columnspan": 1
    },
    {
        "name": "4",
        "row": 3,
        "column": 0,
        "columnspan": 1
    },
    {
        "name": "5",
        "row": 3,
        "column": 1,
        "columnspan": 1
    },
    {
        "name": "6",
        "row": 3,
        "column": 2,
        "columnspan": 1
    },
    {
        "name": "-",
        "row": 3,
        "column": 3,
        "columnspan": 1
    },
    {
        "name": "1",
        "row": 4,
        "column": 0,
        "columnspan": 1
    },
    {
        "name": "2",
        "row": 4,
        "column": 1,
        "columnspan": 1
    },
    {
        "name": "3",
        "row": 4,
        "column": 2,
        "columnspan": 1
    },
    {
        "name": "*",
        "row": 4,
        "column": 3,
        "columnspan": 1
    },
    {
        "name": "0",
        "row": 5,
        "column": 0,
        "columnspan": 1
    },
    {
        "name": "=",
        "row": 5,
        "column": 1,
        "columnspan": 2
    },
    {
        "name": "/",
        "row": 5,
        "column": 3,
        "columnspan": 1
    }
)

# Widget to display a result
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='sw', columnspan=4)

# Button frame
buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=1, column=0, columnspan=4, sticky='sw', pady=2)

# Buttons
for button in buttons:
    tkinter.Button(buttonFrame, text=button["name"]).grid(row=button["row"], column=button["column"], columnspan=button["columnspan"], sticky="nesw", ipadx=5, ipady=5)

mainWindow.mainloop()
