class Solution:

    def __init__(self):
        self.memo = [None for _ in range(31)]

    def fib(self, N):
        if N <= 1:
            return N
        if self.memo[N] is None:
            self.memo[N] = self.fib(N-1) + self.fib(N-2)
        return self.memo[N]

print(Solution().fib(2) == 1)
print(Solution().fib(3) == 2)
print(Solution().fib(4) == 3)
print(Solution().fib(20))
print(Solution().fib(30))