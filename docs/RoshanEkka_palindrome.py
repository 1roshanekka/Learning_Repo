import math
n = int(input('Input a number to check if pallindrome : '))

getCount = 0
x = n
while(x>0):  #no of digits
    getCount += 1
    x = x//10 #update
# print(getCount)

l = n
check = 0
for i in range(getCount, 0, -1):
    # print(i)
    dig = l%10
    l = l//10
    check += dig*math.pow(10,i-1)
    # print(check)

if(check == n):
    print('YES its a pallindrome')
else:
    print('NO its not a pallindrome')

