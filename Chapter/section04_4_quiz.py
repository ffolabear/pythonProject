# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print("1. ")
print(len(q1))

print()

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print("2. ")
print("apple", "orange", "banana", "lemon", sep=';')
print()

# 3. 화면에 * 기호 100개를 표시하세요.
print("3. ")
print("*" * 100)
print()


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
print("4. ")
three = "30"
print(int(three), float(three), complex(three), str(three))
print()

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
print("5. ")
five = "Niceman"
print(five[4:])
print(five[4:7])
five_idx = five.index("man")
print(five_idx)
print(five[five_idx:7])
print()


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
print("6. ")
six = "Strawberry"
print(six[::-1])
six2 = reversed(six)
print(''.join(six2))
print()


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
print("7. ")
seven = "010-7777-9999"
print(seven.replace('-', ''))

# 정규식
import re
print(re.sub('[^0-9]', '', seven))

print()


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
print("8. ")
eight = "http://daum.net"
print(eight.replace("http://", ''))
print(eight[7:])
print(eight[7:len(eight)])
print()


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
print("9. ")
nine = "NiceMan"
print(nine.lower())
print(nine.upper())
print()


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
print("10. ")
ten = "abcdefghijklmn"
print(ten[2:5])
print()


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
print("11. ")
eleven = ["Banana", "Apple", "Orange"]
eleven.remove("Apple")
print(eleven)
print()


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
print("12. ")
twelve = (1, 2, 3, 4)
print(list(twelve))
print()


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
print("13. ")
thirteen = {
    "성인": 100000,
    "청소년": 70000,
    "아동": 30000
}
print(thirteen)
print()


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
print("14. ")
thirteen["소아"] = 0
print(thirteen)
print()


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print("15. ")
print(thirteen.keys())
print()


# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print("16. ")
print(thirteen.values())
print()


# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
