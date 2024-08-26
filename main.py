import turtle
import time

# Setup layar
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Menonaktifkan auto-update layar

# Setup paddle kiri
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=6, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Setup paddle kanan
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=6, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Setup bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")  # Bentuk bola menjadi lingkaran
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.35  # Kecepatan horizontal bola yang ditingkatkan
ball.dy = -0.35  # Kecepatan vertikal bola yang ditingkatkan

# Setup papan skor
score_left = 0
score_right = 0

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Setup pesan "Goal"
goal_message = turtle.Turtle()
goal_message.speed(0)
goal_message.color("yellow")
goal_message.penup()
goal_message.hideturtle()
goal_message.goto(0, 0)

# Update skor
def update_score():
    scoreboard.clear()
    scoreboard.write(f"Player 1: {score_left}  Player 2: {score_right}", align="center", font=("Courier", 24, "normal"))

# Tampilkan pesan "Goal"
def show_goal_message(player):
    goal_message.clear()
    goal_message.write(f"Goal! Player {player}", align="center", font=("Courier", 36, "normal"))
    wn.update()
    time.sleep(1)  # Tampilkan pesan selama 1 detik
    goal_message.clear()

# Gerakan paddle
def paddle_left_up():
    y = paddle_left.ycor()
    if y < 250:
        y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    if y > -240:
        y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    if y < 250:
        y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    if y > -240:
        y -= 20
    paddle_right.sety(y)

# Kontrol keyboard
wn.listen()
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "Up")
wn.onkeypress(paddle_right_down, "Down")

# Loop utama
while True:
    wn.update()

    # Pergerakan bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Deteksi batas atas dan bawah
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Deteksi batas kiri dan kanan
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # Skor untuk Player 1
        score_left += 1
        update_score()
        show_goal_message(1)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        # Skor untuk Player 2
        score_right += 1
        update_score()
        show_goal_message(2)

    # Deteksi tumbukan dengan paddle
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_right.ycor() + 50 > ball.ycor() > paddle_right.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_left.ycor() + 50 > ball.ycor() > paddle_left.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
