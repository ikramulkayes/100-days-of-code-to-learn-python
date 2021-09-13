def plus(n1,n2):
    return n1 + n2
def minus(n1,n2):
    return n1 - n2
def multi(n1,n2):
    return n1 * n2
def devide(n1,n2):
    return n1/n2
sum1 = 0
flag = True
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

while True:
    try:
        n1 = sum1
        if flag:
            print(logo)
            n1 = float(input("What is your first number: "))
            flag = False
        sym = input("+ - * / pick a symbol: ")
        n2 = float(input("What is your second number: "))
        if sym == "+":
            sum1 = plus(n1,n2)
        elif sym == "-":
            sum1 = minus(n1,n2)
        elif sym == "*":
            sum1 = multi(n1,n2)
        elif sym == "/":
            sum1 = devide(n1,n2)
        else:
            print("Syntax error")
            break
        print(n1,sym,n2,"=",sum1)
        again = input("Do you wanna use the sum and continue your calculation? input any key to continue or input n to stop the calculator or if you wanna start a new calculation press y: ")
        if again == "n":
            break
        elif again == "y":
            flag = True
    except:
        print("Enter proper variable")
    
