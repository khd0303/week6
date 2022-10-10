#1

def sum_nums(*numbers):
    arr = []
    result = 0
    for n in numbers:
        result += n
        arr.append(n)
    return result
#print(sum_nums(1,2,3,4,5))
print('합계 :',sum_nums(10,20,30), '평균 :',sum_nums(10,20,30)/3)


print('합계 :',sum_nums(10,20,30,40,50), '평균 :',sum_nums(10,20,30,40,50)/5)

print()
#2

def min_nums(*num):
    arr = []

    for i in num:
        arr.append(i)


    return min(arr)


print('최솟값은 ',min_nums(20,40,30,10))