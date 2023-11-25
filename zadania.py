from sympy import isprime
def loaddata(file):
    data=open(file, "r")
    numbers=list(map(str.strip, data.readlines()))
    return numbers
def mirror(a):
    al=""
    a=str(a)
    for n in range(len(a)):
        i=abs(int(n)-len(a))-1
        al=al+a[i]
    al=int(al)
    return al

def zad1():
    numbers=loaddata("liczby.txt")
    mirrored_numbers=[]
    for i in numbers:
        mirrored_numbers.append(mirror(i))
    print(mirrored_numbers)
    p17=[]
    for i in mirrored_numbers:
        if i%17==0:
            p17.append(i)
    return p17
def zad2():
    numbers=loaddata("liczby.txt")
    mirrored_numbers=[]
    highest_value=0
    highest_index=0
    for i in numbers:
        mirrored_numbers.append(mirror(i))
    for i in range(len(numbers)):
        value=abs(int(numbers[i])-mirrored_numbers[i])
        if value>highest_value:
            highest_index=i
            highest_value=value
    print(numbers[highest_index], highest_value)
def zad3():
    numbers=loaddata("liczby.txt")
    numbers=[eval(item) for item in numbers]
    mirrored_numbers=[]
    prime=[]
    for i in numbers:
        mirrored_numbers.append(mirror(i))
    for i in range(len(numbers)):
        if isprime(numbers[i]) and isprime(mirrored_numbers[i]):
           prime.append(numbers[i])
    print(prime)
def zad4():
    numbers=loaddata("liczby.txt")
    lr=[]
    l2=0
    l3=0
    r=0
    for i in range(len(numbers)):
        for l in range(i+1, len(numbers)):
                if numbers[i]==numbers[l]:
                    lr.append(numbers[l])
    for i in set(lr):
        m=0
        for l in numbers:
            if i==l:
                m+=1
        if m==2:
            l2+=1
        if m==3:
            l3+=1
        r+=m-1
    print(len(numbers)-r, l2, l3)
zad4()