from collections import deque

N = int(input().strip())

card = deque(range(1, N + 1))

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
    
print(card[0])