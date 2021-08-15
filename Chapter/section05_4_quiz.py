# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

print("1. ")
for one in q1.keys():
    if one == "가을":
        print(q1[one])

print()

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

print("2. ")
for two in q2.values():
    if two == "사과":
        print("포함되었음")

print()

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

print("3. ")

q3 = 64

while q3 <= 100:
    if q3 > 80:
        print("A학점")
        break
    elif q3 > 60:
        print("B학점")
        break
    elif q3 > 40:
        print("C학점")
        break
    elif q3 > 20:
        print("D학점")
        break
    else:
        print("B학점")
        break

print()

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

print("4. ")
q4 = [12, 6, 18]

cnt = 0
for i in q4:
    if i > cnt:
        cnt = i

print(cnt)
print()

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

print("5. ")

s = '891022-2473837'

if s[7] == 1 or 3:
    print("남자")
elif s[7] == 2 or 3:
    print("남자")
else:
    print("주민등록번호가 이상합니다.")

print()

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

print("6. ")

for six in q3:
    if six == "정":
        continue
    else:
        print(six, end=' ')

print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

print("7. ")

seven = ""
for i in range(1, 101):
    if i % 2 == 1:
        seven += str(i) + " "

print(seven)
print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

print("8. ")

for eight in q4:
    if len(eight) >= 5:
        print(eight)

print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

print("9. ")

for i in q5:
    if i.islower():
        print(i)

print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

print("10. ")

for i in q6:
    if i.islower():
        print(i.upper())
    else:
        print(i.lower())

print()

# List Comprehension
# 쉽게 List를 만드는 법

# 일반적인 방법
number = []
for n in range(1, 101):
    number.append(n)
print(number)

print()

# List Comprehension
number2 = [x for x in range(1, 101)]
print(number2)

# List Comprehension 를 활용해서 푸는 방법
q5 = [x for x in q3 if x != '정']
print(q5)

q6 = [x for x in range(1, 101) if x % 2 == 1]
print(q6)
