class Node:
    def __init__(self, character, probability, leftnode, rightnode):
        self.character = character
        self.probability = probability
        self.leftnode = leftnode
        self.rightnode = rightnode


text = "i am sajjad"  # input("Enter Text: ")
text = text.replace(" ", "")

frequency_list = {}

for i in text:
    frequency_list[i] = frequency_list.setdefault(i, 0) + 1

node_list = []
# node_list.append(Node('x1', 0.05, None, None))
# node_list.append(Node('x2', 0.10, None, None))
# node_list.append(Node('x3', 0.15, None, None))
# node_list.append(Node('x4', 0.20, None, None))
# node_list.append(Node('x5', 0.23, None, None))
# node_list.append(Node('x6', 0.27, None, None))


for i in frequency_list:
    fre = frequency_list[i] / len(text)
    node_list.append(Node(i, fre, None, None))

while len(node_list) != 1:
    node_list.sort(key=lambda x: x.probability)
    node1 = node_list.pop(0)
    node2 = node_list.pop(0)
    node_list.append(
        Node(node1.character + node2.character, node1.probability + node2.probability, leftnode=node1, rightnode=node2))

source_code = {}

print("Source code Table: ")


def travel(local_node, code):
    if local_node.leftnode is None and local_node.rightnode is None:
        print(f"\t\t\t\t\t{local_node.character} -> {code}")
        source_code[local_node.character] = code
    if local_node.leftnode is not None:
        travel(local_node.leftnode, code + "0")
    if local_node.rightnode is not None:
        travel(local_node.rightnode, code + "1")


travel(node_list[0], "")
encoded_string = ""
for i in text:
    encoded_string += source_code[i]

print(f"Encoded string is: {encoded_string}")

r_source_code = dict(zip(source_code.values(), source_code.keys()))

decoded_string = ""
i = 0
while i < len(encoded_string):
    j = i + 1
    while j < len(encoded_string) + 1:
        temp = encoded_string[i:j]
        if encoded_string[i:j] in r_source_code:
            decoded_string += r_source_code[encoded_string[i:j]]
            i = j
            break
        j = j + 1

print(f"Decoded String is: {decoded_string}")
