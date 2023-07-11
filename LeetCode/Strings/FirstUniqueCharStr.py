s = "aabb"

def first_unique(s):
    
    map={}
    for n in s:
        if n in map:
            map[n]+=1
        else:
            map[n]=1
    print(map)

    for n in map:
        if map[n]==1:
            result=s.index(n)
            return result

    return -1
 # for n in range(0,len(s)):
    #     if n in map and 
    #         return print(n)

first_unique(s)