# Section10_1
# 파이썬 예외의 예시

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 방생하는 예외 처리도 중요

# linter : 코드 스타일, 문법 체크

# SystaxError

# 1. 따옴표를 닫지 않은 경우
# - print('Test)

# 2. 콜론을 찍지 않은 경우
# if True
#     pass

# 3. 존재하지 않는 문법
# x => y

# 4. NameError : 참조변수 없음
# a = 10
# b = 15
# print(c)

# 5. ZeroDivisionError : 0으로 나누기 에러
# print(10/0)

# 6. IndexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3])

# 7. KeyError
dic = {
    'name': 'kim',
    'age': 44,
    'city': 'seoul'
}

# 8. 존재하지 않는 키값을 출력
# print(dic['hobby'])
# 이런 오류를 반지하기 위해서 get 메소드를 사용 -> 에러발생 대신 None 을 리턴
print(dic.get('hobby'))

# 9. AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예와
import time

print(time.time())
# 없는 속성이므로 없는것을 부르는 것은 불가능
# print(time.month())


# 10. ValueError : 참조값이 없을때 발생
x = [1, 5, 9]

# x.remove(3)
# x.index(3)

# 11. FileNotFoundError
# f = open('test.txt', 'r')  해당 경로에 파일이 없을때 발생

# TypeError

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)
# print(x + z)

print(x + list(y))
