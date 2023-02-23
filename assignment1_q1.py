num = int(input("How many terms you want 'fibonacci sequence': "))
a,b=0,1

while b<num:
    print(b)
    a,b = b,a+b
