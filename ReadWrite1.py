a=int(input("Enter a number"))
b=int(input("Enter a number"))
sum = a + b
maths=open("maths.txt", "w")
maths.write(sum)
maths.close()