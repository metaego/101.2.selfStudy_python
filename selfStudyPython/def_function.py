# 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수 정의하라
def mul(*values):
    total_value = 1
    for i in values:
        total_value *= i
    
    return total_value




# recall function
# 불러온 값이 맞는지 확인 비교
print(mul(5, 7, 9, 10))
print(5*7*9*10)