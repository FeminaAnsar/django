num=int(input("Enter number of rows:"))
for row in range (num):
    t=row+1
    m=num-1
    for col in range(row + 1):
        print(t, end=" ")
        t=t+m
        m=m-1

    print()

