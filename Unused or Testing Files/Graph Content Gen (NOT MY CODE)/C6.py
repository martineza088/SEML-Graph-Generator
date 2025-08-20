# @author Alley Koenig

from genFunctions import norepet

def inrange(cycle,min, max):
    ret =True
    for a in cycle:
        if a < min:
            return False
        elif a > max:
            return False
    return ret

count = 0
for k in range(-7,1):
    for v6 in range(1,13):
        for e5 in range(1,13):
            v5 = v6 -e5 +k
            cycle =[v5,v6,e5]
            if not norepet(cycle):
                continue
            if not inrange(cycle,1,12):
                continue
            for e4 in range(1,13):
                for e3 in range(1,13):
                    v4 = v6 +e4 -e5
                    v3 = v6 -e3 +e4 -e5 +k
                    cycle=[v3,v4,v5,v6,e3,e4,e5]
                    if not norepet(cycle):
                        continue
                    if not inrange(cycle,1,12):
                        continue
                    for e2 in range(1,13):
                        for e6 in range(1,13):
                            v1 = v6 -e6 +k
                            v2 = v6 +e2 -e3 +e4 -e5
                            e1 = e2-e3+e4-e5 +e6
                            cycle=[v1,v2,v3,v4,v5,v6,e1,e2,e3,e4,e5,e6]
                            if not norepet(cycle):
                                continue
                            if not inrange(cycle,1,12):
                                continue
                            count +=1
                            print(cycle, ' k=',k)
for k in range(1,13):
    for v6 in range(1,13):
        for e5 in range(1,13):
            v5 = v6 -e5 +k
            cycle =[v5,v6,e5]
            if not norepet(cycle):
                continue
            if not inrange(cycle,1,12):
                continue
            for e4 in range(1,13):
                for e3 in range(1,13):
                    v4 = v6 +e4 -e5
                    v3= v6 -e3 +e4 -e5 +k
                    cycle=[v3,v4,v5,v6,e3,e4,e5]
                    if not norepet(cycle):
                        continue
                    if not inrange(cycle,1,12):
                        continue
                    for e2 in range(1,13):
                        for e6 in range(1,13):
                            v1 = v6 -e6 +k
                            v2 = v6 +e2 -e3 +e4 -e5
                            if not(v2==k):
                                continue
                            e1 = e2-e3+e4-e5 +e6
                            cycle=[v1,v2,v3,v4,v5,v6,e1,e2,e3,e4,e5,e6]
                            if not norepet(cycle):
                                continue
                            if not inrange(cycle,1,12):
                                continue
                            count +=1
                            print(cycle, ' k=',k)
for k in range(13,21):
    for v6 in range(1,13):
        for e5 in range(1,13):
            v5 = v6 -e5 +k
            cycle =[v5,v6,e5]
            if not norepet(cycle):
                continue
            if not inrange(cycle,1,12):
                continue
            for e4 in range(1,13):
                for e3 in range(1,13):
                    v4 = v6 +e4 -e5
                    v3= v6 -e3 +e4 -e5 +k
                    cycle=[v3,v4,v5,v6,e3,e4,e5]
                    if not norepet(cycle):
                        continue
                    if not inrange(cycle,1,12):
                        continue
                    for e2 in range(1,13):
                        for e6 in range(1,13):
                            v1 = v6 -e6 +k
                            v2 = v6 +e2 -e3 +e4 -e5
                            e1 = e2-e3+e4-e5 +e6
                            cycle=[v1,v2,v3,v4,v5,v6,e1,e2,e3,e4,e5,e6]
                            if not norepet(cycle):
                                continue
                            if not inrange(cycle,1,12):
                                continue
                            count +=1
                            print(cycle, ' k=',k)
print(count)


