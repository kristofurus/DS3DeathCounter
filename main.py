import tkinter as tk
from tkinter import font as tkFont

with open("counter.txt", 'r') as f:
    count = int(f.read())


def add_death():
    global count, lab
    count = count + 1
    lab.config(text=f"Death count: {count}")
    with open("counter.txt", 'w') as f:
        f.write(str(count))


root = tk.Tk()
root.geometry("1024x768")
helv36 = tkFont.Font(family='Helvetica', size=24, weight='bold')
root.title("DS3 death counter")
btn = tk.Button(root, text="+1 Byczqu", command=add_death, bg="gray", fg="red", height=5, width=10, font=helv36)
btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
lab = tk.Label(root, text=f"Death count: {count}", font=helv36)
lab.place(anchor=tk.NW)

root.mainloop()
