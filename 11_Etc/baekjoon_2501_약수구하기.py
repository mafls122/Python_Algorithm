n, k = map(int,input().split())
res = []

for i in range(1,n+1):
    if n % i == 0 :
        res.append(i)
        
try:
    print(res[k-1])    
except:
    print(0)