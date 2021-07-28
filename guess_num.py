import random
x = random.randint(0, 100)
while True:
    y = input('請猜數字:')
    y = int(y)
    if y == x:
        print('終於猜對了！')
        break
    elif y > x:
        print('比答案大')
    else:
        print('比答案小')
