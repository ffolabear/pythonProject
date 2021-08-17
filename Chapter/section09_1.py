# Section09_1
# 파일 읽기

# 읽기 모드 r
# 쓰기 모드(기존 파일 삭제) : w
# 추가 모드(파일 생성 또는 추가) : a

# .. : 상대 경로, . : 절대 경로

# 파일 읽기

# 예제1
# 파일을 읽기전에는 파일을 먼저 열어줘야함
f = open('./resource/lorenipsum.txt', 'r')
content = f.read()
print(content)
print(dir(content))

# 파일을 읽은 다음에 반드시 받아줘야함
f.close()

print()
print('---------------------------------------')
print('---------------------------------------')
print()

# 예제2
# with문은 자동으로 리소스를 닫아줌
with open('./resource/lorenipsum.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print()
print('---------------------------------------')
print('---------------------------------------')
print()

# 예제3

with open('./resource/lorenipsum.txt', 'r') as f:
    # 이미 f가 iterable 하기 떄문에 반복문을 돌릴수 있음
    for c in f:
        # 라인 단위로 가져옴
        # strip() 함수를 통해 양쪽 공백을 제거
        print(c.strip())

print()
print('---------------------------------------')
print('---------------------------------------')
print()


# 예제4

with open('./resource/lorenipsum.txt', 'r') as f:
    content = f.read()
    print(">", content)
    # 한번 읽은 파일은 커서가 끝부분에 위치하기 때문에 더이상 읽을 파일이 없음
    content = f.read()
    print(">", content)

print()
print('---------------------------------------')
print('---------------------------------------')
print()


# 예제5

with open('./resource/lorenipsum.txt', 'r') as f:
    # 한줄 한줄 읽기
    line = f.readline()
    # print(line)
    # line이 True일 동안 -> line이 존재할 동안
    while line:
        print(line, end='$$$')
        line = f.readline()

print()
print('---------------------------------------')
print('---------------------------------------')
print()

# 예제6

with open('./resource/lorenipsum.txt', 'r') as f:
    # list 형태로 줄 끝마다 \n을 붙여서 가지고 있음
    contents = f.readlines()
    # print(contents)

    for c in contents:
        print(c, end=' +++++ ')

    print(" 길이 : ", len(contents))


print()
print('---------------------------------------')
print('---------------------------------------')
print()


# 예제7
score = []

with open('resource/score.txt', 'r') as f:
    for line in f:
        # txt 파일에 저장되어있는 것은 문자 취급하기 때문에 형변환을 해줘야함
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))


