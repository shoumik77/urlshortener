

def collatz(number):
    if int(number) % 2 == 0:
        newNum = number // 2
        return newNum
    else:
        newNum = 3*int(number) + 1
        return newNum
    

newNum = input('Enter number: ')

while newNum != 1:
    newNum = collatz(newNum)
    print(newNum)

