from tkinter import *  # Importing the Tkinter library for GUI development

# Global variables to store operator and first number
CurrentOperator = ""  # Stores the selected mathematical operator
OldNum = 0  # Stores the first number before the operator is pressed

# Function to center the application window on the screen
def center_window(window):
    window.update_idletasks()  # Ensures correct dimensions before centering
    width = window.winfo_width()  # Get window width
    height = window.winfo_height()  # Get window height
    screen_width = window.winfo_screenwidth()  # Get screen width
    screen_height = window.winfo_screenheight()  # Get screen height
    x = (screen_width - width) // 2  # Calculate X position for centering
    y = (screen_height - height) // 2  # Calculate Y position for centering
    window.geometry(f"{width}x{height}+{x}+{y}")  # Set new window position

# Function to handle number button clicks
def numpress(num):
    current = screen["text"]  # Get the current text from the screen label
    if CurrentOperator == "":  # If no operator is selected, append to the first number
        screen.config(text=current + str(num))
    else:  # If an operator is selected, append to the second number
        screen.config(text=current + str(num))

# Function to clear the screen
def clear():
    screen.config(text="")  # Reset screen text

# Function to handle operator button clicks
def operation(op):
    global CurrentOperator, OldNum  # Access global variables
    OldNum = float(screen["text"].strip())  # Convert and store the first number
    CurrentOperator = op  # Store the selected operator
    screen.config(text="")  # Clear screen to prepare for second number input

# Function to calculate and display the result
def calculate():
    global OldNum, CurrentOperator  # Access global variables
    NewNum = float(screen["text"].strip())  # Retrieve the second number from the screen

    # Perform the selected operation
    if CurrentOperator == '+':
        result = OldNum + NewNum
    elif CurrentOperator == '-':
        result = OldNum - NewNum
    elif CurrentOperator == '*':
        result = OldNum * NewNum
    elif CurrentOperator == '/':
        result = OldNum / NewNum if NewNum != 0 else "error"  # Handle division by zero

    screen.config(text=str(result))  # Display the result on the screen
    OldNum = 0  # Reset first number
    CurrentOperator = ""  # Reset operator

# Create the main application window
app = Tk()
app.geometry('320x400')  # Set window size
app.title('Calculator')  # Set window title
center_window(app)  # Center the window on the screen

# Display screen (Label widget to show numbers and results)
screen = Label(text=' ', width=22, height=5, background='black', foreground='white',
               font=('Times New Roman', 18, 'bold'))
screen.grid(row=0, column=0, columnspan=4)  # Position it at the top

# Clear button
cl = Button(app, text='clear', width=45, command=clear)
cl.grid(row=1, column=0, columnspan=4)

# Number buttons (0-9)
_9 = Button(app, text=9, width=10, height=3, command=lambda: numpress(9))
_9.grid(row=2, column=2)

_8 = Button(app, text=8, width=10, height=3, command=lambda: numpress(8))
_8.grid(row=2, column=1)

_7 = Button(app, text=7, width=10, height=3, command=lambda: numpress(7))
_7.grid(row=2, column=0)

_6 = Button(app, text=6, width=10, height=3, command=lambda: numpress(6))
_6.grid(row=3, column=2)

_5 = Button(app, text=5, width=10, height=3, command=lambda: numpress(5))
_5.grid(row=3, column=1)

_4 = Button(app, text=4, width=10, height=3, command=lambda: numpress(4))
_4.grid(row=3, column=0)

_3 = Button(app, text=3, width=10, height=3, command=lambda: numpress(3))
_3.grid(row=4, column=2)

_2 = Button(app, text=2, width=10, height=3, command=lambda: numpress(2))
_2.grid(row=4, column=1)

_1 = Button(app, text=1, width=10, height=3, command=lambda: numpress(1))
_1.grid(row=4, column=0)

_0 = Button(app, text=0, width=10, height=3, command=lambda: numpress(0))
_0.grid(row=5, column=1)

# Decimal point button
_dot = Button(app, text='.', width=10, height=3, command=lambda: numpress('.'))
_dot.grid(row=5, column=0)

# Operator buttons
div = Button(app, text='/', width=10, height=3, command=lambda: operation('/'))
div.grid(row=2, column=3)

multiply = Button(app, text='x', width=10, height=3, command=lambda: operation('*'))
multiply.grid(row=3, column=3)

add = Button(app, text='+', width=10, height=3, command=lambda: operation('+'))
add.grid(row=4, column=3)

sub = Button(app, text='-', width=10, height=3, command=lambda: operation('-'))
sub.grid(row=5, column=3)

# Equals button
equal = Button(app, text='=', width=10, height=3, command=calculate)
equal.grid(row=5, column=2)

# Run the application
app.mainloop()  # Keeps the application running until closed
