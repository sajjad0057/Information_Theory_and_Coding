text = "WYS*WYGWYS*WYSWYSG"
table = {}
for i in range(256):
    table[chr(i)] = i
code = 256
output_code = []
i = 0
print("Encoding: ")
print("String\t Output code \t Additional \t code")
while i < len(text):
    current_char = text[i]
    cval, out = "", 0
    while current_char in table:
        cval, out = current_char, table[current_char]
        i += 1
        if i < len(text):
            current_char += text[i]
        else:
            break
    else:
        print(f"{cval}\t\t\t\t{out}\t\t\t{current_char}\t\t\t{code}")
        table[current_char] = code
        code += 1

    output_code.append(out)
    # print(f"{cval}\t\t{out}")
print(f"Output Codes are: {output_code}")
r_source_code = dict(zip(table.values(), table.keys()))

print("Decoding: ", end=" ")
for i in output_code:
    print(r_source_code[i], end="")
