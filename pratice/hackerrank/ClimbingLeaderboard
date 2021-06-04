n = int(input().strip())
scores = map(int,input().strip().split(' '))
m = int(input().strip())
alice = map(int,input().strip().split(' '))

leaderboard = sorted(set(scores), reverse = True)
l = len(leaderboard)

for a in alice:
    while (l > 0) and (a >= leaderboard[l-1]):
        l -= 1
    print(l+1)
