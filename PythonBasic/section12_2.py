# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3
from sqlite3.dbapi2 import Row

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect('./resource/database_1.db')         # 본인 DB 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
# 출력값이 있는것이 아니라 커서의 위치를 변경해준것
c.execute("SELECT * FROM users")

# 커서의 위치 변경
# 1개 로우 선택
# print('One : \n', c.fetchone())

# 지정 로우 선택
# print('Three(ex) : \n', c.fetchmany(size=3))

# 전체 로우 선택
# 5개의 데이터중 - 1개 - 3개 를 했으므로 한개의 데이터만 출력됨
# print('All : \n', c.fetchall())




# 데이터 순회해서 조회
# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 : ', row)


print()
print()

# 순회2 - 좀더 빠르고 더 많이 사용되는 방법
# for row in c.fetchall():
#     print('retrieve2 : ', row)

# 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrieve3 : ', row)


# WHERE 절로 검색하기1
param1 = (3, )
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1 : ', c.fetchone())
# 하나만 가져왔으므로 출력이 되지 않음
print('param1 : ', c.fetchall())

print()
print()

# WHERE 절로 검색하기2
# Integer를 id에 바인딩하기
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2 )
print('param2 : ', c.fetchone())
print('param2 : ', c.fetchall())

print()
print()


# WHERE 절로 검색하기3
# 딕셔너리로 가져오기

c.execute('SELECT * FROM users WHERE id=:Id', {"Id" : 5})
print('param3 : ', c.fetchone())
print('param3 : ', c.fetchall())

print()
print()


# WHERE 절로 검색하기4
# OR, IN 사용하기
param4 = (3, 4)
c.execute('SELECT * FROM users WHERE id IN(?, ?)', param4)
print('param4 : ', c.fetchall())

print()
print()


# WHERE 절로 검색하기5
# OR, IN 사용하기
c.execute('SELECT * FROM users WHERE id IN(%d, %d)' % (3, 4))
print('param5 : ', c.fetchall())

print()
print()


# WHERE 절로 검색하기6
c.execute('SELECT * FROM users WHERE id=:id1 or id=:id2', {"id1" : 2, "id2" : 5})
print('param6 : ', c.fetchall())


# Dump 출력 - 백업
# 생성된 sql을 실행시켜주면 데이터기 생성됨
with conn:
    with open('./resource/dump_210819.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')


# f.close(), conn.close() 함수 내부적으로 호출됨

