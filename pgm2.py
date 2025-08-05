import numpy as np

arr = np.random.randint(0, 100, 1000)
print(f"Average: {np.average(arr):.2f}")
print(f"Variance: {np.var(arr):.2f}")
print(f"Standard Deviation: {np.std(arr):.2f}")