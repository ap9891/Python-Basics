list1 = ['chalk','duster','board','pen']
'''
desired output
chalk and duster and board and pen
'''
# for item in list1:
#     if item != 'pen':
#         print(item,"and ", end=" ")
#     else:
#         print(item)

print(" and ".join(list1))