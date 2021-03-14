a = input ("Enter number: ")
b = input("Enter another number: ")
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b can not be zero")


    