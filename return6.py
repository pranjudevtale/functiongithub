def function_speed(speed):
    if speed<=70:
        print("ok")
    elif 70<speed:
        s=speed-70
        point=s/5
        print(("point",point))
        if  point>12:
            print("licence suspended")
speed=int(input("enter the number "))
function_speed(speed)   