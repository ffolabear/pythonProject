# 파이썬 기초
# oop 연습문제

# 계좌 클래스 만들기
# attribute : 계좌 초기금액
# 생성자에서 초기금액은 0으로 성정
# 속성은 private로 설정
# method : 인출, 저축, 잔약 세가지. 각각 현재 금액 리턴
# 각 method는 private 으로 설정

class Account:

    def __init__(self):
        self.__base = 0

    def withdraw(self):
        return self.__base

    def deposit(self, money):
        self.__base = self.__base + money
        return self.__base


kookmin = Account()
print(kookmin.deposit(1000))


# 학생 성적 관리 class 만들기
# attribute : 국어, 영어, 수학점수 및 학생 이름
# 생성자에서 각 속성을 객체 생성시 전달된 인자값으로 설정
# 각 속성은 private으로 설정
# method : 전체 과목 점수 평균, 전체 과목 총점 리턴
# 각 method 는 private 으로 설정

class Score:

    def __init__(self, _kor=None, _eng=None, _math=None):
        self._kor = 0
        self._eng = 0
        self._math = 0

    def __total(self):
        return self._eng + self._kor + self._math

    def __avg(self):
        return (self._eng + self._kor + self._math) // 3


# 피자가게 관리 class
# attribute : 피자종류(리스트), 피자 가게 이름
# 생성자에서 각 속성을 객체 생성시 전달된 인자값으로 설정, 피자 종륲는 (슈퍼슈프림, '콤비네이션', '치즈')
# 각 속성은 private으로 설정
# method : 원하는 피자를 제공하는지 알려주는 기능. YES 또는 NO 리턴

class Pizzeria:

    def __init__(self, _store=None):
        self._store = _store
        self._pizza = list()
        self._pizza.append('슈퍼슈프림')
        self._pizza.append('콤비네이션')
        self._pizza.append('치즈')

    def order(self, order):
        for i in self._pizza:
            if order == i:
                return 'YES'
            else:
                return 'No'


domino = Pizzeria()
print(domino.order('슈퍼슈프림'))
print(domino.order('불고기'))
