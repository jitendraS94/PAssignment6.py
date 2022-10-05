def cubeOfNaturalNumbers():
    in_num = int(input("Enter the no of Natural Numbers: "))
    result = pow(((in_num * (in_num +1))/2),2)
    print(f'The Cube Sum of First {in_num} Natural Numbers is {result}')

cubeOfNaturalNumbers()