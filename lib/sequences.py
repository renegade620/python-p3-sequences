#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fib_list = [0, 1]
    
    if length == 1:
        print([0])
        return
    
    for i in range(2, length):
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    print(fib_list[:length])

print_fibonacci(9)