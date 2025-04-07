import turtle
import random

def draw_fractal_tree(t, branch_len, angle, min_len=5):
    if branch_len > min_len:
        t.pensize(branch_len / 10)
        t.forward(branch_len)
        
        # Random color for each branch
        t.color(random.random(), random.random(), random.random())
        
        # Right branch
        t.right(angle)
        draw_fractal_tree(t, branch_len * 0.7, angle, min_len)
        
        # Left branch
        t.left(angle * 2)
        draw_fractal_tree(t, branch_len * 0.7, angle, min_len)
        
        # Return to original position
        t.right(angle)
        t.backward(branch_len)

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.left(90)  # Start pointing up
t.penup()
t.setpos(0, -250)  # Start at bottom of screen
t.pendown()
t.color("green")

# Draw the tree
draw_fractal_tree(t, 100, 30)
turtle.done()