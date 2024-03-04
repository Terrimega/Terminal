import turtle
import sys

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=1100, height=700)
wn.tracer(0)  # Desactiva las actualizaciones automáticas de la pantalla

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=6, stretch_len=0.1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=6, stretch_len=0.1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Velocidad horizontal
ball.dy = -2  # Velocidad vertical

# Marcador
score_a = 0
score_b = 0

# Velocidad de los bloques
paddle_speed = 30
ball_speed = 0.08

# Límites de las paletas
def check_boundary(paddle):
    if paddle.ycor() > 250:
        paddle.sety(250)
    if paddle.ycor() < -250:
        paddle.sety(-250)

# Objeto de texto del marcador
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 24, "normal"))

# Funciones de movimiento de los bloques
def paddle_a_up():
    y = paddle_a.ycor()
    y += paddle_speed
    paddle_a.sety(y)
    check_boundary(paddle_a)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= paddle_speed
    paddle_a.sety(y)
    check_boundary(paddle_a)

def paddle_b_up():
    y = paddle_b.ycor()
    y += paddle_speed
    paddle_b.sety(y)
    check_boundary(paddle_b)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= paddle_speed
    paddle_b.sety(y)
    check_boundary(paddle_b)

# Controles para ajustar la velocidad de los bloques y pelota
def increase_speed():
    global  ball_speed
    ball_speed += 0.05

def decrease_speed():
    global  ball_speed

    if ball_speed > 0.1:
        ball_speed -= 0.05

# Función para salir del juego
def exit_game():
    wn.bye()
    sys.exit()

# Teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(increase_speed, "o")
wn.onkeypress(decrease_speed, "l")
wn.onkeypress(exit_game, "q")  # Exit game on "q" key

# Loop principal del juego
while True:
    wn.update()

    # Mover la bola
    ball.setx(ball.xcor() + ball.dx * ball_speed)
    ball.sety(ball.ycor() + ball.dy * ball_speed)

    # Revisar colisiones con los bordes de la pantalla
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        scoreboard.clear()
        scoreboard.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        scoreboard.clear()
        scoreboard.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Revisar colisiones con los bloques
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 71 > ball.ycor() > paddle_b.ycor() - 71):
        ball.color("green")
        ball.dx *= -1

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 71 > ball.ycor() > paddle_a.ycor() - 71):
        ball.color("red")
        ball.dx *= -1
