
def ucln(a, b):
    if (b == 0):
        return a
    return ucln(b, a % b)
ucln(15,20)
    

