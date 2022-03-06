import site
from pywazi import waziNyaa

waziNyaa.giveParams({
    "useProxies": True,	            # 是否使用代理
    "proxyAddress": "127.0.0.1",    # 代理地址
    "proxyPort": 7890               # 代理端口
})

print(waziNyaa.search({
    "page": 1,                                      # 指定页码
    "keyword": "Sono Bisque Doll wa Koi o Suru",    # 搜索关键词
    "site": 0                                       # 搜索站点
}))
