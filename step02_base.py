# 정수형 자료
int_data = 10  # 10
bin_data = 0b10  # 2
oct_data = 0o10  # 8
hex_data = 0x10  # 16
logn_data = 123456789  # 123456789

print(int_data )
print(bin_data )
print(oct_data )
print(hex_data )
print(logn_data)
print()

# 실수형 자료
f1 = 1.0
f2 = 3.14
f3 = 1.56e3  # 1560.0    # 1.56e3 = 1.56*10^3 
f4 = -0.7e-4  # -7e-05  # 0.7*10^-4 -> 7*10^-5

print(f1)
print(f2)
print(f3)
print(f4)
print()
# 실수형과 정수형의 계산은 모두 실수형으로 나옴
# 나눗셈은 정수형끼리 계산해도 실수형으로 나옴


# 복소수형 자료
cl = 1+7j
print('실수 : ', cl.real); print('허수 : ', cl.imag)  # 파이썬 코드를 한줄로 작성하고자 할 때: ;
# print('실수 : ', cl.real), print('허수 : ', cl.imag)
# 실수만 출력하고자 할 때: real (실수로 출력)
# 허수만 출력하고자 할 때: imag (실수로 출력)

c2= complex(2, 3)
# 복소수형 상수 만들기
# complex(실수부, 허수부)
# 출력물: 실수부 + 허수부j
print(c2)

# 대입 연산자 개념
# 대입 연산자는(=) 왼쪽 변수에 오른쪽 값을 대입한다는 의미
# == 는 왼쪽 값과 오른쪽 값이 같다는 의미
print()

# 관계 연산자
x = 1; y = 2
str1 = 'abc'; str2 = 'python'

print('x == y : ', x == y)
print('x != y:', x != y)
print('x == True: ',x == True)
print('x == False: ', x == False)
print('str1 == str2 :', str1 == str2)
print("str2 == 'python' : ", str2 == 'python')
print('str1 < str2:', str1 < str2) # 문자열의 크기 비교는 문자열의 사전 순서로 비교
# print('str2 - str1 :', str2 - str1)

print()

# 논리 연산자
bl1 = True
bl2 = False
bl3 = True
bl4 = False

print('bl1(T) and bl2(F) :', bl1 and bl2)
print('bl1(T) and bl3(T) :', bl1 and bl3 )
print('bl2(F) or bl3(T) :', bl2 or bl3)
print('bl2(F) or bl4(F) :', bl2 or bl4)
print('not bl1(T) : ', not bl1)
print('not bl2(F) : ', not bl2)

print()
print('bl1(T) + bl2(F) :', bl1 + bl2)
print('bl1(T) + bl3(T) :', bl1 + bl3 )
print('bl2(F) * bl3(T) :', bl2 * bl3)
print('bl2(F) * bl4(F) :', bl2 * bl4)

print()
# 시퀀스 자료 크기
strdata1 = 'I love python'
strdata2 = '나는 파이썬을 사랑합니다'
listdata = ['a', 'b', 'c', strdata1, strdata2]
print(len(strdata1))  # 공백포함: 13자
print(len(strdata2))  # 공백포함: 13자
print(len(listdata))  # 공백포함: 5자
print(len(listdata[3]))  # 공백포함: 13자


print()
# in 이해
# 어떤 값이 시퀀스 자료에 있는지 없는지 확인

listdata = [1, 2, 3, 4, 5]
ret1 = 5 in listdata
print(ret1)

strdata = 'abcd'
ret2 = 'c' in strdata
print(ret2)

print()
# 문자열 포맷팅
txt1 = '자바'
txt2 = '파이썬'
num1 = 5
num2 = 10

print('나는 %s보다 %s에 더 익숙합니다'%(txt1, txt2))
print('%s은 %s보다 %d배 더 쉽습니다'%(txt2, txt1, num1))
print('%d + %d = %d'%(num1, num2, num1 + num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가했다'%num1) # %%: %표기하기 위함
print(r'다음 행으로 넘어갈 때는 개행 문자(\n)을 쓰세요.') # 이스케이프 기능을 적용하지 않고 텍스트 적용하고 싶을 때


