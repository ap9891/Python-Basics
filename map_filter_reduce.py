# map,filters and reduce
#map
#map(function_to_apply, list of inputs)
 
# m = [1,2,3,4]
# sq=[]
# wihtout map
# for i in m:
#     sq.append(i**2)
# def s(n):
#     return n**2
# using map
# sq= list(map(s,m))
# print(sq)


# filter

# def greater_than_2(n):
#     if n >2:
#         return True
#     else:
#         return False

# l = [1,2,3,4,5,6,7,8]
# greater_2 = list(filter(greater_than_2,l))
# print(greater_2)

from functools import reduce

# 1. 1 + 2 = 3
# 2. 3 + 3 = 6
# 3. 6 + 4 = 10
def sum_num(a,b):
    return a+b
l = reduce(sum_num, [1,2,3,4])
print(l)

