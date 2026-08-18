"""
Generic Segment Tree Template
==============================
One structure, swap the merge function + identity element to solve:
sum / min / max / gcd / xor / and / or range queries.

Point update + range query: O(log n) each, O(n) build.

QUICK REFERENCE — what to change for your scenario
----------------------------------------------------
1. Point update + range query (sum/min/max/gcd/xor, no range updates)
   -> Use SegmentTree. Only change: `merge` function + `identity` value.
     identity must satisfy merge(identity, x) == x for any x.

2. Range add + range sum
   -> Use LazySegmentTree as-is, no changes needed.

3. Range add + range min (or max)
   -> Use LazySegmentTreeRangeAddMin below. The 3 spots that differ
      from the sum version are marked "DIFFERS FROM SUM VERSION".

4. No updates at all, just static range min/max
   -> Don't use a tree at all — a sparse table gives O(1) query with
      O(n log n) preprocessing. Simpler and faster than either class here.
"""
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


# ---- Same class, five different problems -- only merge/identity change ----
data = [2, 4, 6, 8, 10]

sum_tree = SegmentTree(data, merge=lambda a, b: a + b, identity=0)
min_tree = SegmentTree(data, merge=min, identity=math.inf)
max_tree = SegmentTree(data, merge=max, identity=-math.inf)
gcd_tree = SegmentTree(data, merge=math.gcd, identity=0)
xor_tree = SegmentTree(data, merge=lambda a, b: a ^ b, identity=0)

print(sum_tree.query(1, 4))   # 4+6+8 = 18
print(min_tree.query(0, 3))   # min(2,4,6) = 2


# ============================================================
# RANGE updates (e.g. "add x to every element in [l, r)") need
# lazy propagation, which requires recursion — the iterative
# trick above can't be extended to this cleanly.
# ============================================================

class LazySegmentTree:
    """Range add, range sum. The most common lazy-propagation variant."""

    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)   # 4n is a safe upper bound on tree size
        self.lazy = [0] * (4 * self.n)   # lazy[node] = pending value not yet pushed to children
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, l, r):
        if l == r:
            self.tree[node] = data[l]
            return
        mid = (l + r) // 2
        self._build(data, 2 * node, l, mid)
        self._build(data, 2 * node + 1, mid + 1, r)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]   # combine step: + for sum

    def _push_down(self, node, l, r):
        # Sends this node's pending update down to its children before we
        # recurse into them, so they reflect updates applied to their parent.
        if self.lazy[node]:
            mid = (l + r) // 2
            for child, cl, cr in ((2 * node, l, mid), (2 * node + 1, mid + 1, r)):
                self.lazy[child] += self.lazy[node]                          # pending value: additive, so it stacks
                self.tree[child] += self.lazy[node] * (cr - cl + 1)          # sum needs count of elements affected
            self.lazy[node] = 0

    def update(self, ql, qr, val, node=1, l=0, r=None):
        """Add val to every element in [ql, qr] (inclusive)."""
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:          # no overlap
            return
        if ql <= l and r <= qr:       # fully covered: apply here, don't recurse further
            self.tree[node] += val * (r - l + 1)
            self.lazy[node] += val
            return
        self._push_down(node, l, r)   # partial overlap: must go deeper, so flush first
        mid = (l + r) // 2
        self.update(ql, qr, val, 2 * node, l, mid)
        self.update(ql, qr, val, 2 * node + 1, mid + 1, r)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, ql, qr, node=1, l=0, r=None):
        """Sum over [ql, qr] (inclusive)."""
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return 0                  # identity for sum
        if ql <= l and r <= qr:
            return self.tree[node]
        self._push_down(node, l, r)
        mid = (l + r) // 2
        return self.query(ql, qr, 2 * node, l, mid) + self.query(ql, qr, 2 * node + 1, mid + 1, r)


class LazySegmentTreeRangeAddMin:
    """
    Range add, range min. Same skeleton as LazySegmentTree above, but 3
    spots change because "min" doesn't scale with the number of elements
    the way "sum" does — each is marked DIFFERS FROM SUM VERSION.
    (For range max: swap every min() below for max(), and identity to -inf.)
    """

    def __init__(self, data):
        self.n = len(data)
        self.tree = [math.inf] * (4 * self.n)   # DIFFERS: identity is +inf, not 0
        self.lazy = [0] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, l, r):
        if l == r:
            self.tree[node] = data[l]
            return
        mid = (l + r) // 2
        self._build(data, 2 * node, l, mid)
        self._build(data, 2 * node + 1, mid + 1, r)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])   # DIFFERS: min, not +

    def _push_down(self, node, l, r):
        if self.lazy[node]:
            mid = (l + r) // 2
            for child in (2 * node, 2 * node + 1):
                self.lazy[child] += self.lazy[node]
                self.tree[child] += self.lazy[node]   # DIFFERS: no "* count" — adding val shifts
                                                        # every element (and so the min) by val,
                                                        # regardless of how many elements there are
            self.lazy[node] = 0

    def update(self, ql, qr, val, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.tree[node] += val          # DIFFERS: no "* count", see _push_down note above
            self.lazy[node] += val
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        self.update(ql, qr, val, 2 * node, l, mid)
        self.update(ql, qr, val, 2 * node + 1, mid + 1, r)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, ql, qr, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return math.inf             # identity for min
        if ql <= l and r <= qr:
            return self.tree[node]
        self._push_down(node, l, r)
        mid = (l + r) // 2
        return min(self.query(ql, qr, 2 * node, l, mid), self.query(ql, qr, 2 * node + 1, mid + 1, r))
