def euclidean(a,b):
    t = a % b
    while(t):
        a = b
        b = t
        t = a%b
    return b
