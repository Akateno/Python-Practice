s = ".,"


def valid_palindrome(s):
    new_text=""
    for i in s:
        if i.isalnum():
            new_text+=i
            new_text=new_text.lower()
            s=new_text
    print(s)

    l=0
    r=len(s)-1

    while l<r:
        if s[l] != s[r]:
            return print(False)
        else:
            l+=1
            r-=1
    return print(True)
    
    
    


valid_palindrome(s)