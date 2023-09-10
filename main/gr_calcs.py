import math

GR = math.sqrt(5) + 1
GR /= 2
GR_RECIP = 1 / GR

def test_n(n: int) -> float:
    return n + GR_RECIP * n

def test_v(v: int) -> float: 
    return v / (GR_RECIP + 1)