# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
full_name = (name1 + name2).lower()
full_name = full_name.replace(" ", "")

count_T = full_name.count('t')
count_R = full_name.count('r')
count_U = full_name.count('u')
count_E = full_name.count('e')
true_score = str(count_T + count_R + count_U + count_E)

count_L = full_name.count('l')
count_O = full_name.count('o')
count_V = full_name.count('v')
count_E = full_name.count('e')
love_score = str(count_L + count_O + count_V + count_E)

final_score = int(true_score + love_score)

if (10 > final_score) or (final_score > 90):
     print(f"Your score is {final_score}, you go together like coke and mentos.")
elif 40 < final_score < 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")