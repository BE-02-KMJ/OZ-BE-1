# 문자열 객체를 변수 my_name이 참조했다.
# Reference Count(레퍼런스 카운트)가 1인 상태
my_name = "minjung"

# Reference Count 2인 상태
your_name = my_name

my_name = 1
your_name = 2
# Reference Count 0이 되었다.

# Reference Count 0이 된 것은 Garbage Collection의 소멸대상이 되어 제거된다.