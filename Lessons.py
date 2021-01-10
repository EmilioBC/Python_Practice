# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# # Write your code below this line 👇
# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])
# addNumbers = num1 + num2
# print(addNumbers)


################# BMI CALCULATOR #################

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# newHeight = (float(height) * float(height))
# bmi = int(weight) / newHeight
# print(round(bmi))


############## LIFE CALCULATOR #################

# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# lifeDays = (90 - int(age)) * 365
# lifeWeeks = (90 - int(age)) * 52
# lifeMonths = (90 - int(age)) * 12

# print(f"You have {lifeDays} days, {lifeWeeks} weeks, and {lifeMonths} left")


# ################# ODD or EVEN ##############
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if number % 2 == 0:
#     print(f"{number} is EVEN.")
# else:
#     print(f"{number} is ODD")


############## Nested IF/ELSE TICKETS ##############

# height = int(input("What is your height? "))

# if height >= 120:
#     print("You can ride the roller coaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5")
#     elif age in range(13, 19):
#         print("Please pay $7")
#     else:
#         print("Please pay $12.")
# else:
#     print("You are not tall enough.")


##########BMI Calculator w/ interpretation ######
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# BMI = round(weight / (height * height))

# if BMI <= 18:
#     print(f"Your BMI is {BMI}, you are underweight")
# elif BMI <= 22:
#     print(f"Your BMI is {BMI}, you are normal weight")
# elif BMI <= 28:
#     print(f"Your BMI is {BMI}, you are slightly overweight")
# elif BMI <= 33:
#     print(f"Your BMI is {BMI}, you are obese")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese")


######## LEAP YEAR CALCULATOR #################

# year = int(input("Enter a year: "))

# # if ((year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0)):
# #     print("Leap year")
# # else:
# #     print("Not a Leap year.")

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not a Leap Year")
#     else:
#         print("Not a Leap Year")
# else:
#     print("Not a Leap Year")


############## Nested IF/ELSE TICKETS with Photo##############

# height = int(input("What is your height? "))

# if height >= 120:
#     print("You can ride the roller coaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = int(5)
#     elif age in range(13, 19):
#         bill = int(7)
#     else:
#         bill = int(12)
#     photos = input("You want photos? Y or N. ")
#     if photos == "Y":
#         bill += int(3)
#     else:
#         bill += 0
#     print(f"The total bill is ${bill}.")
# else:
#     print("You are not tall enough.")


############PIZZA ORDER ######################
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if size == "S":
#     price = int(15)
#     if add_pepperoni == "Y":
#         price += 2
# elif size == "M":
#     price = int(20)
#     if add_pepperoni == "Y":
#         price += int(3)
# elif size == "L":
#     price = int(25)
#     if add_pepperoni == "Y":
#         price += int(3)
# if extra_cheese == "Y":
#     price += 1
# print(f"Your final bill is: ${price}")


############### LOVE SCORE ###################################

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# combinedString = name1 + name2
# lowerString = combinedString.lower()

# t = lowerString.count("t")
# r = lowerString.count("r")
# u = lowerString.count("u")
# e = lowerString.count("e")

# true = t + r + u + e

# l = lowerString.count("l")
# o = lowerString.count("o")
# v = lowerString.count("v")
# e = lowerString.count("e")

# love = l + o + v + e

# loveScore = int(str(true) + str(love))


# print(loveScore)

# if loveScore < 10 or loveScore > 90:
#     print(f"Your love score is {loveScore}, you are like coke and mentos.")
# elif loveScore >= 40 and loveScore <= 50:
#     print(f"Your love score is {loveScore}, you are alright together")
# else:
#     print(f"Your score is {loveScore}")


######################### RANDOM NUMBERS ######################

# import random
# # import my_module
# # print(my_module.moduleNumbers)


# randomNumber = random.randint(1, 10)
# print(f"The random number is: {randomNumber}")

# random_float = random.random() * 5
# print(f"This is a random float numbers: {random_float}")


############RANDOM NUMBER EXERCISES ##############
# Remember to use the random module 👇
# import random

# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# random_side = random.randint(0, 1)
# if(random_side == 1):
#     print("Heads")
# else:
#     print("Tails")

########### WHO IS PAYING THE BILL ##############
# import random
# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
# names = namesAsCSV.split(", ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# allNames = len(names)
# pay = random.randint(0, allNames - 1)

# print(f"The one who will pay is {names[pay]}")


############## TREASURE MAP #################
# 🚨 Don't change the code below 👇
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical-1][horizontal-1] = " X"


# # Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

####### ROCK PAPER SCISSORS ###############


#################3.1.6.9#########################
# myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# newList = []

# for element in myList:
#     if element in newList:
#         continue
#     else:
#         newList.append(element)

# myList = newList

# print("The list with unique elements only:")
# print(myList)


################################################# LEAP YEAR 4.1.3.6 ##############
# def isYearLeap(year):

#     if year < 1582:
#         return False
#     elif year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True


# testData = [1900, 2000, 2016, 1987]
# testResults = [False, True, True, False]
# for i in range(len(testData)):
#     yr = testData[i]
#     print(yr, "->", end="")
#     result = isYearLeap(yr)
#     if result == testResults[i]:
#         print("OK")
#     else:
#         print("Failed")


################################################### 4.1.3.7 #############

# def isYearLeap(year):

#     if year < 1582:
#         return False
#     elif year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True


# def daysInMonth(year, month):
#     monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if isYearLeap(year) and month == 2:
#         return 29
#     return monthDays[month - 1]


# testYears = [1900, 2000, 2016, 1987]
# testMonths = [2, 2, 1, 11]
# testResults = [28, 29, 31, 30]
# for i in range(len(testYears)):
#     yr = testYears[i]
#     mo = testMonths[i]
#     print(yr, mo, "->", end="")
#     result = daysInMonth(yr, mo)
#     if result == testResults[i]:
#         print("OK")
#     else:
#         print("Failed")


################## 4.1.3.8 ########################

# def isYearLeap(year):

#     if year < 1582:
#         return False
#     elif year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True


# def daysInMonth(year, month):
#     monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if isYearLeap(year) and month == 2:
#         return 29
#     return monthDays[month - 1]


# def dayOfYear(year, month, day):
#
#     if year < 1582:
#         return None
#     if month > 12 or month < 1:
#         return None
#     if day > daysInMonth(year, month) or day < 1:
#         return None

#
#     totalDays = day
#     month = month - 1
#     while month > 0:
#         totalDays += daysInMonth(year, month)
#         month -= 1
#     return totalDays

# print(dayOfYear(2000, 12, 31))


############# PRIME NUMBERS #####################

# def isPrime(num):
#     divisor = 2
#     while divisor < num:
#         if num % divisor == 0:
#             return False
#         divisor += 1
#     return True


# for i in range(1, 20):
#     if isPrime(i + 1):
#         print(i + 1, end=" ")
# print()


############# Convertion 4.1.3.10 ##########
# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.

# def l100kmtompg(liters):
#     miles = 100 * 1000 / 1609.344  # 100km * (1000 / 1609.344) to get 1km
#     gallons = liters / 3.785411784
#     return miles / gallons


# def mpgtol100km(miles):
#     liters = 3.785411784
#     kilometers = miles * 1609.344 / 1000
#     km100 = kilometers / 100
#     return liters / km100


# print(l100kmtompg(3.9))
# print(l100kmtompg(7.5))
# print(l100kmtompg(10.))
# print(mpgtol100km(60.3))
# print(mpgtol100km(31.4))
# print(mpgtol100km(23.5))

# Expected output:

# 60.31143162393162
# 31.36194444444444
# 23.52145833333333
# 3.9007393587617467
# 7.490910297239916
# 10.009131205673757

########### BMI CALCULATOR 4.1.5.1 ###################
# def bmi(weight, height):
#     if weight > 1 and height > 1:
#         return weight / height ** 2
#     else:
#         return None


# print(bmi(52.5, 1.65))

# DAY 1 Band Name #################3

# 1. Create a greeting for your program.
# print ("Welcome to the Band Name generator")
# #2. Ask the user for the city that they grew up in.
# whatCity = input("Name of city you grew up?: \n")
# #3. Ask the user for the name of a pet.
# whatPet = input("Name of your Pet?: \n")
# #4. Combine the name of their city and pet and show them their band name.
# bandName = whatCity + whatPet
# print ("Your Band name is: \n" + bandName)
# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

############## Day 5 Lesson with Angela Yu. #########

# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇


# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")
bill = float(input("What was the total of the bill? "))
tipPercent = float(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
billSplit = float(input("How many people to split the bill? "))
total = 0

if tipPercent == 10:
    total = (bill / billSplit) * 1.10
elif tipPercent == 12:
    total = (bill / billSplit) * 1.12
elif tipPercent == 15:
    total = (bill / billSplit) * 1.15

roundTotal = round(total, 2)
roundTotal = "{:.2f}".format(total)

print(f"Each person should pay: {roundTotal}")
