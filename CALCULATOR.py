
# #complete calculator
from tkinter import *

root = Tk()
root.title("MY CALCULATOR")
root.maxsize(400, 500)  # for calculator size(width, height)

def btnClick(number):
    global val
    val = val + str(number)
    data.set(val)
    
def btnClear():
    global val
    val = ""
    data.set("")
    
def btnEqual():
    global val
    try:
        # Evaluate the expression and update the display with the result
        result = str(eval(val))
    except ZeroDivisionError:
        # Handle division by zero
        result = "Error"
    except Exception as e:
        # Handle any other exceptions
        result = "Error"
    data.set(result)

val = ""
data = StringVar()

display = Entry(root, textvariable=data, bd=29, justify="left", bg="powder blue", font=("Arial", 20))
display.grid(row=0, columnspan=4)

# Define buttons with their text, positions, and command functions
buttons = [
    ("7 ☻", 1, 0, lambda: btnClick(7)),
    ("8 ☺", 1, 1, lambda: btnClick(8)),
    ("9 ♦", 1, 2, lambda: btnClick(9)),
    ("+", 1, 3, lambda: btnClick("+")),
    ("4 ♣", 2, 0, lambda: btnClick(4)),
    ("5 ♀", 2, 1, lambda: btnClick(5)),
    ("6 ↓", 2, 2, lambda: btnClick(6)),
    ("-", 2, 3, lambda: btnClick("-")),
    ("1 ♪", 3, 0, lambda: btnClick(1)),
    ("2 ♫", 3, 1, lambda: btnClick(2)),
    ("3 ☼", 3, 2, lambda: btnClick(3)),
    ("x", 3, 3, lambda: btnClick("*")),
    ("CLEAR♥", 4, 0, btnClear),
    ("0", 4, 1, lambda: btnClick(0)),
    (".", 4, 2, lambda: btnClick(".")),
    ("÷", 4, 3, lambda: btnClick("/")),
    ("=", 5, 0, btnEqual)
]

# Create and place buttons in the grid
for (text, row, col, command) in buttons:
    Button(root, text=text, font=("Arial", 12, "bold"), bd=12, height=2, width=6, bg="cyan",
           command=command, activebackground="yellow", activeforeground="red").grid(row=row, column=col)

# Adjust the "=" button to span across the bottom row
Button(root, text="=", font=("Arial", 12, "bold"), bd=12, height=2, width=36, bg="green",
       command=btnEqual, activebackground="cyan", activeforeground="red").grid(row=5, columnspan=4)

root.mainloop()


