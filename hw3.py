# Matt Layman -CS111 - HW3

#1.A
def ave(L):
    #set variables
    total = 0
    average = 0
    if L == []: return 0                       #take average of list
    for n in L: total += float(n)
    return total/len(L)

def ioAveNN():
    L = []
    x = int(input("Enter an integer: "))        #gather input
    while x > 0:                                #loop while input > 0
        L.append(x)
        x = int(input("Enter an integer:"))
    return ave(L)

#1.B
def ioAve():
    L = []
    count = 1
    x = input("Enter an integer: ")             #gather input
    while len(L) < count:                       #main loop for numerical char check
        if x[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+", "-"]:
            float(x)
            L.append(x)
            count += 1
            x = input("Enter an integer:")
        else: break                             #break if not numerical char
    return ave(L)

#2.A
import turtle

#star
#set screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("test")

#make turtle
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(4)

#map movement
tess.left(35)
tess.forward(150)
for i in range(4):
    tess.left(145)
    tess.forward(150)

wn.mainloop()

#2.B
#octagon
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(45)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(5)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Draw octagon")

draw_poly(tess, 8, 50)
wn.mainloop()

#equilateral triangle
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(120)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(5)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Draw equilateral triangle")

draw_poly(tess, 3, 50)
wn.mainloop()

#square
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(90)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(5)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Draw square")

draw_poly(tess, 4, 50)
wn.mainloop()

#rectangular polygon
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(72)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(5)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Draw rectangular polygon")

draw_poly(tess, 5, 50)
wn.mainloop()

#regular 17-gon
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(21)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(5)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Draw 17-gon")

draw_poly(tess, 17, 50)
wn.mainloop()

#3.A

def leapyear(y):
    #check leapyear
    return y%400 == 0 or (y%4 == 0 and y%100 != 0)

def istime(t):
    """
    mo = t[0]
    d = t[1]
    y = t[2]
    h = t[3]
    mi = t[4]
    s = t[5]
    """
    #check valid time
    if t[0] in range(1,13) and t[1] <= 31 and t[3] <= 24 and t[4] <= 60 and t[5] <= 60: return True
    elif leapyear(t[2]) and (t[0] == 2 and t[1] <=28): return True
    elif leapyear(t[2]) == False and (t[0] == 2 and t[1] <= 29): return False
    else: return False

#3.B
def normalize(L):
    #normalize list if needed
    if len(L) != 6: return "Error"
    elif L[0] > 31: return L
    else: return [L[2], L[0], L[1], L[3], L[4], L[5]]

#3.C
def cmptimes(t1, t2):
    #comare lists, return results
    if t1 > t2: return 1
    elif t1 == t2: return 0
    elif t1 < t2: return -1
    else: return None

#3.D
print(istime([1960, 2, 29, 12, 44, 2]))
print(istime([1960, 1, 22, 12, 44, 60.1]))
print(normalize([12, 12, 2013, 13, 45, 12.3]))
print(cmptimes([12, 12, 2013, 13, 45, 12.3], [3, 17, 2014, 15, 55, 55.8]))


