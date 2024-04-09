# 파일 복사 또는 이동
import os, shutil

pwd = "C:\\Users\\PC\\Desktop\\OZ-BE\\OS\\Day5"
filenames = os.listdir(pwd)

for filename in filenames:
    if "tokyo" in filename:
        origin = os.path.join(pwd, filename)
        print(origin)
        # shutil.copy(origin, os.path.join(pwd, "tokyo_copy.txt"))
        shutil.move(origin, "C:\\Users\\PC\\Desktop\\OZ-BE\\OS")