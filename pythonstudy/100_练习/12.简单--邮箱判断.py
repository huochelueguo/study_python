# 写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com）， 程序识别用户名和公司名后，将用户名和公司名输出到控制台。
# 要求：
# 1. 校验输入内容是否符合规范（xx@polo.com）, 如是进入下一步，如否则抛出提 示"incorrect email format"。注意必须以.com 结尾
# 2. 可以循环“输入--输出判断结果”这整个过程
# 3. 按字母 Q（不区分大小写）退出循环，结束程序

while True:
    email = input('please enter a email')
    # print(email)
    if email == 'q' or email =='Q':
        print('stop input')
        break
    if not email.endswith('.com'):
        print('incorrect email format')
    if '@' in email:
        username = email.split('@')
        if len(username[0]) == 0 :
            print('incorrect email format')
        elif '.' in email:
            companyname = username[1].split('.')[0]
            if len(companyname) == 0:
                print('incorrect email format')
            else:
                print(username[0])
                print(companyname)
    else:
        print('incorrect email format')