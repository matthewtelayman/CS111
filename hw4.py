# Matt Layman - CS111 - HW4

#1.A

def detab(s, m):
    newstring = ""
    for x in s:
        if x == "\t":
            while (len(newstring)%m != 0): newstring += "_"
        else: newstring += x
    return newstring

print(detab("ab\t\tc\td\te", 10))
print("ab\t\tc\td\te")


#2A

def isPerm(P):
    count = 0                                   #initialize
    for x in range(len(P)):
        s = P[x]
        if s < len(P): count += 1               #add to count if P[x] in len(P)
        else: count += 0
    if count == len(P): return True             #if count = len(P), return true
    else: return False

print(isPerm([1, 0, 2]))

#2B

def apply(L, P):
    if len(L) != len(P): return "Error"
    if isPerm(P) == True:
        m = []                                  #set blank list m
        for x in range(len(L)):
            s = P[x]                            #set initial index of P to s
            t = L[s]                            #set t to s index of L
            m.append(t)                         #append t to list m
        return m
    else: return "Error"

print(apply(['ah', 'boo', 'cc', 'du', 'eh'], [1, 4, 3, 2, 0]))

#2C

def inv(P):
    if isPerm(P) == True:
        m = []                                  #initialize blank list m
        for x in range(len(P)):
            s = len(P) - 1                      #set s to indices of P
            t = P[s]                            #extract last entry of list P
            P = P[:s]                           #set P to rest of list
            m.append(t)                         #append last entry of P to first entry of m
        return m
    else: return "Error"

print(inv([4, 2, 0, 1, 3]))

#3A

def encr(k, m):
    u = []                                      #set blank list u
    t = len(m)
    s = len(k)
    while t%s != 0: m.append("Z")               #while len(m)%len(k) != 0, append Z's
    for x in range(t//s):
        mchunk = m[:s]                          #take chunk of m size of len(k)
        m = m[s:]                               #set rest of string
        e = "".join(apply(mchunk, k))           #apply encryption and join list
        u.append(e)                             #append result to list u
    return "".join(u)                           #join list u

#3B

def decr(k, c):
    u = []
    t = len(c)
    s = len(k)
    while t%s != 0: c.append("Z")
    for x in range(t//s):
        cchunk = c[:s]                          #take chunk of c size of len(k)
        c = c[s:]                               #set rest of string
        j = inv(k)                              #invert permutation that has been applied
        e = "".join(apply(cchunk, j))           #apply inverted permutation to chunk of c and join
        u.append(e)                             #append result to u
    return "".join(u)                           #join list u

#3C

print(encr([3, 2, 4, 1, 0], "SineLaboreNihil"))
# >>> enLiSroebaihliN
print(decr([6, 1, 0, 2, 7, 4, 5, 3], "EAGLSIALDOTMIISNPIVSAINAATREMUNM"))
# >>> LISLGEAAMIINTDOSSIAAVPINEUMMRATN
