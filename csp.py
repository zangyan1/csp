from math import inf
import numpy as np

def backTrack(variable, csp, domain, ans):
    if len(ans) == len(variable):
        return ans

    for v in variable:
        if variable[v] != inf:
            val = v
            index = variable[v]
            variable[v] = inf
            break

    for d in domain[index]:
        if d != "":
            ans[val] = d
            color2delete = d
            temp=csp #记录更新前的csp
            temp1=domain #记录更新前的domain
            # 更新csp
            for i in range(0, len(variable)):
                if csp[index][i] == 1:
                    j = 0
                    for c in domain[i]:
                        if c == color2delete:
                            domain[i][j] = ""
                        j += 1
                    j = 0
            result = backTrack(variable, csp, domain, ans)
            if result != {}:
                return ans
            else:
                csp=temp
                domain=temp1
    return {}


variable = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
csp = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0]
]
# #等于1则代表邻接
domain = [
    ["red", "yellow", "blue"],
    ["red", "yellow", "blue"],
    ["red", "yellow", "blue"],
    ["red", "yellow", "blue"],
    ["red", "yellow", "blue"],
    ["red", "yellow", "blue"]
]
ans = {}
finall_ans = backTrack(variable, csp, domain, ans)
for f in finall_ans:
    print(f)
    print(finall_ans[f])
