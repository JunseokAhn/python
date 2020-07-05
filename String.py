s = "python"
print(s[2], s[-2])

for c in s :
    print(c, end=',')
print()

for i in range(len(s)):
    print(s[i], end=',')
print()

# 이거 안됨. 파이썬에서 string은 편집이 금지된다.
# s[2] = 'k'
# 숫자는 됨
a = 10
a = 20
print(20)

# index 2 ~ < index5
print(s[2:5])
# index 3>
print(s[3:])
# index 4<
print(s[:4])
# index 2> ~ -2<
print(s[2:-2])

days = "월화수목금토일"

print(days[::2])
print(days[::-1])