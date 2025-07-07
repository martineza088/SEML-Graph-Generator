#@author Alley Koenig

from genFunctions import norepet
from genFunctions import inrange

count =0
for k in range(-23,52):
    cycle=[1,2,3,4,5,6,7]
    for e2 in range(8,29):
        v2 = e2 -k+2
        e1 = e2 +1
        cycle= [1,2,3,4,5,6,7, v2,e1,e2]
        if not(norepet(cycle) and inrange(cycle,1, 28)):
            continue
        for e4 in range(8,29):
            v4 = e4 -k +4
            e3 = e4 +1
            cycle= [1,2,3,4,5,6,7, v2,v4,e1,e2,e3,e4]
            if not(norepet(cycle) and inrange(cycle,1, 28)):
                continue
            for e6 in range(8,29):
                v6 = e6 -k +6
                e5 = e6 +1
                cycle= [1,2,3,4,5,6,7, v2,v4,v6,e1,e2,e3,e4,e5,e6]
                if not(norepet(cycle) and inrange(cycle,1, 28)):
                    continue
                for e8 in range(8,29):
                    v8 = e8 -k +8
                    e7 = e8 +1
                    cycle= [1,2,3,4,5,6,7,v2,v4,v6,v8,e1,e2,e3,e4,e5,e6,e7,e8]
                    if not(norepet(cycle) and inrange(cycle,1, 28)):
                        continue
                    for e10 in range(8,29):
                        v10 = e10 -k +10
                        e9 = e10 +1
                        cycle= [1,2,3,4,5,6,7,v2,v4,v6,v8,v10,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
                        if not(norepet(cycle) and inrange(cycle,1, 28)):
                            continue
                        for e12 in range(8,29):
                            v12 = e12 -k +12
                            e11 = e12 +1
                            cycle= [1,2,3,4,5,6,7,v2,v4,v6,v8,v10,v12,
                                e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]
                            if not(norepet(cycle) and inrange(cycle,1, 28)):
                                continue
                            for e14 in range(8,29):
                                v14 = e14 -k + 14
                                e13 = e14 +1
                                cycle= [1,2,3,4,5,6,7,v2,v4,v6,v8,v10,v12,v14,
                                    e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14]
                                if not(norepet(cycle) and inrange(cycle,1, 28)):
                                    continue
                                print([[1,2,3,4,5,6,7],[v2,v4,v6,v8,v10,v12,v14],
                                  [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14]],"k= ",k)
                                count +=1
print("count = ", count)