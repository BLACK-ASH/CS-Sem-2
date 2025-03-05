import heapq

q = []
heapq.heappush(q,(2,"Write A Book"))
heapq.heappush(q,(1,"Lunch & Break"))
heapq.heappush(q,(3,"Relax & Sleep"))

while q:
    next_item = heapq.heappop(q)
    print(next_item)
