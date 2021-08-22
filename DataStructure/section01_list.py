# 파이썬 자료구조
# 1. 배열


# 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
# 같은 종류의 데이터를 순차적으로 저장

# 장점:
# 빠른 접근 가능
# 첫 데이터의 위치에서 상대적인 위치로 데이터 접근(인덱스 번호로 접근)

# 단점:
# 데이터 추가/삭제의 어려움
# 미리 최대 길이를 지정해야 함 (파이썬은 해당사항없음)


# 1차원 배열: 리스트로 구현시
data_list = [1, 2, 3, 4, 5]
print(data_list)

# 2차원 배열: 리스트로 구현시
data_list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data_list2)

print()
print()

# 파이썬 배열은 동적
# 자바의 Collection framework List 와 비슷
lenTest = [1, 2, 4]
print(len(lenTest))
del lenTest[2]
print(len(lenTest))

print()
print()

# 연습1: 위의 2차원 배열에서 9, 8, 7 을 순서대로 출력해보기
print(data_list2[2][2])
print(data_list2[2][1])
print(data_list2[2][0])

print()
print()

# 연습2: 위의 dataset 리스트에서 전체 이름 안에 M 은 몇 번 나왔는지 빈도수 출력하기


dataset = ['Braund, Mr. Owen Harris',
           'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
           'Heikkinen, Miss. Laina',
           'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
           'Allen, Mr. William Henry',
           'Moran, Mr. James',
           'McCarthy, Mr. Timothy J',
           'Palsson, Master. Gosta Leonard',
           'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
           'Nasser, Mrs. Nicholas (Adele Achem)',
           'Sandstrom, Miss. Marguerite Rut',
           'Bonnell, Miss. Elizabeth',
           'Saundercock, Mr. William Henry',
           'Andersson, Mr. Anders Johan',
           'Vestrom, Miss. Hulda Amanda Adolfina',
           'Hewlett, Mrs. (Mary D Kingcome) ',
           'Rice, Master. Eugene',
           'Williams, Mr. Charles Eugene',
           'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
           'Masselmani, Mrs. Fatima',
           'Fynney, Mr. Joseph J',
           'Beesley, Mr. Lawrence',
           'McGowan, Miss. Anna "Annie"',
           'Sloper, Mr. William Thompson',
           'Palsson, Miss. Torborg Danira',
           'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
           'Emir, Mr. Farred Chehab',
           'Fortune, Mr. Charles Alexander',
           'Dwyer, Miss. Ellen "Nellie"',
           'Todoroff, Mr. Lalio']

count = 0

for word in dataset:
    for char in word:
        # 혹은 for char in range(len(word))

        if char == 'M':
            count += 1

print(count)
