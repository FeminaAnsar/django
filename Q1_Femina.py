row=int(input("Enter number :"))
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    for j in range(2*(row-i)):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print("*",end=" ")
    print()
for i in range(row):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(2*(row-i-1)):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()