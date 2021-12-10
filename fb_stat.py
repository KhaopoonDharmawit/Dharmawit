from itertools import count


def sth_d(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def aerial_d(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def longb_d(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def dribbledp_d(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def inter_d(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def tackles_d(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def longb_m(x):
    if x >= 0.5:
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
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def passsuc_m(x):
    if x >= 75:
        ans = "H"
    else:
        ans = "L"
    return ans
def keyp_m(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def disp_f(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def dribbles_f(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def keyp_f(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def shots_f(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def xG_f(x):
    if x >= 0.5:
        ans = "H"
    else:
        ans = "L"
    return ans
def overall(p):
    num_H = p.count("H")
    num_L = p.count("L")
    if num_H > num_L:
        ans = "H"
    elif num_H == num_L:
        ans = "A"
    else:
        ans = "L"
    return ans
 


