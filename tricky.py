'''Q10. Write a program using a while loop that keeps 
asking the user for a number until they enter 0, then prints the sum of all entered numbers.'''


# add=0
# while True:
#     n=int(input('enter a no: '))
#     if n==0:
#         add+=n
        
#         break
#     else:
#         add += n
# print(add)


nested = [[1, 2], [3, 4], [5, 6]]
ll=[]
print(type(nested))
for i in nested:
    for a in i:
        ll.append(a)
print(ll)

       