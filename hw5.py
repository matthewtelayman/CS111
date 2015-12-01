#Matt Layman - CS111 - HW5

#1

def rmDuplic(L):
    M = []                                      #initialize blank list
    for i in L:
        if i not in M: M.append(i)              #if not in new list, append element
    return M


print(rmDuplic([35, 35, 25, 29, 29, 35]))

"""
#2.A

LL = [x for x in range(-10, 11)]
print(LL)
#2.B

SL = [x**(1/2) for x in LL if x > 0]
print(SL)
"""

#3.A

def depth(LL):
    if LL == []: return 1                                   #base case
    elif type(LL) != list: return 0                         #base case
    else: return 1 + max([depth(x) for x in LL])            #recursion step

#3.B
"""
L = []
for i in range(10):
    L = L + [L[len(L)//2:]+[i,[i-1]]]

print(depth(L))
>>> 12
"""

#4.A

def numOccur(s):
    dic = {}                                                #initialize empty dictionary
    letters = "abcdefghijklmnopqrstuvwxyz"                  #key
    for i in s:
        if i in letters:                                    #if element of s in letters
            if i in dic: dic[i] += 1                        #if element in dic, increment 1
            else: dic[i] = 1                                #if element not in dic, make 1
    return dic


#4.B
"""
F = open("C:/users/matt/desktop/homework/rutgers/programming/DictFileSetHW.txt", "r")
s = F.read()
print(numOccur(s))
>>>
{'a': 188, 'c': 74, 'b': 43, 'e': 477, 'd': 123, 'g': 55, 'f': 129, 'i': 244, 'h': 76, 'k': 33, 'j': 4,
 'm': 82, 'l': 121, 'o': 216, 'n': 228, 'q': 8, 'p': 66, 's': 194, 'r': 215, 'u': 95, 't': 277,
 'w': 40, 'v': 36, 'y': 41, 'x': 10, 'z': 9}
 """
