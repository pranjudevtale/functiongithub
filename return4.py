def number():
    num=int(input("enter the number"))
    i=0
    while i<=num:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
number()