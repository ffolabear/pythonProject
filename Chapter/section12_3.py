# Section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB 생성(파일)
conn = sqlite3.connect('./resource/database_1.db')

# Cursor 연결
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 데이터 수정1
# c.execute("UPDATE users SET username = ? WHERE id=?", ('Park', 2))


# 데이터 수정2
# 콜론은 딕셔너리 키값과 붙어있어야함
# c.execute("UPDATE users SET username = :name WHERE id = :id", {'name': 'Mark', 'id': 2})

# 데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id='%d'" % ('Bark', 2))


# 중간 데이터 확인



# print()
# print()


# 방법1
# rows2 = c.fetchall()
# for row in rows2:
#     print("방법1 : ", row)

# print()
# print()


# 방법2
# for row in c.fetchall():
#     print("방법2 : ", row)


# 방법3
# print("방법3")
# for rows in c.execute("SELECT * FROM users"):
#     print(rows)

print()
print()




# Row delete1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# Row delete2
c.execute("DELETE FROM users WHERE id=:id", {'id':5})

# Row delete3
c.execute("DELETE FROM users WHERE id='%d'" % 3)


# 중간 데이터 확인
for data in c.execute("SELECT * FROM users"):
    print(data)


print()
print()

# 전체 데이터 삭제
print("user DB data deleted : " , conn.execute("DELETE FROM users").rowcount, " rows")

# 커밋
conn.commit()

# 접속 해제
conn.close()