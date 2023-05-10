def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def div(a,b):
    return a/b

if __name__=="__main__":
    print("hello, this is a basic calculator \n")
    print('please choose an operation:\n 1- add \n 2-subtract \n 3-multiply \n 4-division \n ')
    choice = int(input())

    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))

    if choice == 1: 
        result = sum(a,b)
        print("The result is:", result)
    elif choice == 2:
        result = subtract(a,b)
        print("The result is:", result)
    elif choice == 3: 
        result = multiply(a,b)
        print("The result is:", result)
    elif choice == 4:
        result = div(a,b)
        print("The result is:", result)
    else:
        print("Invalid choice. Please choose a number from 1 to 4.")


