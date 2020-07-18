score = "40点"
try:
    score = int(score)
    print(score)
except:
    print("例外が発生しますた。")

# NameError 초기화되지않은 변수를 사용할때 발생
# ValueError 타입은맞는데 값의 형식이 잘못됨
# ZeroDivisiionError 0으로 나눔
# IndexError 인덱스범위벗어남
# TypeError 타입이 틀림 int String...

score = 40, 50
try:
    print(score[5])
except ValueError:
    print("形式が間違っています。")
except IndexError as e:
    print("インデックスが間違っています。")
    print(e)
except:
    print("知らないエラー発生！")

dic = {'boy' : '소년',
        'school' : '학교',
        'book' : '책'
      }
try :
    print(dic['girl'])
except :
    print("찾는 단어가 없습니다")

han = dic.get('girl')
if (han == None) :
    print("찾는 단어가 없습니다")

# 에러 강제발생
def calsum(n) :
    if(n<0) :
        raise ValueError
    sum=0
    for i in range(n+1):
        print(i, end='')
        sum+=i
    print()
    return sum

try:
    print(calsum(10))
    print(calsum(-1))
    print(calsum(10))
except:
    print("에러 발생")
finally:
    print("계산 종료")

score = 70
assert score<=80, "점수는 80점 이하여야 합니다."
assert score>=80, "점수는 80점 이상이어야 합니다."