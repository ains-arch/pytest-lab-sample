#!/usr/bin/python3


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    return list(filter(lambda n: int(n/2) == n/2, range(n+1)))
