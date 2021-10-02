from math import sqrt, floor
from random import randint
from collections import deque
from sympy import nextprime


class CloseAddressingHashTable(object):
    """
    use deque as doubly linked list
    support insert, delete and search
    """

    def __init__(self, capacity: int, h: int = 2):
        """
        According to CPython, the random integer is generate by /dev/urandom, based on the environment noise.
        https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/drivers/char/random.c?id=refs/tags/v3.15.6

        from os import urandom as _urandom

        # Generate n random bytes.
        def randbytes(self, n):
            return _urandom(n)

        we will use sympy library to prime computation
        https://github.com/sympy/sympy/blob/master/sympy/ntheory/generate.py
        nextprime() and primerange() search potential primes located at 6 * size + 1 or 6 * size - 1
        """
        self.capacity = capacity
        self.ht = [deque([]) for _ in range(capacity)]
        # choose one hash function
        if h == 0:
            self.h = self.division_method_hashing
        elif h == 1:
            # The value of a is determined by researcher.
            self.a = (sqrt(5) - 1) / 2
            self.h = self.multiplication_method_hashing
        else:
            self.p = nextprime(capacity)
            self.a = randint(1, self.p - 1)
            self.b = randint(0, self.p - 1)
            self.h = self.universal_hashing

    """3 hash functions"""

    def division_method_hashing(self, k):
        return k % self.capacity

    def multiplication_method_hashing(self, k):
        """
        The multiplication method is better than division method (k % size) because the size of hash table is not
        critical.
        """
        # size or local list size
        return floor(self.capacity * (k * self.a % 1))

    def universal_hashing(self, k):
        return ((self.a * k + self.b) % self.p) % self.capacity

    """hash table's functions"""

    def chained_hash_insert(self, x):
        h_val = self.h(x)
        self.ht[h_val].appendleft(x)

    def chained_hash_search(self, x):
        """
        search value x in hash table with worst time complexity O(n)

        :param x: value
        :return: number of value occurrence
        """
        h_val = self.h(x)
        return self.ht[h_val].count(x)

    def chained_hash_delete(self, x):
        """
        delete all element with value x
        worst time complexity O(n)
        """
        h_val = self.h(x)
        for _ in range(self.ht[h_val].count(x)):
            self.ht[h_val].remove(x)