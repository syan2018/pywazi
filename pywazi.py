"""
Program for crawling web resources.
See Readme.md & doc.md for more details.

爬取网络资源的程序。
详情请看 Readme.md & doc.md。
"""

from ins.waziInsLog import waziLog
from ins.waziInsConfig import waziConfig
from sites.waziNyaa import waziNyaa as Wn
from sites.waziJavBus import waziJavBus as Wjb
from sites.waziPicAcg import waziPicAcg as Wpa
from sites.waziDanbooru import waziDanbooru as Wdb
from sites.waziExHentai import waziExHentai as Weh
from sites.waziAsianSister import waziAsianSister as Was

__VERSION__ = "1.4"
__AUTHOR__ = "Yazawazi"

waziNyaa = Wn()
waziJavBus = Wjb()
waziPicAcg = Wpa()
waziDanbooru = Wdb()
waziExHentai = Weh()
waziAsianSister = Was()

def globalParams(params):
    """
    pywazi.globalParams(params)
    *OCD*

    Set global parameters.

    Parameters:
        params: dict
            The parameters.
            {
                "useProxies": bool,                 # Whether to use proxies.
                "proxyAddress": str,                # The address of the proxy.
                "proxyPort": int or str,            # The port of the proxy.
                "useHeaders": bool,                 # (*) Whether to use headers.
                "headers": dict,                    # (*) The custom headers.
            }
            *: The parameters are not recommended. The program will auto set them. If you set them, may cause some problems.
    
    Return:
        Type: dict
        The parameters.

    Errors:
        None
    """
    waziJavBus.giveParams(params)
    waziPicAcg.giveParams(params)
    waziDanbooru.giveParams(params)
    waziExHentai.giveParams(params)
    waziAsianSister.giveParams(params)
    waziNyaa.giveParams(params)
    return params

def globalParamsByFile(filePath):
    """
    pywazi.globalParamsByFile(filePath)
    *OCD*

    Set global parameters.

    Parameters:
        filePath: str
            The path of the config file.
            Config file format:
            {
                "useProxies": bool,                 # Whether to use proxies.
                "proxyAddress": str,                # The address of the proxy.
                "proxyPort": int or str,            # The port of the proxy.
                "useHeaders": bool,                 # (*) Whether to use headers.
                "headers": dict,                    # (*) The custom headers.
            }
            *: The parameters are not recommended. The program will auto set them. If you set them, may cause some problems.
    
    Return:
        Type: dict
        The parameters.

    Errors:
        None
    """
    jsonData = waziConfig.readConfig(filePath)
    waziJavBus.giveParams(jsonData)
    waziPicAcg.giveParams(jsonData)
    waziDanbooru.giveParams(jsonData)
    waziExHentai.giveParams(jsonData)
    waziAsianSister.giveParams(jsonData)
    waziNyaa.giveParams(jsonData)
    return jsonData

def defConfig(filePath):
    """
    pywazi.defConfig(filePath)
    *Transvestism.*

    Use config file to define all modules.

    Parameters:
        filePath: str
            The path of the config file.

    Return:
        Type: bool
        The result.

    Errors:
        Python:
            Perhaps there are potential errors.
    """
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
        elif i["name"] == "Nyaa":
            if "params" in i:
                waziNyaa.giveParams(i["params"])
        elif i["name"] == "Config":
            if "save" in i:
                waziLog.needSave(i["save"])
            if "level" in i:
                waziLog.setMinDisplayLevel(i["level"])
        else:
            pass
    return True

"""
Try to import the config file: "./config.json".
"""
try:
    defConfig("./config.json")
except:
    pass

# [1]: 代码使用： https://github.com/WWILLV/iav （未注明详细的版权协议）
# [2]: Api 参考： https://github.com/AnkiKong/picacomic （MIT 版权）
#      Headers 引用： https://github.com/tonquer/picacg-windows （LGPL-3.0 版权）
#      相关信息参考： https://www.hiczp.com/wang-luo/mo-ni-bi-ka-android-ke-hu-duan.html （版权归 czp，未注明详细的版权协议）
#      在 PicAcg 部分，我参考了一位开源者的代码，但是很可惜，我已经在 GitHub 找不到他的项目了（可能是代码进行改动了）
# 感谢我的朋友： cloudwindy 提供了 ExHentai 账号信息
