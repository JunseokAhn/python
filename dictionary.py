# 맵이랑 똑같음

dic = {
    '時点':"시점",
    '取り戻す':"되돌리다",
    '抱える':"맡다",
    '緊急':'긴급',
    '寄る':'들르다'
    }
print(dic)
print(dic['寄る'])
print(dic.get('伺う'))
print(dic.get('伺う', '辞書にはない単語です。'))

if '伺う' in dic :
    print('辞書にある単語です。')
else :
    print('辞書にない単語です。')

dic['時点'] = 'ziten'
del dic['取り戻す']
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

keyList = dic.keys()
for i in keyList :
    print(i)

# keyList가 진짜 리스트는 아니다.
keyList = list(keyList)

dic2 = {
    '辞書':'사전',
    '時点':'시점',
    '驚く':'놀라다'
}
# 키 값이같으면 밸류가 수정되고, 같은 키값이 아니면 추가됨
dic.update(dic2)
print(dic)

# 2차원리스트를 사전으로 변경
li = [['1', 1], ['2', 2], ['3', 3]]
dic2 = dict(li)
print(dic2)

# 사전은 키의중복을 허용하지 않으므로, 연관된 정보를 저장할때 유용하다.
song = """You raise me up, so I can stand on mountains
You raise me up to walk on stormy seas
I am strong when I am on your shoulders
You raise me up to more than I can be"""

alphabet = dict()
for i in song :
    if i.isalpha() == False :
        continue
    i = i.lower()
    if i not in alphabet :
        alphabet[i] = 1
    else :
        alphabet[i] += 1
print(alphabet)

key = list(alphabet.keys())
key.sort()
for i in key:
    num = alphabet[i]
    print(i, "=>", num)