s = ["h","e","l","l","o"]

#write a function that reverses the string 


def reverse_string(s):
    r=len(s)-1
    l=0

    while l<r:
        s[l],s[r]=s[r],s[l]
        r-=1
        l+=1
    print(s)
    
reverse_string(s)