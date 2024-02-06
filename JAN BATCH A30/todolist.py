

a = []

def create(c):
    global a
    a.append(c)


def display():

    c = 1
    global a
    if len(a) != 0:
        for i in a:
            print(str(c) + " " + i)
            c += 1
    else:
        print("Task List is empty")

def mardone(c):
    a[c-1] = a[c-1] + " Done"

    

def remove(c):
    del a[c-1]
    return True
        
while True:
    print("To Do List\n\n1 - Add\n2 - Mark done\n3 - Remove\n4 - Display\n5 - Exit\n")
    b = int(input("$Choice>>> "))
    if b == 1:
        c = input("$Value>>> ")
        create(c)
    elif b == 2:
        display()
        c = int(input("$TaskNumber>>> "))
        mardone(c)
        display()
    elif b == 3:
        display()
        c = int(input("$TaskNumber>>> "))
        remove(c)
    elif b == 4:
        display()
    elif b == 5:
        exit()
    else:
        print("Invalid input")
        exit()