import math
# 제곱근sqrt sin cos log....
print(math.sqrt(2))

from math import sqrt
print(sqrt(2))

import math as m
print(m.sqrt(2))

from math import sqrt as sq
print(sq(2))

print(math.sin(math.radians(45)))
print(math.factorial(5))

import statistics as s

score = 30,40,50,60,70,80,90

# 평균
print(s.mean(score))
# 중앙값
print(s.median(score))
# 중앙값에서 가장가까운 낮은 값
print(s.median_low(score))
# 중앙값에서 가장가까운 높은 값
print(s.median_high(score))
# 표준편차
print(s.stdev(score))

import time
t = time.time()
print(time.ctime(t))

now = time.localtime(t)
print(now)
now = time.localtime()
print(now)
print("%d년 %d월 %d일" %(now.tm_year, now.tm_mon, now.tm_mday))
import datetime

now = datetime.datetime.now()
print("%d년 %d월 %d일" %(now.year, now.month, now.day))

# 실행시간측정
start = time.time()
for i in range(1000):
    i = i+1
end = time.time()
print(end-start)

# 셋타임아웃
time.sleep(1.5)
print("1.5초뒤에 나오는 문구")
ㅁ\ㅁ

# import turtle

# turtle.penup()
# turtle.goto(-720,0)
# turtle.pendown()
# for x in range(-720, 720) :
#     turtle.goto(x, math.sin(math.radians(x))*100)
# turtle.done()

