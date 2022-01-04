with open('pytest03.py', 'r', encoding='utf-8') as code:
    copy_code = code.read()


with open('pytest02.py', 'a+', encoding='utf-8') as f:
    f.seek(0)
    s = f.read()

    if s == '':
        f.write('import pytest\n')
        f.write('import requests\n')
        f.write('import allure\r\n')
    else:

        for i in range(5):
            func_name = "def test_+'i'+(datas):"
            copy_code.replace('def test_login(datas):', 'def test_+"i"+(datas):')
            f.write(copy_code)
    print('down')