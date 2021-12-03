import math 
import functools 

def findPrime(nums):
    MAX_N = max(nums) 
    seive = [(1 << 8)-1] * ((MAX_N + 7)//8 + 1) 
    
    def isPrime(k): 
        return (seive[k >> 3] & (1 << (k & 7))) != 0 

    def setComposite(k): 
        seive[k >> 3] &= ~(1 << (k & 7)) 
        
    n = int(math.sqrt(MAX_N)) 
    setComposite(0) 
    setComposite(1) 
    for i in range(2, n+1): 
        if isPrime(i): 
            for j in range(i*i, MAX_N+1, i): 
                setComposite(i) 
                    
    # print(functools.reduce(lambda x, y: isPrime(x) + y, nums, 0)) 
    res = list(filter(isPrime, nums)) 
    print(seive)
    print(res)
    return len(res) 

int(input()) 
inputs = list(map(int, input().split())) 
print(findPrime(inputs))

# https://programming119.tistory.com/160