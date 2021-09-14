# print("qq", "vv",sep=" ", end=" ")

import copy

x = 0

# x = [1, 2, (3, 4)]
# x = (1, 2, [3, 4])
# x = (((((1) ,),),),)

print(id(copy.copy(x)))
print(id(copy.deepcopy(x)))


def prob17(a: list[int]):
    a = list(map(str, a))
    b = []
    for idx, s in enumerate(a):
        s = s if s in a[:idx] + a[idx + 1:] else s + ' '
        b += s

    return ''.join(b)


bb = [1, 3, 4]

print(prob17(bb))


# 높이가 n인 M모양의 *을 출력하는 함수

def prob18(height):
    space = 0
    for i in range(1, height + 1):
        if i < height:
            print('*', end="")
            for j in range(1, height):
                if j == i or j == i:
                    print('*', end="")
                else:
                    print(' ', end="")

        elif i == height:
            pass

        print()


prob18(5)


def prob19(x: list[int]):
    for i in x:
        temp = i


p19 = [1, 3, 4, 4, 5, 5, 6]

print(prob19(p19))


def prob20(a: list[int]):
    ans = 0
    for i in range(0, len(a)+1):
        ans += a[i]
        del a[i]
        prob20(a)
    return ans



print(prob20(p19))