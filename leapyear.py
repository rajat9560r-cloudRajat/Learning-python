'''Q7. Write a program that checks if a year is a leap year.
(Leap year: divisible by 4, but not 100, unless also divisible by 400)
Test with: 2000, 1900, 2024, 2023'''

n=int(input('enter a year: '))
if (n%4==0 and n%100!=0) or n%400==0:
    print('leap year')
else:
    print('not a leap year')