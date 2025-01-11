import time

hour=int(input("\nEnter hour:"))
m=int(input("Enter min:"))
s=int(input("Enter sec:"))
print("*"*10+"Countdown"+"*"*10)
while s > 0 or m > 0 or hour > 0:
    print(f"{hour}:{m}:{s}")
    time.sleep(1)
    if s==0:
        if m==0:
            hour-=1
            m=60
        m-=1
        s=59
    elif hour<0:
        break
    else:
        s-=1
print("*"*10+" Times up! "+"*"*10)