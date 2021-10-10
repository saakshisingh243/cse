import math
def Pts_on_Circle(radius,num_pts):
    l=[]
    step=360//num_pts
    for i in range(0,360,step):
        l.append([radius*math.cos(math.radians(i)),radius*math.sin(math.radians(i))])
    return l
#        if (((radius*math.cos(i))**2)+((radius*math.sin(i))**2))==radius**2:
#            print("Yes")
#        else:
#            print()
radius=float(input("ENTER THE RADIUS OF THE CIRCLE:"))
num_pts=int(input("ENTER THE NUMBER OF EQUIDISTANT POINTS REQUIRED ON THE CIRCLE :"))
print("THE",num_pts,"EQUIDISTANT POINTS ON THE CIRCLE OF RADIUS",radius,"ARE:")
output=Pts_on_Circle(radius,num_pts)
for i in output:
#    print("(",i[0],",",i[1],")")
    print("(","{0:.4f}".format(i[0]),",","{0:.2f}".format(i[1]),")")
'''
import math
coor=[]
r=int(input("ENTER THE RADIUS:"))
def points(rad):
    Q=0
    for i in range(20):
        Q+=math.pi/10
        x=rad*round(math.cos(Q),2)
        y=rad*round(math.sin(Q),2)
        coor.append((x,y))
    return coor
coordinates=points(r)
print("Coordinates are:",coordinates)
'''
