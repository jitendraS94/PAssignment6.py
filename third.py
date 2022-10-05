"""3.	Write a Python Program to calculate your Body Mass Index?"""

def calculate_Body_Mass_Index():
    weight = float(input("Enter the weight(kgs) :="))
    if
    height = float(input("Enter the hight(mtr) 1foot = 0.3048:="))
    call_BMI = weight/pow(height,2)
    if (call_BMI <18.5):
        print(call_BMI,"underweight")
    elif call_BMI >=18.5 and call_BMI <24.9 :
        print(call_BMI,"Healthy")
    elif call_BMI >=24.9 and call_BMI <30 :
        print(call_BMI,"Overweight")
    else:
        call_BMI > 30
        print(call_BMI,"Very overweight")

calculate_Body_Mass_Index()
