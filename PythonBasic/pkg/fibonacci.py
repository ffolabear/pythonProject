class Fibonacci:
    # 기본값이 넘어오면 사용하고 넘어오지 않으면 fibonacci로 title 설정
    def __init__(self, title="fibonacci"):
        self.title = title

    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print()

    def fib2(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        return result
