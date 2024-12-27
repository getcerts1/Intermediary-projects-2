import turtle as t
import random



screen = t.Screen()
screen.setup(500,400)
screen.colormode(255)

#let user add max 7 competitors to the game
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
random_colors = []
turtles_objects = {}



while True:
    try:
        Players = int(screen.numinput("Players", "Enter the number of competitors"))
        if Players <= 0 or Players > 8:
            raise ValueError("The number you entered is outside the scope. Please enter a value between 1 and 8.")
        else:
            break
    except ValueError as e:
        print(e)


for i in range(Players):
    r = random.randint(50,200)
    g = random.randint(50, 200)
    b = random.randint(50,200)
    random_colors.append((r,g,b))

for i in range(Players):
    random_name = random.choice(names)
    turtles_objects[random_name] = t.Turtle()
    names.remove(random_name)


x_axis = -240
y_axis = 180
for key,value in turtles_objects.items():
    print(f"{key}:{value}")
    turtles_objects[key].shape("turtle")
    random_color = random.choice(random_colors)
    turtles_objects[key].color(random_color)
    turtles_objects[key].goto(x_axis, y_axis)
    y_axis -= 400 / Players


try:
    Bet = screen.textinput("Bets", "Who will win? Enter a color")
    if Bet is None or Bet not in random_colors:
        raise ValueError("Invalid bet")
except ValueError as e:
    print(f"Error: {e}")
    Bet = None  # Handle the case by assigning a default or exiting


    while True:
        for key in turtles_objects.keys():
            turtles_objects[key].forward(random.randint(5,50))
            x, y = turtles_objects[key].position()
            print(f'{[key]} -- {turtles_objects[key].position()}')
            if x >= 250.00:
                print(f'The winner is {key}')
                print(f'The winner was {key.color}')
                break
        else:
            continue
        break

screen.exitonclick()