x = 3
result = 0
a = 0
b = 0
nn = 10 ** x - 1
# print(nn)

for i in range(nn, 0, -1):
    for j in range(nn, 0, -1):
        num = i * j
        num = str(num)
        num = list(num)

        conn = 'T'
        for k in range(0, x):
            a = num[k]
            b = num[-k-1]
            
            print("num = ", num, "k : " + str(k) + " a : " + a + ", b : " + b)
            print('conn : ' + conn, "i : ", i, "j : ", j)
            if(a!= b):
                conn = 'F'
                break

        if(conn == 'T' ):
            if(result < (i * j)):
                result = i * j
                break
    if(conn == 'T' ):
        if(i < (nn/2)):
            break

print(result)