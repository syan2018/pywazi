from mods import waziFun
from bs4 import BeautifulSoup
from mods.waziURL import waziURL
from ins.waziInsLog import waziLog
from mods.waziCheck import waziCheck

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
        pass

    def search(self, params):
        searchParams = {
            "f": "0",
            "c": "0_0",
            "q": ""
        }
        if "page" in params:
            searchParams["p"] = str(params["page"])
        if "keyword" in params:
            searchParams["q"] = params["keyword"]
        if "category" in params:
            searchParams["c"] = self.check.nyaaSearch["catgroies"][params["category"]]
        if "filter" in params:
            searchParams["f"] = self.check.nyaaSearch["filters"][params["filter"]]
        if "order" in params:
            searchParams.update(self.check.nyaaSearch["orders"][params["order"]])
        url = self.URL.getFullURL(self.urls[params["site"]], searchParams)
        return waziNyaa.parseSearch(self, waziNyaa.returnSoup(self, url))
        
    def searchRSS(self, params):
        pass
