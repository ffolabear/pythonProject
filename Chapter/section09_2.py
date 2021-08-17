# Section09_2
# 파이썬 파일 쓰기

# 예제1
# 'r' -> 'w' 로 바꿔주기
with open('resource/test_1.txt', 'w') as f:
    f.write('Python!!!!!!\n')


# 예제2
# 'a' 를 해주면 더해주기
with open('resource/test_1.txt', 'a') as f:
    f.write('Java!!!!!!\n')


# 예제3
from random import randint

with open('resource/test_2.txt', 'w') as f:
    for cnt in range(6):
        # 형변환을 해주지 않으면 쓸수가 없음
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4
# writelines : 리스트를 파일로 저장
with open('resource/test_3.txt', 'w') as f:
    list = ['kim\n', 'park\n', 'see\n']
    f.writelines(list)

# 에제5
with open('resource/test_4.txt', 'w') as f:
    # 콘솔에 찍히는 것이 아니라 파일로 써짐
    # 로그의 기록에 활용할 수 있음
    print('Test Contents 1!', file=f)
    print('Test Contents 2!', file=f)