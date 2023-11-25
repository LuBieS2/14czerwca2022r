def convert_to_digits(a):
    a=str(a)
    al=[]
    for i in a:
        al.append(int(i))
    return al
def sumakwcyfr(a):
    a=convert_to_digits(a)
    s=0
    for i in a:
        s=s+i**2
    return s
def interesting_or_boring(a):
    s=a
    for i in range(243):
        print(s)
        s=sumakwcyfr(s)

        if s==1:
            print("boring")
            break
    if s!=1:
        print("interesting")
interesting_or_boring(999)