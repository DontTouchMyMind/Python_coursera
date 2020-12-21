import sys


digit_string = sys.argv[1]
total_sum = 0

for digit in digit_string:
    total_sum += int(digit)

print(total_sum)

# Решение от портала
print(sum([int(x) for x in sys.argv[1]]))
