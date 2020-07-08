a = 0
sum = 0
sum2 = 0
while a<=100:
    if a % 2 == 0:
        sum = sum + a
    else:
        sum2 += a
    a = a + 1
print(sum)
print(sum2)