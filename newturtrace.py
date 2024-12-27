import turtle as t
import random
import requests

screen = t.Screen()
screen.setup(500, 400)
screen.colormode(255)

# Let user add max 7 competitors to the game
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
random_colors = []
name_color_match = {}
turtles_objects = {}
turtle_color_names = {}

# Get number of players
while True:
    try:
        Players = int(screen.numinput("Players", "Enter the number of competitors"))
        if Players <= 0 or Players > 8:
            raise ValueError("The number you entered is outside the scope. Please enter a value between 1 and 8.")
        else:
            break
    except ValueError as e:
        print(e)

# Generate random colors for the turtles
for i in range(Players):
    r = random.randint(50, 200)
    g = random.randint(50, 200)
    b = random.randint(50, 200)
    random_colors.append((r, g, b))

# Function to get color name from the API
def get_color_name(rgb_values):
    url = "https://www.thecolorapi.com/id"
    response = requests.get(url, params={'rgb': f'rgb({rgb_values[0]},{rgb_values[1]},{rgb_values[2]})'})
    if response.status_code == 200:
        data = response.json()
        return data.get('name', {}).get('value', 'Unknown')
    else:
        return f"Error: {response.status_code}"

# Map each RGB color to a name
for rgb in random_colors:
    color_name = get_color_name(rgb)
    print(f"RGB {rgb} is {color_name}")
    name_color_match[rgb] = color_name

# Create turtles and assign them random colors
x_axis = -240
y_axis = 180
for i in range(Players):
    random_name = random.choice(names)
    names.remove(random_name)
    turtle = t.Turtle()
    turtle.shape("turtle")
    turtle.penup()
    random_color = random.choice(random_colors)
    turtle.color(random_color)
    turtles_objects[random_name] = turtle
    turtle_color_names[random_name] = name_color_match[random_color]
    turtle.goto(x_axis, y_axis)
    y_axis -= 400 / Players


try:
    options = ", ".join(set(name_color_match.values()))
    Bet = screen.textinput("Bets", f"Who will win? Enter a color: {options}")
    if Bet is None or Bet not in name_color_match.values():
        raise ValueError("Invalid bet")
except ValueError as e:
    print(f"Error: {e}")
    Bet = None


while True:
    for key, turtle in turtles_objects.items():
        turtle.forward(random.randint(5, 50))
        x, y = turtle.position()
        print(f'{key} -- {turtle.position()}')
        if x >= 250.00:  # If the turtle reaches the finish line
            winner_color_name = turtle_color_names[key]
            print(f'The winner is {key}')
            print(f'The winning color is {winner_color_name}')

            if winner_color_name == Bet:
                print(f"Congratulations! You bet correctly, {key} won with the color {winner_color_name}.")
            else:
                print(f"Sorry, {key} won, but the color was {winner_color_name} instead of your bet ({Bet}).")
            break
    else:
        continue
    break

screen.exitonclick()
