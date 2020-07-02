# readlines() #读取文本所有内容，并且以数列的格式返回结果，一般配合for in使用
# readline和readlines的区别：
# 1、readline()按行读取，readlines()一次性读取整个文件
# 2、.readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for … in … 结构进行处理
# 3、仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()。