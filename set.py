asia = {'korea', 'china', 'japan', 'korea'}
print(asia)

print(set("samsung"))
print(set([12,34,56,6]))
print(set({
    '時点':"시점",
    '取り戻す':"되돌리다",
    '抱える':"맡다",
    '緊急':'긴급',
    '寄る':'들르다'
}))

asia.add('vietnam')
# 이미 있는건 추가안됨, 집합은 중복이 불가하다
asia.add('china')
print(asia)
asia.remove('china')

asia.update({'singapore', 'hongkong', 'korea'})
print(asia)

two = {2,4,6,8,10}
three = {3,6,9}

print("교집합", two & three)
print("합집합", two | three)
print("차집합", two - three)
print("배타적 차집합", two ^ three)

mammal = {'코끼리', '고릴라', '사자', '고래', '사람', '원숭이', '개'}
primate = {'사람', '원숭이', '고릴라'}

if '사자' in mammal :
    print("사자는 포유류이다")
else : 
    print("사자는 포유류가 아니다")

print(primate <= mammal)
print(primate < mammal)
print(primate <= primate)
print(primate < primate)