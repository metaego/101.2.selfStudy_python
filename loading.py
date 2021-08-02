from time import sleep
l = 0

for i in range(100):
    msg = '\r진행률 %d%%'%(i + l)  # \r :캐리지 리턴 문자. 커서를 맨 앞에 위치시키기(?)
    # print(''*len(msg), end='')
    print(msg, end='')
    sleep(0.1)