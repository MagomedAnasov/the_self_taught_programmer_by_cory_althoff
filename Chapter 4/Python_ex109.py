try:
    a = input("Enter number: ")
    b = input("Enter another number: ")
    a = int(a)
    b = int(b)
    print(a/b)
except(ZeroDivisionError, ValueError):
    print("Error")