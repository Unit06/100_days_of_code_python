# ๐จ Don't change the code below ๐
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# ๐จ Don't change the code above ๐

#Write your code below this line ๐
bmi = weight / (height*height)
#print(f"{weight} รท ({height} x {height}) = {bmi}")
bmi = round(bmi)

if bmi < 18.5 :
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 < bmi < 25 :
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 < bmi < 30 :
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 < bmi < 35 :
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")