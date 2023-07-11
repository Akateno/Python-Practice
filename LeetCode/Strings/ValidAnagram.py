s ,t= "cat", "car"

def valid_anagram(s,t):
    print(s,t)
    map={}
    map2={}
    for i in s:
        if i in map:
            map[i]+=1
        else:
            map[i]=1
    for i in t:
        if i in map2:
            map2[i]+=1
        else:
            map2[i]=1
    print(map,map2)

    return map ==map2
    
valid_anagram(s,t)
