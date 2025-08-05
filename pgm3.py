import numpy as np

n = int(input("How many values? "))
arr = np.array([[]])
for i in range(n):
    arr = np.append(arr, [int(input(f"a[{i}]: "))])
for i in arr:
    print(f"{i}degree -> {np.deg2rad(i):.2f}rad")