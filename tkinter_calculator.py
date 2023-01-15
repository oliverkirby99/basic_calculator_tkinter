from tkinter import *
import math

root = Tk()
# Set the Window Title
root.title("Calculator")

# Create input field, assign it to root and give it some shape/size
textinput = Entry(root, width=60, borderwidth=10)
# Move the input field to row 0, column 0 and tell it that there will be 3 columns. Padding to space it out a bit.
textinput.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_add(num):
    current_input = textinput.get()  # Get current textbox value
    textinput.delete(0, END)  # Clear the textbox
    textinput.insert(0, str(current_input) + str(num))  # Concatonate the values into the textbox


# Clear the textbox
def button_clear():
    textinput.delete(0, END)


def button_addition():
    first_num = textinput.get()
    global num_get
    global op
    op = "add"
    num_get = int(first_num)
    textinput.delete(0, END)  # Clear the textbox


def button_subtract():
    first_num = textinput.get()
    global num_get
    global op
    op = "sub"
    num_get = int(first_num)
    textinput.delete(0, END)  # Clear the textbox


def button_multiply():
    first_num = textinput.get()
    global num_get
    global op
    op = "mult"
    num_get = int(first_num)
    textinput.delete(0, END)  # Clear the textbox


def button_divide():
    first_num = textinput.get()
    global num_get
    global op
    op = "div"
    num_get = int(first_num)
    textinput.delete(0, END)  # Clear the textbox


# Can't multiply floats. Fix this.
def button_total():
    second_num = textinput.get()
    textinput.delete(0, END)  # Clear the textbox

    if op == "add":
        textinput.insert(0, num_get + int(second_num))
    elif op == "sub":
        textinput.insert(0, num_get - int(second_num))
    elif op == "mult":
        textinput.insert(0, num_get * int(second_num))
    elif op == "div":
        div_ans = num_get / int(second_num)
        if div_ans == int(div_ans):
            textinput.insert(0, math.floor(num_get / int(second_num)))
        else:
            textinput.insert(0, round(num_get / int(second_num), 2))


# Number buttons. Assign to Root. Text Value, Size/Shape, Function("lambda:" allows the function to have "()"),
# Background Colour
button_1 = Button(root, text="1", padx=40, pady=20, borderwidth=5, command=lambda: button_add(1), bg="#d1d9e3")
button_2 = Button(root, text="2", padx=40, pady=20, borderwidth=5, command=lambda: button_add(2), bg="#d1d9e3")
button_3 = Button(root, text="3", padx=40, pady=20, borderwidth=5, command=lambda: button_add(3), bg="#d1d9e3")
button_4 = Button(root, text="4", padx=40, pady=20, borderwidth=5, command=lambda: button_add(4), bg="#d1d9e3")
button_5 = Button(root, text="5", padx=40, pady=20, borderwidth=5, command=lambda: button_add(5), bg="#d1d9e3")
button_6 = Button(root, text="6", padx=40, pady=20, borderwidth=5, command=lambda: button_add(6), bg="#d1d9e3")
button_7 = Button(root, text="7", padx=40, pady=20, borderwidth=5, command=lambda: button_add(7), bg="#d1d9e3")
button_8 = Button(root, text="8", padx=40, pady=20, borderwidth=5, command=lambda: button_add(8), bg="#d1d9e3")
button_9 = Button(root, text="9", padx=40, pady=20, borderwidth=5, command=lambda: button_add(9), bg="#d1d9e3")
button_0 = Button(root, text="0", padx=40, pady=20, borderwidth=5, command=lambda: button_add(0), bg="#d1d9e3")
# Operator buttons.
button_plus = Button(root, text="+", padx=37, pady=20, borderwidth=5, command=button_addition, bg="#e3dad1")
button_minus = Button(root, text="-", padx=39, pady=20, borderwidth=5, command=button_subtract, bg="#e3dad1")
button_multi = Button(root, text="*", padx=39, pady=20, borderwidth=5, command=button_multiply, bg="#e3dad1")
button_divi = Button(root, text="/", padx=39, pady=20, borderwidth=5, command=button_divide, bg="#e3dad1")
# Functional buttons.
button_equals = Button(root, text="=", padx=39, pady=20, borderwidth=5, command=button_total, bg="#e3dad1")
button_clear = Button(root, text="C", padx=39, pady=20, borderwidth=5, command=button_clear, bg="#e3dad1")

# Display number buttons.
# 1-3 Bottom Row
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
# 4-6 Middle Row
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
# 7-9 Top Row
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
# Bottom Bottom Row
button_0.grid(row=4, column=1)
button_equals.grid(row=4, column=0)
button_clear.grid(row=4, column=2)
# Symbols
button_plus.grid(row=1, column=3)  # Top Row
button_minus.grid(row=2, column=3)  # Mid Row
button_multi.grid(row=3, column=3)  # Bot Row
button_divi.grid(row=4, column=3)  # Bot Bot

# root.mainloop() is the function that opens the application window and keeps it updated.
root.mainloop()
