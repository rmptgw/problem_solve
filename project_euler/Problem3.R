# 문제 사이트 : https://euler.synap.co.kr/problem=3
# 사용언어 : R
# 레포지토리 : git

x <- 600851475143;
# x <- 13195;

# x <- 10;

print(x)

i <- 2
fin <- c()

while(i <= x){
	if( x %% i == 0 ){
		cat("i : ", i, "\n")
		x <- x / i
		fin <- c(fin, i)
		fin <- unique(fin)
		fin <- sort(fin)
		next
	} 
	i <- i + 1	
}
cat("######\n")
print(fin)
