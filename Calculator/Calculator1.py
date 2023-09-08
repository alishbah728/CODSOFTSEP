import tkinter as tk

WIDTH = 267
HEIGHT = 403
DISPLAY_FONT = ("Arial", 30)
BUTTON_FONT = ("Arial", 25)

window = tk.Tk()
window.title("Calculator")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(0, 0)


def calculate():
    try:
        result = eval(display.get())
        input_text.set(result)
    except:
        input_text.set("Wrong Input!")


# Display
input_text = tk.StringVar()
display = tk.Entry(window, font=DISPLAY_FONT, textvariable=input_text, bg="black", fg="white", width=12)
display.grid(row=0, columnspan=4, ipady=10)

# Buttons

# First row
tk.Button(window, text="(", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str("("))).grid(row=1, column=0)
tk.Button(window, text=")", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(")"))).grid(row=1, column=1)
tk.Button(window, text="⌫", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.delete(len(display.get())-1)).grid(row=1, column=2)
tk.Button(window, text="=", font=BUTTON_FONT, fg="black", bg="light blue", width=3, height=1, command=calculate).grid(row=1, column=3)

# Second Row
tk.Button(window, text="1", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(1))).grid(row=2, column=0)
tk.Button(window, text="2", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(2))).grid(row=2, column=1)
tk.Button(window, text="3", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(3))).grid(row=2, column=2)
tk.Button(window, text="+", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str("+"))).grid(row=2, column=3)

# Third row
tk.Button(window, text="4", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(4))).grid(row=3, column=0)
tk.Button(window, text="5", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(5))).grid(row=3, column=1)
tk.Button(window, text="6", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(6))).grid(row=3, column=2)
tk.Button(window, text="-", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str("-"))).grid(row=3, column=3)

# Fourth Row
tk.Button(window, text="7", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(7))).grid(row=4, column=0)
tk.Button(window, text="8", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(8))).grid(row=4, column=1)
tk.Button(window, text="9", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(9))).grid(row=4, column=2)
tk.Button(window, text="x", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str("*"))).grid(row=4, column=3)

# Fifth Row
tk.Button(window, text="C", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: input_text.set("")).grid(row=5, column=0)
tk.Button(window, text="0", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str(0))).grid(row=5, column=1)
tk.Button(window, text=".", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str("."))).grid(row=5, column=2)
tk.Button(window, text="/", font=BUTTON_FONT, fg="black", bg="white", width=3, height=1, command=lambda: display.insert(tk.INSERT, str("/"))).grid(row=5, column=3)

window.mainloop()