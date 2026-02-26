import numpy as np
import time

arr = np.arange(1_000_000)

start = time.time()
result = []

for i in arr:
    result.append(i * 2)

end = time.time()
print("Loop time:", end - start)

import numpy as np
import time

arr = np.arange(1_000_000)


start = time.time()
result = arr * 2
end = time.time()

print("Vectorized time:", end - start)

#Executed in optimized C code
#Better CPU cache utilization