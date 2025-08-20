# @author Alley Koenig

# CHANGE OUTPUT FORMAT FOR THIS (- wrong format, - output includes k-values -> must be excluded, - takes a long time to create output)

from genFunctions import norepet
from genFunctions import inrange

count = 0
k = 0
for v10 in range(1,21):
    print(v10)
    for e10 in range(1,21):
        v1= v10 -e10 + k
        #if not(v1 ==1):
            #continue
        cycle = [v1,v10,e10]
        if not(norepet(cycle) and inrange(cycle,1, 20)):
            continue
        for e9 in range(1,21):
            for e8 in range(1,21):
                v9 = v10 -e9 + k
                v8 = v10 +e8 -e9
                cycle =[v1,v8,v9,v10,e8,e9,e10]
                if not(norepet(cycle) and inrange(cycle,1, 20)):
                    continue
                for e7 in range(1,21):
                    for e6 in range(1,21):
                        v6= v10 +e6 -e7 +e8 -e9
                        v7 = v10 -e7+e8 -e9 + k
                        cycle =[v1,v6,v7,v8,v9,v10,e6,e7,e8,e9,e10]
                        if not(norepet(cycle) and inrange(cycle,1, 20)):
                            continue
                        for e5 in range(1,21):
                            for e4 in range(1,21):
                                v4 = v10 +e4 -e5 +e6 -e7 +e8 -e9 
                                v5 = v10 -e5 +e6 -e7 +e8 -e9 + k
                                cycle =[v1,v4,v5,v6,v7,v8,v9,v10,e4,e5,e6,e7,e8,e9,e10]
                                if not(norepet(cycle) and inrange(cycle,1, 20)):
                                    continue
                                for e3 in range(1,21):
                                    for e2 in range(1,21):
                                        v2 = v10 +e2 -e3 +e4 -e5 +e6 -e7 +e8 -e9
                                        v3 = v10 -e3 +e4  -e5 +e6 -e7 +e8 -e9 + k
                                        e1 = e2 -e3 +e4 -e5 +e6 -e7 +e8 -e9 +e10
                                        cycle =[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
                                        if not(norepet(cycle) and inrange(cycle,1, 20)):
                                            continue
                                        odd=[v1,v3,v5,v7,v9]
                                        if not ((1 in odd)and (2 in odd) and (3 in odd)):
                                            continue
                                        count +=1
                                        cycle = [[v1,v3,v5,v7,v9],[v2,v4,v6,v8,v10],
                                                [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]]
                                        reformattedCycle = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
                                        print(reformattedCycle, ' k =', k)
print(count)