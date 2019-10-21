import tkinter
from math import sqrt, pi, cos, sin
import numpy as np
from graphics.Graphics import GUI


gui = GUI(width=800, height=800, point_radius=10)

def mouse_motion(event):
    '''As the mouse moves while held down, check if any points
       that the mouse glides over can be colored.'''
    if not gui.in_bounds(event.x, event.y) or not gui.mouse_down: return
    gui.color_point(event.x, event.y)

def click(event):
    '''Records the coordinates of the most recent mouse click
       and colors the point on the canvas if appropriate.'''
    if gui.in_bounds(event.x, event.y):
        gui.x_mouse_click = event.x
        gui.y_mouse_click = event.y
        gui.mouse_down = True
        # Color the point that the user clicks on
        gui.color_point(event.x, event.y) 
    else:
        gui.x_mouse_click = -1
        gui.y_mouse_click = -1
        gui.mouse_down = False

def release(event):
    gui.mouse_down = False

# Bind the user mouse and clicking events to the functions above.
gui.canvas.bind('<Motion>', mouse_motion)
gui.canvas.bind('<Button-1>', click)
gui.canvas.bind('<ButtonRelease-1>', release)

# Add the button that generates the best fit line.
B = tkinter.Button(gui.window, text ="Generate Best Fit Ellipse", command = gui.best_fit)
B.pack()

gui.window.mainloop() # open the window 

