
# March 2, 2023
# Struggling to wrap my head around this logic.
def toBits(n):
    l = []
    while n>0:
        rest = int(n%2)
        print("num",n,"rest",rest,"next",int((n-n%2)/2))
        l.append(rest)
        n = int((n-rest)/2)
    return l
print(toBits(18)[::-1]) # it's backwards
print(format(18,"08b"))

# % python3 toBitsHardWayTryingToWrapHeadAround.py
# num 18 rest 0 next 9
# num 9 rest 1 next 4
# num 4 rest 0 next 2
# num 2 rest 0 next 1
# num 1 rest 1 next 0
# [1, 0, 0, 1, 0]
# 00010010

# Manually writing out??
# 18%2 = 0
# (18-0)/2 = 9
# 9%2 = 1
# (9-1)/2 = 4
# 4%2 = 0
# (4-0)/2 = 2
# 2%2 = 0
# (2-0)/2 = 1
# 1%2 = 1
# (1-1)/2 = 0 (end of loop, ignore)

# it goes up the powers backwards??
# Oh, I can kind of understand? But doesn't click well, it's weird
# this feels dirty. finding powers backwards
# maybe i'll find this explained better in future :u