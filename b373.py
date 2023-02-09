# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:05:47 2021

@author: YOSO_WANHH
"""
def BubbleSort(a,n):
    sum = 0
    for i in range(n-1):
    
        for j in  range(n-1):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
                sum = sum +1
    print(sum)
            

n = int(input())
a = [int(i) for i in input().split()]
BubbleSort(a,n)


    