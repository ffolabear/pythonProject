# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)
nowdatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDateTime : ', nowdatetime)

print()

# sqlite3 관련정보 출력
print("sqlite3.version: ", sqlite3.version)
print("sqlite3.sqlite_version: ", sqlite3.sqlite_version)

print()
print()

# DB 생성 & Auto Commit <-> RollBack
# isolation_level=None 설정을 통해 Auto Commit 설정
conn = sqlite3.connect('./resource/database_1.db', isolation_level=None)

# Cursor 가져오기
c = conn.cursor()
print('Cursor Type : ', type(c))

print()
print()

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(\
    id INTEGER PRIMARY KEY,\
    username text,\
    email text,\
    phone text,\
    website text,\
    regdate text)")

# 데이터 삽입
# 방법1
c.execute("INSERT INTO users VALUES (\
    1, 'Kim', 'Abc@gmail.com', '010-0000-0000', 'ABC.com', ?)", (nowdatetime,))

# 방법2
c.execute('INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)',
          (2, 'Park', 'Park@ff.com', '010-1111-1111', 'Park.com', nowdatetime))

# 많은 데이터 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@gmail.com', '010-2222-3333', 'Lee.com', nowdatetime),
    (4, 'cho', 'cho@gmail.com', '010-4444-5555', 'cho.com', nowdatetime),
    (5, 'kee', 'kee@gmail.com', '010-6666-7777', 'kee.com', nowdatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate)\
    VALUES (?, ?, ?, ?, ?, ?)", userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")

# 지운 데이터 확인
# print("users db data deleted : ", conn.execute("DELETE FROM users").rowcount)


# 커밋 : isolation_level = None 일 경우 자동 반영(Auto Commit)
# 아니라면 conn.commit() 실행해줘야함

# 롤백
# conn.rollback() 으로 되돌리기

# 리소스를 사용한 후에는 닫기
conn.close()
