# Section06_2
# 파이썬 람다식


# 메모리 절약, 가독석 향상, 코드 간결

# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 (Heap 초기화) -> 메모리 초기화


# 일반 함수와 비교

def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
# 생성한 객체의 주소를 출력 -> 메모리를 점유하고 있음
# 함수도 객체
print(var_func, var_func(10), type(var_func), sep='      ')

print()
print()

# 람다함수
# 주로 익명함수를 사용할때 선언
# 메모리를 절약한다는 장점이 있지만 가독성이 좋지않음

# num이 인자
lambda_mul_10 = lambda num: num * 10
print(lambda_mul_10, lambda_mul_10(10), type(lambda_mul_10), sep='   ')

print()
print()


def func_final(x, y, func):
    print(x * y * func(10))


# 10 * 10 * 람다(10 * 10) = 10000
func_final(10, 10, lambda_mul_10)

# 간편하게 선언 및 사용 가능
# 10 * 10 * 새로운 람다(10 * 1000) = 1000000
func_final(10, 10, lambda x: x * 1000)
