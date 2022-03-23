
low=int(input("Enter lower limit:"))
up=int(input("Enter upper limit:"))
sum=0

prime=[i for i in range(low, up+1) if 0 not in [i%n for n in range(2, i)]]
sum=0
for num in prime:
    if num==1:
        prime.remove(num)
    else:
        sum=sum+num
print(prime)
print("Sum of prime numbers in the given range=",sum)
