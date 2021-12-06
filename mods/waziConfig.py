import json
from mods import waziFun
from ins.waziInsLog import waziLog

class waziConfig:
    # Read JSON Config
    # 读取 JSON 配置
    def __init__(self):
        super(waziConfig, self).__init__()
        self.name = self.__class__.__name__

    def readConfig(self, filePath):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到配置文件路径信息和保存信息，准备读取并返回内容。")
        waziLog.log("debug", f"({self.name}.{fuName}) 文件路径： {filePath}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在打开。")
        with open(filePath, "rb") as f:
            jsonData = json.load(f)
        waziLog.log("debug", f"({self.name}.{fuName}) 数据已取得： {jsonData}")
        waziLog.log("info", f"({self.name}.{fuName}) 数据已返回。")
        return jsonData
