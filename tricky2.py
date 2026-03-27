'''Q15. Write a function that takes a list of numbers and returns a dictionary with:

"max" → maximum value
"min" → minimum value
"avg" → average value

Test with: [4, 7, 2, 9, 1]'''



diss={}
lst=[4, 7, 2, 9, 1]

def gphard(lst):
    avg=sum(lst)/len(lst)   
    diss['max']=max(lst)
    diss['min']=min(lst)
    diss['avg']=avg

    return diss

print(gphard(lst))