'''
1) 리스트 : 순서o, 수정o, 중복o
        - 인덱싱
        - 슬라이싱
        - 연산
        - 수정
        - 삭제 : del
        - 요소 추가 : append()
        - 정렬 : sort()
        - 뒤집기 : reverse()
        - 위치 반환: index()
        - 요소 삽입 : insert()
        - 요소 제거 : remove(), pop()
        - 갯수 세기: count()
        - 리스트 확장: expend()
'''


# 연산 +, *
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

print(a*3)

print(str(a[1])+'hi')
# 길이 구하기:len()
print(len(a))


# 리스트 수정
a[1] = 5
print(a)

# 리스트 삭제
del a[1]
print(a)

del a[:]  # 요소 여러개 삭제
print(a)