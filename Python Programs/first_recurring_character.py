# FIRST RECURRING CHARACTER

def firstRecurringCharacter(ipStr):
    counts = {}
    for char in ipStr:
        print(counts)
        if char in counts:
            return char
        counts[char] = 1
    return None

ip = "ABBA"
print("INPUT STRING: "+str(ip))
op = firstRecurringCharacter(ip)
print("FIRST RECURRING CHARACTER: "+str(op))
