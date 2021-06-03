def solve(a):
    m = list([0] * 100)
    maxcount = 1
    for x in a:
        m[x] += 1 
    for k, x in enumerate(m[0:len(m)-1]):
        maxcount = max(maxcount, m[k]+m[k+1])
    return maxcount

n = int(input().strip())
a = list(map(int, input().rstrip().split()))

print(solve(a))

