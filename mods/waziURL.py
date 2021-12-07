from mods import waziFun
from ins.waziInsLog import waziLog

class waziURL:
    # A class for URL encoding.
    # 一个进行 URL 编码的类。
    def __init__(self):
        super(waziURL, self).__init__()
        self.name = self.__class__.__name__

    def getFullURL(self, url, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和 Params 信息，准备合成。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， params： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查末尾字符串。")
        if url.endswith("?"):
            waziLog.log("debug", f"({self.name}.{fuName}) 末尾字符串为 ?，无需手动添加。")
            newURL = url + params
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 末尾字符串没有 ?，正在手动添加。")
            newURL = url + "?" + params
        waziLog.log("info", f"({self.name}.{fuName}) URL 合成成功： {newURL}")
        return newURL

    def getExHentaiAllURL(self, url, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和 Params 信息，准备递交 getFullURL 合成。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， params： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在更新 Params 信息。")
        allParams = {
            "f_cats": "0",
            "advsearch": "1",
            "f_sname": "on",
            "f_stags": "on",
            "f_sh": "on",
            "f_sdt2": "on",
            "f_sfl": "on",
            "f_sfu": "on",
            "f_sft": "on"
        }
        queryParams = params
        queryParams.update(allParams)
        waziLog.log("info", f"({self.name}.{fuName}) 请求参数更新完成，正在递交 getFullURL 合成： {queryParams}")
        return waziURL.getFullURL(self, url, queryParams)
