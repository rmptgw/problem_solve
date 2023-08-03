result = 0
i = 1
while(True):
    conn = True
    for k in range(1,21):
        if( i % k > 0 ):
            conn = False
            break
        
    if( conn == True ):
        break
    i += 1
    
print(result)