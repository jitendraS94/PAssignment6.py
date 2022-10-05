"""1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?"""

num = int(input("Enter the number"))

def Fibonacci_Sequence():
    a = 1
    b = 1
    print(a)
    print(b)
    for i in range(num):
        c = a + b
        a = b
        b = c
        print(c)

Fibonacci_Sequence()