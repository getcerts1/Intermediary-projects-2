from turtle import Turtle


test_turt = Turtle()


try:
  userinput = input('what is 2+2')

except ValueError:
  print('this is a false input try again')