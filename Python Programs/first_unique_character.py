# First Unique Character in a String

def firstUniqueCharacter(ipStr):
    counts = {}
    for char in ipStr:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    print(counts)
    if 1 in counts.values():
        for key, value in counts.items():
            if value == 1:
                return key , ipStr.index(key)
    else:
        return -1 

ip = "ABBCAD"
print("INPUT STRING: "+str(ip))
op , index = firstUniqueCharacter(ip)
print("FIRST Unique CHARACTER "+str(op)+" at index "+str(index))
