
#       Anna Engel      |       Module 11 Program       |       Intro to Programming

import math

stepsFile = open("steps.txt", "r") #opens the steps.txt file so it can be read
count = 0 #sets the counter to 0         

for line in stepsFile:
    count +=1 #adds one to count each time loop runs
    steps = int(line)
    count = count + steps
    avg = count / 365 #takes the average of all steps
print("\n",count,"steps taken this year!")
print("That's about", round(avg), "steps each day!\n")
##Starts the January Function
#JANUARY
with open('steps.txt') as f:
   jan = f.read().split()[0:31]
  #print(jan) 
def sum_digits_string(jan):
    sum_digit = 0
    for x in jan:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for Jan-31 is" , sum_digits_string(jan))     
avg_jan = sum_digits_string(jan)
print("Thats an average of" , avg_jan / 31 , "per day! \n") # Prints the average for Jan
##Starts the Feb Function
#FEBUARY
with open('steps.txt') as f:
   feb = f.read().split()[32:60]
   #print(feb) 
def sum_digits_string(feb):
    sum_digit = 0
    for x in feb:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for Feb-28 is" , sum_digits_string(feb))     
avg_feb = sum_digits_string(feb)
print("Thats an average of" , avg_feb / 28 , "per day! \n") # Prints the average for Feb
##Starts the Mar Function
#MARCH
with open('steps.txt') as f:
   mar = f.read().split()[61:92] #Reads the lines which represent the entries for March
   #print(mar) 
def sum_digits_string(mar):
    sum_digit = 0
    for x in mar:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for Mar-31 is" , sum_digits_string(mar))     
avg_mar = sum_digits_string(mar)
print("Thats an average of" , avg_mar / 31 , "per day! \n") # Prints the average for Mar
##Starts the Apr Function
#April
with open('steps.txt') as f:
   apr = f.read().split()[93:122] #Reads the lines which represent the entries for March
   #print(apr) 
def sum_digits_string(apr):
    sum_digit = 0
    for x in apr:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for Apr-30 is" , sum_digits_string(apr))     
avg_apr = sum_digits_string(apr)
print("Thats an average of" , avg_apr / 30 , "per day! \n") # Prints the average for Apr
##Starts the May Function
##MAY
with open('steps.txt') as f:
   may = f.read().split()[123:154] #Reads the lines which represent the entries for May
   #print(may) 
def sum_digits_string(may):
    sum_digit = 0
    for x in may:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for May-31 is" , sum_digits_string(may))     
avg_may = sum_digits_string(may)
print("Thats an average of" , avg_may / 31 , "per day! \n") # Prints the average for May
##Start June Function
#JUNE
with open('steps.txt') as f:
   june = f.read().split()[155:184] #Reads the lines which represent the entries for June
   #print(june) 
def sum_digits_string(june):
    sum_digit = 0
    for x in apr:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for June-30 is" , sum_digits_string(june))     
avg_june = sum_digits_string(june)
print("Thats an average of" , avg_june / 30 , "per day! \n") # Prints the average for June
##Start July Function
##JULY
with open('steps.txt') as f:
   july = f.read().split()[185:215] #Reads the lines which represent the entries for july
   #print(july) 
def sum_digits_string(july):
    sum_digit = 0
    for x in july:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for July-31 is" , sum_digits_string(july))     
avg_july = sum_digits_string(july)
print("Thats an average of" , avg_july / 31 , "per day! \n") # Prints the average for July
#Start August Function
#AUGUST
with open('steps.txt') as f:
   aug = f.read().split()[215:246] #Reads the lines which represent the entries for Aug
   #print(Aug) 
def sum_digits_string(aug):
    sum_digit = 0
    for x in aug:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for Aug-31 is" , sum_digits_string(aug))     
avg_aug = sum_digits_string(aug)
print("Thats an average of" , avg_aug / 31 , "per day! \n") # Prints the average for August
##Start the September Function
#September
with open('steps.txt') as f:
   sep = f.read().split()[247:277] #Reads the lines which represent the entries for September
   #print(September) 
def sum_digits_string(sep):
    sum_digit = 0
    for x in sep:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for September-30 is" , sum_digits_string(sep))     
avg_sep = sum_digits_string(sep)
print("Thats an average of" , avg_sep / 30 , "per day! \n") # Prints the average for September
##Start October function
#OCTOBER
with open('steps.txt') as f:
    oct = f.read().split()[278:309] #Reads the lines which represent the entries for October
   #print(oct) 
def sum_digits_string(oct):
    sum_digit = 0
    for x in oct:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for October-31 is" , sum_digits_string(oct))     
avg_oct = sum_digits_string(oct)
print("Thats an average of" , avg_oct / 31 , "per day! \n") # Prints the average for October
#Start November function
#NOVEMBER
with open('steps.txt') as f:
    nov = f.read().split()[310:340] #Reads the lines which represent the entries for November
   #print(oct) 
def sum_digits_string(nov):
    sum_digit = 0
    for x in nov:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for November-30 is" , sum_digits_string(nov))     
avg_nov = sum_digits_string(nov)
print("Thats an average of" , avg_nov / 30 , "per day! \n") # Prints the average for November
#Start December Function
#DECEMBER
with open('steps.txt') as f:
    dec = f.read().split()[341:365] #Reads the lines which represent the entries for October
   #print(oct) 
def sum_digits_string(dec):
    sum_digit = 0
    for x in dec:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print("The total steps for December-31 is" , sum_digits_string(dec))     
avg_dec = sum_digits_string(dec)
print("Thats an average of" , avg_dec / 31 , "per day! \n") # Prints the average for December