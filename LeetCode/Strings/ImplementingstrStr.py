haystack,needle="sadbutsad", "sad"

def implement_str(haystack,needle):
    print(needle,haystack)
    if needle in haystack:
        result=haystack.index(needle)
        print(result)


implement_str(haystack,needle)