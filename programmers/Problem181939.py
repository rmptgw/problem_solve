### 더 크게 합치기
# URL : https://school.programmers.co.kr/learn/courses/30/lessons/181939
## 문제 설명
# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.
## 제한사항
# 1 ≤ a, b < 10,000
## 입출력 예
# a	b	result
# 9	91	991
# 89	8	898
## 입출력 예 설명
# 입출력 예 #1
# a ⊕ b = 991 이고, b ⊕ a = 919 입니다. 둘 중 더 큰 값은 991 이므로 991을 return 합니다.
# 입출력 예 #2
# a ⊕ b = 898 이고, b ⊕ a = 889 입니다. 둘 중 더 큰 값은 898 이므로 898을 return 합니다.
def solution(a, b):
    answer = 0
    ln_a = len(str(a))
    ln_b = len(str(b))
    c = a * (10 ** ln_b) + b
    d = b * (10 ** ln_a) + a
    # print('len a =', ln_a, 'len b =', ln_b)
    # print('c =', c, 'd =', d)
    if( c >= d ):
        answer = c
    else :
        answer = d
        
    return answer

print(solution(9,91))
print(solution(89,8))