
import random

def operation(user_input):
    global password
    
    for x in range(user_input):
        l = random.randint(0,3)
        if l == 0:
            a = random.randint(0,25)
            password = password + upper_case[a]
        elif l == 1:
            b = random.randint(0,25)
            password = password + lower_case[b]
        elif l == 2:
            c = random.randint(0,9)
            password = password + number[c]
        else:
            d = random.randint(0,11)
            password = password + symbols[d]
        

    print("Generated password is : " + password)



def main():
    global password , upper_case , lower_case , number , symbols
        
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_case = list(upper_case)

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    lower_case = list(lower_case)

    number = "1234567890"
    number = list(number)

    symbols = "!@#$%^&*()_-"
    symbols = list(symbols)

    password = ""

    user_input = int(input("Enter the lenght of the character : " )) 

    operation(user_input)


main()