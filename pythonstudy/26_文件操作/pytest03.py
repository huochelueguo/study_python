data = []


@pytest.mark.parametrize('datas', data)  # 用一个参数接受数据，就是传入一个元组，元组里的数据运用索引的方法就可以提取出来；
def test_login(datas):
    print(datas)
    r = requests.post(url=datas['url1'], data=datas['body'])
    print(r.json())
    test = r.text
    assert 'success' in test


