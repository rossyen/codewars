# BMI_calculator.py
'''
DESCRIPTION:
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''

def bmi(weight, height):
    BMI = weight/height**2
    if BMI <= 18.5:
        return "Underweight"
    elif BMI <= 25.0:
        return "Normal"
    elif BMI <= 30.0:
        return "Overweight"
    elif BMI > 30:
        return "Obese"

