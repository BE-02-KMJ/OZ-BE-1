# 파일 관련 예외 운영체제와 관계
try :
    f = open("none.txt","r")
    print(f.read())
    f.close()
except FileNotFoundError as e :
    print(e)
    print(issubclass(FileNotFoundError, OSError))
    # FileNotFoundError가 OSError의 하위 에러 맞는지 확인
    print(issubclass(ZeroDivisionError, OSError))