'''
format function
'''

users = ['a','b','c','d']
computer=['c1','c2','c3','c4']

# for i in range(0,len(users)):
#     print(users[i], " is ",computer[i])

for i in range(0,len(users)):
    template = "computer used by {} is {}"
    print(template.format(users[i],computer[i]))