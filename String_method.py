s = "python programming"
# len은 내장함수라서 len(s)
print(len(s))
# find, rfind는 검색결과없으면 -1리턴
print(s.find('o'))
print(s.rfind('o'))
# find랑 index랑 차이??
print(s.index('r'))
# 갯수
print(s.count('n'))

print()
print('a' in s)
print('pro' in s)
print('x' not in s)

name = "안준석"
if name.startswith("김"):
    print("김 가입니다")
if name.startswith("안"):
    print("안 가입니다")

file = "girl.jpg"
if(file.endswith(".jpg")):
    print("jpg file")

height = input("키를 입력하세요 : ")
if height.isdecimal():
    print("키 = ", height)
else:
    print("int만 입력하세요")

print()
print(s.lower())
print(s.upper())

# 대소문자 정반대
print(s.swapcase())
# 첫글자 대문자
print(s.capitalize())
# 문장 첫글자 대문자
print(s.title())

s = "    blank      blank  "
print(s.lstrip() + "1")
print(s.rstrip() + "1")
print(s.strip() + "1")

print()
s = "a b c"
print(s.split())
s = "a->b->c"
print(s.split("->"))
for i in s :
    print(i, " and ", end = ' ')

print()
traveler = """강나루 건너서\n밀밭 길을\n\n구름에 달 가듯이\n가는 나그네\n
길은 이줄기\n남도 삼백리\n\n술 익는 마을마다\n타는 저녁놀\n
구름에 달 가듯이\n가는 나그네"""
poet = traveler.splitlines()
for line in poet :
    print(line)

s = "._."
print(s.join("\n대한민국"))

s = "abc"
s2 = " -> "
print(s2.join(s))

s= "a b c"
s2= s.split()
print(" and ".join(s2))

s = "apple is apple"
print(s.replace("apple", "banana"))

hello = "안녕하세요"
print(hello.ljust(30))
# 총 문자열이 30줄 즉, 안녕하세요5자를뺀 25자의 공백이 왼쪽에삽입된다
print(hello.rjust(30))
# 왼쪽12자, 오른쪽13자의 공백이 삽입된다
print(hello.center(30))

print()


traveler = """강나루 건너서\n밀밭 길을\n\n구름에 달 가듯이\n가는 나그네\n
길은 이줄기\n남도 삼백리\n\n술 익는 마을마다\n타는 저녁놀\n
구름에 달 가듯이\n가는 나그네"""
poet = traveler.splitlines()
for line in poet :
    print(line.center(30))