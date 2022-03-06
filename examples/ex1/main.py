from pywazi import waziDanbooru

waziDanbooru.giveParams({
    "useProxies": True,	            # 是否使用代理
    "proxyAddress": "127.0.0.1",    # 代理地址
    "proxyPort": 7890               # 代理端口
})

waziDanbooru.setApi("https://konachan.com") # 设置你想爬的 Danbooru 类网站地址

for page in range(1, 6):
    # 爬五页
    waziDanbooru.downloadPosts(
        page = page,                   # 指定页码
        tags = "rating:explicit",      # 标签
        limit = 40,                    # 每页限制几张图片，最多就 40 张
        path = "./download"            # 下载目录
    )