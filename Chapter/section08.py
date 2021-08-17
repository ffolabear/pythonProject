# Section08
# 파이썬 모듈과 패키지

# 파이썬 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)
print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용2(클래스) - 권장 X
from pkg.fibonacci import *

Fibonacci.fib(300)
print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(300)
print("ex2 : ", fb.fib2(400))
print("ex2 : ", fb().title)

# 사용4(함수)
import pkg.calculation as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))
print("ex4 : ", c.div(10, 100))

# 사용5(함수) - 권장
from pkg.calculation import div as c

print("ex5 : ", int(c(100, 10)))

# 사용6
import pkg.prints as p
import builtins

p.prt()
p.prt2()
print(dir(builtins))
