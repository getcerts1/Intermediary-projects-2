from turtle import Turtle


test_turt = Turtle()


try:
  userinput = input('what is 2+2')

except TypeError:
  print('this is a false input try again')