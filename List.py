score = [88, 95, 70, 100, 99]
sum = 0
for i in score :
    sum+=i
print("총점 : ", sum)
print("평균 : ", sum/len(score))
print(score[-1])
# 2부터 3전까지 == 2번인덱스만 출력
print(score[2:3])
# 0부터 7까지 2씩 올려가며 출력
print(score[0:7:2])
# 한꺼번에 여러 인덱스 변경가능
score[0:3] = [ 1, 2, 3]
print(score)
# 리스트의 한 인덱스를 여러개로 바꾸면서 삽입가능
score[3:4] = [4, 5, 6, 7, 8, 9, 10]
print(score)
# 8~9번인덱스 삭제
score[8:11] = []
print(score)
# 6~7인덱스삭제
del score[6:8]
print(score)
score2 = [7,8]
score = score + score2
# 리스트끼리 덧셈 가능
print(score)
# 리스트 곱셈가능
score2 = score2*2
print(score2)
# 걍 다됨
score2 = [[1,2,3],[4,5],[6,7,8,9,10]]
print(score2)
print(score2[1])
print(score2[1][1])

score = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7]
]

total = 0
totalsub = 0
for student in score :
    sum = 0
    for subject in student :
        sum+=subject
    print("총점 %d, 평균 %.2f" %(sum, sum/len(student)))
    total += sum
    totalsub += len(student)
print("전체평균 %.2f" % (total/totalsub))

# List Comprehension, 포문을 응용하여 리스트를 정의하는 문법
nums = []
for n in range(1, 11) :
    nums.append(n*2)

# ==
nums = [n*2 for n in range(1,11)]
for i in nums :
    print(i, end= " ")
print()

# if문도 사용가능
nums = [n for n in range(1,11) if n % 3 == 0]
print(nums)

nums = [n*n for n in range(1,11) if n % 3 == 0]
print(nums)