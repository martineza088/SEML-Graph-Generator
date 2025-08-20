# @author Alley Koenig

import networkx as nx
import plotly as ply
import numpy as np
import sympy as sym

def norepet(cycle):
    ret = True
    NewList = []
    for a in cycle:
        if a not in NewList:
            NewList.append(a)
        else:
            return False
    return ret

def inrange(cycle,min, max):
    ret = True
    for a in cycle:
        if a < min:
            return False
        elif a > max:
            return False
        if not(a % 1 == 0):
            return False
    return ret

