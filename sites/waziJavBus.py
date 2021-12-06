import re
import urllib.parse
import urllib.request
from mods import waziFun
from bs4 import BeautifulSoup
from mods.waziURL import waziURL
from ins.waziInsLog import waziLog
from mods.waziRequest import waziRequest

# 第一个非常棘手的事情 那就是这个网站有个 cf 的反 bot 机制
# 绕过 cf 反 bot 机制可以使用 urllib
# 第二个非常棘手的事情 那就是不知道为什么获得到的信息总比浏览器获取到的少
# 具体的副作用就是无法获得论坛热帖和女优列表获取失败（代理？）

class waziJavBus:
    # JavBus is a website that collects adult video's magnet url schemes. (Almost from Japan)
    # JavBus 是一个收集成人视频的种子网站。（大部分来自日本）
    # [1]
    def __init__(self):
        super(waziJavBus, self).__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.164 Safari/537.36",
            "Host": "www.javbus.com",
            "Connection": "close",
            "X-Requested-With": "XMLHttpRequest"
        }
        self.newHeaders = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.164 Safari/537.36",
            "existmag": "mag"
        }
        self.proxies = {
            "proxyAddress": "127.0.0.1",
            "proxyPort": "7890"
        }
        self.apiUrl = "https://www.javbus.com"
        self.eaApiUrl = "https://www.javbus.red"
        self.URL = waziURL()
        self.request = waziRequest()
        self.params = {}
        self.name = self.__class__.__name__

    def giveParams(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到配置信息，正在写入。")
        self.params = params
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.params}")
        return self.params

    def changeType(self, magType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到磁力链接显示模式，正在写入 Header。")
        waziLog.log("debug", f"({self.name}.{fuName}) 显示模式： {magType}")
        if int(magType) == 0:
            waziLog.log("debug", f"({self.name}.{fuName}) 仅显示有磁力的影片，写入 existmag = mag")
            self.newHeaders["existmag"] = "mag"
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 显示所有磁力影片，写入 existmag = all")
            self.newHeaders["existmag"] = "all"
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.newHeaders['existmag']}")
        return self.newHeaders["existmag"]

    def setApiUrl(self, url):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到镜像 URL，正在写入配置。")
        newUrl = url
        if newUrl.endswith("/"):
            waziLog.log("debug", f"({self.name}.{fuName}) 已自动删除末尾字符。")
            newUrl = newUrl[:-1]
        self.apiUrl = newUrl
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.apiUrl}")
        return self.apiUrl

    def setEAApiUrl(self, url):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到欧美镜像 URL，正在写入配置。")
        newUrl = url
        if newUrl.endswith("/"):
            waziLog.log("debug", f"({self.name}.{fuName}) 已自动删除末尾字符。")
            newUrl = newUrl[:-1]
        self.eaApiUrl = newUrl
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.eaApiUrl}")
        return self.eaApiUrl

    # What? urllib, fucking old stubborn, use requests please!
    # But hey, look at this:
    # https://stackoverflow.com/questions/62684468/pythons-requests-triggers-cloudflares-security-while-urllib-does-not
    # I do not want to modify my request model, so just urllib!
    def getPage(self, url, headers):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和请求头部，正在通过 urllib.request 获取。")
        newRequest = urllib.request
        waziLog.log("debug", f"({self.name}.{fuName}) 已新建 urllib.request。")
        if "useProxies" in self.params:
            if self.params["useProxies"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 需要使用代理。")
                if "proxyAddress" in self.params and "proxyPort" in self.params:
                    waziLog.log("debug", f"({self.name}.{fuName}) 用户存在代理地址，使用用户代理。")
                    proxy = newRequest.ProxyHandler({
                        "https": self.params["proxyAddress"] + ":" + str(self.params["proxyPort"])
                    })
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 用户不存在代理地址，使用默认设置。")
                    proxy = newRequest.ProxyHandler({
                        "https": self.proxies["proxyAddress"] + ":" + str(self.proxies["proxyPort"])
                    })
                waziLog.log("debug", f"({self.name}.{fuName}) 正在 build_opener。")
                opener = newRequest.build_opener(proxy, newRequest.HTTPHandler)
                waziLog.log("debug", f"({self.name}.{fuName}) build_opener 完成，正在 install_opener。")
                newRequest.install_opener(opener)
                waziLog.log("debug", f"({self.name}.{fuName}) install_opener 完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试 urlopen。")
        try:
            response = newRequest.urlopen(newRequest.Request(url = url, headers = headers))
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 无法请求，请检查网络代理，若网络代理正常，则等待更新。")
            return "Error. / 错误。"
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 数据已获取，返回。")
            return BeautifulSoup(response.read(), "lxml")

    def getItems(self, soup, itemsType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息和显示模式，正在分析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 显示模式： {itemsType}")
        itemsDict = []
        if soup == "Error. / 错误。":
            waziLog.log("error", f"({self.name}.{fuName}) 无法分析，因为 Soup 信息告知存在错误。")
            return itemsDict
        if itemsType == "normal":
            waziLog.log("debug", f"({self.name}.{fuName}) Normal 模式，直接获取所有 item。")
            items = soup.find_all(class_ = "item")
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成。")
        elif itemsType == "worker":
            waziLog.log("debug", f"({self.name}.{fuName}) Worker 模式，从 #waterfall > .#waterfall 中获取所有 item。")
            items = soup.find(id = "waterfall").find(id = "waterfall").find_all(class_ = "item")
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成。")
            workerInfo = soup.find(id = "waterfall").find(class_ = "item")
            waziLog.log("debug", f"({self.name}.{fuName}) 已获取工作者信息。")
            workerBasic = []
            waziLog.log("debug", f"({self.name}.{fuName}) 进入遍历获取。")
            for i in workerInfo.find_all("p"):
                workerType = i.text.split(": ")[0]
                workerContent = i.text.split(": ")[1]
                waziLog.log("debug", f"({self.name}.{fuName}) 数据已获取： {workerType} - {workerContent}")
                workerBasic.append({
                    "type": workerType,
                    "content": workerContent
                })
                waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
            workerDict = {
                "name": workerInfo.find(class_ = "pb10").text,
                "img": self.apiUrl + workerInfo.find("img").attrs["src"],
                "basic": workerBasic
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 工作者数据已完成添加： {workerDict}")
            itemsDict.append(workerDict)
            waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 其他模式，从 #waterfall > .#waterfall 中获取所有 item。")
            items = soup.find(id="waterfall").find(id="waterfall").find_all(class_="item")
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成。")
        if items is None:
            waziLog.log("error", f"({self.name}.{fuName}) 无法分析，因为列表为空。")
            return "Error. / 错误。"
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在进入遍历分析。")
            for item in items:
                tagList = []
                waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取项目。")
                try:
                    tags = item.find(class_ = "item-tag").find_all("button")
                except:
                    waziLog.log("error", f"({self.name}.{fuName}) 无法获取，请检查 URL 等。")
                    return "Error. / 错误。"
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 正在检查标签。")
                    if tags is None:
                        waziLog.log("debug", f"({self.name}.{fuName}) 标签不存在，跳过分析。")
                    else:
                        waziLog.log("debug", f"({self.name}.{fuName}) 标签存在，请等待遍历。")
                        for tag in tags:
                            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取标签。")
                            tagType = tag.text.replace(" ", "")
                            tagTitle = tag.attrs["title"].replace(" ", "")
                            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {tagType}, {tagTitle}")
                            tagList.append({
                                "type": tagType,
                                "title": tagTitle
                            })
                            waziLog.log("debug", f"({self.name}.{fuName}) 增加完毕。")
                others = {
                    "type": "Item Tag",
                    "has": ["tags"],
                    "tags": tagList
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 数据已写入。")
                waziLog.log("debug", f"({self.name}.{fuName}) 正在组合其它数据。")
                itemDict = {
                    "link": item.find(class_ = "movie-box").attrs["href"],
                    "frame": self.apiUrl + item.find("img").attrs["src"],
                    "title": item.find(class_ = "photo-info").span.text.split("\n")[0],
                    "avId": item.find_all("date")[0].text,
                    "time": item.find_all("date")[1].text,
                    "others": others
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 组合完毕： {itemDict}")
                itemsDict.append(itemDict)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
            waziLog.log("info", f"({self.name}.{fuName}) 数据返回： {itemsDict}")
            return itemsDict

    def getTags(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息，正在分析。")
        if soup == "Error. / 错误。":
            waziLog.log("error", f"({self.name}.{fuName}) 无法分析，因为 Soup 信息告知存在错误。")
            return []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取所有标签和标签类别。")
        titles = soup.find(class_ = "container-fluid pt10").find_all("h4")
        rowGenre = soup.find(class_ = "container-fluid pt10").find_all(class_ = "row genre-box")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在检查。")
        if titles is None or rowGenre is None:
            waziLog.log("error", f"({self.name}.{fuName}) 检查失败，有一方为空。")
            return "Error. / 错误。"
        tags = []
        waziLog.log("error", f"({self.name}.{fuName}) 准备进入以标签类别为计数的标签遍历。")
        for i in rowGenre:
            thisRowTags = {
                "tagType": "",
                "tags": []
            }
            for j in i.find_all("a"):
                waziLog.log("debug", f"({self.name}.{fuName}) 正在获取标签。")
                tagName = j.text
                tagId = j.attrs["href"].split("/")[-1]
                waziLog.log("debug", f"({self.name}.{fuName}) 已获取，标签名： {tagName}， 标签 ID： {tagId}")
                thisRowTags["tags"].append({
                    "name": tagName,
                    "tagId": tagId
                })
                waziLog.log("debug", f"({self.name}.{fuName}) 数据增加完毕。")
            tags.append(thisRowTags)
            waziLog.log("debug", f"({self.name}.{fuName}) 该标签类别下数据增加完毕。")
        count = 0
        waziLog.log("debug", f"({self.name}.{fuName}) 准备进入标签类别遍历。")
        for i in titles:
            waziLog.log("debug", f"({self.name}.{fuName}) 修改 {count} 的 tagType 为 {i.text}")
            tags[count]["tagType"] = i.text
            count += 1
        waziLog.log("info", f"({self.name}.{fuName}) 数据返回： {tags}")
        return tags

    def getWorkers(self, soup, avType, avTypeFromWebSite):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息和出演类型，是否需要从网站确定出演类型。")
        waziLog.log("debug", f"({self.name}.{fuName}) 出演类型（可能）： {avType}")
        waziLog.log("debug", f"({self.name}.{fuName}) 是否从网站确定出演类型： {avTypeFromWebSite}")
        if soup == "Error. / 错误。":
            waziLog.log("error", f"({self.name}.{fuName}) 无法分析，因为 Soup 信息告知存在错误。")
            return []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 items 元素。")
        items = soup.find(id = "waterfall").find_all(class_ = "item")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在检查。")
        if items is None:
            waziLog.log("error", f"({self.name}.{fuName}) 检查未通过，不存在 items 元素。")
            return "Error. / 错误。"
        workers = []
        waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
        for item in items:
            if avTypeFromWebSite:
                waziLog.log("debug", f"({self.name}.{fuName}) 需要从网站上自行确定工作者演出类型。")
                if item.find("button").text == "無碼":
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 1。")
                    avTypeInfo = 1
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码，设置为 0。")
                    avTypeInfo = 0
                waziLog.log("debug", f"({self.name}.{fuName}) 设置完成。")
                waziLog.log("debug", f"({self.name}.{fuName}) 正在组合剩下元素。")
                itemDict = {
                    "link": item.find("a").attrs["href"],
                    "frame": self.apiUrl + item.find("img").attrs["src"],
                    "name":  item.find("span", class_ = "mleft").text,
                    "workerId": item.find("a").attrs["href"].split("/")[-1],
                    "avType": avTypeInfo
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {itemDict}")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 用户自行给出工作者出演类型。")
                waziLog.log("debug", f"({self.name}.{fuName}) 出演类型： {avType}")
                waziLog.log("debug", f"({self.name}.{fuName}) 正在组合剩下元素。")
                itemDict = {
                    "link": item.find("a").attrs["href"],
                    "frame": self.apiUrl + item.find("img").attrs["src"],
                    "name": item.find("span").text,
                    "workerId": item.find("a").attrs["href"].split("/")[-1],
                    "avType": avType
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {itemDict}")
            waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
            workers.append(itemDict)
        waziLog.log("info", f"({self.name}.{fuName}) 数据返回： {workers}")
        return workers

    def getDetails(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息，正在分析。")
        if soup == "Error. / 错误。":
            waziLog.log("error", f"({self.name}.{fuName}) 无法分析，因为 Soup 信息告知存在错误。")
            return {}
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取识别码。")
        avId = soup.find("span", text = "識別碼:")
        if avId:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在识别码，正在获取。")
            avId = avId.parent.find_all("span")[1].text
            waziLog.log("debug", f"({self.name}.{fuName}) 识别码： {avId}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在识别码。")
            avId = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取发行日期。")
        time = soup.find("span", text = "發行日期:")
        if time:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在发行日期，正在获取。")
            time = time.parent.contents[1].split(" ")[1]
            waziLog.log("debug", f"({self.name}.{fuName}) 发行日期： {time}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存发行日期。")
            time = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取长度。")
        long = soup.find("span", text = "長度:")
        if long:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在长度，正在获取。")
            long = long.parent.contents[1].split(" ")[1].split("分鐘")[0]
            waziLog.log("debug", f"({self.name}.{fuName}) 长度： {long}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在长度。")
            long = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取导演。")
        director = soup.find("span", text = "導演:")
        if director:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在导演，正在获取。")
            if "uncensored" in director.parent.a.attrs["href"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 1。")
                directorType = 1
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码，设置为 0。")
                directorType = 0
            waziLog.log("debug", f"({self.name}.{fuName}) 设置完成，正在组合剩下元素。")
            director = {
                "name": director.parent.a.text,
                "id": director.parent.a.attrs["href"].split("/")[-1],
                "type": directorType
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {director}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在导演。")
            director = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取制作商。")
        studio = soup.find("span", text = "製作商:")
        if studio:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在制作商，正在获取。")
            if "uncensored" in studio.parent.a.attrs["href"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 1。")
                studioType = 1
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码，设置为 0。")
                studioType = 0
            waziLog.log("debug", f"({self.name}.{fuName}) 设置完成，正在组合剩下元素。")
            studio = {
                "name": studio.parent.a.text,
                "id": studio.parent.a.attrs["href"].split("/")[-1],
                "type": studioType
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {studio}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在制作商。")
            studio = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取发行商。")
        label = soup.find("span", text = "發行商:")
        if label:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在发行商，正在获取。")
            if "uncensored" in label.parent.a.attrs["href"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 1。")
                labelType = 1
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 0。")
                labelType = 0
            waziLog.log("debug", f"({self.name}.{fuName}) 设置完成，正在组合剩下元素。")
            label = {
                "name": label.parent.a.text,
                "id": label.parent.a.attrs["href"].split("/")[-1],
                "type": labelType
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {label}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在制作商。")
            label = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取系列。")
        series = soup.find("span", text = "系列:")
        if series:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在系列，正在获取。")
            if "uncensored" in series.parent.a.attrs["href"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 1。")
                seriesType = 1
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 0。")
                seriesType = 0
            waziLog.log("debug", f"({self.name}.{fuName}) 设置完成，正在组合剩下元素。")
            series = {
                "name": series.parent.a.text,
                "id": series.parent.a.attrs["href"].split("/")[-1],
                "type": seriesType
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {series}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在系列。")
            series = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取标签。")
        tags = soup.find_all("input", attrs = {"type": "checkbox", "name": "gr_sel"})
        if tags:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在标签，正在获取。")
            tagsList = []
            waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
            for i in tags:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在获取单个标签。")
                tag = i.find_next("a")
                waziLog.log("debug", f"({self.name}.{fuName}) 获取完成。")
                if "uncensored" in tag.attrs["href"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 1。")
                    tagType = 1
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 0。")
                    tagType = 0
                waziLog.log("debug", f"({self.name}.{fuName}) 设置完成，正在组合剩下元素。")
                tagDict = {
                    "name": tag.text,
                    "id": tag.attrs["href"].split("/")[-1],
                    "type": tagType
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {tagDict}")
                tagsList.append(tagDict)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据追加完成。")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在标签。")
            tagsList = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取工作者。")
        workers = soup.select('span[onmouseover^="hoverdiv"]')
        if workers:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在工作者，正在获取。")
            workersList = []
            waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
            for i in workers:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在获取单个工作者。")
                worker = i.a
                waziLog.log("debug", f"({self.name}.{fuName}) 获取完成。")
                if "uncensored" in worker.attrs["href"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 1。")
                    workerType = 1
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码，设置为 0。")
                    workerType = 0
                waziLog.log("debug", f"({self.name}.{fuName}) 设置完成，正在组合剩下元素。")
                workerDict = {
                    "name": worker.text,
                    "id": worker.attrs["href"].split("/")[-1],
                    "type": workerType
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {workerDict}")
                workersList.append(workerDict)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据追加完成。")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在工作者。")
            workersList = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取电影截图。")
        samples = soup.find(id = "sample-waterfall")
        if samples:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在电影截图，正在获取。")
            samplesList = []
            waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
            for i in samples.find_all("img"):
                waziLog.log("debug", f"({self.name}.{fuName}) 正在获取单个图集。")
                sampleDict = {
                    "title": i.attrs["title"],
                    "url": self.apiUrl + i.attrs["src"]
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {sampleDict}")
                samplesList.append(sampleDict)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据追加完成。")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在电影截图。")
            samplesList = "None. / 无。"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取同类影片。")
        try:
            sameVideos = soup.find_all("h4", text = "同類影片")[0].find_next("div", id = "related-waterfall")
        except:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在同类影片。")
            sameVideosList = "None. / 无。"
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 获取成功，正在检查。")
            if sameVideos.find_previous_sibling().text == "論壇熱帖":
                waziLog.log("debug", f"({self.name}.{fuName}) 检查失败，不存在同类影片。")
                sameVideosList = "None. / 无。"
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在同类影片，正在获取。")
                sameVideosList = []
                waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
                for sameVideo in sameVideos.find_all("a"):
                    waziLog.log("debug", f"({self.name}.{fuName}) 正在获取单个影片。")
                    sameVideoDict = {
                        "frame": sameVideo.attrs["href"],
                        "title": sameVideo.span.text,
                        "img": self.apiUrl + sameVideo.img.attrs["src"]
                    }
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {sameVideoDict}")
                    sameVideosList.append(sameVideoDict)
                    waziLog.log("debug", f"({self.name}.{fuName}) 数据追加完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取论坛热帖。")
        try:
            hots = soup.find_all("h4", text = "論壇熱帖")[0].find_next("div", id = "related-waterfall")
        except:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在论坛热帖。")
            hotsList = "None. / 无。"
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在论坛热帖，正在获取。")
            hotsList = []
            waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
            for hot in hots.find_all("a"):
                waziLog.log("debug", f"({self.name}.{fuName}) 正在获取单个论坛热帖。")
                hotDict = {
                    "url": hot.attrs["href"],
                    "title": hot.span.text,
                    "cover": hot.img.attrs["src"]
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {hotDict}")
                hotsList.append(hotDict)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据追加完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取封面。")
        cover = soup.find(class_ = "bigImage")
        if cover:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在封面，正在获取。")
            coverTitle = cover.img.attrs["title"]
            cover = self.apiUrl + cover.attrs["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 封面标题： {coverTitle}， 封面地址： {cover}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在封面。")
            cover = "None. / 无."
            coverTitle = "None. / 无."
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取标题。")
        title = soup.find("h3")
        if title:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在标题，正在获取。")
            title = soup.find("h3").text
            waziLog.log("debug", f"({self.name}.{fuName}) 标题： {title}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在标题。")
            title = "None. / 无."
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合所有元素。")
        detail = {
            "title": title,
            "cover": cover,
            "coverTitle": coverTitle,
            "avId": avId,
            "time": time,
            "long": long,
            "director": director,
            "studio": studio,
            "label": label,
            "series": series,
            "tags": tagsList,
            "workers": workersList,
            "samples": samplesList,
            "sameVideos": sameVideosList,
            "hots": hotsList
        }
        waziLog.log("info", f"({self.name}.{fuName}) 组合完成，数据： {detail}")
        return detail

    def browse(self, page, tag, avType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，标签和 AV 类型，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 标签： {tag}， AV 类型： {avType}")
        if int(avType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                if tag == "":
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到无标签。")
                    url = self.apiUrl + "/uncensored/" + str(page)
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到存在标签。")
                    url = self.apiUrl + "/uncensored/genre/" + tag + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                if tag == "":
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到无标签。")
                    url = self.apiUrl + "/uncensored/"
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到存在标签。")
                    url = self.apiUrl + "/uncensored/genre/" + tag
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                if tag == "":
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到无标签。")
                    url = self.apiUrl + "/" + str(page)
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到存在标签。")
                    url = self.apiUrl + "/genre/" + tag + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                if tag == "":
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到无标签。")
                    url = self.apiUrl + "/"
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 检测到存在标签。")
                    url = self.apiUrl + "/genre/" + tag
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "normal")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def eaBrowse(self, page, tag):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和标签，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        if int(page) > 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
            if tag == "":
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到无标签。")
                url = self.eaApiUrl + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到存在标签。")
                url = self.eaApiUrl + "/genre/" + tag + "/" + str(page)
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
            if tag == "":
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到无标签。")
                url = self.eaApiUrl + "/"
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到存在标签。")
                url = self.eaApiUrl + "/genre/" + tag
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "normal")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withWorkerBrowse(self, page, workerId, avType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，工作者 ID 和 AV 类型，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 工作者 ID： {workerId}， AV 类型： {avType}")
        if workerId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为工作者 ID 不存在。")
            return "Error. / 错误。"
        if int(avType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/uncensored/star/" + workerId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/uncensored/star/" + workerId
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/star/" + workerId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/star/" + workerId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "worker")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withEAWorkerBrowse(self, page, workerId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和工作者 ID，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 工作者 ID： {workerId}")
        if workerId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为工作者 ID 不存在。")
            return "Error. / 错误。"
        if int(page) > 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
            url = self.eaApiUrl + "/star/" + workerId + "/" + str(page)
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
            url = self.eaApiUrl + "/star/" + workerId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "worker")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withDirectorBrowse(self, page, directorId, avType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，导演 ID 和 AV 类型，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 导演 ID： {directorId}， AV 类型： {avType}")
        if directorId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为导演 ID 不存在。")
            return "Error. / 错误。"
        if int(avType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/uncensored/director/" + directorId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/uncensored/director/" + directorId
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/director/" + directorId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/director/" + directorId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "director")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withEADirectorBrowse(self, page, directorId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和导演 ID，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 导演 ID： {directorId}")
        if directorId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为导演 ID 不存在。")
            return "Error. / 错误。"
        if int(page) > 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
            url = self.eaApiUrl + "/director/" + directorId + "/" + str(page)
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
            url = self.eaApiUrl + "/director/" + directorId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "director")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withStudioBrowse(self, page, studioId, avType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，工作室 ID 和 AV 类型，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 导演 ID： {studioId}， AV 类型： {avType}")
        if studioId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为工作室 ID 不存在。")
            return "Error. / 错误。"
        if int(avType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/uncensored/studio/" + studioId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/uncensored/studio/" + studioId
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/studio/" + studioId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/studio/" + studioId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "normal")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withEAStudioBrowse(self, page, studioId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和工作室 ID，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 导演 ID： {studioId}")
        if studioId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为工作室 ID 不存在。")
            return "Error. / 错误。"
        if int(page) > 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
            url = self.eaApiUrl + "/studio/" + studioId + "/" + str(page)
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
            url = self.eaApiUrl + "/studio/" + studioId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "normal")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withLabelBrowse(self, page, labelId, avType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，发行商 ID 和 AV 类型，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 发行商 ID： {labelId}， AV 类型： {avType}")
        if labelId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为发行商 ID 不存在。")
            return "Error. / 错误。"
        if int(avType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/uncensored/label/" + labelId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/uncensored/label/" + labelId
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页")
                url = self.apiUrl + "/label/" + labelId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/label/" + labelId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "normal")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withEALabelBrowse(self, page, labelId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和发行商 ID，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 发行商 ID： {labelId}")
        if labelId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为发行商 ID 不存在。")
            return "Error. / 错误。"
        if int(page) > 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
            url = self.eaApiUrl + "/label/" + labelId + "/" + str(page)
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码。")
            url = self.eaApiUrl + "/label/" + labelId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "normal")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withSeriesBrowse(self, page, seriesId, avType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，系列 ID 和 AV 类型，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 系列 ID： {seriesId}， AV 类型： {avType}")
        if seriesId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为系列 ID 不存在。")
            return "Error. / 错误。"
        if int(avType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/uncensored/series/" + seriesId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/uncensored/series/" + seriesId
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/series/" + seriesId + "/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/series/" + seriesId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "normal")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def withEASeriesBrowse(self, page, seriesId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和系列 ID，正在获取。")
        waziLog.log("error", f"({self.name}.{fuName}) 页码： {page}， 系列 ID： {seriesId}")
        if seriesId == "":
            waziLog.log("error", f"({self.name}.{fuName}) 无法合成 URL，因为系列 ID 不存在。")
            return "Error. / 错误。"
        if int(page) > 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
            url = self.eaApiUrl + "/series/" + seriesId + "/" + str(page)
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
            url = self.eaApiUrl + "/series/" + seriesId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getItems 获取标签。")
        items = waziJavBus.getItems(self, pageSoup, "normal")
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def getTagsList(self, avType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 AV 类型，正在获取： {avType}")
        if int(avType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码。")
            url = self.apiUrl + "/uncensored/genre"
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码")
            url = self.apiUrl + "/genre"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getTags 获取标签。")
        items = waziJavBus.getTags(self, pageSoup)
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def getEATagsList(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取。")
        url = self.eaApiUrl + "/genre"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getTags 获取标签。")
        items = waziJavBus.getTags(self, pageSoup)
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def getAVWorkersList(self, page, avType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和 AV 类型，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， AV 类型： {avType}")
        if int(avType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/uncensored/actresses/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/uncensored/actresses"
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到有码。")
            if int(page) > 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
                url = self.apiUrl + "/actresses/" + str(page)
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
                url = self.apiUrl + "/actresses"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getWorkers 获取工作者列表。")
        items = waziJavBus.getWorkers(self, pageSoup, avType, False)
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def getEAAVWorkersList(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在获取： {page}")
        if int(page) > 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页。")
            url = self.eaApiUrl + "/actresses/" + str(page)
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到单页。")
            url = self.eaApiUrl + "/actresses"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getWorkers 获取工作者列表。")
        items = waziJavBus.getWorkers(self, pageSoup, 1, False)
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def getAVDetails(self, avId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到番号，正在获取： {avId}")
        url = self.apiUrl + "/" + avId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getDetails 获取详细信息。")
        items = waziJavBus.getDetails(self, pageSoup)
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def getEAAVDetails(self, avId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到番号，正在获取： {avId}")
        url = self.eaApiUrl + "/" + avId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交 URL 至 getPage 处理。")
        pageSoup = waziJavBus.getPage(self, url, self.newHeaders)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getDetails 获取详细信息。")
        items = waziJavBus.getDetails(self, pageSoup)
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {items}")
        return items

    def getAVDetailsWithMagnet(self, avId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到番号，正在获取： {avId}")
        url = self.apiUrl + "/" + avId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取详细信息。")
        details = waziJavBus.getDetails(self, waziJavBus.getPage(self, url, self.newHeaders))
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {details}，正在获取磁力链接信息。")
        magnets = waziJavBus.getMagnet(self, avId, False)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {magnets}，正在组合。")
        details.update(magnets = magnets)
        waziLog.log("info", f"({self.name}.{fuName}) 组合完成： {details}")
        return details

    def getEAAVDetailsWithMagnet(self, avId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到番号，正在获取： {avId}")
        url = self.eaApiUrl + "/" + avId
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取详细信息。")
        details = waziJavBus.getDetails(self, waziJavBus.getPage(self, url, self.newHeaders))
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {details}，正在获取磁力链接信息。")
        magnets = waziJavBus.getMagnet(self, avId, True)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {magnets}，正在组合。")
        details.update(magnets = magnets)
        waziLog.log("info", f"({self.name}.{fuName}) 组合完成： {details}")
        return details

    def search(self, searchType, keyWord, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到搜索类型，关键词和页码信息，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 搜索类型： {searchType}， 关键词： {keyWord}， 页码： {page}")
        if int(searchType) == 0:
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索有码影片，正在组合 URL。")
            url = self.apiUrl + "/search/" + keyWord + "/" + str(page) + "&type=1"
        elif int(searchType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索无码影片，正在组合 URL。")
            url = self.apiUrl + "/uncensored/search/" + keyWord + "/" + str(page) + "&type=1"
        elif int(searchType) == 2:
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索工作者，正在组合 URL。")
            url = self.apiUrl + "/searchstar/" + keyWord + "/" + str(page)
            waziLog.log("debug", f"({self.name}.{fuName}) URL 组合完成： {url}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在进入相关函数。")
            return waziJavBus.getWorkers(self, waziJavBus.getPage(self, url, self.newHeaders), 0, True)
        elif int(searchType) == 3:
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索导演，正在组合 URL。")
            url = self.apiUrl + "/search/" + keyWord + "/" + str(page) + "&type=2"
        elif int(searchType) == 4:
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索制作商，正在组合 URL。")
            url = self.apiUrl + "/search/" + keyWord + "/" + str(page) + "&type=3"
        elif int(searchType) == 5:
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索发行商，正在组合 URL。")
            url = self.apiUrl + "/search/" + keyWord + "/" + str(page) + "&type=4"
        elif int(searchType) == 6:
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索系列，正在组合 URL。")
            url = self.apiUrl + "/search/" + keyWord + "/" + str(page) + "&type=5"
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 不存在搜索信息，返回空列表。")
            return []
        waziLog.log("debug", f"({self.name}.{fuName}) URL 组合完成： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进入相关函数。")
        return waziJavBus.getItems(self, waziJavBus.getPage(self, url, self.newHeaders), "normal")

    def eaSearch(self, searchType, keyWord, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到搜索类型，关键词和页码信息，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) 搜索类型： {searchType}， 关键词： {keyWord}， 页码： {page}")
        if int(searchType) == 0:
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索影片，正在组合 URL。")
            url = self.eaApiUrl + "/search/" + keyWord + "/" + str(page)
            waziLog.log("debug", f"({self.name}.{fuName}) URL 组合完成： {url}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在进入相关函数。")
            return waziJavBus.getItems(self, waziJavBus.getPage(self, url, self.newHeaders), "normal")
        elif int(searchType) == 1:
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索工作者，正在组合 URL。")
            url = self.eaApiUrl + "/searchstar/" + keyWord + "/" + str(page)
            waziLog.log("debug", f"({self.name}.{fuName}) URL 组合完成： {url}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在进入相关函数。")
            return waziJavBus.getWorkers(self, waziJavBus.getPage(self, url, self.newHeaders), 1, False)
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 不存在搜索信息，返回空列表。")
            return []

    def getAjax(self, avId, isEa):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 AV 番号和欧美区信息，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) AV 番号： {avId}， 欧美区信息： {isEa}")
        if isEa:
            waziLog.log("debug", f"({self.name}.{fuName}) 属于欧美区，正在合成 URL。")
            url = self.eaApiUrl + "/" + avId
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不属于欧美区，正在合成 URL。")
            url = self.apiUrl + "/" + avId
        waziLog.log("debug", f"({self.name}.{fuName}) 合成完毕： {url}，正在修改请求头部。")
        tempHeaders = self.headers
        tempHeaders["Referer"] = url
        waziLog.log("debug", f"({self.name}.{fuName}) 修改请求头部完成： {tempHeaders}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改用户参数。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 修改用户参数完成： {tempParams}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备发起请求。")
        requestParams = self.request.handleParams(tempParams, "get", url, tempHeaders, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 发起请求完成，正在解析。")
        html = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml").prettify()
        waziLog.log("debug", f"({self.name}.{fuName}) 解析完成，正在获取 img 数据。")
        imgPattern = re.compile(r"var img = '.*?'")
        match = imgPattern.findall(html)
        img = match[0].replace("var img = '", "").replace("'", "")
        waziLog.log("debug", f"({self.name}.{fuName}) img 数据获取完成： {img}，正在获取 uc 数据。")
        ucPattern = re.compile(r"var uc = .*?;")
        match = ucPattern.findall(html)
        uc = match[0].replace("var uc = ", "").replace(";", "")
        waziLog.log("debug", f"({self.name}.{fuName}) uc 数据获取完成： {uc}，正在获取 gid 数据。")
        gidPattern = re.compile(r"var gid = .*?;")
        match = gidPattern.findall(html)
        gid = match[0].replace("var gid = ", "").replace(";", "")
        waziLog.log("debug", f"({self.name}.{fuName}) gid 数据获取完成： {gid}，正在组合数据。")
        params = {
            "gid": gid,
            "lang": "zh",
            "img": img,
            "uc": uc
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合数据完毕： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合 URL。")
        if isEa:
            url = self.URL.getFullURL(self.eaApiUrl + "/ajax/uncledatoolsbyajax.php", params)
        else:
            url = self.URL.getFullURL(self.apiUrl + "/ajax/uncledatoolsbyajax.php", params)
        waziLog.log("info", f"({self.name}.{fuName}) URL 组合完毕： {url}，数据返回。")
        return url

    def getMagnet(self, avId, isEa):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 AV 番号和欧美区信息，正在获取。")
        waziLog.log("debug", f"({self.name}.{fuName}) AV 番号： {avId}， 欧美区信息： {isEa}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getAjax 获取链接。")
        ajaxUrl = waziJavBus.getAjax(self, avId, isEa)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {ajaxUrl}，正在组合用户参数。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {tempParams}， 正在发起请求。")
        requestParams = self.request.handleParams(tempParams, "get", ajaxUrl, self.headers, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 发起请求完毕，正在解析。")
        soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
        waziLog.log("debug", f"({self.name}.{fuName}) 解析完成，正在检查相关内容。")
        if "暫時沒有磁力連結,請等待網友分享!" in str(soup):
            waziLog.log("debug", f"({self.name}.{fuName}) 该番号不存在磁力链接，返回空列表。")
            return []
        avLists = []
        waziLog.log("debug", f"({self.name}.{fuName}) 检查通过，正在进入遍历。")
        for tr in soup.find_all("tr"):
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取所有 a 标签。")
            others = tr.find_all("td")[0].find_all("a")
            others.pop(0)
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成。")
            if len(others) == 0:
                waziLog.log("debug", f"({self.name}.{fuName}) 无标签。")
                tags = []
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在标签，正在遍历搜索。")
                tags = []
                for i in others:
                    tag = {
                        "title": i.attrs["title"],
                        "type": i.txt
                    }
                    waziLog.log("debug", f"({self.name}.{fuName}) 已获取标签： {tag}")
                    tags.append(tag)
                    waziLog.log("debug", f"({self.name}.{fuName}) 标签数据已追加。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在组合剩余数据。")
            avDist = {
                "title": tr.find_all("td")[0].contents[1].text.strip(),
                "tags": tags,
                "size": tr.find_all("td")[1].text.strip(),
                "date": tr.find_all("td")[2].text.strip(),
                "magnet": tr.a.attrs["href"]
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {avDist}")
            avLists.append(avDist)
            waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 数据获取完毕： {avLists}， 数据返回。")
        return avLists
