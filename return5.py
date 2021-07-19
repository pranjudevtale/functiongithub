def list():
    num=int(input("enter the number"))
    i=0
    sum=0
    while i<=num:
        if i%3==0 or i%5==0:
            print(i)
            sum=sum+i
        i=i+1
    print(sum)
list()