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
    return "".join(A) 

encoded_string = encode(strs)
def decode(encoded_string):
    A = []
    i = 0
    while i<len(encoded_string):
        j=i
        while encoded_string[j] != '#':
            j+=1
        length = int(encoded_string[i:j])
        i=j+1
        j = i+length
        A.append(encoded_string[i:j])
        i = j
    return A

def encode1(strs):
    A=[]
    for word in strs:
        A.append(str(len(word)))
        A.append('#')
        A.append(word)
    return "".join(A)

encoded_string2 = encode1(strs)
print("encoded_string2: ", encoded_string2)
def decode1(string):
    A=[]
    i=0
    while i<len(string):
        j = i
        while string[j] != "#":
            j+=1
        num = int(string[i:j])
        i = j+1
        j = i + num
        A.append(string[i:j])
        i = j
    return A

print(decode1(encoded_string2))