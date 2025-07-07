# @author Alley Koenig

from genFunctions import norepet
from genFunctions import inrange


count = 0
for k in range(-11,1):
    for v8 in range(1,17):
        for e8 in range(1,17):
            v1 = v8 -e8 + k
            cycle =[v1,v8,e8]
            if not(norepet(cycle) and inrange(cycle,1, 16)):
                continue
            for e7 in range(1,17):
                for e6 in range(1,17):
                    v6= v8 +e6- e7 
                    v7= v8 -e7 +k
                    cycle = [v1,v6,v7,v8,e6,e7,e8]
                    if not(norepet(cycle) and inrange(cycle,1, 16)):
                        continue
                    for e4 in range(1,17):
                        for e5 in range(1,17):
                            v4 = v8 +e4 -e5 +e6 -e7
                            v5 = v8 -e5 +e6 -e7 +k
                            cycle = [v1,v4,v5,v6,v7,v8,e4,e5,e6,e7,e8]
                            if not(norepet(cycle) and inrange(cycle,1, 16)):
                                continue
                            for e2 in range(1,17):
                                for e3 in range(1,17):
                                    v2 = v8 +e2-e3+e4-e5+e6-e7
                                    v3 = v8 -e3+e4-e5+e6-e7 +k
                                    e1 = e2 -e3 +e4 -e5 +e6 -e7 +e8
                                    cycle = [v1,v3,v5,v7,v2,v4,v6,v8,e1,e2,e3,e4,e5,e6,e7,e8]
                                    if not(norepet(cycle) and inrange(cycle,1, 16)):
                                        continue
                                    count += 1
                                    print(cycle, ' k=',k)
for k in range(1,17):
    for v8 in range(1,17):
        for e8 in range(1,17):
            v1 = v8 -e8+k
            cycle =[v1,v8,e8]
            if not(norepet(cycle) and inrange(cycle,1, 16)):
                continue
            for e7 in range(1,17):
                for e6 in range(1,17):
                    v6= v8 +e6- e7 
                    v7= v8 -e7 +k
                    cycle = [v1,v6,v7,v8,e6,e7,e8]
                    if not(norepet(cycle) and inrange(cycle,1, 16)):
                        continue
                    for e4 in range(1,17):
                        for e5 in range(1,17):
                            v4 = v8 +e4 -e5 +e6 -e7
                            v5 = v8 -e5 +e6 -e7 +k
                            cycle = [v1,v4,v5,v6,v7,v8,e4,e5,e6,e7,e8]
                            if not(norepet(cycle) and inrange(cycle,1, 16)):
                                continue
                            for e2 in range(1,17):
                                for e3 in range(1,17):
                                    v2 = v8 +e2-e3+e4-e5+e6-e7
                                    if not (v2==k):
                                        continue
                                    v3 = v8 -e3+e4-e5+e6-e7 +k
                                    e1 = e2 -e3 +e4 -e5 +e6 -e7 +e8
                                    cycle = [v1,v3,v5,v7,v2,v4,v6,v8,e1,e2,e3,e4,e5,e6,e7,e8]
                                    if not(norepet(cycle) and inrange(cycle,1, 16)):
                                        continue
                                    count += 1
                                    print(cycle, ' k=',k)
for k in range(17,29):
    for v8 in range(1,17):
        for e8 in range(1,17):
            v1 = v8 -e8+k
            cycle =[v1,v8,e8]
            if not(norepet(cycle) and inrange(cycle,1, 16)):
                continue
            for e7 in range(1,17):
                for e6 in range(1,17):
                    v6= v8 +e6- e7 
                    v7= v8 -e7 +k
                    cycle = [v1,v6,v7,v8,e6,e7,e8]
                    if not(norepet(cycle) and inrange(cycle,1, 16)):
                        continue
                    for e4 in range(1,17):
                        for e5 in range(1,17):
                            v4 = v8 +e4 -e5 +e6 -e7
                            v5 = v8 -e5 +e6 -e7 +k
                            cycle = [v1,v4,v5,v6,v7,v8,e4,e5,e6,e7,e8]
                            if not(norepet(cycle) and inrange(cycle,1, 16)):
                                continue
                            for e2 in range(1,17):
                                for e3 in range(1,17):
                                    v2 = v8 +e2-e3+e4-e5+e6-e7
                                    v3 = v8 -e3+e4-e5+e6-e7 +k
                                    e1 = e2 -e3 +e4 -e5 +e6 -e7 +e8
                                    cycle = [v1,v3,v5,v7,v2,v4,v6,v8,e1,e2,e3,e4,e5,e6,e7,e8]
                                    if not(norepet(cycle) and inrange(cycle,1, 16)):
                                        continue
                                    count += 1
                                    print(cycle, ' k=',k)
print(count)