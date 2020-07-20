import calendar

# print(calendar.calendar(2020))
# print(calendar.month(2020, 7))
# print(calendar.prcal(2020))

# 0월요일 ~ 6일요일까지, 달력의 첫번쨰요일 세팅
calendar.setfirstweekday(3)
print(calendar.prmonth(2020, 7))

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
day = calendar.weekday(2020,7,27)
print(day)
print(days[day])

import random

print(random.random())
# int
print(random.randint(1,10))
# double
print(random.uniform(1,10))
print(random.choice(days))
print(random.sample(days,2))

lotto = random.sample(range(1,46), 6)
lotto.sort()
print(lotto)

import sys
print(sys.argv)

number = random.randint(1,100)
count = 0
while True :
    question = "숫자를 입력하세요"
    num = int(input(question))

    if(number>num):
        print("그것보다 큽니다")
        count = count+1
    elif(number<num):
        print("그것보다 작습니다")
        count = count+1
    else:
        print("정답입니다!")
        print("시도한횟수 : %d" %(count))
        break