import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

from datetime import datetime

# 보내는 사람 정보
me = "your email"
my_password = "your password"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
you = "받는 사람 이메일"

# 파일에 붙여줄 날짜 설정
date = datetime.today().strftime("%Y{} %m{} %d{}".format('년', '월', '일'))

# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "%s 코로나확진자 관련 뉴스" % date
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "%s 코로나확진자 관련 뉴스입니다. " % date
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# 파일 첨부하기
part = MIMEBase('application', "octet-stream")
with open("보내는 파일 이름", 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename="%s 코로나 관련 기사" % date)
msg.attach(part)

# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()
