score = 88, 95, 70, 100, 99
sum = 0
for i in score:
    sum+= i
print(sum)

oneTuple = 2,
oneTuple2 = (2)
print(oneTuple)
print(oneTuple2)

tu = 1, 2, 3, 4, 5
print(tu[3])
print(tu[1:4])
print(tu + (6,7))
print(tu*2)
# tu[1] == 100, del tu[1] 이런 수정, 삭제는 불가능하다.

tu = "이순신", "김유신", "강감찬"
lee, kim, kang = tu
print(lee)
print(kim)
print(kang)

# 원래의 값을 잃지않고 교환이 이루어지기때문에 튜플끼리는 교환이가능
a, b = 12, 34
print(a, b)
a, b = b, a
print(a, b)
c, d, e = 1, 2, 3
c, d = a, b
print(c,d,e)

import time

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print("今は%d時 %d分です。"%(result[0], result[1]))

# 몫과 나머지를 튜플로반한화는 divmod함수
d, m = divmod(7, 3)
print(d, m)

# 튜플은 변경이불가능하므로 내부구조가 단순하고 읽는속도도 빠르다.
# 변경불가능하므로 안정적이다.

# 튜플함수, 리스트함수를 사용하면 튜플<->리스트 가능
# 가능은한데 시간이 오래걸린다
score = 88, 95, 70, 100, 99
tu = tuple(score)
print(tu)
li = list(tu)
print(li)
