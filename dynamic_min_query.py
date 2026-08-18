import math


class SegmentTree:
    def __init__(self, data, merge, identity):
        # merge: the operation you're combining ranges with (+, min, max, gcd, ^, ...)
        # identity: the "do nothing" value for that operation
        #   sum -> 0            (x + 0 == x)
        #   min -> +infinity    (min(x, inf) == x)
        #   max -> -infinity    (max(x, -inf) == x)
        #   gcd -> 0            (gcd(x, 0) == x)
        #   xor -> 0            (x ^ 0 == x)
        # These two lines are the ONLY thing you change between problems.
        self.n = len(data)
        self.merge = merge
        self.identity = identity
        self.tree = [identity] * (2 * self.n)
        for i, v in enumerate(data):
            self.tree[self.n + i] = v
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = merge(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, value):
        """Point update: set index i to value. Same code for every merge type."""
        i += self.n
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = self.merge(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        """Range query over half-open interval [l, r). Same code for every merge type."""
        res = self.identity
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = self.merge(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.merge(res, self.tree[r])
            l //= 2
            r //= 2
        return res




n, q = map(int, input().split())

arr = list(map(int, input().split()))

seg = SegmentTree(arr, merge=min, identity=math.inf)

for j in range(q):
    t, one, two = map(int, input().split())
    if t == 1:
        seg.update(i = one - 1, value = two)
    else:
        print(seg.query(l = one - 1, r = two))