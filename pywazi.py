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
from sites.waziAsianSister import waziAsianSister as Was

__VERSION__ = "1.3"
__AUTHOR__ = "Yazawazi"

waziJavBus = Wjb()
waziPicAcg = Wpa()
waziDanbooru = Wdb()
waziExHentai = Weh()
waziAsianSister = Was()

def globalParams(filePath):
    jsonData = waziConfig.readConfig(filePath)
    waziJavBus.giveParams(jsonData)
    waziPicAcg.giveParams(jsonData)
    waziDanbooru.giveParams(jsonData)
    waziExHentai.giveParams(jsonData)
    waziAsianSister.giveParams(jsonData)
    return jsonData

def defConfig(filePath):
    jsonData = waziConfig.readConfig(filePath)
    for i in jsonData:
        if i["name"] == "JavBus":
            if "params" in i:
                waziJavBus.giveParams(i["params"])
            if "url" in i:
                waziJavBus.setApiUrl(i["url"])
            if "eaUrl" in i:
                waziJavBus.setEAApiUrl(i["eaUrl"])
            if "type" in i:
                waziJavBus.changeType(i["type"])
        elif i["name"] == "PicAcg":
            if "params" in i:
                waziPicAcg.giveParams(i["params"])
            if "login" in i:
                waziPicAcg.login(i["login"]["username"], i["login"]["password"])
            if "image" in i:
                waziPicAcg.changeImageQuality(i["image"])
        elif i["name"] == "Danbooru":
            if "params" in i:
                waziDanbooru.giveParams(i["params"])
            if "url" in i:
                waziDanbooru.setApi(i["url"])
        elif i["name"] == "ExHentai":
            if "params" in i:
                waziExHentai.giveParams(i["params"])
            if "cookies" in i:
                waziExHentai.setCookies(i["cookies"])
            if "parse" in i:
                waziExHentai.setParse(i["parse"])
            if "fullComment" in i:
                waziExHentai.needFullComments(i["fullComment"])
            if "thumbType" in i:
                waziExHentai.changeThumbnailMode(i["thumbType"])
            if "method" in i:
                waziExHentai.changeMethod(i["method"])
            if "jump" in i:
                waziExHentai.setJump(i["jump"])
        elif i["name"] == "AsianSister":
            if "params" in i:
                waziAsianSister.giveParams(i["params"])
        elif i["name"] == "Config":
            if "save" in i:
                waziLog.needSave(i["save"])
            if "level" in i:
                waziLog.setMinDisplayLevel(i["level"])
        else:
            pass
    return True


try:
    returnInfo = defConfig("./config.json")
except:
    pass

# [1]: 代码使用： https://github.com/WWILLV/iav （未注明详细的版权协议）
# [2]: Api 参考： https://github.com/AnkiKong/picacomic （MIT 版权）
#      Headers 引用： https://github.com/tonquer/picacg-windows （LGPL-3.0 版权）
#      相关信息参考： https://www.hiczp.com/wang-luo/mo-ni-bi-ka-android-ke-hu-duan.html （版权归 czp，未注明详细的版权协议）
#      我参考了一位开源者的代码，但是很可惜，我已经在 GitHub 找不到他的项目了（可能是代码进行改动了）
# 感谢我的朋友： cloudwindy 提供了 ExHentai 账号信息
