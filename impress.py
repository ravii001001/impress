import turtle
import turtle as trt 
from turtle import *
import time
import random

# --- Window Setup ---
win = Screen()
win.setup(1250, 650)
win.title('My Cute Baby - I ❤️ U')
win.bgcolor('white')
time.sleep(1)

# --- Feature 1: Background Love Confetti ---
def drop_confetti():
    confetti = trt.Turtle()
    confetti.hideturtle()
    confetti.speed(0)
    confetti.penup()
    # Drops 25 soft pastel love dots across the sky
    for _ in range(25):
        cx = random.randint(-600, 600)
        cy = random.randint(150, 320)
        confetti.goto(cx, cy)
        confetti.color(random.choice(['#ff9999', '#ffccf2', '#b3ffff', '#ffff99']))
        confetti.dot(random.randint(6, 14))

# Draw the confetti pattern early
drop_confetti()

# --- Magical Backdrop Sparkles ---
sparkle = trt.Turtle()
sparkle.hideturtle()
sparkle.speed(0)
sparkle.width(2)

def draw_sparkle(x, y):
    sparkle.penup()
    sparkle.goto(x, y)
    sparkle.pendown()
    sparkle.color(random.choice(['gold', 'yellow', '#ffb3ff']))
    for _ in range(8):
        sparkle.forward(12)
        sparkle.backward(12)
        sparkle.right(45)

for _ in range(15):
    draw_sparkle(random.randint(200, 580), random.randint(-200, 250))

# --- Main Turtle Styling ---
a = trt.Turtle()
a.speed(7)
a.color('blue', 'red')
a.shape('arrow')
a.penup()
a.goto(-600, 250)
a.width(8)

# --- Draw "B" ---
a.left(90)
a.penup()
a.left(180)
a.pendown()
a.circle(150/4)
a.forward(150/2)
a.circle(150/4)

# --- Draw "A" ---
a.penup()
a.forward(150/4)
a.left(90)
a.forward(150/4+75)
a.left(90)
win.bgcolor('#75a3a3')
a.pendown()
a.forward(150)
a.right(90)
a.forward(70)
a.right(90)
a.forward(150/2)
a.right(90)
a.forward(70)
a.bk(70)
a.left(90)
a.forward(150/2)
a.left(90)

# --- Draw Second "B" ---
a.penup()
a.forward(150/4)
a.left(90)
a.forward(112.5)
a.left(180)
a.pendown()
a.circle(150/4)
a.forward(150/2)
a.circle(150/4)
win.bgcolor('#bfff80')

# --- Draw "Y" ---
a.penup()
a.forward(150/4)
a.left(90)
a.forward(3*(150/4))
a.pendown()
a.forward(70)
a.left(90)
a.forward(150)
a.bk(150/2)
a.left(90)
a.forward(70)
a.right(90)
a.forward(150/2)

a.penup()
a.backward(150)
a.right(90)

# --- Feature 2: Gradient Heart Shading Functions ---
def curve(): 
    for i in range(100): 
        # Alternates hues dynamically for a vibrating color gradient effect
        if i % 2 == 0:
            a.color('#ff3366')
        else:
            a.color('#ff66cc')
        a.right(2) 
        a.forward(2) 

def heart(): 
    a.fillcolor('red')  
    a.begin_fill() 
    a.left(140) 
    a.forward(113)
    win.bgcolor('#ffcccc')
    curve() 
    a.left(120) 
    curve() 
    # Reset color to uniform red to safely close the fill shape boundaries
    a.color('red')
    a.forward(112) 
    a.end_fill() 
 
a.penup()
a.setpos(0, -100) 
a.pendown()
a.width(4)
a.shape('turtle')
heart()

# --- Frame Around Heart ---
a.penup()
a.setpos(120, -100)
a.left(50)
win.bgcolor('#80dfff')
a.pendown()
a.width(8)
a.color('white', 'yellow')
a.forward(150)
a.left(90)
a.forward(80)
a.left(90)
a.forward(150)

# --- Rose Flower Setup ---
a.penup()
a.setpos(400, 245)
a.pendown()
a.width(2)
a.color('black', 'red')
a.shape('circle')
a.right(90)

# Rose Flower Base
a.fillcolor("red")
a.begin_fill()
a.circle(10, 180)
a.circle(25, 110)
a.left(50)
a.circle(60, 45)
a.circle(20, 170)
a.right(24)
a.fd(30)
a.left(10)
a.circle(30, 110)
a.fd(20)
a.left(40)
a.circle(90, 70)
a.circle(30, 150)
a.right(30)
a.fd(15)
a.circle(80, 90)
a.left(15)
a.fd(45)
a.right(165)
a.fd(20)
a.left(155)
a.circle(150, 80)
a.left(50)
a.circle(150, 90)
a.end_fill()

# Rose Petal 1
a.left(150)
a.circle(-90, 70)
a.left(20)
a.circle(75, 105)
a.setheading(60)
a.circle(80, 98)
a.circle(-90, 40)

# Rose Petal 2
a.left(180)
a.circle(90, 40)
a.circle(-80, 98)
a.setheading(-83)

# Leaves 1
a.fd(30)
a.left(90)
a.fd(25)
a.left(45)
a.fillcolor("green")
a.begin_fill()
a.circle(-80, 90)
a.right(90)
a.circle(-80, 90)
a.end_fill()
a.right(135)
a.fd(60)
a.left(180)
a.fd(85)
a.left(90)
a.fd(80)

# Leaves 2
a.right(90)
a.right(45)
a.fillcolor("green")
a.begin_fill()
a.circle(80, 90)
a.left(90)
a.circle(80, 90)
a.end_fill()
a.left(135)
a.fd(60)
a.left(180)
a.fd(60)
a.right(90)
a.circle(200, 60)
a.hideturtle()

# --- Animated Text Engine ---
pen = trt.Turtle()
pen.hideturtle()
pen.speed(0)

def type_text(message, x, y, color, font_size):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    
    current_str = ""
    for char in message:
        current_str += char
        pen.clear()
        pen.write(current_str, font=("Courier", font_size, "italic"))
        time.sleep(0.03) # Fluid letter-by-letter typing speed
    
    # Permanently stamp sentence onto the screen surface
    stamp_pen = trt.Turtle()
    stamp_pen.hideturtle()
    stamp_pen.penup()
    stamp_pen.goto(x, y)
    stamp_pen.color(color)
    stamp_pen.write(message, font=("Courier", font_size, "italic"))

def txt():
    win.bgcolor('#ecb3ff')
    
    type_text("❤️❤️❤️ My Angel Baby ❤️❤️❤️", -600, 95, 'deep pink', 15)
    time.sleep(0.3)
    
    type_text("My Sweet Heart ❤️❤️❤️", -600, 55, 'red', 15)
    time.sleep(0.3)
    
    type_text(" ❤️❤️ My Lovely Cutiee ❤️❤️ ", -600, 15, 'red', 15)
    time.sleep(0.3)
    
    type_text("You are mine BABY", -600, -35, '#992600', 20)
    time.sleep(0.3)
    
    type_text("I love you Baby ❤️...", -600, -95, 'deep pink', 15)
    time.sleep(0.3)
    
    type_text("U are the most liked Person❤️ in my life Baby...", -600, -135, 'deep pink', 15)
    time.sleep(0.3)
    
    type_text("I will never forget our memories...", -600, -175, 'deep pink', 15)
    time.sleep(0.3)
    
    type_text("Your smile is my favorite thing in the world.", -600, -215, 'deep pink', 15)
    time.sleep(0.3)
    
    type_text("The way you understand and support me...", -600, -255, 'deep pink', 15)
    time.sleep(0.3)
    
    type_text("I am missing 🙁 you every moment Dear", -600, -295, 'deep pink', 15)
    time.sleep(0.3)
    
    type_text("I Love you Baby ❤️...You are MINE...", -600, -335, 'red', 15)

# Execute core script sequence
txt()

# --- Feature 3: Feature Mouse-Click Interactivity ---
def draw_heart_at_click(x, y):
    click_pen = trt.Turtle()
    click_pen.hideturtle()
    click_pen.speed(0)
    click_pen.color('#ff3366', '#ffb3cc')
    click_pen.penup()
    click_pen.goto(x, y)
    click_pen.pendown()
    
    click_pen.begin_fill()
    click_pen.left(140)
    click_pen.forward(20)
    for _ in range(10):
        click_pen.right(18)
        click_pen.forward(2)
    click_pen.left(120)
    for _ in range(10):
        click_pen.right(18)
        click_pen.forward(2)
    click_pen.forward(20)
    click_pen.end_fill()

# Triggers heart spawns on mouse click
win.onclick(draw_heart_at_click)

# --- Feature 4: Pulse Layout Effect & Keep Open Loop ---
# Keeps the program background feeling "alive" with dynamic window titles
while True:
    try:
        win.title("My Cute Baby - ❤️ I LOVE YOU ❤️")
        time.sleep(0.6)
        win.title("My Cute Baby - 💖 YOU ARE MINE 💖")
        time.sleep(0.6)
    except trt.Terminator:
        break # Exit loop cleanly if window is closed by user
