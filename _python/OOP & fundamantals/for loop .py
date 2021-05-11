for i in range(0, 151):
    print(i)

for i in range(5, 1000):
    print(i*5)

for i in range(0, 100):
    if i % 5 == 0:
        print("coding")
    if i % 10 == 0:
        print("coding dojo")
sum = 0
for i in range(0, 500000):
    if i % 2 != 0:
        sum += i
print(sum)

for i in range(2018, 0, -4):
    if i > 0:
        print(i)
lownum = 2
highnum = 9
mult = 3
for i in range(lownum, highnum+1, 1):
    if i % mult == 0:
        print(i)
