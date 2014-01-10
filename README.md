Stream.py
======

A utility class for the brute-forcing of problems with natural number solutions. 
You can pretend you're filtering an infinite set without using infinite memory!
Inspired by [streamjs](streamjs.org).

First n numbers:

    >>> ints = Stream()
    >>> ints.pluck(5)
    [0, 1, 2, 3, 4]

First n prime numbers:

    >>> primes = Stream(filter_function = isPrime) # imagine an efficient implementation I prepared earlier
    >>> list(primes.pluck(15))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

Brute-force algebra problems:

    >>> problem = lambda x: x+5 == 2*x
    >>> list(Stream(filter_function = problem).pluck(1))
    [5]

How about something more arbitrary... What's the sum of the first fifteen squares that are divisible by 9?

    >>> sum(Stream(map_function = lambda x: x**2, filter_function = lambda x: x % 9 == 0).pluck(15))
    9135
