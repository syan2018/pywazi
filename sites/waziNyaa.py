from mods import waziFun
from ins.waziInsLog import waziLog

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
        self.name = self.__class__.__name__
    
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
        pass

    def searchRSS(self, params):
        pass
