# Matthew Layman -- CS111 -- HW1

#1.A
def temp(T, unit):
    if unit in ["F", "f"]:
        return 32 + (9/5 * T)
    elif unit in ["K", "k"]:
        return T + 273.15
    elif unit in ["C", "c"]:
        return (5/9)*(T - 32)
    else:
        return None

#1.B
"""in order to write a compare function, both temperatures must be in the same
unit. to do this, a third variable is required in the first function to convert
T1 into T2, compare them equally and return a result."""

def temp(T, unit, convertedUnit):
    #check unit, convert into convertedUnit
    if unit in ["F", "f"]:
        if convertedUnit in ["C", "c"]:
            return (5/9)*(T-32)
        elif convertedUnit in ["K", "k"]:
            return (T + 459.67) * (5/9)
    elif unit in ["K", "k"]:
        if convertedUnit in ["C", "c"]:
            return (T - 273.15)
        elif convertedUnit in["F", "f"]:
            return (T * (9/5)) - 459.67
    elif unit in ["C", "c"]:
        if convertedUnit in ["F", "f"]:
            return (9/5 * T) + 32
        elif convertedUnit in ["K", "k"]:
            return (T + 273.15)
    else:
        return None

def comp(T1, u1, T2, u2):

    temp1 = temp(T1, u1, u2)
    #compare temps, return result
    if temp1 > T2:
        return -1
    elif temp1 == T2:
        return 0
    elif temp1 < T2:
        return 1
    else:
        return None

#2
def P(P_0, t, i):
    #declare variables
    time = int(t)
    rate = float(i)
    po = float(P_0)

    #compound interest formula
    p = po*((1 + (rate)/100))**time
    #return total
    return p

#3
def leapyear(y):
    #check leapyear
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False
