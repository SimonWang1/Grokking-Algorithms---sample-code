# 使用散列表做缓存伪代码
cache = {}


def get_page(url):
    # 返回缓存数据
    if cache.get(url):
        return cache(url)
    else:
        data = get_data_from_server(url)
        # 将数据保存在缓存中
        cache[url] = data
        return data


def get_data_from_server(url):
    cache[url] = '123.456.778.90'
    data = 'some data'
    return data
