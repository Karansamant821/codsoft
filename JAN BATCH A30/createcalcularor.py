
def main():
    print("calculator")
    print()
    a = float(input("Enter the first number >>> "))
    b = float(input("Enter the second number >>> "))
    print()
    display(a,b)

def ques():
    print()
    x = input("Do you want to restart the program? (Y/N) >>> ")
    if x == "Y" or x == "y":
        restart()
    else:
        exit()

def restart():
    main()

def display(a,b):
    print()
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Division")
    print("4 - Multiplication")
    print("5 - Modulo")
    print("0 - Exit")

    try:
        c = int(input("Enter your choice >>> "))
    except:
        print("Invalid input")
        print("Terminating the program...")
        print("")
        exit()

    if c==1:
        print("Sum of {} and {} is {}".format(a,b,a+b))
        ques()
    elif c==2:
        print("Sub of {} and {} is {}".format(a,b,a-b))
        ques()
    elif c==3:
        print("Division of {} and {} is {}".format(a,b,a/b))
        ques()
    elif c ==4:
        print("Multiplication of {} and {} is {}".format(a,b,a*b))
        ques()
    elif c ==5:
        print("Modulo of {} and {} is {}".format(a,b,a%b))
        ques()
    elif c == 0:
        exit()
    else:
        print("Wrong number")
        print("Taking back to option page")
        display(a,b)

main()