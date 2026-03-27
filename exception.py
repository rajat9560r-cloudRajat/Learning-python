'''Q21. Write a program that:

Asks user to enter two numbers
Divides them
Handles ZeroDivisionError and ValueError properly'''

# try:
#     n=int(input('enter a no: '))
#     i=int(input('enter a no: '))
#     print('--Answer-',n/i)
# except  ZeroDivisionError:
#     print('---Any number is zero')

# except ValueError :
#     print('---Input is wrong')

# else:
#     print('---Divided without error and inputs are right')

# finally:
#     print('----I can do this all day')



def safe_index(lst,i):
    try:
       
        return lst[i]
    except IndexError:

        return 'index out of range'    
    except:
        return 'error occured somewhere'
    

print(safe_index([1,2,3], 5))
print(safe_index([1,2,3], 0))
print(safe_index([1,2,3], 1))
print(safe_index([1,2,3], 2))