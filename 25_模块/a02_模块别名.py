# 当导入模块的名称过长是，可以使用给模块建一个别名，避免代码中模块名称够长
# 模块导入的别名也应该符合大驼峰命名法
import a_被导入模块01 as Im


hanshu = Im.hanshu()
print(f'{hanshu}')
print(Im.title)
lei = Im.lei()
print(lei)