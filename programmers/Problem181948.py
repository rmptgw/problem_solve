### 특수문자 출력하기
# URL : https://school.programmers.co.kr/learn/courses/30/lessons/181948
## 문제 설명
# 다음과 같이 출력하도록 코드를 작성해 주세요.
## 출력 예시
# !@#$%^&*(\'"<>?:;
str = '!@#$%^&*(\'"<>?:;'
str = list(str)
for i in range(0,len(str)):
    if(str[i] == "'"):
        str[i] = '\\' + str[i]
    
str = ''.join(str)
print(str)