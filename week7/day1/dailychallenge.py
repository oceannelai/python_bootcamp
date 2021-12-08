import numpy as np
import matplotlib.pyplot as plt
import random
N = random.randint(2, 39)
M = random.randint(2, 49)
def table(M,N):
    if M<50 and N<40:
        return np.random.randint(1,101,(M,N))
# print(table(M,N))

table_a = table(M,N)
# print(table_a)

# print(table_a[2])

# print(table_a[:,2])

table_a[-1] = 7
# print(table_a)

table_a[:,-1] = table_a[:,0] + table_a[:,1]
print(table_a)