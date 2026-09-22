#methode 1

num = int(input ("Enter a number: "))
if (num % 2) == 0:
   print(f"{num} is Even")
else:
   print(f"{num} is Odd")


#methode 2
print(f"{num} is Even") if (num % 2) == 0 else print(f"{num} is Odd")