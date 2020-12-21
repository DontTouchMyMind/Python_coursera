import sys


input_data = int(sys.argv[1])
sharp_count = 0
while input_data > 0:
    input_data -= 1
    sharp_count += 1
    print(' ' * input_data + '#' * sharp_count)

# Решение от портала
num_steps = int(sys.argv[1])

for i in range(num_steps):
    print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")