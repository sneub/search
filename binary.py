#!/usr/bin/env python

def bsearch(n, x, low=None, high=None):
    if high == None and low == None:
        low = 0
        high = len(n)
    if low > high:
        return False
    mid = (low + high)/2
    if n[mid] == x:
        return mid
    elif n[mid] < x:
        return bsearch(n, x, mid+1, high)
    else:
        return bsearch(n, x, low, mid-1)
