#4)lculate the BMI of a person based on their height and weight entered 
# by the user and classify their BMI category using if-else

height = int(input("Pleace Enter Your Height: "))
weight = int(input("Pleace Enter Your Weight: "))

height_metres = height / 100.0

bmi = weight / (height ** 2)

if bmi <18.5:
    bmi_category = "underweight"

elif bmi < 25:
    bmi_category = "Normal weight"

elif bmi < 30:
    bmi_category = "Overweight"

else:
    bmi_category = "Obesity"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {bmi_category}")

