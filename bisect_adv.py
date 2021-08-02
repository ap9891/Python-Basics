import bisect
number = 5
a = [1,2,4,6,7,8,9,34]
# return the posn where element is to be inserted
print(bisect.bisect(a,number))
# inserts the element
# bisect.insort(a,number)
print(a)
