n = 123456

count = 0
n1 = n
while n1 > 0:
    n1 = n1 // 10
    count = count + 1

first = n // 10 ** (count-1)
second = 0

for i in range(count, 1, -1):
    second = first
    first = n % 10 ** (i-1) // 10 ** (i - 2)
    #print('Second = ', second, 'i = ', i)
    #print('First = ', first, 'i = ', i)


