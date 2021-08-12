'''
 - 문자열 슬라이싱
        - 문자열 포맷팅: %, format(), f''
        - 문자열 갯수세기: count()
        - 문자열 찾기: find(), index()
        - 문자열 삽입: "".join()
        - 문자열 대소문자 변환: upper(), lower()
        - 문자열 공백 지우기: lstrip(), rstrip(), strip()
        - 문자열 바꾸기: replace()
        - 문자열 나누기: split()
'''


# 1.2. 문자열
# 문자열 슬라이싱
a = "Life is too short, you need Python"
print(a[0])
print(a[:4] + a[17]+ a[-6:])

# 문자열은 수정이 불가능하다
# a[1] = 'e'  # 해당 코드 실행시 에러 발생

# 문자열 포맷팅
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

print("%10s" % "hi")  # 문자열 길이가 10인 공간에서 값을 오른쪽 정렬, 나머지는 공백
print("%-10sjane." % 'hi')  # 문자열 길이가 10인 공간에서 값을 왼쪽 정렬, 나머지는 공백
print("{0:<10}".format("hi")) # 치환되는 문자열을 왼쪽 정렬, 문자열의 자릿수는 10
print("{0:>10}".format("hi")) # 치환되는 문자열을 오른쪽 정렬, 문자열의 자릿수는 10
print("{0:^10}".format("hi")) # 치환되는 문자열을 가운데 정렬, 문자열의 자릿수는 10
print("{0:=^10}".format("hi")) # 치환되는 문자열을 가운데 정렬, 나머지 공백은 = 로 채움
print("{0:!<10}".format("hi"))  # 치횐되는 문자열을 왼쪽 정렬, 나머지 공백은 !로 채움

print("%0.4f" % 3.42134234)

print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

y = 3.42134234
print("{0:0.4f}".format(y))  # 소숫점자리를 4번째 자리까지 표현
print("{0:10.4f}".format(y)) # 소숫점자리를 4번째 자리까지 표현하고 자릿수는 10개

print("{{ and }}".format())  # 중괄호를 문자열 그대로 출력하고 싶을 때


# f문자열 포맷팅. 파이썬 3.6이상부터 가능
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다')
print(f'내년이면 {age+1}살입니다')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print( f'{"hi":<10}') # 왼쪽 정렬
print(f'{"hi":>10}') # 오른쪽 정렬
print(f'{"hi":^10}') # 가운데 정렬
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

y = 3.42134234
print(f'{y:10.4f}') # 소숫점자리 4자리까지 표현하고 자릿수는 10자리

print(f'{{ and }}')


# 문자열 관련 함수
# 문자 갯수 세기(count)
a = 'hobby'
print(a.count('b'))

# 위치 알려주기(find)- 찾는 값이 없으면 -1 반환
a = 'python is the best choice'
print(a.find('o'))  # 많은 문자열 중 처음나온 위치를 반환. 
print(a.find('Python'))
print(a.find('python'))

# 위치 알려주기(index)- 찾는 값이 없으면 error 발생
print(a.index('i'))
print(a.index('is'))
# print(a.index('Python'))


# 문자열 삽입(join)
print(",".join('abcd'))


# 문자열 소문자-> 대문자 변환(upper)
print(a.upper())  # 원본에 영향을 미치지 않음
print(a)

# 문자열 대문자 -> 소문자 변환(lower)
b = a.upper()
print(b)
print(b.lower())
print(b)  # 원본에 영향을 미치지 않음

# 공백지우기(lstrip, rstrip, strip)
a = "  hi"
b = "hi  "
c = "  hi  "
print(a.lstrip())
print(b.rstrip())
print(c.strip())

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))


 # 문자열 나누기(split)
a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))