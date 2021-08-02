# take input from user
number = int(input())
temp = number
reverse=0

while(number>0):
    dig = number%10
    reverse = reverse*10 + dig
    number = number// 10
# print(reverse)
if reverse == temp:
    print("yes")
else:
    print("no")