# 1 BASIC
for i in range(151):
    print(i)

# 2 MULTIPLES OF FIVE
for i in range(1001):
    if i % 5 == 0:
        print(i)

# 3 COUNTING THE DOJO WAY
for i in range(101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4 WOAH THAT SUCKER'S HUGE
sum = 0
for i in range(500000):
    sum += i
print(sum)

# 5 COUNTDOWN BY 4S
num = 2018
while num > 0:
    print(num)
    num -= 4

# 6 FLEXIBLE COUNTER
lowNum = 1
highNum = 10
mult = 2
for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)