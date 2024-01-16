import tkinter as tk

def btn_click(num):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(num))

def btn_clear():
    display.delete(0, tk.END)

def btn_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")
root.configure(bg="#333333")

display = tk.Entry(root, font=("Arial", 20), bg="#FFFFFF", justify="right")
display.pack(pady=20)

button_frame = tk.Frame(root, bg="#333333")
button_frame.pack()

buttons = [["7", "8", "9", "/"],["4", "5", "6", "*"],["1", "2", "3", "-"],["0", ".", "=", "+"]]
for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = tk.Button(button_frame, text=button_text, font=("Arial", 15), padx=20, pady=10, bg="#FFFFFF", fg="#333333")
        button.grid(row=i, column=j, padx=5, pady=5)
        button.config(command=lambda num=button_text: btn_click(num))

clear_button = tk.Button(button_frame, text="C", font=("Arial", 15), padx=20, pady=10, bg="#FF5555", fg="#FFFFFF")
clear_button.grid(row=4, column=3, padx=5, pady=5)
clear_button.config(command=btn_clear)

equal_button = tk.Button(button_frame, text="=", font=("Arial", 15), padx=20, pady=10, bg="#55FF55", fg="#FFFFFF")
equal_button.grid(row=4, column=2, padx=5, pady=5)
equal_button.config(command=btn_equal)

root.mainloop()