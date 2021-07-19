def perfect():
    t=0
    while t<=1000:
        sum=0
        temp=t
        while temp>0:
            i=1
            f=1
            reminder=temp%10
            while i<=reminder:
                f=f*i
                i=i+1
            sum=sum+f
            temp=temp//10
        if sum==t:
            print("it is perfect number",sum)
        t=t+1
perfect()                  