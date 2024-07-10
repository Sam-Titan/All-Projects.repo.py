import tkinter as tk
root = tk.Tk()
root.title("The button pusher")
root.geometry("400x400")
count = 0
def count_clicked():
    global count
    count += 1
    label.config(text=f"It was clicked {count} times")

label = tk.Label(root, text="Counting the number of times the button was clicked")
label.pack()
button = tk.Button(root, text="Click me", command=count_clicked)
button.pack()
root.mainloop()