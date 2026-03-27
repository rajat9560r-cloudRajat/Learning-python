'''Q12. Write a function is_palindrome(s) that returns True if a string is a palindrome.
Test with: "racecar", "hello", "madam"'''

# def is_palindrome(n):
#     if n==n[::-1]:
#         return True
#     else:
#         return False
# n=input('enter a string: ')
# print(is_palindrome(n))


'''Q13. Write a function count_vowels(s) that returns the count of vowels in a string.
Test with: "Hello World"'''

def vowels(n):
    coun=0
    for i in n.lower():
        if i in 'aeiou':
            coun+=1
    return coun
    
n=input('entere a string: ')
print(vowels(n))