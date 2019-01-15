from time import time
import random

for test_case in range(5):
    N = 10 ** (test_case+1)
    p = random.randint(7,19)
    start_time = time()
    
    P = int(((p-1)*p)/2)
    M=int(N/p)
    c=int(N%p)
    C=int((c*(c+1))/2)
    sum = M*P+C
    
    end_time = time()
    print(f'''For N={N},sum={sum}.Required time {end_time-start_time}''')
