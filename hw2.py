#Matt Layman - CS111 - HW2
key = ord("A")

#1A
def add(c1, c2):
    #converts characters into numbers, adds them and switches back to characters
    first = ord(c1)
    second = ord(c2)
    total = (first + second - key)
    if total > ord("Z"):
        return chr(total-26)
    else:
        return chr(total)

#1B
def encr(k, m):
    #encrypts string m using key k
    mEncrypted = ""

    for x in range(len(m)):
        tempChar = m[0]                #slice first letter of string
        m = m[1:]                      #declare m as rest of string
        tempChar = add(k, tempChar)    #add/encrypt
        mEncrypted += tempChar         #add encryption to a string

    return mEncrypted

#1C
def sub(c1, c2):
    #converts characters into numbers, subtracts them and switches back to characters
    first = ord(c1)
    second = ord(c2)
    total = (first - second + key)
    if total < key:
        return chr(total+26)
    else:
        return chr(total)

#1D
def decr(k, m):
    #converts string m into using key k
    mDecrypted = ""

    for x in range(len(m)):
        tempChar = m[0]                #slice first letter of string
        m = m[1:]                      #declare m as rest of string
        tempChar = sub(k, tempChar)    #subtract/decrypt
        mDecrypted += tempChar         #add decryption to a string

    return mDecrypted

#2A
def leapyear(y):
    #check leapyear
    return y%400 == 0 or (y%4 == 0 and y%100 != 0)

def realdate(*date):
    #split date into variables
    y = date[0]
    m = date[1]
    d = date[2]
    date = [y, m, d]
    #check real date
    if m in [1, 3, 5, 7, 8, 10, 12] and d <= 31:
        return True
    elif m in [4, 6, 9, 11] and d <= 30:
        return True
    #check leap year
    elif leapyear(y) == True and (m == 2 and d <= 28):
        return True
    elif leapyear(y) == False and (m == 2 and d <= 29):
        return True
    else:
        return False

#2B
def cmpdates(date1, date2):
    #split dates into variables and form lists
    y1 = date1[0]
    m1 = date1[1]
    d1 = date1[2]
    date1 = [y1, m1, d1]
    y2 = date2[0]
    m2 = date2[1]
    d2 = date2[2]
    date2 = [y2, m2, d2]
    #compare lists, return result
    if date1 < date2:
        return 1
    elif date1 == date2:
        return 0
    elif date1 > date2:
        return -1
    else:
        return None


print(cmpdates([1995, 4, 5],[1993, 5, 5]))
print(realdate(1992, 2, 29))
print(encr("T", "GALLIAESTOMNISDIVISAINPARTESTRES"))
