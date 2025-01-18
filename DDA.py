x1=int(input("Enter x coordinate of point A:"))
y1=int(input("Enter y coordinate of point A:"))
x2=int(input("Enter x coordinate of point B:"))
y2=int(input("Enter y coordinate of point B:"))

dx=x2-x1
dy=y2-y1

step=max(abs(dx),abs(dy))
if step==0:
    print(f"Points:({x1},{y1})")
else:
    xin=dx/step
    yin=dy/step
    x,y=x1,y1
    print(str(x1)+","+str(y1)+"\n")
    for _ in range(step):
        x+=xin
        y+=yin
    
        print(f"Points: ({round(x)}, {round(y)}) \n")
