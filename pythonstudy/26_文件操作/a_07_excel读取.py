# excel的读取写：Pandas方法
# 安装方法：
# 1、pip install pandas
# 2、pip install xlrd
# 参考：https://www.cnblogs.com/liulinghua90/p/9935642.html
# https://mp.weixin.qq.com/s?__biz=MzU5Mjg2OTQ1MA==&mid=2247484097&idx=1&sn=ad8fabbd84bf67655996026fc0ac5688&chksm=fe1863e4c96feaf200e9398bb7c824e99d3fc01ec965666497ce584466dc93f83dd5d127a46d&scene=21#wechat_redirect
# https://mp.weixin.qq.com/s?__biz=MzU5Mjg2OTQ1MA==&mid=2247484131&idx=1&sn=137286d36c707e10bbc761681a666654&chksm=fe1863c6c96fead0e7b2ab9af2db28f0c26df2b878eb66930e69f23bdc611b7f34cadb0b7d50&scene=21#wechat_redirect


# 读取excel
# 方法1：默认读取第一个表单；类似打开文件方法，将excel读取出来，得到的结果是一个二维矩阵
import pandas as pd

file_path = '/Users/sunwenxiao/Desktop/test.xlsx'
excel = pd.read_excel(file_path)
print(excel)
print('*' * 100)

# 方法二：通过指定表单名的方式来读取，读取代码中增加sheet_name参数
excel = pd.read_excel(file_path, sheet_name='test1')
print(f"可以通过指定sheet方法输出内容：\n{excel}")
print('*' * 100)

# 方法三：通过表单索引来指定要访问的表单，0表示第一个表单，即sheet_name值
# 也可以采用表单名和索引的双重方式来定位表单
# 也可以同时定位多个表单，方式都罗列如下所示
try:
    df = pd.read_excel(file_path, sheet_name=['test1', 'test2'])
    print(f"可以通过制定sheet_name数组索引或者值方式输出：\n{excel}")
except Exception as result:
    print(f'出现问题啦：{format(result)}')
finally:
    print('*' * 100)


