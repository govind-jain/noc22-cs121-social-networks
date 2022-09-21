import numpy as np

A = np.mat('1 2;3 4');
B = np.mat('1;1');
C = np.mat('11;15');

for i in range(100):
    B = A * B
    B = B/np.linalg.norm(B)

for i in range(100):
    C = A * C
    C = C/np.linalg.norm(C)

print('*****************')
print(B)
print('*****************')
print(C)
print('*****************')

if (B==C).all():
    print("B and C have same values.")
else:
    print("B and C have different values.")
