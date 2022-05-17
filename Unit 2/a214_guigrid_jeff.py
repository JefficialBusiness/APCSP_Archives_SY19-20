##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

root = tk.Tk()
root.wm_geometry("300x300")
Frame = tk.Frame(root)

bottomframe = tk.Frame(root)

b = tk.Frame(width=200, height=150, bg="blue", colormap="new")
g = tk.Frame(width=200, height=150, bg="green", colormap="new")
r = tk.Frame(width=200, height=150, bg="red", colormap="new")
y = tk.Frame(width=200, height=150, bg="yellow", colormap="new")

r.grid(row=1, column=0)
g.grid(row=0, column=1)
b.grid(row=0, column=0)
y.grid(row=1, column=1)

root.mainloop()
