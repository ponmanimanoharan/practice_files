# Modify this program to greet you instead of the World!
print("Hello, Ponmani Manoharan!")

# Modify this program to print Humpty Dumpty riddle correctly
print("\n")
print("Humpty Dumpty sat on a wall,")
print("Humpty Dumpty had a great fall.")
print("All the king's horses and all the king's men")
print("Couldn't put Humpty together again.")

# Greet 3 of your classmates with this program, in three separate lines
print("\n")
print("Hello, Esther!")
print("Hello, Mary!")
print("Hello, Joe!")

# Write a program that prints a few details to the terminal window about you
print("\n")
my_detials = ["Ponmani Manoharan", 23, 1.73]
for x in my_detials:
    print(x)

# Create a program that prints a few operations on two numbers: 22 and 13
print("\n")
# Print the result of 13 added to 22
print(13+22)
# Print the result of 13 substracted from 22
print(22-13)
# Print the result of 22 multiplied by 13
print(22*3)
# Print the result of 22 divided by 13 (as a decimal fraction)
print(22/13)
# Print the integer part of 22 divided by 13
print(22//13)
# Print the remainder of 22 divided by 13
print(22 % 13)
print("\n")

# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
# 5 workdays in one week
work_days = 5
hours_spent = 6
weeks_of_work = 17

total_working_hours_workdays = work_days*hours_spent*weeks_of_work
"""print(total_working_hours_workdays)


print(17*5)"""
# 85 week days in 17 weeks
# 1 days = 24 hours
# working hours = 6
# 85*6
"""print(85*6)
print("if the attendee only codes on workdays and have spent 6 hours everyday for 17 weeks:  Number of hours attended are 510 hours and Number of days 21.25")"""
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52
average_work_hour = 17*52
percentage_of_coding_hrs_average = round(100*(total_working_hours_workdays/average_work_hour))
print(total_working_hours_workdays)
print(percentage_of_coding_hrs_average)
"""print(5*6*17)
print(17*52)
print((510/884)*100)"""
print("\n")
fav_number = 8
print("my favourite number is : " + str(fav_number))
print("\n")
a = 123
b = 526
print("original values : " + str(a),str(b))
temp = a
a = b
b = temp
print("swapped values : " + str(a), str(b))
print("\n")
print("Body Mass Index")
massinkg = 81.2
heightinm = 1.78
BMI = massinkg/heightinm
print("the Body mass index is : " + str(BMI))
# print body mass index based on these values
print("\n")
# Define several things as a variable then print their values
name = "Ponmani Manoharan"
# Your name as a string
age = 23
# Your age as an integer
height = 1.73
# Your height in meters as a float
Married = False
# Whether you are married or not as a boolean
print(name,age,height,Married)
print("\n")
a = 3
a += 10
# make the "a" variable's value bigger by 10

print(a)

b = 100
b -= 7
# make b smaller by 7

print(b)

c = 44
c *= c
# please double c's value

print(c)

d = 12

d /= 5
# please divide by 5 d's value

print(d)

e = 8

e = e**3
# please cube of e's value

print(e)

f1 = 123
f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)
print(f1>f2)
g1 = 350
g2 = 200
print((g2*2) > g1)
# tell if the double of g2 is bigger than g1 (pras a boolean)

h = 1357988018575474
# tell if 11 is a divisor of h (pras a boolean)
print(h%11 == 0)
i1 = 10
i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)
print(i1 > (i2**2) < (i2**3))
j = 1521
# tell if j is divisible by 3 or 5 (pras a boolean)
print(j%3 == 0 or j%5 == 0)
print("\n")

# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
#
# Surface Area: 600
# Volume: 1000

l = 10.0
b = 10.0
h = 10.0
volume_of_cuboid = (l*b*h)
Surface_area= 2 * (l*b+b*h+l*h)
print("Volume : "+ str(volume_of_cuboid), "Surface Area : "+ str(Surface_area))
print("\n")

current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variable
total_seconds = 24*3600
past_seconds = (current_hours * 3600) + (current_minutes * 60) + current_seconds
remaining_seconds = total_seconds - past_seconds
print("The remaining seconds :" + str(remaining_seconds))
print("\n")
# Modify this program to greet the user instead of the World!
# The program should ask for the name of the user

"""user = input("Please enter your name : ")
print("Hello, " + user + "!")
print("\n")
# miles to kilometer converter
distance_in_miles = input("please enter distance in miles: ")
convert_miles_to_kilometers = int(distance_in_miles) * 1.609344
print("The kilometer : " + str(convert_miles_to_kilometers))
print("\n")

# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

chicken_owned = int(input("Enter the number of chickens owned : "))

pigs_owned = int(input("Enter the number of pigs owned : "))

if chicken_owned != 0:
    chicken_owned *= 2
    print(chicken_owned)
if pigs_owned != 0:
    pigs_owned *=4
    print(pigs_owned)"""


print("\n")

# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

"""five_int = []
for i in range(5):
    five_value = input("enter the five numbers : ")
    five_int.append(int(five_value))

print(five_int)

sum_five = sum(five_int)/len(five_int)
print(sum(five_int))
print(sum_five)

"""

print("\n")
# Write a program that reads a number from the standard input,
# Then prints "Odd" if the number is odd, or "Even" if it is even.
"""check_number = int(input("enter the number : "))
if check_number%2 == 0:
    print("even")
else:
    print("odd")"""

# Write a program that reads a number form the standard input,
# If the number is zero or smaller it should print: Not enough
# If the number is one it should print: One
# If the number is two it should print: Two
# If the number is more than two it should print: A lot

"""check_number = int(input("enter the number : "))

if check_number == 0 or check_number <= 0 :
    print("not enough")
elif check_number == 1:
    print("One")
elif check_number == 2:
    print("Two")
else:
    print("A lot")"""

# Write a program that asks for two numbers and prints the bigger one
"""num_one = int(input("enter number one : "))
num_two = int(input("enter number two : "))
if num_one > num_two :
    print("Number one is bigger ")
elif num_one < num_two:
    print("Number two is bigger ")
else:
    print("wrong input")"""


# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people

"""number_of_girls  =  int(input("enter the number of girls : "))
number_of_boys  =  int(input("enter the number of boys : "))
total_number_of_people = number_of_boys + number_of_girls
if number_of_girls == number_of_boys:
    print("The party is exellent!")
elif number_of_girls == 0:
    print("Sausage party")
elif total_number_of_people > 20 and number_of_girls != number_of_boys:
    print("Quite cool party!")
elif total_number_of_people < 20:
    print("Average party...")"""

a = 24
out = 0
# if a is even increment out by one

if a % 2 == 0:
    out += 1
print(out)
b = 87
out2 = ""
# if b is between 10 and 20 set out2 to "Sweet!"
# if less than 10 set out2 to "Less!",
# if more than 20 set out2 to "More!"
if 10<b<20:
    out2 += "Sweet!"
elif b<10:
    out2 += "Less!"
elif b> 20:
    out2 += "More!"

print(out2)



c = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits are smaller than 50,
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same

if credits >=50 and is_bonus == False:
    c -= 2
elif credits <50 and is_bonus == False:
    c -=1
elif is_bonus == True:
    c =c

print(c)


d = 8
time = 120
out3 = ""
# if d is dividable by 4
# and time is not more than 200
# set out3 to "check"
# if time is more than 200
# set out3 to "Time out"
# otherwise set out3 to "Run Forest Run!"


#print(out3)
