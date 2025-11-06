#Below you will find several older homework questions done correctly using input
#and print statements. our task is to take each one and convert it to arguments and returns instead.


#modify the below function such that it asks the user for 2 numbers as input.
#Then have it print out the larger number
def larger(n1,n2):

    if n1>n2:
        return n1
    else:
        return n2
print(larger(5,8))

#Modify the below function such that it asks for the users score as an input.
#Then based on the score print out a letter grade.
# 90+ A
# 80+ B
# 70+ C
# 60+ D
# 59- F
def grade(score):
    if(score>=90):
        return "A"
    elif(score>=80):
        return "B"
    elif(score>=70):
        return "C"
    elif(score>=60):
        return "D"
    else:
        return "F"
print(grade(85))

#Modify the below function such that it asks the user for a number then
#if the number is divisible by 3 print "fizz"
#if the number is divisible by 5 print "buzz"
#if both are the case then print "Fizzbuzz" instead of the prior two
#if niether are the case print the number.
def fizzBuzz(n):
    if n%3==0 and n%5==0:
        return "fizzbuzz"
    elif n%3==0:
        return "fizz"
    elif n%5==0:
        return "buzz"
    else:
        return n
print(fizzBuzz(15))

#modify the below function such that it asks the user for an input number.
#if the number is even divide it by two.
#if the number is odd multiply it by 3 and add 1
#then print the new number.
def collatz(n):
    if(n==1):
        return 1
    if(n%2==0):
        return n/2
    else:
        return (3*n+1)

print(collatz(1))

#Modify the below function such that it asks the user for a temperature.
#The format for temperature should end in F For Fahrenheit and C for Celcius
#Then given the temperature if it is in Fahrenheit convert it to Celsius on vice versa
#Example 32F -> 0C  20C -> 68F
def convertTemperature(temperature):
    number=int(temperature[:-1 ])
    unit=temperature[-1]

    if unit=="C":
        return str(int(number *9/5+32))+"F"
    elif unit=="F":
        return str(int((number-32) *5/9))+"C"

print(convertTemperature("32F"))
