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
    
    def returnSoup(self, link):
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
        pass

    def parseSearch(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        table = soup.find("tbody")
        if table is None:
            waziLog.log("warn", f"({self.name}.{fuName}) 无法获取到表格，返回空列表。")
            return []
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 获取到表格，开始解析。")
            rows = table.find_all("tr")
            waziLog.log("info", f"({self.name}.{fuName}) 表格解析完成，共 {len(rows)} 行。")

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
        return waziNyaa.parseSearch(self, waziNyaa.returnSoup(self, url))
        
    def searchRSS(self, params):
        pass
    
    def getViewFromId(self, site, id):
        pass