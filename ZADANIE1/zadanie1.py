import turtle
import math
import random

# Globalne parametry
a, b = 1, 1  # Proporcje częstotliwości (X:Y)
delta = math.pi / 2  # Przesunięcie fazowe
running = False  # Flaga do sterowania animacją
current_color = "cyan"

# Ustawienia ekranu i żółwia
screen = turtle.Screen()
screen.title("Krzywe Lissajous")
screen.bgcolor("black")
screen.setup(width=800, height=600)  # Mniejsze okno: szerokość=800, wysokość=600
screen.tracer(0)  # Wyłącz automatyczne odświeżanie ekranu

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.hideturtle()

dot = turtle.Turtle()
dot.shape("circle")
dot.color("red")
dot.penup()

legend = turtle.Turtle()
legend.hideturtle()
legend.penup()

# Funkcja konwertująca fazę na ułamek liczby pi
def format_delta_as_pi(delta):
    k = delta / math.pi
    return f"{round(k, 2)}π"

# Funkcja wyświetlająca opis i legendę na ekranie
def display_legend():
    legend.clear()
    # Pierwsza linia: Krzywe Lissajous
    legend.goto(-380, 260)
    legend.color("white")
    legend.write(
        f"Krzywe Lissajous: Stosunek częstotliwości X:Y = {a}:{b}, faza = {format_delta_as_pi(delta)}",
        align="left",
        font=("Arial", 12, "normal")
    )

    # Druga linia: Klawisze
    legend.goto(-380, 240)
    legend.color("white")
    legend.write(
        "Klawisze: Lewo/Prawo: zmiana X, Góra/Dół: zmiana Y, Z/X: zmiana fazy",
        align="left",
        font=("Arial", 10, "normal")
    )

    # Trzecia linia: Spacja i C
    legend.goto(-380, 220)
    legend.color("yellow")
    legend.write(
        "Spacja: Start/Stop, C: Wyczyść",
        align="left",
        font=("Arial", 10, "bold")
    )

# Funkcja rysująca krzywą Lissajous
def draw_lissajous():
    global running, current_color

    if running:
        running = False
        return

    running = True
    current_color = (random.random(), random.random(), random.random())
    t.color(current_color)
    dot.color(current_color)

    A = 200
    B = 200
    steps = 1000
    step_size = 0.02

    t.penup()
    dot.penup()

    for i in range(steps):
        if not running:
            break
        t_rad = i * step_size
        x = A * math.sin(a * t_rad + delta)
        y = B * math.sin(b * t_rad)

        t.goto(x, y)
        dot.goto(x, y)

        t.pendown()
        screen.update()

    t.penup()
    running = False



# Obsługa klawiszy
def increase_a():
    global a
    a += 1
    display_legend()

def decrease_a():
    global a
    if a > 1:
        a -= 1
    display_legend()

def increase_b():
    global b
    b += 1
    display_legend()

def decrease_b():
    global b
    if b > 1:
        b -= 1
    display_legend()

def increase_delta():
    global delta
    delta += math.pi / 16  # Zwiększ fazę o mały krok
    display_legend()

def decrease_delta():
    global delta
    delta -= math.pi / 16  # Zmniejsz fazę o mały krok
    display_legend()

def clear_screen():
    global running
    running = False  # Zatrzymaj animację
    t.clear()
    dot.goto(0, 0)
    display_legend()

# Przypisanie klawiszy
screen.listen()
screen.onkey(increase_a, "Right")  # Zwiększ X (strzałka w prawo)
screen.onkey(decrease_a, "Left")   # Zmniejsz X (strzałka w lewo)
screen.onkey(increase_b, "Up")     # Zwiększ Y (strzałka w górę)
screen.onkey(decrease_b, "Down")   # Zmniejsz Y (strzałka w dół)
screen.onkey(increase_delta, "z")  # Zwiększ fazę
screen.onkey(decrease_delta, "x")  # Zmniejsz fazę
screen.onkey(clear_screen, "c")    # Czyść ekran
screen.onkey(draw_lissajous, "space")  # Rozpocznij/zatrzymaj rysowanie

# Start programu
display_legend()
screen.mainloop()
