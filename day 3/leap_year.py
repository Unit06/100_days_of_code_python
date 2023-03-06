# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
check4 = year%4 
check100 = year%100
check400 = year%400

if (check4==0) and ((check100!=0) or (check400==0)):
    print("Leap year.")
else:
    print("Not leap year.")