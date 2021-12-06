from mods import waziFun
from ins.waziInsLog import waziLog

class waziFileName:
    def __init__(self):
        super(waziFileName, self).__init__()
        self.name = self.__class__.__name__

    def toRight(self, name):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到文件名，正在删除不合法字符串：\\ / : ? \" < > |")
        waziLog.log("debug", f"({self.name}.{fuName}) 文件名为： {name}")
        finalName = name.replace("\\", "").replace("/", "").replace(":", "").replace("?", "").replace("\"", "")\
                        .replace("<", "").replace(">", "").replace("|", "")
        waziLog.log("info", f"({self.name}.{fuName}) 修正后文件名： {finalName}")
        return finalName
