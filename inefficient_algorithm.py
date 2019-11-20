import time
import random


start_time = time.time()

ROUTES_TO = [random.randint(0, 10000) for n in range(10000)]
ROUTES_BACK = [random.randint(0, 10000) for n in range(10000)]
MAX = 10000

count = 0
current_max = 0

for i in range(len(ROUTES_TO)):
    for j in range(len(ROUTES_BACK)):
        total = ROUTES_TO[i] + ROUTES_BACK[j]
        if total > MAX:
            continue
        if total > current_max:
            current_max = total
            count = 1
        elif total == current_max:
            count += 1

end_time = time.time()

print (f'upper limit set to = {MAX}')
print (f'current maximum possible = {current_max}, number of combinations = {count}')
print( f'time elapsed = {round(end_time - start_time, 2)}')

