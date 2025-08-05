import numpy as np

n = int(input("How many values? "))
arr = np.array([])
for i in range(n):
    arr = np.append(arr, int(input(f"a[{i}]: ")))
print("The converted temp are: ")
for i in arr:
    f = i
    c = (f - 32) * ( 5 / 9 )
    print(f, " -> ", c)