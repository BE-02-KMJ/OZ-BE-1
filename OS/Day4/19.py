foods = ['hamburger', 'pizza', 'salad', 'cheese']

# foods(변수 또는 참조자)를 기반으로 메모리 공간의 주소 알아낼 수 있다.
print(id(foods))
print(hex(id(foods)))   # 16진수로 보기

mv = memoryview(b"happy day") # b: 문자열을 bite형태로 저장

print(mv)

# slicing도 가능. 유니코드로 출력.
print(mv[0])
print(mv[1])
print(mv[2])
print(mv[3])    # 2,3은 모두 p이므로 값 동일.
# indexing error도 발생할 수 있으므로 조심!