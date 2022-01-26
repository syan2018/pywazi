from mods import waziFun
from bs4 import BeautifulSoup
from mods.waziURL import waziURL
from ins.waziInsLog import waziLog
from mods.waziRequest import waziRequest
from mods.waziFileName import waziFileName

class waziAsianSister:
    # AsianSister is a website that full of Asian Porn
    # AsianSister: https://asiansister.com/
    def __init__(self):
        super(waziAsianSister, self).__init__()
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

    def returnSoup(self, link):
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

    def getPage(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在生成 URL： {page}。")
        url = "https://asiansister.com/_page" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        return str(soup)
