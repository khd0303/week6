def circle_get_circum(radius):
    area = radius**2*3.14

    circum = (2*radius)*3.14

    return area, circum





radius = 10

area, circum = circle_get_circum(radius)


print('반지름',int(radius),'인 원의 면적은',area,'원의 둘레는',circum)


#원의 둘레의 계산 결과값이 62.8이 나와야 하는데  62.800000000000004로 나오는 원인을 해결못하겟습니다