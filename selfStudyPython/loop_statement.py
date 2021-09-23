# print([273, 32, 103, "문자열", True, False][0])
# print('273, 32, 103, "문자열", True, False'[0])

# list_a = [273, 32, 103, "문자열", True, False]
# # del list_a[6]
# list_a.pop(6)

# 리스트 문제
# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[], [], []]

# for number in numbers:
#     output[(number+2)%3].append(number)

# print(output)

# # 딕셔너리 문제
# numbers = ["a","b","b","c"]
# count = {}
# for number in numbers:
#     if number in count:  # 딕셔너리에 키가 있는지 여부
#         count[number] += 1
#     else:
#         count[number] = 1

# print(count)

# 역반복문
# for i in range(4, 0-1, -1):  # 0까지 출력하고 싶을 때 -1.. 이해 못함..
#     print("현재 반복 변수: {}".format(i))

# 또는 reversed()함수 사용
# for i in reversed(range(5)):
#     print("현재 반복 변수: {}".format(i))


# # 딕셔너리 생성 문제
# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# character = {}

# for i in range(len(key_list)):
#     character[key_list[i]] = value_list[i]

# print(character)

# # 1부터 숫자를 하나씩 증가시키면서 더하는데, 몇을 더해야 10000을 넘는가?
# limit = 10000
# i = 1
# sum_value = 0
# while True:
#     if sum_value < limit:
#         sum_value += i
#         i += 1
#         print("i: ", i, "sum_value: ", sum_value)
#     else:
#         break

# print(i)
# print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다".format(i, limit, sum_value))

# 1부터 100까지 숫자 중 100의 보수를 곱했을 때 
# 최대값이 되는 경우는 어떤 숫자를 곱했을 때인가?
max_value = 0
a = 0
b = 0

for i in range(1, 101):
    j = 100 - i
    if (i * j) > max_value:
        max_value = i*j
        a = i
        b = j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))