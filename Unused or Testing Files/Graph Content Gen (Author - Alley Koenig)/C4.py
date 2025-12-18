#@author Alley Koenig

from genFunctions import norepet
from genFunctions import inrange

count =0
for k in range(-3,1):
    for v4 in range(1,9):
        for e4 in range(1,9):
            v1 =v4 -e4 +k
            cycle = [v1,v4,e4]
            if not(norepet(cycle) and inrange(cycle,1, 8)):
                continue
            for e2 in range(1,9):
                for e3 in range(1,9):
                    v2 = v4 +e2-e3
                    v3 = v4 -e3 +k
                    e1 = e2 -e3 +e4
                    cycle=[v1,v2,v3,v4,e1,e2,e3,e4]
                    if not(norepet(cycle) and inrange(cycle,1, 8)):
                        continue
                    count += 1
                    print(cycle, ' k =',k)
for k in range(1,9):
    for v4 in range(1,9):
        for e4 in range(1,9):
            v1 =v4 -e4 +k
            cycle = [v1,v4,e4]
            if not(norepet(cycle) and inrange(cycle,1, 8)):
                continue
            for e2 in range(1,9):
                for e3 in range(1,9):
                    v2 = v4 +e2-e3
                    if not(v2==k):
                        continue
                    v3 = v4 -e3 +k
                    e1 = e2 -e3 +e4
                    cycle=[v1,v2,v3,v4,e1,e2,e3,e4]
                    if not(norepet(cycle) and inrange(cycle,1, 8)):
                        continue
                    count += 1
                    print(cycle, ' k =',k)
for k in range(9,13):
    for v4 in range(1,9):
        for e4 in range(1,9):
            v1 =v4 -e4 +k
            cycle = [v1,v4,e4]
            if not(norepet(cycle) and inrange(cycle,1, 8)):
                continue
            for e2 in range(1,9):
                for e3 in range(1,9):
                    v2 = v4 +e2-e3
                    v3 = v4 -e3 +k
                    e1 = e2 -e3 +e4
                    cycle=[v1,v2,v3,v4,e1,e2,e3,e4]
                    if not(norepet(cycle) and inrange(cycle,1, 8)):
                        continue
                    count += 1
                    print(cycle, ' k =',k)
print(count)
