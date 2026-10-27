
import numpy as np
import random

n = int(input("Enter grid size: "))
start = int(input("Enter start position: "))
goal = int(input("Enter goal position: "))

obstacles = []
positions = input("Enter obstacle positions separated by spaces: ").split()

for p in positions:
    obstacles.append(int(p))

# Q-table
Q = np.zeros((n*n, 4))

def move(s, a):           #0=up, 1=down, 2=left, 3=right
    r, c = divmod(s, n)

    if a == 0:
        r = max(0, r-1)
    elif a == 1:
        r = min(n-1, r+1)
    elif a == 2:
        c = max(0, c-1)
    else:
        c = min(n-1, c+1)

    ns = r*n + c

    if ns in obstacles:
        return s, -5
    if ns == goal:
        return ns, 10

    return ns, -1

for episode in range(2000):
    s = start

    for step in range(100):
        # Explore or exploit
        if random.random() < 0.2:
            a = random.randint(0, 3)
        else:
            a = np.argmax(Q[s])

        ns, reward = move(s, a)

        old_value = Q[s, a]
        future_value = max(Q[ns])
        new_value = reward + 0.9 * future_value
        Q[s, a] = old_value + 0.1 * (new_value - old_value)

        s = ns

        if s == goal:
            break

s = start
path = [s]
visited = {s}

for step in range(n*n):
    a = np.argmax(Q[s])
    ns, reward = move(s, a)

    if ns == s or ns in visited:
        break

    s = ns
    path.append(s)
    visited.add(s)

    if s == goal:
        break

print("Learned path:", path)
print("Goal reached:", s == goal)
