# OS 파일 시스템 관련 함수
import os

pwd = "c:\\Users\\PC\\Desktop\\OZ-BE\\OS"

# 디렉터리 내부 list-up
filenames = os.listdir(pwd)
# print(filenames)

# 디렉터리인지 아닌지 여부 조회
print(os.path.isdir(filenames[0]))
print(os.path.isdir(filenames[5]))
# print(os.path.isdir(pwd + "\\Day?"))

# 파일인지 아닌지 여부 조회
print(os.path.isfile(filenames[0]))
print(os.path.isfile(filenames[5]))

# 파일이름과 확장자 분리
filepath = pwd + "\\" + filenames[5]
print(filepath)
name, ext = os.path.splitext(filepath)
print(name)
print(ext)