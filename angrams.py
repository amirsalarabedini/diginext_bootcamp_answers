from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)

    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)
        
    return list(anagrams.values())

strs = ["eat", "tesa", "tan", "ate", "nat", "bat",]
result = group_anagrams(strs)
print(result)  