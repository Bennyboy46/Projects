height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in lbs: "))

def BMI(height, weight):
    bmi = weight / (height ** 2) * 703
    if bmi < 16:
        return "severely underweight", bmi
    elif 16 <= bmi < 18.5:
        return "underweight", bmi
    elif 18.5 <= bmi < 25:
        return "healthy", bmi
    elif 25 <= bmi < 30:
        return "overweight", bmi
    else:
        return "obese", bmi

quote, bmi = BMI(height, weight)
print("Your BMI is {:.2f} and you are {}".format(bmi, quote))
