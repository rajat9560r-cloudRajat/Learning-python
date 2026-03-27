'''Q16. Write a recursive function to calculate factorial of n.
Test with: 5, 0
Q17. Write a recursive function to calculate the nth Fibonacci number.
Test with: 6 (answer should be 8)
Q18. Write a recursive function to reverse a string.
Test with: "hello" → "olleh"
Q19. Write a recursive function to find the sum of all digits of a number.
Test with: 1234 → 10'''


# def recursion(n):
#     if n==0:
#         return 1
#     else:
#         return recursion(n-1)*n
    
# n=int(input('enter a no: '))
# print(recursion(n))


# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n+1):
#         print(a)
#         c=a+b
#         a=b
#         b=c
# n=int(input('enter a no; '))
# fibonacci(n)



# def fibo_recu(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo_recu(n-1) + fibo_recu(n-2)
# n=int(input('enter a no: '))
# print(fibo_recu(n))



# def str_rev(n):
#     if n=="":
#         return ""
#     else:
#         return n[-1] + str_rev(n[:-1])

# print(str_rev('hello'))




# n=6060

# add=0
# while n>0:
#     add += n%10
#     n = n//10
# print(add)

add=0
def numbers(n):
    if n==0:
        return n
    else:
        return n%10 + numbers(n//10)
n=74674
print(numbers(n))