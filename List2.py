nums = [1,2,3,4]
nums.append(5)
nums.insert(2,99)
print(nums)

# 2번 인덱스에 삽입 == 2:2도 된다
nums[2:3] = [11,22,33]
print(nums)

nums2 = [44, 55, 66]

nums.extend(nums2)
print(nums)
# == nums = nums + nums2

# 값으로 지우기 remove, 인덱스로지우기 del
nums.remove(11)
del(nums[0])
nums[1:3] = []
print(nums)

print(nums.pop())
print(nums.pop())
print(nums)

# pop으로 빼내고 append로넣으면 FIFO, 스택구조가된다.
print(nums.pop(0))
print(nums.append(2))
print(nums)

print(nums.index(44))
print(nums.count(44))

print(len(nums))
print(max(nums))
print(min(nums))

nums.sort()
nums.reverse()
print(nums)
nums = sorted(nums)
print(nums)


nums = [4,7,1,10,5]
nums.sort(reverse=True)
print(nums)

country = ["Korea", "japan", "CHINA", "America"]
# 대문자끼리 우선비교하게된다.
country.sort()
print(country)
# 그래서 일시적으로 전부 소문자로 바꿔주는 옵션
country.sort(key=str.lower)
print(country)

answer = input("決済しますか？")
if answer in ['yes', 'y', 'ok', '예', 'はい'] :
    print("購入に成功しました！")
else :
    print("購入に失敗しました！")

