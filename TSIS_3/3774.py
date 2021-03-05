ans = dict()
pairs = dict()
def create_tree(p):
    if p in ans:
        return ans[p]
    else:
        try:
            res = 0
            if p in pairs:
                for ch in pairs[p]:
                    res += create_tree(ch) + 1
            ans[p] = res
            return res
        except:
            pass
n = int(input())
for i in range(0, n-1):
    child, parent = input().split()
    if parent in pairs:
        pairs[parent].append(child)
    else:
        pairs[parent] = [child]
if n > 0:
    for k in pairs:
        create_tree(k)
    for key in sorted(ans.keys()):
        print(key, ans[key])