m = [1, 0, 0, 1, 1]
m.reverse()
g = [[1, 1, 1], [1, 0, 1]]

ans = [[] for i in range(len(g))]

for idx, x in enumerate(g):
    padded_m = ([0] * (len(x) - 1)) + m + ([0] * (len(x) - 1))
    i = len(padded_m)
    while i > len(x) - 1:
        result = [num1 * num2 for num1, num2 in zip(padded_m[i - 3:i], x)]
        ans[idx].append(sum(result) % 2)
        i = i - 1
print(f"ans: {ans}")
for i in range(len(ans[0])):
    for j in range(len(ans)):
        print(ans[j][i], end="")
