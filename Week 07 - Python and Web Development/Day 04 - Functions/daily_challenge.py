'''Write a function to compute 5/0 and use try/except to catch the exceptions.
Bonus : use some Buit-in exceptions of Python '''

def divide_numbers():
    numerator = input("Please choose a numerator: ")
    denominator = input("Please choose a denominator: ")
    try:
        result = int(numerator) / int(denominator)
        print(result)
    except ZeroDivisionError:
        print("Denominator cannot be 0. Please try again.")
    except ValueError:
        print("Value is not a number. Please try again.")
    finally:
        print("Program ended.")

divide_numbers()

