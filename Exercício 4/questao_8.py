def palindroma(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and palindroma(string[1:-1])
    
print(palindroma("radar"))