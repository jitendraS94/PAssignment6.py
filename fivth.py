"""5.	Write a Python Program for cube sum of first n natural numbers?"""

def cube_sum_nat_num():
    p=1
    num = int(input("Enter the number"))
    if num ==1:
        print(1)
    else:
        for i in range(2,num+1):
            p = p+( i**3)
            print(p)



cube_sum_nat_num()
