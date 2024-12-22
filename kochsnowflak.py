import tkinter as tk
import math

def draw_koch(order, x1, y1, x2, y2, canvas):
    if order == 0:
        canvas.create_line(x1, y1, x2, y2)
    else:
        dx, dy = (x2 - x1) / 3, (y2 - y1) / 3
        xA, yA = x1 + dx, y1 + dy
        xB, yB = x1 + 2 * dx, y1 + 2 * dy
        xC = (xA + xB) / 2 - (yB - yA) * math.sqrt(3) / 2
        yC = (yA + yB) / 2 + (xB - xA) * math.sqrt(3) / 2
        draw_koch(order - 1, x1, y1, xA, yA, canvas)
        draw_koch(order - 1, xA, yA, xC, yC, canvas)
        draw_koch(order - 1, xC, yC, xB, yB, canvas)
        draw_koch(order - 1, xB, yB, x2, y2, canvas)

def draw_snowflake(order):
    canvas.delete("all")
    w, h = 600, 600
    p1, p2 = (w / 4, h / 2), (3 * w / 4, h / 2)
    p3 = ((p1[0] + p2[0]) / 2, p1[1] - math.sqrt(3) * (p2[0] - p1[0]) / 2)
    draw_koch(order, *p1, *p2, canvas)
    draw_koch(order, *p2, *p3, canvas)
    draw_koch(order, *p3, *p1, canvas)

def increase_order():
    global order
    order += 1
    label.config(text=f"Order: {order}")
    draw_snowflake(order)

def decrease_order():
    global order
    if order > 0:
        order -= 1
        label.config(text=f"Order: {order}")
        draw_snowflake(order)

root = tk.Tk()
root.title("Koch Snowflake")
order = 0

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

control_frame = tk.Frame(root)
control_frame.pack()

tk.Button(control_frame, text="-", command=decrease_order).pack(side=tk.LEFT)
label = tk.Label(control_frame, text=f"Order: {order}")
label.pack(side=tk.LEFT)
tk.Button(control_frame, text="+", command=increase_order).pack(side=tk.LEFT)

draw_snowflake(order)
root.mainloop()