# 2021.09.26 - p.227 마무리2
# # 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수 정의하라
# def mul(*values):
#     total_value = 1
#     for i in values:
#         total_value *= i
    
#     return total_value

# # recall function
# # 불러온 값이 맞는지 확인 비교
# print(mul(5, 7, 9, 10))
# print(5*7*9*10)

#######################################################################################################
# 2021.09.27
# p.243 05-2 함수의 활용_마무리1
# 재귀함수를 만들어서 리스트를 평탄화하는 함수를 만들어보라. 
# 리스트 평탄화는 중첩된 리스트가 있을때 중첩을 모두 제거하고 풀어서 1차원 리스트로 만드는 것을 의미함

# def flatten(data):
#     output = []
#     for item in data:
#         if type(item) is list:
#             output += flatten(item)
#         else:
#             output += [item]
#     return output

# example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print("원본:", example)
# print("변환:", flatten(example))



#######################################################################################################
# p.244-245 05-2 함수의 활용_마무리2
# https://www.youtube.com/watch?v=594WmZdC_ts&list=PLBXuLgInP-5n-KjzrCVs4dH3cW716J3tp&index=3
# 패밀리 레스토랑에서 여러 개의 테이블에 나누어 앉으려고 한다
# 이때 한 사람만 앉는 테이블이 없게 그룹을 지어야 한다
# 인원 수를 나누는 패턴만 구하면 되며, 누가 어디에 앉는지 등은 고려하지 않아도 괜찮다
# 예를 들어 6명이라면 다음과 같은 네가지 경우를 생각할 수 있다
# 2명+2명+2명, 2명+4명, 3명+3명, 6명

# 한 개의 테이블에 앉을 수 있는 최대 사람의 수는 10명이다
# 100명의 사람이 하나 이상의테이블에 나누어 앉는 패턴을 구하세요

# 앉힐수있는최소사람수 = 2
# 앉힐수있는최대사람수 = 10
# 전체사람의수 = 100
# memo= {}

# def 문제(남은사람수, 앉힌사람수):
#     key = str([남은사람수, 앉힌사람수])

#     # 종료조건
#     if key in memo:
#         return memo[key]
#     if 남은사람수 < 0:
#         return 0
#     if 남은사람수 == 0:
#         return 1

#     # 재귀조건
#     count = 0
#     for i in range(앉힌사람수, 앉힐수있는최대사람수 +1):
#         count += 문제(남은사람수 - i, i)

#     # 메모화 처리
#     memo[key] = count

#     #종료
#     return count

# print(문제(전체사람의수, 앉힐수있는최소사람수))

# 튜플은 딕셔너리의 키로 사용 가능
# dic = {
#     (0, 0): 10
# }
# print(dic[(0,0)])
# print(dic[0,0])  # 튜플은 괄호가 생략되기 때문이 해당과 같은 타입도 가능


#######################################################################################################
# 현대 프로그래밍 언어는 함수를 하나의 자료형으로 취급하기 때문에 함수를 매개변수로 전달할 수 있음.(2021.09.28)
# 함수의 매개 변수로 함수 전달하기(p.252)

# 매개변수로 받은 함수를 10번 호출하는 함수
# def call_10_times(func):
#     for i in range(10):
#         # 콜백함수: 다른 함수에서 호출하는 함수
#          func(i)

# # 간단한 출력하는 함수
# def print_hello(number):
#     print("안녕하세요", number)

# # 조합하기
# # call_10_times(print_hello)

# # 람다 정의
# call_10_times(lambda number: print("안녕하세요", number))

#######################################################################################################
# filter 함수와 람다 함수 콜라보(2021.09.28)
# 방법1
# def 짝수만(number):
#     return number % 2 == 0

# a = list(range(100))
# b = filter(짝수만, a)
# print(list(b))


# 방법2
# a = list(range(100))
# b = filter(lambda number: number % 2 == 0, a)
# print(list(b))

# # 방법3
# 짝수만 = lambda number: number % 2 == 0

# a = list(range(100))
# b = filter(짝수만, a)
# print(list(b))



#######################################################################################################
# map함수와 람다 함수 콜라보(2021.09.28)
# 방법1
# def 제곱(number):
#     return number * number

# a = list(range(100))
# print(list(map(제곱, a))) # 기존의 리스트를 기반으로 새로운 리스트를 만들때 사용


# # 방법2
# a = list(range(100))
# print(list(map(lambda number: number * number, a)))

# # 방법3
# a = list(range(100))
# print(list(map(lambda number: number * number, a)))
# print([i * i for i in a])
# print([i * i for i in a if i % 2 == 0])

# 리스트 내포를 사용하는 경우, 결과로 리스트가 나온다.
# 그만큼의 리스트가 하나 더 복제되서 메모리를 차지한다는 의미이다.
# map(), filter()함수 등은 제너레이터 함수라서 
# 내부의 데이터가 실제로 메모리에 용량을 차지하지 않음(호출되기 전까지 가상의 값만 가지고 있음)

#######################################################################################################
# 텍스트 파일 처리 기본(2021.09.28)
# 파일 읽고 쓰는 코드
# 파일 새로 쓰기
# file = open("test.txt", "w")
# file.write("안녕하세요")
# file.close()

# 파일 이어 쓰기
# file = open("test.txt", "a", encoding="utf8")
# file.write("안녕하세요")
# file.close()

# 파일 읽기
# file = open("test.txt", "r",encoding="utf8")
# print(file.read())
# file.close()

# with()함수
# with open("test.txt", "w", encoding="utf8") as file:
#     file.write("안녕하세요")

# with open("test.txt", "a", encoding="utf8") as file:
#     file.write("안녕하세요")

# with open("test.txt", "r", encoding="utf8") as file:
#     file.read()