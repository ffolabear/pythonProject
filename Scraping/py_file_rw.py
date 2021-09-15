from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
# 파일 이름은 맞게 바꿔주세요!
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(type(lines))
    for line in lines[2:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅠ', '').replace('ㅜ', '')\
                                       .replace('ㅇㅇ', '').replace('아', '').replace('나', '')\
                                       .replace('이모티콘\n', '').replace('사진\n', '')\
                                       .replace('삭제된 메시지입니다', '')

# print(text)


mask = np.array(Image.open('apple.png'))
wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("py_day3_hw.png")
