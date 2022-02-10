from mods import waziFun
from bs4 import BeautifulSoup
from mods.waziURL import waziURL
from ins.waziInsLog import waziLog
from mods.waziCheck import waziCheck
from mods.waziRequest import waziRequest

class waziNyaa:
    # TODO: Support sukebei.nyaa.si and nyaa.si
    def __init__(self):
        super(waziNyaa, self).__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.164 Safari/537.36"
        }
        self.proxies = {
            "proxyAddress": "127.0.0.1",
            "proxyPort": "7890"
        }
        self.params = {}
        self.urls = ["https://nyaa.si/", "https://sukebei.nyaa.si/"]
        self.URL = waziURL()
        self.check = waziCheck()
        self.request = waziRequest()
        self.name = self.__class__.__name__
    
    def returnSoup(self, link, xml):
        # TODO: Put this function in waziRequest
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得 Soup： {link}")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        waziLog.log("debug", f"({self.name}.{fuName}) 需要检查 URL 并进行处理。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起网络请求。")
        requestParams = self.request.handleParams(tempParams, "get", link, tempHeaders, self.proxies)
        try:
            if xml:
                soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "xml")
            else:
                soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取，返回无效 Soup。")
            return BeautifulSoup("<html></html>", "lxml")
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 获取成功，Soup 返回中。")
            return soup
    
    def giveParams(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到配置信息，正在写入。")
        self.params = params
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.params}")
        return self.params

    def parsePage(self, soup):
        pass

    def parseRSS(self, rss):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 RSS 数据，正在解析。")
        items = rss.find_all("item")
        if items is None:
            waziLog.log("warn", f"({self.name}.{fuName}) 无法解析 RSS 中的 item 内容，返回空列表。")
            return []
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 获取列表成功，正在分析。")
            result = []
            for item in items:
                itemInfo = {}
                waziLog.log("debug", f"({self.name}.{fuName}) 正在解析种子类型。")
                if item.find("nyaa:trusted").text == "Yes":
                    itemInfo["type"] = self.check.nyaaTranslations["success"]
                elif item.find("nyaa:remake").text == "Yes":
                    itemInfo["type"] = self.check.nyaaTranslations["danger"]
                else:
                    itemInfo["type"] = self.check.nyaaTranslations["default"]
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子分类。")
                itemInfo["category"] = item.find("nyaa:category").text
                itemInfo["categoryId"] = item.find("nyaa:categoryId").text
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子评论数量。")
                itemInfo["comments"] = int(item.find("nyaa:comments").text)
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子标题。")
                itemInfo["title"] = item.find("title").text
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子链接。")
                itemInfo["link"] = item.find("guid").text
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子 ID。")
                itemInfo["id"] = int(item.find("guid").text.split("/")[-1])
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件下载地址。")
                itemInfo["torrent"] = item.find("link").text
                itemInfo["magnet"] = "magnet:?xt=urn:btih:" + item.find("nyaa:infoHash").text
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件大小。")
                itemInfo["size"] = item.find("nyaa:size").text
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件时间。")
                itemInfo["time"] = item.find("pubDate").text
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件做种人数。")
                itemInfo["seeders"] = int(item.find("nyaa:seeders").text)
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件吸血鬼数量。")
                itemInfo["leechers"] = int(item.find("nyaa:leechers").text)
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件完全下载数量。")
                itemInfo["completes"] = int(item.find("nyaa:downloads").text)
                waziLog.log("debug", f"({self.name}.{fuName}) 单个解析完成： {itemInfo}")
                result.append(itemInfo)
                waziLog.log("debug", f"({self.name}.{fuName}) 已追加。")
            return result

    def parseSearch(self, soup, site):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        table = soup.find("tbody")
        if table is None:
            waziLog.log("warn", f"({self.name}.{fuName}) 无法获取到表格，返回空列表。")
            return []
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 获取到表格，开始解析。")
            rows = table.find_all("tr")
            waziLog.log("info", f"({self.name}.{fuName}) 获取 tr 完成，共 {len(rows)} 行。")
            waziLog.log("debug", f"({self.name}.{fuName}) 开始解析 tr。")
            result = []
            for row in rows:
                rowInfo = {}
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子类型。")
                try:
                    rowInfo["type"] = self.check.nyaaTranslations[row.attrs["class"][0]]
                except:
                    waziLog.log("warn", f"({self.name}.{fuName}) 解析种子类型失败，写入 class。")
                    rowInfo["type"] = row.attrs["class"][0]
                    rowInfo["typeExtra"] = "class"
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子分类。")
                rowInfo["category"] = row.find("td").find("a").attrs["title"]
                rowInfo["categoryId"] = row.find("td").find("a").find("img").attrs["src"].split("/")[-1].split(".")[0]
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子评论数量。")
                comment = row.find("a", class_ = "comments")
                if comment:
                    rowInfo["comments"] = int(comment.text)
                else:
                    rowInfo["comments"] = 0
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子标题。")
                href = row.find_all("td")[1].find_all("a")[-1]
                rowInfo["title"] = href.attrs["title"]
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子链接。")
                rowInfo["link"] = self.urls[site] + "view/" + href.attrs["href"].split("/")[-1]
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子 ID。")
                rowInfo["id"] = int(href.attrs["href"].split("/")[-1])
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件下载地址。")
                rowInfo["torrent"] = self.urls[site] + "download/" + row.find_all("td")[2].find("a").attrs["href"].split("/")[-1]
                rowInfo["magnet"] = row.find_all("td")[2].find_all("a")[-1].attrs["href"]
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件大小。")
                rowInfo["size"] = row.find_all("td")[3].text
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件时间。")
                rowInfo["time"] = row.find_all("td")[4].text
                rowInfo["timeStamp"] = row.find_all("td")[4].attrs["data-timestamp"]
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件做种人数。")
                rowInfo["seeders"] = int(row.find_all("td")[5].text)
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件吸血鬼数量。")
                rowInfo["leechers"] = int(row.find_all("td")[6].text)
                waziLog.log("debug", f"({self.name}.{fuName}) 解析种子文件完全下载人数。")
                rowInfo["completes"] = int(row.find_all("td")[7].text)
                waziLog.log("debug", f"({self.name}.{fuName}) 单个解析完成： {rowInfo}")
                result.append(rowInfo)
                waziLog.log("debug", f"({self.name}.{fuName}) 已追加。")
            return result

    def search(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到搜索请求，正在获取 Soup。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户搜索请求： {params}")
        searchParams = {
            "f": "0",
            "c": "0_0",
            "q": ""
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查搜索参数。")
        if "page" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到页码参数，正在设置页码。")
            searchParams["p"] = str(params["page"])
        if "keyword" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到搜索内容参数，正在设置搜索内容。")
            searchParams["q"] = params["keyword"]
        if "category" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到分类参数，正在设置分类。")
            searchParams["c"] = self.check.nyaaSearch["catgroies"][params["category"]]
        if "filter" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到过滤参数，正在设置过滤。")
            searchParams["f"] = self.check.nyaaSearch["filters"][params["filter"]]
        if "order" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到排序参数，正在设置排序。")
            searchParams.update(self.check.nyaaSearch["orders"][params["order"]])
        waziLog.log("debug", f"({self.name}.{fuName}) 正在合成 URL。")
        url = self.URL.getFullURL(self.urls[int(params["site"])], searchParams)
        waziLog.log("debug", f"({self.name}.{fuName}) 合成完成，正在解析： {url}")
        return waziNyaa.parseSearch(self, waziNyaa.returnSoup(self, url, False), int(params["site"]))
        
    def searchRSS(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到搜索请求，正在获取 XML 结果。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户搜索请求： {params}")
        searchParams = {
            "page": "rss",
            "f": "0",
            "c": "0_0",
            "q": ""
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查搜索参数。")
        if "page" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到页码参数，正在设置页码。")
            searchParams["p"] = str(params["page"])
        if "keyword" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到搜索内容参数，正在设置搜索内容。")
            searchParams["q"] = params["keyword"]
        if "category" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到分类参数，正在设置分类。")
            searchParams["c"] = self.check.nyaaSearch["catgroies"][params["category"]]
        if "filter" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到过滤参数，正在设置过滤。")
            searchParams["f"] = self.check.nyaaSearch["filters"][params["filter"]]
        if "order" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到排序参数，正在设置排序。")
            searchParams.update(self.check.nyaaSearch["orders"][params["order"]])
        waziLog.log("debug", f"({self.name}.{fuName}) 正在合成 URL。")
        url = self.URL.getFullURL(self.urls[int(params["site"])], searchParams)
        waziLog.log("debug", f"({self.name}.{fuName}) 合成完成，正在解析： {url}")
        return waziNyaa.parseRSS(self, waziNyaa.returnSoup(self, url, True))
    
    def getViewFromId(self, id, site):
        pass