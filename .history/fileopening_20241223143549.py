
filename = input('enter the file name')

with open(file=filename):
  print(filename.read())