sum = 0
for num in range(5):
    sum+=num
print(sum)

sum=0
for num in range(11):
    sum+=num
print(sum)

def calcsum(n):
    sum=0
    for num in range(n+1):
        sum+=num
    return sum

print(calcsum(5))

def calcrange(begin, end):
    sum=0
    for num in range(begin, end+1):
        sum+=num
    return sum

print("3부터 7까지의 합", calcrange(3,7))