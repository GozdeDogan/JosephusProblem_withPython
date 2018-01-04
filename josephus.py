import sys

def main():
    n = 4
    k = 2
    
    res = josephus(n, k)
    print "not dead:", res 
    
def josephus(n, k):
    if n==1:
        print "n:", n, "\tres: 1" 
        return 1
    else:
        res = (josephus(n-1, k) + k-1)%n + 1
        print "n:", n, "\tres:", res
        return res
        
if __name__ == "__main__":
    main()
