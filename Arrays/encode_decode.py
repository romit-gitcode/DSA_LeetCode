# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Input: 
strs = ["Hello","World"]
# Output: ["Hello","World"]

# Very Basic encode decode
def encode0(strs):
    return "".join(strs)

def decode0(strs):
    return strs.split(",")

#  Solution 1: 
def encode(strs):
    A = []
    for word in strs:
        A.append(str(len(word)))
        A.append('#')
        A.append(word)
    print(A)
    return "".join(A) 

print(encode(strs))
# print(decode(encode(strs)))