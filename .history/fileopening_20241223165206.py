


try:
    while True:
      userinput = input('What is your name? ')
      if not userinput.strip():  # Check if input is empty or only whitespace
          raise ValueError('Input cannot be empty.')
      elif userinput.isdigit():
          raise ValueError('please enter an alphabetical value')
      print(f'Hello {userinput}')
      break
except ValueError as e:
    print(f'Error: {e}')
