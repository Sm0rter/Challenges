# Variables
more = True


# Functions
def GCD(a:int,b:int):
    if b == 0 or a == 1:
        return(a)
    return(GCD(b,a%b))


# Main Loop
while more == True:
    num1 = int(input("What is the first number "))
    num2 = int(input("What is the second number "))
    gcd = GCD(num1,num2)
    print(gcd)
    moreq = input("Do you want to continue? (y/n) ")
    if moreq == "n":
       more = False
    else:
        more = True