x=int(input("Please enter an integer:"))

def num(x):
    if x < 0:
        x = 0
        print('Negative changed to Zero')
    elif x ==0:
        print('Zero')
    elif x == 1:
        print('One')
    else:
        print('More')

while x < 9:
    num(x)
    x=int(input("Please enter an Integer:"))