# Section06_1
# 파이썬 함수식

# 함수 정의
# def 함수명(parameter):
#   코드...

# 함수(의 호출
# 함수명()

#  함수 선언의 위치 중요!

# 예제 1


def hello(word):
    print("Hello", word)


hello("python")
hello(7777)


# 예제 2 - 리턴값이 있는 함수
def hello_return(word):
    val = "Hello " + str(word)
    return val


str = hello_return("ddd")
print(str)


# 예제 3 - 다중 리턴
def func_mul(x):
    a = x * 100
    b = x * 200
    c = x * 300
    return a, b, c


ans1, ans2, ans3 = func_mul(1)
print(ans1, ans2, ans3)


# 예제 4 - 데이터 타입변환
def func_mul2(x):
    a = x * 100
    b = x * 200
    c = x * 300
    # 튜플로 리턴받기
    return (a, b, c)


tuple = func_mul2(1)
print(type(tuple), tuple)

print()
print()


# 예제4
#  *args, *kwargs

# *args
# 가변인자

def args_func(*args):
    print(args, type(args))
    for t in args:
        print(t)


# 튜플로 리턴하기 떄문에 iterator 사용가능
args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')


# enumerate 인덱스를 만들어서 순회가능
def args_func2(*args):
    for i, v in enumerate(args):
        print(i, v)


args_func2('a', 'b', 'c')


def args_func3(*args):
    # 인덱스도 만들고 숫자도 출력가능
    for i, v in enumerate(range(10)):
        print(i, v)


args_func3('a')

print()
print()


# *kwargs
# 키워드의 줄인말

# * 한 개면 Tuple 로

def kwargs_func2(*kwargs):
    for i in kwargs:
        print(i)
    print(type(kwargs))


kwargs1 = kwargs_func2('a', 'b', 'c')
print(kwargs1, type(kwargs1))


# * 두 개면 Dictionary 로

def kwargs_func(**kwargs):
    for i, v in kwargs.items():
        print(i, v)
    print(type(kwargs))


kwargs_func(name1='Kim', name2='Park', name3='Lee')

print()
print()


# 여러가지 혼합해서 사용하기

# 필수인자 : arg1, arg2
# 가변인자 : *args(튜플), **kwargs(딕셔너리)

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)
    print(type(args), type(kwargs))


# 필수인자만 전달해주면 함수의 호출에 문제없음
example_mul("필수인자만 전달\n", 10, 20)
print()
example_mul("필수인자만 전달\n", 10, 20, 'park', 'kim', age1=25, age2=30)

print()
print()


# 중첩함수 - 클로져
# 데코레이터 활용에 응용

# 예제 5
def nested_func(num):
    def func_in_func(num):
        print("in nested", num)

    print("in func: ", num)
    func_in_func(num + 10000)


nested_func(10000)

print()
print()


# 예제 6 - 힌트
# (hint)

# 인자의 타입과 리턴 타입이 뭔지 알게해줌
# 코드의 실행에 영향을 미치지는 않음

def func_mul2(x: int) -> list:
    a = x * 100
    b = x * 200
    c = x * 300

    return [a, b, c]
