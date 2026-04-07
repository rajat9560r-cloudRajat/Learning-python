'''count vowels'''
cnt=0
def vowels(str,cnt):
    for i in str:
        if i in 'aeiou':
            cnt+=1
    return cnt
str=input('enter a string: ')
print(vowels(str,cnt))


'''sum of even no in list'''
cnt=0
def eveninlist(lst,cnt):
    for i in lst:
        if i%2==0:
            cnt+=i
    return cnt
lst=[1,2,3,4,5,6,7,8,9,0]
print(eveninlist(lst,cnt))


'''reverse a string'''
def revstr(str):
    rev=str[::-1]
    return rev
str=input('enter a string: ')
print(revstr(str))


'''duplicate in a list- T/F'''
def duplicacy(lst):
    lst1=set(lst)
    if len(lst1)==len(lst):
        return False
    else:
        return True
lst=[1,2,3,4,5,6,7,8,9,4,5,4]
print(duplicacy(lst))


'''largest in a list'''
def findlar(lst):
    lar=lst[0]
    for i in lst:
        if i>lar:
            lar=i
    return lar
lst=[28,32,43,56,554,43]
print(findlar(lst))