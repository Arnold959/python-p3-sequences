#!/usr/bin/env python3

def print_fibonacci(length): 
    if length <= 0:
        print("[]")
        return
    fib =[0,1]
    if length == 1:
        print([0])
        return
    for  i in range(2,length):
        fib.append(fib[i-1]+fib[i-2])
        print(fib)
    pass