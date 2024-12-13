# Python Program to Check Leap Year

num = int(input("Enter the year: "))

if (num%4) == 0 and (num%100)!= 0:
    print('{} is a leap year'.format(num))

elif (num%400) == 0 and (num%100) == 0:
    print("{} is a leap year".formar(num))

else :
    print("{} is not a leap year".format(num))