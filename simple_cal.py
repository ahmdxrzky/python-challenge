def calculator(num1, operator, num2):
    if operator == "+":
        print(f'Result from above operation is: {num1 + num2}')
    elif operator == "-":
        print(f'Result from above operation is: {num1 - num2}')
    elif operator == "*":
        print(f'Result from above operation is: {num1 * num2}')
    else:
        print(f'Result from above operation is: {num1 / num2}')

if __name__ == '__main__':
    expression = input("Input math expression: ").split(" ")
    try:
        calculator(int(expression[0]), expression[1], int(expression[2]))
    except ValueError:
        print("Only accept three inputs. Numeral, operator, and numeral, respectively.")