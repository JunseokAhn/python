# r = read
# w = write
# a = add
# x = ?? 기록

# t = 텍스트
# b = 이진파일 binary

f = open("live.txt", "wt")
f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지말라.
우울한 날들을 견디면
기쁨의 날이 오리니""")
f.close()

# 파일 한번에 읽어오기
try:
    f = open("live.txt", "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다")
finally:
    f.close()

# 파일 조금씩 읽어오기(큰 파일 읽기에 유리)
f = open("live.txt", "rt")
while True:
    text = f.read(10)
    if len(text) == 0: break
    print(text, end = '')
f.close()
print()

f = open("live.txt", "rt")
text = ""
line = 1
while True:
    row = f.readline()
    if not row: break
    text += str(line) + " : " + row
    line += 1
f.close()
print(text)

# 가장 간단한 방법
f = open("live.txt", "rt")
for line in f:
    print(line, end='')
f.close()
print()

# seek(시작위치, 기준)
# 기준이0이면 파일처음부터, 1이면 현재위치부터, 2면 끝에서부터
f = open("live.txt", "rt")
f.seek(12,0)
text = f.read()
f.close()
print(text)

f = open("live.txt", "at")
f.write("\n\n푸쉬킨")
f.close()

# with를 사용하면 굳이 close를 안해도 자동으로 닫아줘서 편함
with open("live.txt", "rt") as f:
    text = f.read()
print(text)