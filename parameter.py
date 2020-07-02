# 가변인수를 받는경우, 앞에 *를 붙인다
def intsum(*ints):
    sum = 0
    for num in ints:
        sum+=num
    return sum

print(intsum(1,2,3))
print(intsum(8,10))

def calcstep(begin, end, step):
    sum = 0
    for num in range(begin, end+1, step):
        sum += num
    return sum

# 1+3+5+7+9
print(calcstep(1,10,2))
# 2+4+6+8+10
print(calcstep(2,10,2))

# step default = 1
def calcstep(begin, end, step = 1):
    sum = 0
    for num in range(begin, end, step):
        sum += num
    return sum

print(calcstep(1,10))
print(calcstep(1,10,2))

print(calcstep(1, 10, step=3))
# 숫자인수(위치인수)는 앞부분에있어야하고,키워드인수(형식인수)는 뒷부분에 있어야 한다. 즉, 이런건 안됨
# print(calcstep(begin=1, 10, step=4))
# print(calcstep(begin=1, 10, 1))
# 키워드인수만으로 구성된다면, 순서는 상관없음
print(calcstep(step=3, begin=1, end=10))


# 키워드가변인수를 받는경우, 앞에 **를 붙인다.
def calcstep(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']

    sum=0
    for num in range(begin, end+1, step):
        sum+= num
    return sum

print("3~5 : ", calcstep(begin = 3, end = 5, step=1))
print("3~5 : ", calcstep(step=1, end=5, begin=3))


def calcscore(name, *score, **option):
    print(name)
    sum=0
    for num in score:
        sum += num
    print("총 점 : ", sum)
    if option['avg'] == True:
        print("평균 :",sum/len(score))

calcscore("안준석", 90, 95, 100, avg=True)
calcscore("김홍일", 90, 95, 100, avg=False)