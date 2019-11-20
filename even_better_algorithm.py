import time
import random


start_time = time.time()
random.seed(0)

MAX = 10000
ROUTES_TO = [random.randint(0, 10000) for n in range(10000)]
ROUTES_BACK = [random.randint(0, 10000) for n in range(10000)]

ROUTES_TO.sort(reverse=True)
ROUTES_BACK.sort(reverse=True)

count = 0
current_max = 0


for i in range(len(ROUTES_TO)):
    for j in range(len(ROUTES_BACK)):
        total = ROUTES_TO[i] + ROUTES_BACK[j]
        if total > MAX:
            continue
        if total < current_max:
            break
        elif total == current_max:
            count += 1
        else:
            current_max = total
            count = 1

end_time = time.time()

print (f'upper limit set to = {MAX}')
print (f'current maximum possible = {current_max}, number of combinations = {count}')
print( f'time elapsed = {round(end_time - start_time, 2)}')

