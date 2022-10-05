"""2.	Write a Python Program to Find Factorial of Number Using Recursion?"""

def Factorial_of_Number_Using_Recursion():
    num = int(input("Enter the number :="))
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
        print(fact)


Factorial_of_Number_Using_Recursion()