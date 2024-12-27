import turtle as t
import random
import requests



screen = t.Screen()
screen.setup(500,400)
screen.colormode(255)

#let user add max 7 competitors to the game
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
random_colors = []
name_color_match = {}
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


def get_color_name(rgb_values):
    url = "https://www.thecolorapi.com/id"

    #send GET request to the API with RGB params
    response = requests.get(url, params={'rgb': f'rgb({rgb_values[0]},{rgb_values[1]},{rgb_values[2]})'})

    if response.status_code == 200:
        data = response.json()
        api_color_name = data.get('name', {}).get('value', 'Unknown')
        return api_color_name
    else:
        return f"Error: {response.status_code}"



for rgb in random_colors:
    color_name = get_color_name(rgb)
    print(f"RGB {rgb} is {color_name}")
    name_color_match[rgb] = color_name


for i in range(Players):
    random_name = random.choice(names)
    turtles_objects[random_name] = t.Turtle()
    names.remove(random_name)


x_axis = -240
y_axis = 180
for key,value in turtles_objects.items():
    print(f"{key}:{value}")
    turtles_objects[key].shape("turtle")
    turtles_objects[key].penup()
    random_color = random.choice(random_colors)
    turtles_objects[key].color(random_color)
    turtles_objects[key].goto(x_axis, y_axis)
    y_axis -= 400 / Players


try:
    options = ""
    for key, value in name_color_match.items():
        options+= f'{name_color_match[key]} - '

    Bet = screen.textinput("Bets", f"Who will win? Enter a color {options}")
    if Bet is None or Bet not in name_color_match:
        raise ValueError("Invalid bet")
except ValueError as e:
    print(f"Error: {e}")
    Bet = None


    while True:
        for key, turtle in turtles_objects.items():
            turtles_objects[key].forward(random.randint(5,50))
            x, y = turtles_objects[key].position()
            print(f'{[key]} -- {turtles_objects[key].position()}')
            if x >= 250.00:
                print(f'The winner is {key}')
                print(f'{turtle.color()[0]} -- {Bet[1]}')
                if turtle.color()[0] == Bet:
                    print("congrats")

                else:
                    print("unlucky")
                    break
        else:
            continue
        break

screen.exitonclick()