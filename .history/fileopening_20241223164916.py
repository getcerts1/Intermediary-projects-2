


try:
    userinput = input('What is your name? ')
    if not userinput.strip():  # Check if input is empty or only whitespace
        raise ValueError('Input cannot be empty.')
    print(f'Hello {userinput}')
except ValueError as e:
    print(f'Error: {e}')
