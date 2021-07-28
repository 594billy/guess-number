import random
a = input('請輸入最小值：')
b = input('請輸入最大值：')
a = int(a)
b = int(b)
x = random.randint(a, b)
count = 0
while True:
    y = input('請猜數字：')
    count = count + 1
    y = int(y)
    if y == x:
        print('終於猜對了！')
        print('你總共猜了', count, '次！')
        break
    elif y > x:
        print('比答案大')

    else:
        print('比答案小')
    print('你總共猜了', count, '次！')
