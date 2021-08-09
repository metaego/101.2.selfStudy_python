# 파이썬 예약어 확인
import keyword

print(keyword.kwlist)

'''
* 자료형의 개념
1) 수치형 자료
정수형 상수, 실수형 상수, 복소수형 상수

2) 문자열 자료
'' 또는 ""로 표기

3) 리스트 자료
[]안에 임의의 객체를 순서있게 나열한 자료형
순서가 있으므로 인덱스로 값을 접근 가능

4) 튜플 자료
리스트와 비슷하지만 요소 값을 변경할 수 없음

5) 사전 자료
{키:값}으로 된 쌍이 요소로 구성된 순서없는 자료형
순서없는 자료형이므로 인덱스 대신 키를 이용하여 대응하는 값을 접근함
'''

# print()함수는 \n이 기본값으로 설정.
# 줄바꿈없이 출력하고 싶다면 end=""를 옵션으로 주면 된다
print('#', end="")
print('#')


# 들여쓰기 개념
listdata = 'a'

if 'a' in listdata: print('a가 listdata에 있습니다')


# for 반복문 개념
# for문의 범위로 사용되는 것은 "시퀀스(sequence) 자료형" 또는 "반복 가능한 자료형" 이어야 함
# sequence 자료형: 리스트, 튜플, range, 문자열처럼 값이 연속적으로 이어지는 자료형
"""
- 문자열
- 리스트, 튜플
- 사전
- range()
- 그 외 반복 가능한 객체
"""
# 문자열을 범위로 지정
str = 'abcdef'
for c in str:
    print(c)
print()

# 리스트를 범위로 지정
list = [1,2,3,4,5]
for c in list:
    print(c)
print()

# 사전을 범위로 지정
ascii_codes = {'a':97, 'b':98, 'c':99}
for c in ascii_codes:
    print(c)
print()

# range()함수를 범위로 지정
for c in range(10):
    print(c)


scope = [1, 2, 3,]
print(scope)
print(len(scope))
for x in scope:
    print(x)
else:
    # for문이 모두 실행되었을 때 실행할 코드
    print('perfect!')

    # for x in scope:
    #     if x == True:
    #         print('True')
    #     else:
    #         print("False")


# for문이 "지정된 자료나 반복 가능한 객체를 이용"해 반복문 수행
# while문은 "특정 조건을 만족"하는 경우 지속적으로 반복을 수행


# None 개념
# None: Types.NoneType의 유일한 값. 값이 존재하지 않는 변수에 대입하여 이 변수에 아무런 값이 없다는 것을 나타내기 위해 주로 활용
val = None
condition = 1
print(val)
if condition == 1:
    val = [1, 2, 3]
    print(val)

else:
    val= 'I love Python'
    print(val)