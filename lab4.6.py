def print_root(a,b,c):
    r1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
    r2 = (-b-(b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는',r1,'또는',r2)

#1
#(1)
print_root(1,4,-21)



print()
#(2)
print_root(1,-6, 8)



#2
def print_area(width,height):
    result = height*width*0.5
    print('밑변',int(width),'높이',int(height),'인 삼각형의 면적은 :',int(result))

print()
print()
print_area(10,20)