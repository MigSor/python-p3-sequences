#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    for num in range(length):
        if len(fibonacci) > 1:
            num_to_add = fibonacci[-2] + fibonacci[-1]
            fibonacci.append(num_to_add)
        else:
            fibonacci.append(num)
    print(fibonacci)
