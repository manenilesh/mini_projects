import tkinter as tk

window = tk.Tk()
window.title("My first GUI")
window.geometry("300x200")  # Right: no spaces around 'x'


label = tk.Label(window, text="Hello Guys")
label.pack()

window.mainloop()