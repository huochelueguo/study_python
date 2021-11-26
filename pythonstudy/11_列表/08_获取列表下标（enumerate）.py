# enumerate 不仅可以作用于字典，同时也可以作用于列表/元组，获取列表每个元素的序号
# 同样：下标从0开始

l = [1, 2, 3, 4, 5]
for k, v in enumerate(l):
    print(k, v)
print('-' * 50)

t = (1, 2, 3, 4, 5)
for k, v in enumerate(t):
    print(k, v)
print('-' * 50)

d = {'1': 'a', '2':'b', '3':'c' }
for k,v in enumerate(d):
    print(k, v)