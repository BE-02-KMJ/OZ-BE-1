# 기본적인 파일 입출력 예시
with open("number1.txt", "w") as f:
    f.write("one!")

with open("number2.txt", "w") as f:
    f.write("two!")

with open("number3.txt", "w") as f:
    f.write("three!")

with open("number4.txt", "w") as f:
    f.write("four!")

# glob : 파일 네임의 패턴을 이용해 여러개의 파일을 한꺼번에 접근할 때 사용
import glob

for filename in glob.glob("*.txt", recursive=True): # recursive : 재귀
    print(filename)

import fileinput

with fileinput.input(glob.glob("*.txt")) as fi :
    for line in fi :
        print(line)

import fnmatch, os

for filename in os.listdir('.') :
    if fnmatch.fnmatch(filename, "??????*.txt"):
        print(filename)