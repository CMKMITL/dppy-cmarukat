#!/usr/bin/env python3

n = 0

while n <= 10:
    m = 0
    print(f"Table de {n}: ", end = " ")
    while m <=10:
        print(m*n, end =" ")
        m = m+1    
    print()    
    n = n+1