import os
import json
import urllib.parse
import urllib.request
from mods import waziFun
from mods.waziURL import waziURL
from ins.waziInsLog import waziLog
from mods.waziRequest import waziRequest
from mods.waziFileName import waziFileName

class waziDanbooru:
    # Danbooru is a powerful image board system which uses tagging extensively.
    # like https://yande.re/ https://konachan.com/ (R-18 NSFW)
    # Danbooru 是一个非常牛逼的画廊展示系统（相册图库差不多吧），主要就是用标签系统多一点。
    # 像 https://yande.re/ https://konachan.com/ （R-18 不适合在公开场合或工作环境浏览）
    def __init__(self):
        super(waziDanbooru, self).__init__()
        self.request = waziRequest()
        self.URL = waziURL()
        self.fileName = waziFileName()
        self.api = ""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.164 Safari/537.36"
        }
        self.proxies = {
            "proxyAddress": "127.0.0.1",
            "proxyPort": "7890"
        }
        self.params = {}
        self.name = self.__class__.__name__

    def giveParams(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到配置信息，正在写入。")
        self.params = params
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.params}")
        return self.params

    def setApi(self, url):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Danbooru 类网站 API 地址，正在写入配置。")
        self.api = url
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前 API 地址为： {self.api}")
        return self.api

    def toAPIJson(self, port, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求接口和 GET 参数，正在准备使用 waziRequest 发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求接口： {port}， GET 参数： {params}")
        url = self.URL.getFullURL(urllib.parse.urljoin(self.api, port), params)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziRequest 获取完整的参数。")
        tempParams = self.request.handleParams(self.params, "get", url, self.headers, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 完整的参数获取完成： {tempParams}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试通过 waziRequest 请求 URL。")
        try:
            temp = self.request.do(tempParams)
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取 API 信息，返回空字典。")
            return {}
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 成功请求，正在转换为字典格式返回。")
            try:
                jsons = json.loads(temp.data.decode("utf-8"))
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 无法转换，疑似返回错误内容，程序返回空字典： "
                                     f"{temp.data.decode('utf-8')}")
                return {}
            else:
                waziLog.log("info", f"({self.name}.{fuName}) 转换完成，API 信息为： {jsons}")
                return jsons

    def getPosts(self, page, tags, limit):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，标签，每页限制量信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 标签： {tags}， 每页限制量： {limit}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "page": str(page),
            "tags": tags,
            "limit": str(limit)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, "/post.json", params)

    def downloadFile(self, url, orgName, path):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，文件名和路径，正在准备下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 文件名： {orgName}， 路径： {path}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取路径是否存在。")
        isExists = os.path.exists(path)
        waziLog.log("debug", f"({self.name}.{fuName}) 路径是否存在： {isExists}")
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到路径不存在，准备创建。")
            try:
                os.makedirs(path)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 创建失败。")
                return False
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 成功创建，继续执行。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在处理请求参数。")
        requestParams = self.request.handleParams(self.params, "get", url, self.headers, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 处理完毕，正在修正文件名。")
        fileName = os.path.join(path, self.fileName.toRight(orgName))
        waziLog.log("debug", f"({self.name}.{fuName}) 文件名修正完成： {fileName}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在请求： {url}")
        with open(fileName, "wb") as f:
            try:
                temp = self.request.do(requestParams)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 该文件无法下载！")
                return False
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在将数据写入。")
                f.write(temp.data)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据写入完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 文件： {fileName}， 完成。")
        return True

    def download(self, posts, path, key):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Posts 和路径信息，正在准备下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) Posts 信息： {posts}， 路径信息： {path}， 键名： {key}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查 Posts 是否为空。")
        if not posts:
            waziLog.log("error", f"({self.name}.{fuName}) 列表为空，返回空元组。")
            return [], []
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 列表不为空，继续执行。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取路径是否存在。")
        isExists = os.path.exists(path)
        waziLog.log("debug", f"({self.name}.{fuName}) 路径是否存在： {isExists}")
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到路径不存在，准备创建。")
            try:
                os.makedirs(path)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 创建失败，返回空元组结束任务。")
                return [], []
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 成功创建，继续执行。")
        downloadFiles = []
        cantDownload = []
        waziLog.log("debug", f"({self.name}.{fuName}) 开始遍历 API 信息列表。")
        for i in posts:
            if key in i:
                pass
            else:
                waziLog.log("error", f"({self.name}.{fuName}) 无法查询到字段 {key} 的信息。")
                return [], []
            waziLog.log("debug", f"({self.name}.{fuName}) 目前正在处理的信息： {i}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziRequest 请求： {i[key]}")
            requestParams = self.request.handleParams(self.params, "get", i[key], self.headers, self.proxies)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取下载文件路径。")
            fileName = os.path.join(path, self.fileName.toRight(str(i["id"]) + "." + i[key].split(".")[-1]))
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {fileName}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在请求： {i[key]}")
            with open(fileName, "wb") as f:
                try:
                    temp = self.request.do(requestParams)
                except:
                    waziLog.log("warn", f"({self.name}.{fuName}) 图像： {i[key]} 无法下载， ID 为： {i['id']}")
                    cantDownload.append({"fileURL": i[key], "id": i["id"]})
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 正在将数据写入。")
                    f.write(temp.data)
                    waziLog.log("debug", f"({self.name}.{fuName}) 数据写入完成。")
            waziLog.log("debug", f"({self.name}.{fuName}) 文件： {fileName}， 完成。")
            downloadFiles.append(fileName)
        waziLog.log("info", f"({self.name}.{fuName}) 完成下载，返回元组为： {(downloadFiles, cantDownload)}")
        return downloadFiles, cantDownload

    def downloadPosts(self, page, tags, limit, path, key = "file_url"):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，标签，每页限制量信息，路径信息，正在准备下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 标签： {tags}， 每页限制量： {limit}， "
                             f"下载路径： {path}， 键名： {key}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备递交 getPosts 获取 API 信息列表。")
        lists = waziDanbooru.getPosts(self, page, tags, limit)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，提交给 download 函数。")
        return waziDanbooru.download(self, lists, path, key)

    # 我将不再 Code 任何对于搜索时特殊标签的合成函数
    # 我觉得这个是用户的事情 请前往： https://yande.re/help/cheatsheet 获取更多介绍和帮助

    # 尺寸限制
    def getSizeLimit(self, size):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到尺寸信息，正在处理。")
        waziLog.log("debug", f"({self.name}.{fuName}) 尺寸内容： {size}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建空尺寸限制内容。")
        text = ""
        waziLog.log("debug", f"({self.name}.{fuName}) 创建完成，正在分析。")
        if "limit" in size:
            waziLog.log("debug", f"({self.name}.{fuName}) 创建完成，正在分析。")
            if size["limit"] == "b":
                waziLog.log("debug", f"({self.name}.{fuName}) 大于尺寸，正在分析。")
                if "width" in size:
                    waziLog.log("debug", f"({self.name}.{fuName}) 存在 width，正在写入。")
                    text += "width:" + str(size["width"]) + ".. "
                    waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
                if "height" in size:
                    waziLog.log("debug", f"({self.name}.{fuName}) 存在 height，正在写入。")
                    text += "height:" + str(size["height"]) + ".. "
                    waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
                waziLog.log("info", f"({self.name}.{fuName}) 全部写入成功，返回： {text}")
            elif size["limit"] == "e":
                waziLog.log("debug", f"({self.name}.{fuName}) 匹配尺寸，正在分析。")
                if "width" in size:
                    waziLog.log("debug", f"({self.name}.{fuName}) 存在 width，正在写入。")
                    text += "width:" + str(size["width"]) + " "
                    waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
                if "height" in size:
                    waziLog.log("debug", f"({self.name}.{fuName}) 存在 height，正在写入。")
                    text += "height:" + str(size["height"]) + " "
                    waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
                waziLog.log("info", f"({self.name}.{fuName}) 全部写入成功，返回： {text}")
            elif size["limit"] == "s":
                if "width" in size:
                    waziLog.log("debug", f"({self.name}.{fuName}) 存在 width，正在写入。")
                    text += "width:.." + str(size["width"]) + " "
                    waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
                if "height" in size:
                    waziLog.log("debug", f"({self.name}.{fuName}) 存在 height，正在写入。")
                    text += "height:.." + str(size["height"]) + " "
                    waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
                waziLog.log("info", f"({self.name}.{fuName}) 全部写入成功，返回： {text}")
            else:
                waziLog.log("warn", f"({self.name}.{fuName}) 找不到尺寸限制条件，返回空内容。")
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 不存在限制条件，返回空内容。")
        return text

    # 排序 order:score
    def getOrder(self, orderType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到排序信息，正在处理。")
        waziLog.log("debug", f"({self.name}.{fuName}) 排序内容： {orderType}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备遍历分析。")
        text = ""
        for i in orderType:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在分析： {i}")
            if i == "score":
                waziLog.log("debug", f"({self.name}.{fuName}) 按分数排序，正在写入。")
                text += "order:score "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
            elif i == "fav":
                waziLog.log("debug", f"({self.name}.{fuName}) 按收藏次数排序，正在写入。")
                text += "order:fav "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
            elif i == "wide":
                waziLog.log("debug", f"({self.name}.{fuName}) 大图排序，正在写入。")
                text += "order:wide "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
            elif i == "nonwide":
                waziLog.log("debug", f"({self.name}.{fuName}) 非大图排序，正在写入。")
                text += "order:nonwide "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 自定义排序模式： {i}")
                text += "order:" + i + " "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 返回： {text}")
        return text

    # 过滤
    def getRating(self, ratingType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到过滤信息，正在处理。")
        waziLog.log("debug", f"({self.name}.{fuName}) 过滤内容： {ratingType}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备遍历分析。")
        text = ""
        for i in ratingType:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在分析： {i}")
            if i == "safe":
                waziLog.log("debug", f"({self.name}.{fuName}) 安全模式，正在写入。")
                text += "rating:safe "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
            elif i == "questionable":
                waziLog.log("debug", f"({self.name}.{fuName}) 软色情模式，正在写入。")
                text += "rating:questionable "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
            elif i == "explicit":
                waziLog.log("debug", f"({self.name}.{fuName}) 色情模式，正在写入。")
                text += "rating:explicit "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
            elif i == "questionableplus":
                waziLog.log("debug", f"({self.name}.{fuName}) 软色情&直球黄色模式，正在写入。")
                text += "rating:questionableplus "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
            elif i == "questionableless":
                waziLog.log("debug", f"({self.name}.{fuName} 软色情&不搞黄色模式，正在写入。")
                text += "rating:questionableless "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 自定义过滤模式： {i}")
                text += "rating:" + i + " "
                waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 返回： {text}")
        return text

    # 标签
    def getTags(self, page, limit, order):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，每页限制量和排序方式信息，正在合成 URL 。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 每页限制量： {limit}， 排序方式： {order}")
        if order in ["date", "count", "name"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 排序符合规则。")
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 排序不符合规则，返回空列表。")
            return []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "page": str(page),
            "limit": str(limit),
            "order": order
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, "/tag.json", params)

    def getArtists(self, page, order):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和排序方式信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 排序方式： {order}")
        if order in ["date", "name"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 排序符合规则。")
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 排序不符合规则，返回空列表。")
            return []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "page": str(page),
            "order": order
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, "/artist.json", params)

    def getComments(self, imgId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图片 ID 信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图片 ID： {imgId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "id": str(imgId)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, "/comment/show.json", params)

    def getPools(self, query, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集名称和页码信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图集名称： {query}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "query": query,
            "page": str(page)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, "/pool.json", params)

    def getPoolsFromId(self, poolId, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集 ID 和页码信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图集 ID： {poolId}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "id": str(poolId),
            "page": str(page)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, "/pool/show.json", params)

    def downloadPools(self, poolId, page, path, key = "file_url"):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集 ID、页码和路径信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图集 ID： {poolId}， 页码： {page}， 路径： {path}， 键名： {key}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "id": str(poolId),
            "page": str(page)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        lists = waziDanbooru.toAPIJson(self, "/pool/show.json", params)
        if not lists:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取该页内容，返回空元组。")
            return [], []
        else:
            try:
                lists = lists["posts"]
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 无法获取该页详细信息，返回空元组。")
                return [], []
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，提交给 download 函数。")
        return waziDanbooru.download(self, lists, path, key)

    def downloadPoolsWithZip(self, poolId, needJPG, path):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集 ID、是否需要 JPG 格式信息和路径，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图集 ID： {poolId}， 是否需要 JPG 格式： {needJPG}， 路径： {path}")
        if needJPG:
            url = urllib.parse.urljoin(self.api, f"/pool/zip/{poolId}?jpeg=1")
        else:
            url = urllib.parse.urljoin(self.api, f"/pool/zip/{poolId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 合成完成： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 downloadFile 下载。")
        if waziDanbooru.downloadFile(self, url, f"{poolId}.zip", path):
            waziLog.log("info", f"({self.name}.{fuName}) 下载成功！")
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 无法下载，请检查该站点是否允许图集直接使用 ZIP 下载。")

    def customApi(self, port, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求接口和请求参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求接口： {port}， 请求参数： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, port, params)
