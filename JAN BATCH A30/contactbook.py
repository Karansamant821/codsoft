"""
search contact
"""

cl = []

def add(n, m):
    global cl
    d = n + " " + m 
    cl.append(d)

def view():
    c = 1
    if len(cl) != 0:
        for i in cl:
            print(str(c) + " " + i)
            c += 1
    else:
        print("Task List is empty")

def delete(b):
    del cl[b-1]
    return True

def search(b):
    for i in cl:
        if b in i:
            print(i)

        

def display():
    print("\nContact Book\n1 - Add Contact\n2 - View Contact\n3 - Search Contact\n4 - Remove Contact\n5 - Quit\n")

def main():
    while True:
        display()
        a = int(input("$Choice>>> "))
        if a == 1:
            n = input("$Name>>> ")
            n = n.lower()
            m = input("$Number>>> ")
            add(n , m)

        elif a == 2 :
            view()

        elif a == 3:
            b = input("$Search>>> ")
            b = b.lower()
            search(b)

        elif a == 4:
            view()
            b = int(input("$Choice>>> "))
            delete(b)

        elif a == 5:
            exit()

        else:
            print("Invalid input")
            exit()

main()