
from math import log2
 
class SparseTable:
    """
    Sparse Table for idempotent range queries (min, max, gcd, AND, OR, etc.)
    Build: O(n log n)   Query: O(1)
    Only valid for idempotent ops — do NOT use for range sum
    (use a Fenwick tree / segment tree instead).
    """
 
    def __init__(self, arr, merge=min):
        self.n = len(arr)
        self.merge = merge
 
        # log_table[i] = floor(log2(i))
        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
 
        self.LOG = self.log_table[self.n] + 1 if self.n > 0 else 1
 
        # table[k][i] = result over [i, i + 2^k - 1]
        self.table = [arr[:]]
        for k in range(1, self.LOG):
            prev = self.table[k - 1]
            length = 1 << k
            half = 1 << (k - 1)
            row = [
                merge(prev[i], prev[i + half])
                for i in range(self.n - length + 1)
            ]
            self.table.append(row)
 
    def query(self, l, r):
        """Query on inclusive range [l, r], 0-indexed."""
        k = self.log_table[r - l + 1]
        return self.merge(self.table[k][l], self.table[k][r - (1 << k) + 1])
 
 
n, q = map(int, input().split())
arr = list(map(int, input().split()))

sp = SparseTable(arr, merge=min)
for i in range(q):
    l, r = map(int, input().split())
    print(sp.query(l - 1, r - 1))