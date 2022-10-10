'''
#1
def mean_of_n(nums):
    result = sum(nums)/len(nums)
    print('평균값은',result)
def max_of_n(nums):
    result = max(nums)
    print('최댓값은',result)
def min_of_n(nums):
    result = min(nums)
    print('최솟값은',result)
nums = []
print('정수값을 여러개 입력하시오(0입력시 반복 종료) : ')
while True:
    num = int(input())
    nums.append(num)

    if num == 0:
        break

mean_of_n(nums)
max_of_n(nums)
min_of_n(nums)
'''
'''
#2
def area(x1,y1,x2,y2):
    width = x2 - x1
    height = y2 - y1

    print('직각삼각형의 면적은 :',(width*height)*0.5)
x1 = int(input('x1좌표를 입력하시오 :'))
y1 = int(input('y1좌표를 입력하시오 :'))
x2 = int(input('x2좌표를 입력하시오 :'))
y2 = int(input('y2좌표를 입력하시오 :'))

area(x1,y1,x2,y2)
'''
'''
#3
numbers = []
a,b,c,d,e,f,g = map(int,input('쉼표로 구분된 정수를 7개 입력하시오 ').split(','))

numbers.append(a)
numbers.append(b)
numbers.append(c)
numbers.append(d)
numbers.append(e)
numbers.append(f)
numbers.append(g)

print('입력된 정수의 리스트: ',numbers)

numbers.sort()

print('정렬된 정수의 리스트:', numbers)
'''

#6
'''
def max2(m,n):
    result = max(m,n)
    print('{}과 {}중 큰 수는 : {}'.format(m,n,result))
def min2(m,n):
    result = min(m,n)
    print('{}과 {}중 작은 수는 : {}'.format(m,n,result))

m,n = map(int,input('m과 n을 각각 입력하시오(쉼표로 구분)').split(','))
max2(m,n)
min2(m,n)
'''

'''
#7

def mile2km(m):
    km = m * 1.61
    print('{}마일 = {} 킬로미터'.format(m,km))

for i in range(1,6):
    mile2km(i)
'''


def distance(x1,y1,x2,y2):
    dist = ((x2-x1)**2+(y2-y1)**2)**0.5
    print('두점의 거리 : ',dist)


x1 = int(input('x1좌표를 입력하시오 :'))
y1 = int(input('y1좌표를 입력하시오 :'))
x2 = int(input('x2좌표를 입력하시오 :'))
y2 = int(input('y2좌표를 입력하시오 :'))

distance(x1,y1,x2,y2)