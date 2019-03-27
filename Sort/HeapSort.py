import math


class Heap(object):
    def __init__(self, L = []):
        self.list = L
        self.size = len(L)

    def Swap(self,i, j):
        temp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = temp

    def Parent(self,i):
        return int(math.floor((i-1)/2))

    def LeftChild(self,i):
        return 2*(i+1)

    def RightChild(self,i):
        return 2*(i+1) + 1

    def ShiftUp(self, i):
        while i > 0 and self.list[self.Parent(i)] < self.list[i]:
            self.Swap(i, self.Parent(i))
            i = self.Parent(i)

    def ShiftDown(self,i):
        maxIndex = i
        left = self.LeftChild(i)
        if left <= self.size and self.list[left-1] > self.list[maxIndex]:
            maxIndex = left - 1
        right = self.RightChild(i)
        if right <= self.size and self.list[right-1] > self.list[maxIndex]:
            maxIndex = right - 1
        if i != maxIndex:
            self.Swap(i, maxIndex)
            self.ShiftDown(maxIndex)

    def Insert(self, p):
        self.size = self.size + 1
        #self.list[self.size] = p
        self.list.append(p)
        self.ShiftUp(self.size-1)

    def ExtractMax(self):
        result = self.list[0]
        self.list[0] = self.list[self.size-1]
        self.size = self.size - 1
        self.ShiftDown(0)
        return result

    def Remove(self, i):
        self.list[i] = math.inf
        self.ShiftUp(i)
        self.ExtractMax(i)

    def ChangePriority(self, i, p):
        oldp = self.list[i]
        self.list[i] = p
        if p > oldp:
            self.ShiftUp(i)
        else:
            self.ShiftDown(i)

def HeapSort(L):
    h = Heap()
    for n in L:
        h.Insert(n)
    for i in range(len(L)-1, -1, -1):
        L[i] = h.ExtractMax()

