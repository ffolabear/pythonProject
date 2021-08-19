# Section 13-1
# 파이썬 타이핑 게임 제작
# 타이핑 게임 제장 및 기본 완성


import random
import time

# 영어단어 리스트
words = []

# 게임 시도 횟수
n = 1

# 정답 갯수
cor_cnt = 0

with open('./resource/word.txt', 'r') as f:
    for c in f:
        # 단어 양쪽별 공백을 제거
        words.append(c.strip())

# 단어 리스트 확인
# print(words)

# 사용자의 입력을 처리하는 함수
input("Press Enter when you ready!")

# 게임 시작 시간
start = time.time()

# 게임은 총 5번 실행
while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()
    print(" - Question # {}".format(n))
    print(q)

    # 타이핑 입력
    x = input()
    print()

    if (str(q).strip() == str(x).strip()):
        print("Correct!")
        # 정답 1증가
        cor_cnt += 1
    else:
        print('Wrong')

    n += 1

# 게임 종료시간
end = time.time()

# 게임 플레이 타임 계산
playtime = end - start
# 소수3째 자리까지 출력
playtime = format(playtime, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

print("게임 시간 : ", playtime, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass
