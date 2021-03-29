def try_me():
    while True:
        try:
            print("Input first number:")
            a = float(input())
            break
        except ValueError:
            print("That's not a number, try again")
    
    while True:
        try:
            print("Input second number:")
            b = float(input())
            break
        except ValueError:
            print("That's not a number, try again")

    return f"{a} + {b} = {a + b}. Incredible."