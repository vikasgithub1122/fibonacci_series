num = int(input("How many terms you want 'fibonacci sequence': "))

n1, n2 = 0, 1 # first two number
count = 0

if num< 0:
   print("Please enter a positive integer")

elif num == 1 & num==0:
   print("Fibonacci sequence upto",num,":")
   print(n1)
   
else:
   print("Fibonacci sequence:")
   while count < num:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1