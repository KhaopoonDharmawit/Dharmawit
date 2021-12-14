from itertools import count


def blocks_d(x):
    if x >= 0.7:
        ans = "H"
    else:
        ans = "L"
    return ans
def aerial_d(x):
    if x >= 4.0:
        ans = "H"
    else:
        ans = "L"
    return ans
def longb_d(x):
    if x >= 4.0:
        ans = "H"
    else:
        ans = "L"
    return ans
def dribbledp_d(x):
    if x <= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def inter_d(x):
    if x >= 1.0:
        ans = "H"
    else:
        ans = "L"
    return ans
def tackles_d(x):
    if x >= 1.0:
        ans = "H"
    else:
        ans = "L"
    return ans
def tackles_m(x):
    if x >= 2.0:
        ans = "H"
    else:
        ans = "L"
    return ans
def longb_m(x):
    if x >= 3.0:
        ans = "H"
    else:
        ans = "L"
    return ans
def disp_m(x):
    if x <= 1.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def dribbles_m(x):
    if x >= 1.0:
        ans = "H"
    else:
        ans = "L"
    return ans
def passsuc_m(x):
    if x >= 75.0:
        ans = "H"
    else:
        ans = "L"
    return ans
def keyp_m(x):
    if x >= 2.0:
        ans = "H"
    else:
        ans = "L"
    return ans
def aerial_f(x):
    if x >= 3.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def disp_f(x):
    if x <= 2.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def dribbles_f(x):
    if x >= 2.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def keyp_f(x):
    if x >= 1.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def shots_f(x):
    if x >= 2.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def xG_f(x):
    if x >= 0.5 :
        ans = "H"
    else:
        ans = "L"
    return ans
def overall(p):
    num_H = p.count("H")
    num_L = p.count("L")
    if num_H > num_L:
        ans = "This player has a high potential\n to be a World Class player!"
    elif num_H == num_L:
        ans = "This player is average and well-rounded."
    else:
        ans = "This player still lacks of some abilities,\n more days to improve."
    return ans
 


