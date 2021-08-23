# Section07_1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스의 차이가 중요!!!!!!!!!
# 네임스페이스 : 객체를 인스턴스화할때 저장된 공간

# 클래스 변수 : 직접 사용가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제
# 클래스 이름은 대문자로
# 카멜케이스를 사용해서 이름지음

# 사람의 정보를 저장하는 클래스
class UserInfo:
    # 속성과 메소드
    # 초기화 하는 함수
    def __init__(self, name):
        self.name = name
        print("초기화 : ", name)

    def user_info_p(self):
        print("이름 : ", self.name)


# 인스턴스화 해서 메모리 상에 올려주면
# user1 에 클래스가 할당되고 초기화 메소드 __init__ 이 실행

# 각 객체의 네임스페이스(객체 별로 가지고 있는 공간)에 그 객체만의 값이 들어있음
user1 = UserInfo("FF")
user1.user_info_p()
print("id : ", id(user1))
print("네임스페이스 : ", user1.__dict__)

print()

user2 = UserInfo("KK")
user2.user_info_p()
print("id : ", id(user2))
print("네임스페이스 : ", user2.__dict__)

# 각 네임스페이스는 딕셔너리
print(type(user1.__dict__))

print()
print()


# self

# 예제2

class SelfTest:

    def function1():
        print("funtion1 called")

    def function2(self):
        print(id(self))
        print("funtion2 called")


self_test = SelfTest()

# 클래스 메소드이므로 인스턴스에서 호출할 수 없음
# self_test.function1()
# 다음과 같이 호출해야함
SelfTest.function1()

# 인스턴스의 id와 function2)에서 출력한 id가 같음
# -> 인스턴스의 self 인자가 function2 로 넘어감

print()
print()

self_test.function2()
print(id(self_test))

print()
print()

# 인스턴스 메소드이므로 self 인자가 없어서 호출 할 수 없음
# SelfTest.function2()
# 다음과 같이 직접 self에 해당하는 인자를 넣어줘야 호출 가능

SelfTest.function2(self_test)

print()
print()


# 예제3
# 클래스 변수, 인스턴스 변수
# (인스턴스 변수는 무조건 self가 들어가야함!! 클래스 변수는 self가 없음!! )


class WareHouse:
    # self가 없기때문에 공유하는 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

# 클래스 변수이므로 인스턴스의 네임스페이스에는 없음
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__)

print()
print()

print(user1.name)
print(user2.name)
print(user3.name)

print()
print()

# stock_num 은 인스턴스의 네임스페이스에는 존재하지 않지만 출력가능
# 자기 네임스페이스에 없으면 클래스의 네임스페이스에서 찾음
print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

print()
print()

del user3

# 클래스 변수이므로 객체를 삭제해주면 전체적으로 감소된 값을 공유
print(user1.stock_num)
print(user2.stock_num)
