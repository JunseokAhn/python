score = 1,2,3,4,5
no = 1
for i in score :
    print(str(no)+"번 학생의 성적 : ", i)
    no+=1

race = 'zerg', 'terran', 'protoss'
# enumerate는 순서값과 요소값을 한번에 구해주는데, 뒤에 숫자붙이면 그 숫자부터 순서가 시작됨
print(list(enumerate(race)))
print(list(enumerate(race, 0)))

for no, s in enumerate(score,3):
    print("%d번 학생의 성적 : %d" %(no, s))

day = "mon", "tue", "wed", "thu", "fri", "sat", "sun"
food = "갈비", "순대", "칼국수", "삼겹살"
menu = zip(day, food)
for a, b in menu:
    print("%s요일 메뉴 : %s" %(a,b))

print(dict(zip(day, food)))

tf = True, False, True, False
# any는 참이 하나라도있으면 true, all은 전부  참일때 true
print(any(tf))
print(all(tf))

def flunk(s) :
    return s<60

score = 40,50,60,70,80
# 함수에 전달하는 파라미터를 전달하는방식이 좀 특이하다.
for i in filter(flunk, score) :
    print(i)

def half(s):
    return s/2

# 뭔가 필터랑 차이를 모르겠음
for s in map(half, score):
    print(s, end=' ')
print()

def sum(s, b):
    return s+b

bonus = 1,2,3,4

for s in map(sum, score, bonus):
    print(s, end=" ")
print()
# 그냥 포문에 조건식을 박아버리는 람다
# x에 60보다 작은 스코어를 대입한다는 뜻
for s in filter(lambda x : x < 60, score) :
    print(s, end=" ")
print()

for s in map(lambda x : x/2, score) : 
    print(s, end=" ")
print()

list1 = [1,2,3]
list2 = list1
# 같은 메모리를 가르키고있기때문에 list1[1]도 100이된다.
list2[1] = 100
print(list1)

# 이를 막으려면 copy함수로 복사본을 생성하면된다.
list1 = [1,2,3]
list2 = list1.copy()
list2[1] = 100
print(list1)

list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = list1.copy()
list2[0][1] = 'c'
# list0라는 같은곳을 가르키기때문에 전부 c로바뀜
print(list1)
print(list2)

# list0까지 포함한 카피 = copy.deepcopy()
import copy
list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = copy.deepcopy(list1)
list1[0][1] = 'c'
print(list1)
print(list2)

print("list1 == list2 ? ", list1 is list2)

# 이런경우는 리스트만 그렇고, 변수는 다른값을 대입하면 참조가 변경되며 즉시 분리된다.
a='a'
b=a
print("a =", a, "b =", b, ":", a is b)
b='b'
print("a =", a, "b =", b, ":", a is b)

