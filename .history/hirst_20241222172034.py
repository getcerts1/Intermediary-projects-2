import turtle
import tkinter as TK

# Set up the screen
screen = turtle.Screen()
screen.tracer(0)  # Disable automatic updates

# Create the turtle
t = turtle.Turtle()

# Drawing
for i in range(100):
    t.forward(i)
    t.right(45)
    screen.update()  # Update the screen manually

turtle.done()
