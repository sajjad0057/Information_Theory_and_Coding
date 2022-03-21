msg = [0, 1, 0, 1]
msg.reverse()
m = len(msg)
r = 1

while pow(2, r) < m + r + 1:
    r += 1

code = [0 for i in range(m + r + 1)]
for i in range(r):
    code[pow(2, i)] = -1
j = 0
for i in range(1, len(code)):
    if code[i] != -1:
        code[i] = msg[j]
        j += 1

for i in range(1, len(code)):
    if code[i] == -1:
        count = 0
        for j in range(i + 1, len(code)):
            if j & 1 << i - 1 == 1:
                if code[j] == 1:
                    count += 1
        if count % 2 == 0:
            code[i] = 0
        else:
            code[i] = 1
msg.reverse()
code.reverse()
print(f"Message bits are: {msg}")
print(f"Hamming code is: {code[:-1]}")