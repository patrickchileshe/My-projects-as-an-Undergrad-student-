#Different method of making a calculator

import tkinter

button_values = [
    
    ['AC', '+/-', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '√', '=']
]

right_symbols = ["/", "*", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]


row_count = len(button_values) #5
column_count = len(button_values[0]) #4

colour_light_gray = "#D4D4D2"
colour_black = "#1C1C1C"
colour_dark_gray = "#505050"
colour_orange = "#ff9500"
colour_white = "#FFFFFF"

#window set up
window = tkinter.Tk() #create the window
window.title("Calculator")
window.resizable(False, False) #Like this the user can not resize the window

frame = tkinter.Frame(window) #placing the frame inside the frame
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=colour_black, foreground=colour_white, anchor= "e", width= column_count) 

label.grid(row=0, column=0, columnspan=column_count, sticky="we")
#the sticky stretches the colour either n= north s= south w= west e= east so in this case we

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), 
                                width=column_count-1, height=1,
                                command= lambda value=value: buttton_clicked(value))
        
        if value in top_symbols:
            button.config(foreground=colour_black, background=colour_light_gray)
        elif value in right_symbols:
            button.config(foreground=colour_white, background= colour_orange)
        else: button.config(foreground=colour_white, background= colour_black)
        button.grid(row=row+1, column=column)

frame.pack()


#A+B, A-B, A*B, A/B

A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A= "0"
    B= None
    operator= None
    

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def buttton_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B= label["text"]
                numA = float(A)
                numB = float(B)
                
                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "*":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "/":
                    label["text"] = remove_zero_decimal(numA / numB)
                
                clear_all()

        elif value in "+-*/": #500 +, *
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            
            operator = value
    
    elif value in top_symbols:
        if value == "AC":
            clear_all(value)
            label["text"]= "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"]= remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"]= remove_zero_decimal(result)
    else: #digits or.
        if value== ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value # replace 0
            else:
                label["text"] += value # append digit

#/centre window
window.update() #update window with the new size dimensions
window_width = window.winfo_width()
windw_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


window.mainloop()
