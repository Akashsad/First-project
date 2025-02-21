from tkinter import *

first_number = None
second_number = None
operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)
    expression_label.config(text=expression_label["text"] + str(digit))

def clear():
    global first_number, second_number, operator
    first_number = None
    second_number = None
    operator = None
    result_label.config(text='')
    expression_label.config(text='')

def get_operator(op):
    global first_number, operator
    if result_label['text']:  # Ensure there's input before storing first_number
        first_number = int(result_label['text'])
        operator = op
        result_label.config(text='')  # Clear result label for second number input
        expression_label.config(text=expression_label["text"] + f" {op} ")

def get_result():
    global first_number, second_number, operator

    if first_number is None or not result_label['text']:
        return  # Prevent errors if "=" is pressed before entering values

    second_number = int(result_label['text'])

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        if second_number == 0:
            result_label.config(text='Error')  # Handle division by zero
            return
        else:
            result = first_number / second_number

    result_label.config(text=str(result))
    expression_label.config(text=expression_label["text"] + f" = {result}")

def on_key_press(event):
    """Handles keyboard input."""
    key = event.char
    if key.isdigit():
        get_digit(key)
    elif key in ['+', '-', '*', '/']:
        get_operator(key)
    elif key == '=' or event.keysym == "Return":
        get_result()
    elif event.keysym == "BackSpace":
        current_text = result_label["text"]
        expression_text = expression_label["text"]
        if current_text:
            result_label.config(text=current_text[:-1])
        if expression_text:
            expression_label.config(text=expression_text[:-1])
    elif event.keysym == "Escape":
        clear()

root = Tk()
root.title('Calculator')
root.geometry('300x400')  # Default size
root.minsize(280, 380)  # Prevents excessive shrinking
root.configure(background='black')

# Labels to show the input expression and result
expression_label = Label(root, text='', bg='black', fg='white', anchor="e")
expression_label.grid(row=0, column=0, columnspan=4, pady=(20, 5), sticky='ew')
expression_label.config(font=('verdana', 18, 'bold'))

result_label = Label(root, text='', bg='black', fg='white', anchor="e")
result_label.grid(row=1, column=0, columnspan=4, pady=(5, 25), sticky='ew')
result_label.config(font=('verdana', 30, 'bold'))

# Create buttons with proper lambda function binding
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('/', 5, 3)
]

for text, row, col in buttons:
    def make_command(t=text):
        if t.isdigit():
            return lambda: get_digit(t)
        elif t == 'C':
            return clear
        elif t == '=':
            return get_result
        else:
            return lambda: get_operator(t)

    btn = Button(root, text=text, bg='#00a65a', fg='white', width=5, height=2, command=make_command())
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn.config(font=('verdana', 14))

# Make columns and rows expandable for resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Keyboard bindings
root.bind("<Key>", on_key_press)

root.mainloop()