'''Q5. Write a program that takes a number and prints:

"Fizz" if divisible by 3
"Buzz" if divisible by 5
"FizzBuzz" if both
The number itself otherwise

Test with: 9, 10, 15, 7'''
while True:
    n=abs(int(input('enter a no: ')))
    if n!=0:
        if n%5==0 and n%3 != 0:
            print('buzz')
        elif n%3==0 and n%5 != 0:
            print('fizz')
        elif  n%5==0 and n%3==0:
            print('fizzbuzz')
        else:
            print('by itself', n)
        
    else:
        
        break