x = 2
result = 0
for i in range(x*2, 0, -1):
    num = str(i)
    num = list(num)
    
    
    for j in range(0, x):
        a = num[j]
        b = num[-j]
        
        print("a : " + a + ", b : " + b)
        if(a!= b):
            conn = 'F'
        else :
            conn = 'T'
    
    if(conn == 'T'):
        result = i
        break;
        
print(result)