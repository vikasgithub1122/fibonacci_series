num = int(input("How many terms you want 'fibonacci sequence': "))

n1, n2 = 0, 1 # first two number


if num< 0:
   print("Please enter a positive integer")

elif num == 1 & num==0:
   print("Fibonacci sequence upto",num,":")
   print(n1)
   
else:
   print("Fibonacci sequence:")
   while n2<num:
      print(n2)
      n1,n2 = n2,n1+n2
