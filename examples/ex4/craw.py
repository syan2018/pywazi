import os
import time
from pywazi import *

# 日志拜拜
waziLog.needSave(False)
waziLog.setMinDisplayLevel(-1)

# 代理配置
waziDanbooru.giveParams({
    "useProxies": True,
    "proxyAddress": "127.0.0.1",
    "proxyPort": 7890
})

# API 配置
waziDanbooru.setApi("https://yande.re")

# 创建文件夹
os.makedirs("./train", exist_ok = True)
os.makedirs("./train/notsafe", exist_ok = True)
os.makedirs("./train/safe", exist_ok = True)
os.makedirs("./test", exist_ok = True)
os.makedirs("./test/notsafe", exist_ok = True)
os.makedirs("./test/safe", exist_ok = True)

for page in range(1, 151):
    print("训练，限制：", page)
    waziDanbooru.downloadPosts(page, "rating:explicit", 40, "./train/notsafe", "sample_url")
    time.sleep(1)

for page in range(151, 161):
    print("测试，限制：", page)
    waziDanbooru.downloadPosts(page, "rating:explicit", 40, "./test/notsafe", "sample_url")
    time.sleep(1)

for page in range(1, 151):
    print("训练，安全：", page)
    waziDanbooru.downloadPosts(page, "rating:safe", 40, "./train/safe", "sample_url")
    time.sleep(1)

for page in range(151, 161):
    print("测试，安全：", page)
    waziDanbooru.downloadPosts(page, "rating:safe", 40, "./test/safe", "sample_url")
    time.sleep(1)

