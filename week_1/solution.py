import sys
from math import sqrt

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

k = b / 2

x1 = (-1 * k + sqrt(k**2 - a * c)) / a
x2 = (-1 * k - sqrt(k**2 - a * c)) / a

print(int(x1))
print(int(x2))

# Решение от портала
#
# import sys
# import math
#
# a = int(sys.argv[1])
# b = int(sys.argv[2])
# c = int(sys.argv[3])
#
# d = b * b - 4 * a * c
#
# x1 = (-b + math.sqrt(d)) / (2 * a)
# x2 = (-b - math.sqrt(d)) / (2 * a)
#
# print(int(x1))
# print(int(x2))