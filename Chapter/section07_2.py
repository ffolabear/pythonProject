# Section07_2
# 파이썬 클래스 상세 이해
# 상속, 다중상속


# 예제1
# 상속 기본
# 코드의 재사용성, 가독성 증가

# 슈퍼클래스(부모) -> 서브클래스(자식)
# 자식 클래스는 부모클래스의 모든 속성, 메소드 사용 가능


class Car:
    """Parent Class"""

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        return "Super Class 'Show Method!'"


class BMW(Car):
    """Sub Class"""

    def __init__(self, car_name, type, color):
        # 부모의 초기화 메소드를 호출
        super().__init__(type, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class Benz(Car):
    """Sub Class"""

    def __init__(self, type, color, car_name):
        # 부모의 초기화 메소드를 호출
        super().__init__(type, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    # 부모에도 있는 show 메소드를 재정의
    def show(self):
        print(super().show())
        return 'Benz info : %s %s %s' % (self.car_name, self.type, self.color)


# 일반 사용 방법


model1 = BMW('520d', 'sedan', 'red')

# 부모 클래스에서 상속받음
print(model1.color, id(model1.color))
print(model1.type, id(model1.type))
print(model1.show())
print(id(Car))

print()

# 자식 클래스
print(model1.car_name, id(model1.car_name))
print(model1.show_model())
print(id(model1))

print(model1.__dict__)

print()

# 메소드 오버라이딩
# 오버로딩 은 없음
# 부모에도 있는 메소드를 재정의

model2 = Benz('220d', 'suv', 'green')
print(model2.show())

print()

# Parnet Method Cal
# super 키워드를 통해서 부모의 메소드도 호출해줬음

model3 = Benz('GLP', ' coupe', 'navy')

print(model3.show())

print()

# 상속관계가 깊을때 깊이를 list에 담아서 리턴해주는 메소드

# -> 오른쪽으로 갈수록 더 큰 범위
# 모든 클래스는 Object 클래스를 상속받는다

print(BMW.mro())
print(Benz.mro())
print(type(Benz.mro()))

print()
print()


# 다중 상속
# 하지만 복잡한 다중 상속은 연관관계의 파악이 어려워 구조파악이 어려움

# 모든 클래스는 Object를 상속받는다는 명시적 표현. 없어도 무방함

class X(object):
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class C(B, A, Z):
    pass


print(C.mro())
print(A.mro())
