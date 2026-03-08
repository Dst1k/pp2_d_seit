class cl1:
    def __init__(self, n, words):
        self.n = n
        self.words = words

    def pairs(self):
        for index, word in enumerate(self.words):
            print(f"{index}:{word}", end=" ")
n = int(input())
words = input().split()
indexer = cl1(n, words)
indexer.pairs()

class cl2:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def dotp(self):
        sum = 0
        for a,b in zip(self.a,self.b):
            sum += a*b
        return sum
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = cl2(a,b)
print(l.dotp())