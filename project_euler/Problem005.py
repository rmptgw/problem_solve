# 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
result = 0
num = []
for k in range(2,21):
    for i in range(1,k+1):
        if(k % i == 0):
            num.append(i)
            continue   

num = set(num)

print(num)