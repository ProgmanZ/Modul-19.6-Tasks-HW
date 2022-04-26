k = int(input())
n_set = set()
enter = list()
export = dict()
for i in range(k):
    enter.append(int(input()))

for elm in enter:
    n_set.add(elm)

for x in n_set:
    export[x] = f(x)

for s in enter:
    print(export[s])
