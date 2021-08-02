a=['codewithharry','pen','book','mixer']

# 1
# i=0
# for item in a:
#     i =i +1
#     if i%2==0:
#         print(item)

# does the same work as 1 in fewer lines of code
for i, item in enumerate(a):
    if (i+1)%2==0:
        print(item)