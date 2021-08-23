# Section10_2
# 파이썬 예외 처리

# 예외 처리 기본

# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

print()
print()

# 예제1

name = ['Kim', 'Park', 'Lee']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z))

except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print("Ok! Next!")


print()
print()

# 예제2

try:
    z = 'Kf'
    x = name.index(z)
    print('{} Found it! in name'.format(z))

# 어떤 에러가 발생할지 모를떄는 에러명을 명시해주지 않는다
except:
    print('Not found it! - Error!')
else:
    print("Ok! Next!")

print()
print()

# 예제3

try:
    z = 'Kf'
    x = name.index(z)
    print('{} Found it! in name'.format(z))

# 어떤 에러가 발생할지 모를떄는 에러명을 명시해주지 않는다
except:
    print('Not found it! - Error!')
else:
    print("Ok! Next!")
# 무조건 해줘야하는 작업이 있을때 작성 ex) DBConnection 종료
finally:
    print("Finally ok!")

print()
print()

# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('Ok Finally!!')

print()
print()

# 예제5
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z))

# 에러마다 명시해주는 것이 파악할때는 좋음

except ValueError as l:
    print(l)
except IndexError:
    print('Not found it! - IndexError!')
except Exception:
    print('Not found it! - Error!')
else:
    print("Ok! Next!")
finally:
    print("Finally ok!")


print()
print()

# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kss'
    if a == 'Kim':
        print('ok 허락!')
    else:
        # 상황에 맞지 않는 에러라도 원하는 에러로 발생시킬수 있음
        raise ValueError

# 위에서 명시한 ValueError를 처리하는 곳
except ValueError:
    print("문제 발생!")

except Exception as f:
    print(f)
else:
    print('Ok!')