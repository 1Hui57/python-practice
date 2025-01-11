def add(n1,n2):
    return (n1+n2)

#計算兩個點的距離
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
#計算線段斜率

def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

distance(1,1,5,5)