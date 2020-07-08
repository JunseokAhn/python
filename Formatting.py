price = 500
print("이렇게하면 문장안에" + " 숫자형을 붙일수있다 " + str(price) )
print("이것도 된다 %d" % price)


# % d더블 f플롯 s스트링 c캐릭터 h헥타르 o옥트 %% %문자
month = 1
day = 1
anni = "신년"
print("%d월 %d일은 %s이다" %(month, day, anni))
print(str(month) + '월 ' + str(day) + '일은 ' + anni+'이다' )

value = 123
print("###%d###" %value)
# 총5글자 즉 2글자가 왼쪽에 삽입된다.
print("###%5d###" %value)
print("###%10d###" %value)
print("###%1d###" %value)

price = 500, 1500, 15000
for p in price :
    print("가격 : %5d원" %p)


for p in price :
    print("가격 : %-5d원" %p)

pie = 3.14159265

print("%f" %pie)
print("%10f" %pie)
print("%10.8f" %pie)
print("%10.10f" %pie)
print("%10.4f" %3)
print("%10.5f" %pie)
print("%10.2f" %pie)

name = "준석"
age = 29
height = 167.7
print("이름:{}, 나이:{}, 키:{}".format(name, age, height))

print("이름:{1}, 나이:{0}, 키:{2}".format(name, age, height))


# 키워드인수를 사용하는 경우, 지역변수를 사용하기때문에, 직접 지정해줘야된다.
print("이름:{height}, 나이:{name}, 키:{age}".format(name="준석", age=29, height=167.7))

boy = {"name" : "한결",
       "age" : 16,
       "height" : 162.5}

print("이름 : {0[name]}, 나이 : {0[age]}, 키 : {0[height]}".format(boy))

name = "한결"
age = 16
height = 162.5

# 인덱스와 타입을 한꺼번에 지정할때는 인덱스:타입
print("이름 : {0:s}, 나이 : {1:d}, 키 : {2:4.1f}".format(name, age, height))

print("이름 : {0:10s}, 나이 : {1:5d}, 키 : {2:4.1f}".format(name, age, height))

# ^가운데정렬 <왼쪽정렬 >오른쪽정렬
print("이름 : {0:^10s}, 나이 : {1:>5d}, 키 : {2:<4.1f}".format(name, age, height))

# 정렬문자앞에 문자입력하면 공백대신에 채움문자 출력(한글자)
print("이름 : {0:!^10s}, 나이 : {1:0>5d}, 키 : {2:あ<10.1f}".format(name, age, height))
