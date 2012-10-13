Stream.py
======

A utility class for the brute-forcing of problems with natural number solutions. 
You can pretend you're filtering an infinite set without using infinite memory!
Inspired by [streamjs](streamjs.org).

First n numbers:

    >>> realNumbers = Stream()
    >>> realNumbers.pluck(5)
    [0, 1, 2, 3, 4]

First n prime numbers:

    >>> def isPrime(n):
      if n<=1:
    		return False
    	elif n%2 == 0:
    		return False
    	else:
    		for possibleFactor in range(3, n, 2):
    			if n%possibleFactor == 0:
    				return False
    	return True
    
    >>> primes = Stream(filterFunction = isPrime)
    >>> primes.pluck(15)
    [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

Brute-force algebra problems:

    >>> Stream(filterFunction = lambda x: x+5 == 2*x).pluck(1)
    [5]

But this limits your domain to positive ints. How about positive and negative ints?

    >>> Stream(mapFunction = lambda x: x/2 if x%2 == 0 else -x/2).pluck(5)
    [0, -1, 1, -2, 2]

How about something more arbitrary... What's the sum of the first fifteen squares that are divisible by 9?

    >>> sum(Stream(mapFunction = lambda x: x**2, filterFunction = lambda x: True if x%9 == 0 else False).pluck(15))
    9135