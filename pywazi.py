"""
Program for crawling web resources.
See Readme.md & doc.md for more details.

爬取网络资源的程序。
详情请看 Readme.md & doc.md。
"""

from ins.waziInsLog import waziLog
from ins.waziInsConfig import waziConfig
from sites.waziJavBus import waziJavBus as Wjb
from sites.waziPicAcg import waziPicAcg as Wpa
from sites.waziDanbooru import waziDanbooru as Wdb
from sites.waziExHentai import waziExHentai as Weh

waziJavBus = Wjb()
waziPicAcg = Wpa()
waziDanbooru = Wdb()
waziExHentai = Weh()

def globalParams(filePath):
    jsonData = waziConfig.readConfig(filePath)
    waziJavBus.giveParams(jsonData)
    waziPicAcg.giveParams(jsonData)
    waziDanbooru.giveParams(jsonData)
    waziExHentai.giveParams(jsonData)
    return jsonData

def readConfig(filePath):
    jsonData = waziConfig.readConfig(filePath)
    for i in jsonData:
        if i["name"] == "JavBus":
            if i["params"] is None:
                pass
            else:
                waziJavBus.giveParams(i["params"])
            if i["url"] is None:
                pass
            else:
                waziJavBus.setApiUrl(i["url"])
            if i["eaUrl"] is None:
                pass
            else:
                waziJavBus.setEAApiUrl(i["eaUrl"])
            if i["type"] is None:
                pass
            else:
                waziJavBus.changeType(i["type"])
        elif i["name"] == "PicAcg":
            if i["params"] is None:
                pass
            else:
                waziPicAcg.giveParams(i["params"])
            if i["login"] is None:
                pass
            else:
                waziPicAcg.login(i["login"]["username"], i["login"]["password"])
            if i["image"] is None:
                pass
            else:
                waziPicAcg.changeImageQuality(i["image"])
        elif i["name"] == "Danbooru":
            if i["params"] is None:
                pass
            else:
                waziDanbooru.giveParams(i["params"])
            if i["url"] is None:
                pass
            else:
                waziDanbooru.setApi(i["url"])
        elif i["name"] == "ExHentai":
            if i["params"] is None:
                pass
            else:
                waziExHentai.giveParams(i["params"])
            if i["cookies"] is None:
                pass
            else:
                waziExHentai.setCookies(i["cookies"])
            if i["parse"] is None:
                pass
            else:
                waziExHentai.setParse(i["parse"])
            if i["fullComment"] is None:
                pass
            else:
                waziExHentai.needFullComments(i["fullComment"])
            if i["thumbType"] is None:
                pass
            else:
                waziExHentai.changeThumbnailMode(i["thumbType"])
            if i["method"] is None:
                pass
            else:
                waziExHentai.changeMethod(i["method"])
            if i["jump"] is None:
                pass
            else:
                waziExHentai.setJump(i["jump"])
        elif i["name"] == "Config":
            if i["save"] is None:
                pass
            else:
                waziLog.needSave(i["save"])
            if i["level"] is None:
                pass
            else:
                waziLog.setMinDisplayLevel(i["level"])
        else:
            pass
    return True


try:
    returnInfo = readConfig("config.json")
except:
    pass

# [1]: 代码使用： https://github.com/WWILLV/iav （未注明详细的版权协议）
# [2]: Api 参考： https://github.com/AnkiKong/picacomic （MIT 版权）
#      Headers 引用： https://github.com/tonquer/picacg-windows （LGPL-3.0 版权）
#      相关信息参考： https://www.hiczp.com/wang-luo/mo-ni-bi-ka-android-ke-hu-duan.html （版权归 czp，未注明详细的版权协议）
#      我参考了一位开源者的代码，但是很可惜，我已经在 GitHub 找不到他的项目了（可能是代码进行改动了）
# 感谢我的朋友： cloudwindy 提供了 ExHentai 账号信息
