
import random

def intro():
    print()
    print("ROCK(R) PAPER(P) SCISSOR(S)")
    print()
    main()

def checkmove(b,e):
    if b == e:
        return "Same moves"
    elif b == "S" and e == "P":
        return "Player wins"
    elif b == "P" and e == "R":
        return "Player wins"
    elif b == "R" and e == "S":
        return "Player wins"
    elif e == "S" and b == "P":
        return "Computer wins"
    elif e == "P" and b == "R":
        return "Computer wins"
    elif e == "R" and b == "S":
        return "Computer wins"  
    
def restart():
    intro()
    
def ques():
    x = input("Do you want rematch(Y/N) >>> ")
    if x == "Y" or x == "y":
        restart()
    else:
        exit()

def main():
    global cs , ps
    cs = 0
    ps = 0
    a =int(input("Enter the number of points >>> "))
    choice = ["R" , "P","S"]
    while True:
        b = input("Prompt(R/P/S) >>> ")
        b = b.upper()
        if b not in choice:
            continue
        d = random.randint(0,2)
        e = choice[d]
        print("Your choosed {}".format(b))
        print("Computer choosed {}".format(e))
        f = checkmove(b,e)
        if f =="Player wins":
            ps = ps + 1
            print("Player wins")
        elif f == "Computer wins":
            cs = cs + 1
            print("Computer wins")
        else:
            continue
        print("Your score is {}".format(ps))
        print("Computer score is {}".format(cs))
        print()
        if ps == a:
            break
        elif cs == a:
            break


    if cs == a:
        print("Computer wins")
        ques()
    else:
        print("Player wins")
        ques()


intro()