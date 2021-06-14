from collections import defaultdict

n, m = map(int, input().split())
adj = defaultdict(list)
for i in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
    adj[v].append((w, u))
a, b, k = map(int, input().split())
        

queue = [(-1, a, 0)]
visited = set()
count = 0
while queue:
    previous,vertex,total = queue.pop(0)
    if total == k and vertex == b:
        count += 1
        continue
    elif total > k or (vertex == b and total != k):
        continue
    else:
        for weight, nextVertex in adj[vertex]:
            if (previous, vertex, nextVertex) not in visited:
                visited.add((previous, vertex, nextVertex))
                queue.append((vertex, nextVertex,total + weight))
if count > 0 :
        print(count)
else: 
        print(-1)
