def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def BubbleSort(L):
    n = len(L)
    left, right = 0, n-1
    while left < right:
        for i in range(left, right, 1):
            if L[i] > L[i+1]:
                swap(L, i, i+1)
        right -= 1
        for j in range(right, left, -1):
            if L[j] < L[j-1]:
                swap(L, j, j-1)
        left += 1

def InsertionSort(L):
    n = len(L) - 1
    for i in range(1,n+1):
        get = L[i]
        left = 0
        right = i-1
        while(left<=right):
            mid = int((left+right)/2)
            if (L[mid] > get):
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i-1,left,-1):
            L[j+1] = L[j]
        L[left] = get

def Merge(B,C):
    D = []
    while len(B) and len(C):
        bs = B[0]
        cs = C[0]
        if bs <= cs:
            D.append(bs)
            B.pop(0)
        else:
            D.append(cs)
            C.pop(0)

    if B:
        D = D + B
    elif C:
        D = D + C
    return D


def MergeSort(L):
    if len(L) == 1:
        return L
    m = int(len(L)/2)
    B = MergeSort(L[0:m])
    C = MergeSort(L[m:])
    A = Merge(B,C)
    return A


def Partition(A,l,r):
    x = A[l]
    j = l
    for i in range(l+1,r+1):
        if A[i] <= A[l]:
            j = j + 1
            swap(A,i,j)
    swap(A,j,l)
    return j


def QuickSortIteration(A,l,r):
    if l >= r:
        return
    m = Partition(A,l,r)
    QuickSortIteration(A,l,m-1)
    QuickSortIteration(A, m+1, r)


def QuickSort(L):
    QuickSortIteration(L, 0, len(L)-1)


def LeftChild(i):
    return 2*(i+1)


def RightChild(i):
    return 2*(i+1)+1


def ShiftDown(L, i, size):
    maxIndex = i
    left = LeftChild(i)
    if left <= size and L[left-1] > L[maxIndex]:
        maxIndex = left - 1
    right = RightChild(i)
    if right <= size and L[right-1] > L[maxIndex]:
        maxIndex = right - 1

    if i != maxIndex:
        swap(L, i, maxIndex)
        ShiftDown(L, maxIndex, size)


def BuildHeap(L):
    size = len(L)
    for i in range(int(size/2), -1, -1):
        ShiftDown(L, i, size)
    return size


def ArrayHeapSort(L):
    size = BuildHeap(L)
    for i in range(size-1):
        swap(L, 0, size-1)
        size = size - 1
        ShiftDown(L, 0, size)