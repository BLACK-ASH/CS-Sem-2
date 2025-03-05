from collections import deque

d = deque()

d.append(0)
d.append(2)
d.append(4)
d.append(6)
d.append(8)
d.append(10)

print("Before POP : ",d)
d.pop
print("After POP : ",d)

a = d.popleft()
print(d)
print(a)
