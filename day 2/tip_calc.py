#fstring
#score = 0
#height = 1.8
#isWinning = True
#
#print(f"your score is {score}, h = {height}")

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
perc = input("What percentage tip would you like to give? 10, 12, or 15? ")
person = input("How many people to split the bill? ")

pay = (float(bill) / float(person)) * (int(perc) / 100 + 1)
pay = "{:.2f}".format(pay)

print(f"Each person should pay: ${pay}")