# 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
import numpy as np
result = 0
num = []
prime_factor = [[1][0]]
# Solve : 2 ~ 20 까지 소인수분해 후 최대공약수 구하기
for k in range(2,21):
    # 각 수에서 약수 담을 list
    div = []
    
    # 약수 구하기
    for i in range(1,k + 1):
        if(k % i == 0 & i != 1):
            div.append(i)
            continue
    
    # 약수 출력
    print(div)

    if(len(div) == 1):
        # 소수이면 num 추가
        num.append(k)
    else:
        # 소수가 아니면 소인수분해
        for i in div:
            while(True):
                if(k%i==0):
                     