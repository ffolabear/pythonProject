# Section11
# 파이썬 외부 파일 처리
# Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME 형식 -> text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r', encoding='CP949') as f:
    reader = csv.reader(f)
    # 보통 첫라인(Header)은 항목의 이름을 모아놓은 곳이기 때문에 커서를 옮겨줌
    # next(reader)

    # 확인
    print(reader)
    print(type(reader))
    # dir을 찍어보면 iter가 있는것을 알수 있음
    # print(dir(reader))

    for c in reader:
        print(c)

print()
print()

# 예제2
with open('./resource/sample2.csv', 'r', encoding='CP949') as f: \
        # 구분자를 명시해주면 ,로 나눠진 값으로 받음
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)

print()
print()

# 예제3 - Dict 변환
with open('./resource/sample1.csv', 'r', encoding='CP949') as f:
    reader = csv.DictReader(f)
    for c in reader:
        # item 별 key, value 출력
        for k, v in c.items():
            print(k, v)
        print('--------------------')

# 예제4 - csv 파일로 write 하기

w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

# with에서 자체적으로 줄바꿈을 해줌
# newline 옵션을 통해서 줄바꿈을 설정
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    # 자동으로 줄바꿈을 해줌
    for v in w:
        wt.writerow(v)

    # 예제5 - for문 없이 파일 write 쓰기
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    # 만약 줄마다 체크할 필요가 없고 한번에 써도될때 사용
    wt.writerows(w)

print()
print()

# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나
# pandas를 주로 사용(openpyxl (1위), xlrd(2위)) 포함

# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요
# pip install pandas 설치 필요

import pandas as pd

# sheetname='시트명' 또는 숫자, header=3, skiprow=1 실습
# 여러개의 sheet일 경우 숫자로 가져옴
# skiprow 에 가져오지 않을 행 적어줌
xlsx = pd.read_excel('./resource/sample.xlsx', )

# 상위 데이터 확인 1 ~ 5개 까지
print(xlsx.head())

print()

# 하위 데이터 끝 5개
print(xlsx.tail())

print()

# 구조 확인 - 행 / 열
print(xlsx.shape)

# 엑셀 or CSV 로 write 하기
# index 옵션은 열에 번호를 붙여줌
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
