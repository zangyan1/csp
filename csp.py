from math import inf
import numpy as np
def MRV(csp):    #合法取值最少的变量
    c=np.sum(csp,axis=1)
    index=0
    j=0
    max=0
    for i in c:
        if i>max:
            index=j
            max=i
        j+=1
    return index



def backTrack(variable, csp, domain, ans):
    if len(ans) == len(variable):
        return ans
    # index=MRV(csp)
    # val=variable.get(index)     #已知值，没有办法返回键的
    # index2=MRV(csp)
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
                ans.pop(val, color2delete)
                for i in range(0, len(variable)):
                    if csp[index][i] == 1:
                        for c in domain[i]:
                            if c == "":
                                c = color2delete
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
