import os
import re
import json
from unittest import mock
import urllib.parse
import urllib.request
from mods import waziFun
from bs4 import BeautifulSoup
from mods.waziURL import waziURL
from ins.waziInsLog import waziLog
from mods.waziCheck import waziCheck
from mods.waziRequest import waziRequest
from mods.waziFileName import waziFileName

# 流程太臃肿了，不过我就是不改，嘻嘻。

class waziExHentai:
    # ExHentai is the world's largest erotic homoerotic manga site.
    # ExHentai 是全世界最大的色情同人志漫画网站。
    def __init__(self):
        super(waziExHentai, self).__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.164 Safari/537.36",
            "Cookie": "",
            "Connection": "keep-alive"
        }
        self.proxies = {
            "proxyAddress": "127.0.0.1",
            "proxyPort": "7890"
        }
        self.request = waziRequest()
        self.check = waziCheck()
        self.URL = waziURL()
        self.fileName = waziFileName()
        self.urls = {
            "main": "https://exhentai.org/",
            "galleryTorrent": "https://exhentai.org/gallerytorrents.php?gid=",
            "api": "https://exhentai.org/api.php",
            "mpv": "https://exhentai.org/mpv/"
        }
        self.params = {}
        self.needParse = True
        self.jumpWarn = False
        self.fullComments = True
        self.name = self.__class__.__name__

    def giveParams(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到配置信息，正在写入。")
        self.params = params
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.params}")
        return self.params

    def setParse(self, boolean):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到解析器参数，正在写入。")
        self.needParse = boolean
        if not self.needParse:
            waziExHentai.changeMethod(self, "Extended")
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.needParse}")
        return self.needParse

    def setCookies(self, cookies):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Cookies 账号信息，正在写入。")
        self.headers["Cookie"] = cookies
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前账号使用的 Cookies 为： {self.headers['Cookie']}")
        return self.headers["Cookie"]

    def needFullComments(self, boolean):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在写入。")
        self.fullComments = boolean
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.fullComments}")
        return self.fullComments

    def changeThumbnailMode(self, method):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到缩略图显示模式，准备对比并发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 显示模式： {method}")
        if method == "normal":
            waziLog.log("debug", f"({self.name}.{fuName}) 正常模式，设置为 ts_m")
            url = "https://exhentai.org/?inline_set=ts_m"
        elif method == "large":
            waziLog.log("debug", f"({self.name}.{fuName}) 大尺寸模式，设置为 ts_l")
            url = "https://exhentai.org/?inline_set=ts_l"
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 无任何匹配模式，不进行任何设置。")
            return method
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改请求参数。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数修改完毕，正在提交给 handleParams 处理。")
        requestParams = self.request.handleParams(tempParams, "get", url, self.headers, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) handleParams 处理完毕，正在发起请求。")
        self.request.do(requestParams)
        waziLog.log("info", f"({self.name}.{fuName}) 请求发起完毕，缩略图显示模式 {method} 已返回。")
        return method

    def changeMethod(self, method):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到显示模式，准备比对并发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 显示模式： {method}")
        if method == "Minimal":
            waziLog.log("debug", f"({self.name}.{fuName}) Minimal 模式，设置为 dm_m")
            url = "https://exhentai.org/?inline_set=dm_m"
        elif method == "Minimal+":
            waziLog.log("debug", f"({self.name}.{fuName}) Minimal+ 模式，设置为 dm_p")
            url = "https://exhentai.org/?inline_set=dm_p"
        elif method == "Compact":
            waziLog.log("debug", f"({self.name}.{fuName}) Compact 模式，设置为 dm_l")
            url = "https://exhentai.org/?inline_set=dm_l"
        elif method == "Extended":
            waziLog.log("debug", f"({self.name}.{fuName}) Extended 模式，设置为 dm_e")
            url = "https://exhentai.org/?inline_set=dm_e"
        elif method == "Thumbnail":
            waziLog.log("debug", f"({self.name}.{fuName}) Thumbnail 模式，设置为 dm_t")
            url = "https://exhentai.org/?inline_set=dm_t"
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 无任何匹配模式，不进行任何设置。")
            return method
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改请求参数。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数修改完毕，正在提交给 handleParams 处理。")
        requestParams = self.request.handleParams(tempParams, "get", url, self.headers, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) handleParams 处理完毕，正在发起请求。")
        self.request.do(requestParams)
        waziLog.log("info", f"({self.name}.{fuName}) 请求发起完毕，模式 {method} 已返回。")
        return method

    def setJump(self, jumpNeed):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到画廊警告是否跳过参数，正在写入。")
        self.jumpWarn = jumpNeed
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.jumpWarn}")
        return self.jumpWarn

    def getDisplayMode(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到首页 Soup 信息，正在分析。")
        try:
            options = soup.find_all(id = "dms")[0].find("select").find_all("option")
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取首页显示模式，返回空内容。")
            return ""
        else:
            for i in options:
                if "selected" in i.attrs:
                    waziLog.log("info", f"({self.name}.{fuName}) 成功获取首页显示模式： {i.get_text()}")
                    return i.get_text()

    def getMainInfo(self, soup, parserType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到首页 Soup 信息和解析器显示模式，正在分配至对应函数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 解析器显示模式： {parserType}")
        if parserType == "Extended":
            waziLog.log("info", f"({self.name}.{fuName}) Extended 解析器开始工作。")
            return waziExHentai.getExtendedMain(self, soup)
        elif parserType == "Minimal":
            waziLog.log("info", f"({self.name}.{fuName}) Minimal 解析器开始工作。")
            return waziExHentai.getMinimalMain(self, soup)
        elif parserType == "Minimal+":
            waziLog.log("info", f"({self.name}.{fuName}) Minimal+ 解析器开始工作。")
            return waziExHentai.getMinimalPlusMain(self, soup)
        elif parserType == "Compact":
            waziLog.log("info", f"({self.name}.{fuName}) Compact 解析器开始工作。")
            return waziExHentai.getCompactMain(self, soup)
        elif parserType == "Thumbnail":
            waziLog.log("info", f"({self.name}.{fuName}) Thumbnail 解析器开始工作。")
            return waziExHentai.getThumbnailMain(self, soup)
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 无法找到对应解析器，默认返回为空列表。")
            return []

    # These parsers are fragile, and as soon as an update or a slight change in the style of the site is made,
    # these conditions may render them inoperable.
    #
    # I recommend that you use Extended display mode because it is the most comprehensive (relatively) way to get
    # information and I have the most confidence in this mode.
    #
    # 这些解析器都很脆弱，只要一更新或者网站的样式稍微修改，
    # 这些情况都有可能使他们无法运行。
    #
    # 我建议你使用 Extended 显示模式，因为该模式下获取的信息最全面（相对），并且这个模式我最有把握。

    # 任何异常优先考虑 ExHentai 改版；额外情况；代码错误

    def getRatingNum(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到首页或搜索结果 Soup，正在获取评分。")
        ratingNum = self.check.returnRatingNum(
            soup.find(class_ = "ir").attrs["style"].split("background-position:")[1].split(";")[0]
        )
        waziLog.log("info", f"({self.name}.{fuName}) 获取完毕，评分为： {ratingNum}")
        return ratingNum

    def getMinimalJSON(self, soup, parseType):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息和 Minimal 解析器模式，正在解析。")
        waziLog.log("debug", f"({self.name}.{fuName}) Minimal 解析器模式： {parseType}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取评分。")
        ratingNum = waziExHentai.getRatingNum(self, soup)
        waziLog.log("debug", f"({self.name}.{fuName}) 评分为： {ratingNum}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取封面。")
        cover = soup.find(class_ = "glthumb").find("img").attrs["src"]
        waziLog.log("debug", f"({self.name}.{fuName}) 原始封面地址为： {cover}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查封面地址合法性。")
        if "data:image" in cover:
            waziLog.log("debug", f"({self.name}.{fuName}) 封面地址为 base64，不符合，重新搜索： " + cover)
            cover = soup.find(class_ = "glthumb").find("img").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索完成： {cover}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 地址合法： {cover}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查解析器模式来确定标题搜索模式。")
        if parseType == "plus":
            waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 Plus 模式查找标题。")
            title = soup.find(class_ = "gl3m glname").find(class_ = "glink").get_text()
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在通过普通模式查找标题。")
            title = soup.find(class_ = "gl3m glname").get_text()
        waziLog.log("debug", f"({self.name}.{fuName}) 标题为： {title}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合剩余内容。")
        tempBooks = {
            "title": title,
            "URL": soup.find(class_ = "gl3m glname").find("a").attrs["href"],
            "cat": soup.find(class_ = "gl1m glcat").get_text(),
            "cover": cover,
            "uploader": soup.find(class_ = "gl5m glhide").get_text(),
            "uploaderURL": soup.find(class_ = "gl5m glhide").find("a").attrs["href"],
            "time": soup.find(class_ = "gl2m").find_all("div")[-1].get_text(),
            "hasTorrents": self.check.returnHasTorrents(soup.find(class_ = "gl6m").find("img")),
            "rating": ratingNum,
            "pages": soup.find_all("div")[2].find_all("div")[-1].get_text().split(" ")[0]
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完毕，内容： {tempBooks}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查解析器模式来确定是否存在附加内容。")
        if parseType == "plus":
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到 Plus 模式，正在检测附加内容。")
            if soup.find(class_ = "gltm") is None:
                waziLog.log("debug", f"({self.name}.{fuName}) 不存在附加内容，设置为空。")
                markedTags = []
                waziLog.log("debug", f"({self.name}.{fuName}) 设置完成。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在附加内容，正在获取。")
                waziLog.log("debug", f"({self.name}.{fuName}) 正在创建附加内容列表。")
                markedTags = []
                waziLog.log("debug", f"({self.name}.{fuName}) 创建完成，准备遍历 gltm 获取。")
                for c in soup.find(class_ = "gltm").find_all("div"):
                    title = c.attrs["title"]
                    className = c.attrs["class"]
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取到 title： {title}")
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取到 className： {className}")
                    tagDict = {
                        "title": title,
                        "className": className
                    }
                    if "style" in c.attrs:
                        style = c.attrs["style"]
                        tagDict["style"] = style
                        waziLog.log("debug", f"({self.name}.{fuName}) 获取到 style： {c.attrs['style']}")
                    markedTags.append(tagDict)
            waziLog.log("debug", f"({self.name}.{fuName}) 附加内容列表写入完成，正在添加到字典。")
            tempBooks["others"] = {
                "type": "Minimal+ Own Information",
                "has": ["markedTags"],
                "markedTags": markedTags
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成，添加内容为： {tempBooks['others']}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) Normal 模式跳过附加内容解析。")
        waziLog.log("info", f"({self.name}.{fuName}) 解析完成： {tempBooks}")
        return tempBooks

    def itgGltmDel(self, soup, className):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到首页 Soup 信息和 class 名，正在获取 tr 所有内容。")
        bigBody = soup.find_all(class_ = className)[0].find_all("tr")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取成功，正在删除头内容。")
        bigBody.pop(0)
        waziLog.log("info", f"({self.name}.{fuName}) 删除头内容成功，数据已返回。")
        return bigBody

    def getMinimalMain(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到首页 Soup 信息，正在以普通模式进行分析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建内容列表。")
        booksList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 空内容列表创建完毕。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziExHentai.itgGltmDel 获取 tr 内容。")
        bigBody = waziExHentai.itgGltmDel(self, soup, "itg gltm")
        for i in bigBody:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getMinimalJSON 的 normal 模式分析信息。")
            booksList.append(waziExHentai.getMinimalJSON(self, i, "normal"))
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，已成功追加到内容列表。")
        waziLog.log("info", f"({self.name}.{fuName}) 内容列表： {booksList}")
        return booksList

    def getMinimalPlusMain(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到首页 Soup 信息，正在以扩展模式进行分析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建内容列表。")
        booksList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 空内容列表创建完毕。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 tr 所有信息。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziExHentai.itgGltmDel 获取 tr 内容。")
        bigBody = waziExHentai.itgGltmDel(self, soup, "itg gltm")
        for i in bigBody:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getMinimalJSON 的 plus 模式分析信息。")
            booksList.append(waziExHentai.getMinimalJSON(self, i, "plus"))
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，已成功追加到内容列表。")
        waziLog.log("info", f"({self.name}.{fuName}) 内容列表： {booksList}")
        return booksList

    def getCompactMain(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息，正在解析。")
        booksList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziExHentai.itgGltmDel 获取 tr 内容。")
        body = waziExHentai.itgGltmDel(self, soup, "itg gltc")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取成功，正在遍历 tr 内容。")
        for i in body:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取评分。")
            ratingNum = waziExHentai.getRatingNum(self, i)
            waziLog.log("debug", f"({self.name}.{fuName}) 评分为： {ratingNum}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取封面。")
            cover = soup.find(class_="glthumb").find("img").attrs["src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 原始封面地址为： {cover}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查封面地址合法性。")
            if "data:image" in cover:
                waziLog.log("debug", f"({self.name}.{fuName}) 封面地址为 base64，不符合，重新搜索： " + cover)
                cover = soup.find(class_="glthumb").find("img").attrs["data-src"]
                waziLog.log("debug", f"({self.name}.{fuName}) 搜索完成： {cover}")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 地址合法： {cover}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取画廊地址。")
            href = i.find_all("a")[1].attrs["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查画廊地址合法性。")
            if "https://exhentai.org/uploader/" in href:
                waziLog.log("debug", f"({self.name}.{fuName}) 该地址为上传者地址，不符合，重新搜索： " + href)
                href = i.find_all("a")[0].attrs["href"]
                waziLog.log("debug", f"({self.name}.{fuName}) 搜索完成： {href}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取标签。")
            tagsDiv = i.find_all(class_ = "gt")
            if tagsDiv is None:
                waziLog.log("debug", f"({self.name}.{fuName}) 无标签，跳过。")
                tags = []
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在标签，正在遍历添加。")
                tags = []
                for c in tagsDiv:
                    title = c.attrs["title"]
                    className = c.attrs["class"]
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取到 title： {title}")
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取到 className： {className}")
                    tagDict = {
                        "title": title,
                        "className": className
                    }
                    if "style" in c.attrs:
                        style = c.attrs["style"]
                        tagDict["style"] = style
                        waziLog.log("debug", f"({self.name}.{fuName}) 获取到 style： {c.attrs['style']}")
                    tags.append(tagDict)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在组合剩余内容。")
            tempBooks = {
                "title": i.find(class_ = "glink").get_text(),
                "URL": href,
                "cat": i.find(class_ = "cn").get_text(),
                "cover": cover,
                "uploader": i.find_all("a", attrs = {"href": re.compile("uploader")})[0].get_text(),
                "uploaderURL": i.find_all("a", attrs = {"href": re.compile("uploader")})[0].attrs["href"],
                "time": i.find_all("div", attrs = {"onclick": re.compile("popUp")})[0].get_text(),
                "hasTorrents": self.check.returnHasTorrents(i.find_all(class_ = "gldown")[0].find("img")),
                "rating": ratingNum,
                "pages": int(i.find_all(class_ = "gl4c glhide")[0].find_all("div")[1].get_text().split(" ")[0]),
                "others": {
                    "type": "Compact Own Information",
                    "has": ["tags"],
                    "tags": tags
                }
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完毕，内容： {tempBooks}")
            booksList.append(tempBooks)
            waziLog.log("debug", f"({self.name}.{fuName}) 组合内容列表已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 内容列表： {booksList}")
        return booksList

    def getThumbnailMain(self, soup):
        fuName = waziFun.getFuncName()
        booksList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息，正在解析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在取出所有 gl1t 数据。")
        body = soup.find(class_ = "itg gld").find_all(class_ = "gl1t")
        waziLog.log("debug", f"({self.name}.{fuName}) 取出完毕，正在进入遍历。")
        for i in body:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取评分。")
            ratingNum = waziExHentai.getRatingNum(self, i)
            waziLog.log("debug", f"({self.name}.{fuName}) 评分为： {ratingNum}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取标签。")
            if i.find(class_ = "gl6t") is None:
                waziLog.log("debug", f"({self.name}.{fuName}) 无标签，跳过。")
                markedTags = []
            else:
                markedTags = []
                waziLog.log("debug", f"({self.name}.{fuName}) 存在标签，正在遍历添加。")
                gtList = i.find(class_ = "gl6t").find_all(class_ = "gt")
                for gt in gtList:
                    title = gt.attrs["title"]
                    className = gt.attrs["class"]
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取到 title： {title}")
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取到 className： {className}")
                    tagDict = {
                        "title": title,
                        "className": className
                    }
                    if "style" in gt.attrs:
                        style = gt.attrs["style"]
                        tagDict["style"] = style
                        waziLog.log("debug", f"({self.name}.{fuName}) 获取到 style： {gt.attrs['style']}")
                    markedTags.append(tagDict)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在组合剩余内容。")
            tempBooks = {
                "title": i.find(class_ = "gl4t glname glink").get_text(),
                "URL": i.find_all("a")[0].attrs["href"],
                "cat": i.find(class_ = "cs").get_text(),
                "cover": i.find("img").attrs["src"],
                "uploader": "Uploader information is not available in thumbnail mode. / 缩略模式下无法获取上传者信息。",
                "uploaderURL": "Uploader information is not available in thumbnail mode. / 缩略模式下无法获取上传者信息。",
                "time": i.find_all("div", attrs = {"onclick": re.compile("popUp")})[0].get_text(),
                "rating": ratingNum,
                "pages": int(i.find(class_ = "gl5t").find_all("div")[5].get_text().split(" ")[0]),
                "others": {
                    "type": "Thumbnail Own Information",
                    "has": ["markedTags"],
                    "markedTags": markedTags
                }
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完毕，内容： {tempBooks}")
            booksList.append(tempBooks)
            waziLog.log("debug", f"({self.name}.{fuName}) 组合内容列表已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 内容列表： {booksList}")
        return booksList

    def getExtendedMain(self, soup):
        fuName = waziFun.getFuncName()
        booksList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息，正在解析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在取出所有 gl2e 和 gl1e 数据。")
        urls = soup.find_all(class_ = "itg glte")[0].find_all(class_ = "gl2e")
        covers = soup.find_all(class_ = "itg glte")[0].find_all(class_ = "gl1e")
        waziLog.log("debug", f"({self.name}.{fuName}) 取出完毕，正在进入遍历。")
        coverTimes = -1
        for tempUrl in urls:
            coverTimes += 1
            waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取标签。")
            try:
                divs = tempUrl.find_all("table")[0].find_all("div")
            except:
                waziLog.log("debug", f"({self.name}.{fuName}) 无标签，跳过。")
                tags = []
            else:
                tags = []
                waziLog.log("debug", f"({self.name}.{fuName}) 存在标签，正在遍历添加。")
                for i in divs:
                    title = i.attrs["title"]
                    className = i.attrs["class"]
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取到 title： {title}")
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取到 className： {className}")
                    tagDict = {
                        "title": title,
                        "className": className
                    }
                    if "style" in i.attrs:
                        style = i.attrs["style"]
                        tagDict["style"] = style
                        waziLog.log("debug", f"({self.name}.{fuName}) 获取到 style： {i.attrs['style']}")
                    tags.append(tagDict)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取评分。")
            ratingNum = waziExHentai.getRatingNum(self, tempUrl)
            waziLog.log("debug", f"({self.name}.{fuName}) 评分为： {ratingNum}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在组合剩余内容。")
            tempBooks = {
                "title": tempUrl.find_all(class_ = "glink")[0].get_text(),
                "URL": tempUrl.find_all("a", attrs = {"href": re.compile("/g/")})[0].attrs["href"],
                "cat": tempUrl.find_all(class_ = "cn")[0].get_text(),
                "cover": covers[coverTimes].find_all("img")[0].attrs["src"],
                "uploader": tempUrl.find_all("a", attrs = {"href": re.compile("uploader")})[0].get_text(),
                "uploaderURL": tempUrl.find_all("a", attrs = {"href": re.compile("uploader")})[0].attrs["href"],
                "time": tempUrl.find_all("div", attrs = {"onclick": re.compile("popUp")})[0].get_text(),
                "hasTorrents": self.check.returnHasTorrents(tempUrl.find_all(class_ = "gldown")[0].find("img")),
                "rating": ratingNum,
                "pages": int(tempUrl.find_all(class_ = "gl3e")[0].find_all("div")[4].get_text().split(" ")[0]),
                "others": {
                    "type": "Extended Own Information",
                    "has": ["tags"],
                    "tags": tags
                }
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完毕，内容： {tempBooks}")
            booksList.append(tempBooks)
            waziLog.log("debug", f"({self.name}.{fuName}) 组合内容列表已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 内容列表： {booksList}")
        return booksList

    def getBooks(self, url):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，正在通过 returnSoup 获取： {url}")
        soup = waziExHentai.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 已返回，正在检查解析器参数。")
        if self.needParse:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要解析器，正在通过 getDisplayMode 获取显示模式。")
            parserType = waziExHentai.getDisplayMode(self, soup)
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，显示模式为： {parserType}，递交给 getMainInfo。")
            return waziExHentai.getMainInfo(self, soup, parserType)
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不需要解析器，以 Extended 递交给 getMainInfo。")
            return waziExHentai.getMainInfo(self, soup, "Extended")

    def browse(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码参数，正在合成请求参数： {page}")
        params = {
            "page": str(page)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 参数合成完毕，正在提交给 getFullURL 合成完整 URL。")
        url = self.URL.getFullURL(self.urls["main"], params)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return waziExHentai.getBooks(self, url)

    def allBrowse(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码参数，正在合成请求参数： {page}")
        params = {
            "f_spf": "",
            "f_spt": "",
            "page": str(page)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 参数合成完毕，正在提交给 getExHentaiAllURL 合成完整 URL。")
        url = self.URL.getExHentaiAllURL(self.urls["main"], params)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return waziExHentai.getBooks(self, url)

    def search(self, page, text):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和搜索内容参数，正在合成请求参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 搜索内容： {text}")
        params = {
            "page": str(page),
            "f_search": text
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 参数合成完毕，正在提交给 getFullURL 合成完整 URL。")
        url = self.URL.getFullURL(self.urls["main"], params)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return waziExHentai.getBooks(self, url)

    def allSearch(self, page, text):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和搜索内容参数，正在合成请求参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 搜索内容： {text}")
        params = {
            "page": str(page),
            "f_search": text
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 参数合成完毕，正在提交给 getExHentaiAllURL 合成完整 URL。")
        url = self.URL.getExHentaiAllURL(self.urls["main"], params)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return waziExHentai.getBooks(self, url)

    def tagSearch(self, page, tag):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和标签参数，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 标签： {tag}")
        url = self.urls["main"] + "tag/" + tag + "/" + str(page) + "?empty=0"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return waziExHentai.getBooks(self, url)

    def uploaderSearch(self, page, uploader):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和上传者参数，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 标签： {uploader}")
        url = self.urls["main"] + "uploader/" + uploader + "/" + str(page) + "?empty=0"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return waziExHentai.getBooks(self, url)

    def uploaderAllSearch(self, page, uploader):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和上传者参数，正在合成请求参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 标签： {uploader}")
        params = {
            "page": str(page),
            "f_search": "uploader%3A" + uploader,
            "f_spf": "",
            "f_spt": ""
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 参数合成完毕，正在提交给 getExHentaiAllURL 合成完整 URL。")
        url = self.URL.getExHentaiAllURL(self.urls["main"], params)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return waziExHentai.getBooks(self, url)

    def advancedSearch(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在合成请求参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 参数： {params}")
        queryParams = {
            "f_cats": str(self.check.getSources(params))
        }
        waziLog.log("debug", f"({self.name}.{fuName}) f_cats 数值写入完毕，数据为： {queryParams['f_cats']}")
        if str(params["search"]):
            waziLog.log("debug", f"({self.name}.{fuName}) 参数中存在搜索内容，准备写入。")
            queryParams["f_search"] = str(params["search"])
            waziLog.log("debug", f"({self.name}.{fuName}) 已写入搜索内容，数据为： {queryParams['f_search']}")
        queryParams["advsearch"] = "1"
        waziLog.log("debug", f"({self.name}.{fuName}) 已打开高级搜索，正在解析剩余参数。")
        if params["sgn"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索画廊名称，写入 f_sname = on")
            queryParams["f_sname"] = "on"
        if params["sgt"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索画廊标签，写入 f_stags = on")
            queryParams["f_stags"] = "on"
        if params["sgd"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索画廊描述，写入 f_sdesc = on")
            queryParams["f_sdesc"] = "on"
        if params["stf"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索种子名称，写入 f_storr = on")
            queryParams["f_storr"] = "on"
        if params["osgwt"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要仅带有种子的画廊，写入 f_sto = on")
            queryParams["f_sto"] = "on"
        if params["slpt"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索冷门标签和低评分标签，写入 f_sdt1 = on")
            queryParams["f_sdt1"] = "on"
        if params["sdt"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索投票过给差的标签，写入 f_sdt2 = on")
            queryParams["f_sdt2"] = "on"
        if params["seg"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索被移除的画廊，写入 f_sh = on")
            queryParams["f_sh"] = "on"
        if params["mr"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要限定最低评分，写入 f_sr = on 和 f_srdd = {params['mrs']}")
            queryParams["f_sr"] = "on"
            queryParams["f_srdd"] = str(params["mrs"])
        if params["b"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索限定范围，写入 f_sp = on f_spf = {params['f_spf']} 和 "
                                 f"f_spt = {params['f_spt']}")
            queryParams["f_sp"] = "on"
            queryParams["f_spf"] = str(params["b1"])
            queryParams["f_spt"] = str(params["b2"])
        if params["dfl"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要关掉默认或设置对语言的过滤，写入 f_sfl = on")
            queryParams["f_sfl"] = "on"
        if params["dfu"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要关掉默认或设置对上传者的过滤，写入 f_sfu = on")
            queryParams["f_sfu"] = "on"
        if params["dft"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要关掉默认或设置对标签的过滤，写入 f_sft = on")
            queryParams["f_sft"] = "on"
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {params['page']} 正在写入。")
        queryParams["page"] = str(params["page"])
        waziLog.log("debug", f"({self.name}.{fuName}) 参数合成完毕，正在提交给 getFullURL 合成完整 URL。")
        url = self.URL.getFullURL(self.urls["main"], queryParams)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return waziExHentai.getBooks(self, url)

    def imageSearch(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在合成请求参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 参数： {params}")
        if params["type"] == "sha1":
            waziLog.log("debug", f"({self.name}.{fuName}) 参数中存在 SHA-1 值： {params['sha1']}，正在写入。")
            sha1 = params["sha1"]
        elif params["type"] == "file":
            waziLog.log("debug", f"({self.name}.{fuName}) 参数中存在文件路径： {params['path']}，正在获取其 SHA-1 值并写入。")
            sha1 = self.check.getFileSHA1(params["path"])
            waziLog.log("debug", f"({self.name}.{fuName}) 文件 SHA-1 值为： {sha1}")
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 不存在 SHA-1 信息，自动设置为空。")
            sha1 = ""
        queryParams = {
            "f_shash": sha1
        }
        waziLog.log("debug", f"({self.name}.{fuName}) SHA-1 值已写入请求参数，正在检查余下参数内容。")
        if params["similar"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索近似图片，写入 fs_similar = 1")
            queryParams["fs_similar"] = "1"
        if params["cover"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索封面，写入 fs_covers = 1")
            queryParams["fs_covers"] = "1"
        if params["exp"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索被移除画廊，写入 fs_exp = 1")
            queryParams["fs_exp"] = "1"
        if params["page"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要限定页码，写入 page = {params['page']}")
            queryParams["page"] = str(params["page"])
        waziLog.log("debug", f"({self.name}.{fuName}) 参数合成完毕，正在提交给 getFullURL 合成完整 URL。")
        url = self.URL.getFullURL(self.urls["main"], queryParams)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return waziExHentai.getBooks(self, url)

    def customSearch(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在合成请求参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 参数： {params}")
        queryParams = {}
        if "page" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在 page 参数，正在写入。")
            queryParams["page"] = params["page"]
            waziLog.log("debug", f"({self.name}.{fuName}) 写入完成，page 为： {queryParams['page']}")
        if "cats" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在 cats 参数，正在计算 f_cats 并写入。")
            queryParams["f_cats"] = str(self.check.getSources(params))
            waziLog.log("debug", f"({self.name}.{fuName}) 写入完成，f_cats 为： {queryParams['f_cats']}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在 cats 参数，f_cats 写入为 0。")
            queryParams["f_cats"] = "0"
        queryParams["f_search"] = ""
        waziLog.log("debug", f"({self.name}.{fuName}) 准备检查搜索内容。")
        if "uploaders" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在上传者信息，准备遍历。")
            for i in params["uploaders"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 上传者： {i}")
                queryParams["f_search"] += "uploader:" + i + "+"
            queryParams["f_search"] = queryParams["f_search"][:-1]
            waziLog.log("debug", f"({self.name}.{fuName}) 上传者数据写入完成，目前搜索内容：{queryParams['f_search']}")
        if "tags" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在标签信息，准备遍历。")
            if queryParams["f_search"] != "":
                waziLog.log("debug", f"({self.name}.{fuName}) 检查到搜索内容非空，自动添加“+”。")
                queryParams["f_search"] += "+"
            for i in params["tags"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 标签： {i}")
                queryParams["f_search"] += i + "+"
            queryParams["f_search"] = queryParams["f_search"][:-1]
            waziLog.log("debug", f"({self.name}.{fuName}) 标签数据写入完成，目前搜索内容：{queryParams['f_search']}")
        if "text" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在搜索内容信息，准备写入。")
            if queryParams["f_search"] != "":
                waziLog.log("debug", f"({self.name}.{fuName}) 检查到搜索内容非空，自动添加“+”。")
                queryParams["f_search"] += "+"
            waziLog.log("debug", f"({self.name}.{fuName}) 搜索内容： {params['text']}")
            queryParams["f_search"] += params["text"]
            waziLog.log("debug", f"({self.name}.{fuName}) 自定义搜索内容写入完成，目前搜索内容：{queryParams['f_search']}")
        if "advanced" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在高级搜索内容，准备检索并写入数据。")
            queryParams["advanced"] = "1"
            if "search" in params["advanced"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在高级搜索 search 内容，开始检索。")
                if params["advanced"]["search"]["galleryName"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要检索画廊名，写入 f_sname = on")
                    queryParams["f_sname"] = "on"
                elif not params["advanced"]["search"]["galleryName"]:
                    queryParams["f_sname"] = ""
                else:
                    pass
                if params["advanced"]["search"]["galleryTags"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要检索画廊标签，写入 f_stags = on")
                    queryParams["f_stags"] = "on"
                elif not params["advanced"]["search"]["galleryTags"]:
                    queryParams["f_stags"] = ""
                else:
                    pass
                if params["advanced"]["search"]["galleryDescription"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要检索画廊描述，写入 f_sdesc = on")
                    queryParams["f_sdesc"] = "on"
                elif not params["advanced"]["search"]["galleryDescription"]:
                    queryParams["f_sdesc"] = ""
                else:
                    pass
                if params["advanced"]["search"]["torrentFilenames"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索种子名，写入 f_storr = on")
                    queryParams["f_storr"] = "on"
                elif not params["advanced"]["search"]["torrentFilenames"]:
                    queryParams["f_storr"] = ""
                else:
                    pass
                if params["advanced"]["search"]["low-powerTags"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索搜索低能标签，写入 f_sdt1 = on")
                    queryParams["f_sdt1"] = "on"
                elif not params["advanced"]["search"]["low-powerTags"]:
                    queryParams["f_sdt1"] = ""
                else:
                    pass
                if params["advanced"]["search"]["downvotedTags"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索投票过给差的标签，写入 f_sdt2 = on")
                    queryParams["f_sdt2"] = "on"
                elif not params["advanced"]["search"]["downvotedTags"]:
                    queryParams["f_sdt2"] = ""
                else:
                    pass
                if params["advanced"]["search"]["expungedGalleries"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索被移除的画廊，写入 f_sh = on")
                    queryParams["f_sh"] = "on"
                elif not params["advanced"]["search"]["expungedGalleries"]:
                    queryParams["f_sh"] = ""
                else:
                    pass
            if "limit" in params["advanced"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在高级搜索 limit 内容，开始检索。")
                if params["advanced"]["limit"]["onlyShowGalleriesWithTorrents"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要只搜索带种子的画廊，写入 f_sto = on")
                    queryParams["f_sto"] = "on"
                elif not params["advanced"]["limit"]["onlyShowGalleriesWithTorrents"]:
                    queryParams["f_sto"] = ""
                else:
                    pass
                if params["advanced"]["limit"]["minimumRating"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要限定搜索评分，写入 f_sr = on 和 f_srdd = "
                                         f"{params['advanced']['limit']['minimumRatingNumber']}")
                    queryParams["f_sr"] = "on"
                    queryParams["f_srdd"] = str(params["advanced"]["limit"]["minimumRatingNumber"])
                elif not params["advanced"]["limit"]["minimumRating"]:
                    queryParams["f_sr"] = ""
                    queryParams["f_srdd"] = ""
                else:
                    pass
                if params["advanced"]["limit"]["between"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要限定搜索范围，写入 f_sp = on f_spf = "
                                         f"{params['advanced']['limit']['betweenPages'][0]} 和 f_spt = "
                                         f"{params['advanced']['limit']['betweenPages'][1]}")
                    queryParams["f_sp"] = "on"
                    queryParams["f_spf"] = str(params["advanced"]["limit"]["betweenPages"][0])
                    queryParams["f_spt"] = str(params["advanced"]["limit"]["betweenPages"][1])
                elif not params["advanced"]["limit"]["between"]:
                    queryParams["f_sp"] = ""
                    queryParams["f_spf"] = ""
                    queryParams["f_spt"] = ""
                else:
                    pass
            if "disableFilters" in params["advanced"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在高级搜索 disableFilters 内容，开始检索。")
                if params["advanced"]["disableFilters"]["language"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要关掉对于语言的过滤，写入 f_sfl = on")
                    queryParams["f_sfl"] = "on"
                elif not params["advanced"]["disableFilters"]["language"]:
                    queryParams["f_sfl"] = ""
                else:
                    pass
                if params["advanced"]["disableFilters"]["uploader"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要关掉对于上传者的过滤，写入 f_sfu = on")
                    queryParams["f_sfu"] = "on"
                elif not params["advanced"]["disableFilters"]["uploader"]:
                    queryParams["f_sfu"] = ""
                else:
                    pass
                if params["advanced"]["disableFilters"]["tags"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要关掉对于标签的过滤，写入 f_sfu = on")
                    queryParams["f_sft"] = "on"
                elif not params["advanced"]["disableFilters"]["tags"]:
                    queryParams["f_sft"] = ""
                else:
                    pass
        if "file" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在文件搜索内容，准备检索并写入数据。")
            if "main" in params["file"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在文件搜索 main 内容，开始检索。")
                if "type" in params["file"]["main"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 存在 type，正在分析。")
                    if params["file"]["main"]["type"] == "path":
                        waziLog.log("debug", f"({self.name}.{fuName}) 给出文件路径，通过 getFileSHA1 获取 SHA-1 值。")
                        queryParams["f_shash"] = self.check.getFileSHA1(params["file"]["main"]["value"])
                        waziLog.log("debug", f"({self.name}.{fuName}) 获取并写入成功，f_shash = {queryParams['f_shash']}")
                    elif params["file"]["main"]["type"] == "sha1":
                        waziLog.log("debug", f"({self.name}.{fuName}) 给出文件 SHA-1 值，写入 f_shash = "
                                             f"{params['file']['main']['value']}")
                        queryParams["f_shash"] = params["file"]["main"]["value"]
                    else:
                        pass
            if "options" in params["file"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在 options，正在分析。")
                if params["file"]["options"]["useSimilarityScan"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要启用相似搜索，写入 fs_similar = 1")
                    queryParams["fs_similar"] = "1"
                elif not params["file"]["options"]["useSimilarityScan"]:
                    queryParams["fs_similar"] = ""
                else:
                    pass
                if params["file"]["options"]["onlySearchCovers"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要只搜索封面，写入 fs_covers = 1")
                    queryParams["fs_covers"] = "1"
                elif not params["file"]["options"]["onlySearchCovers"]:
                    queryParams["fs_covers"] = ""
                else:
                    pass
                if params["file"]["options"]["showExpunged"]:
                    waziLog.log("debug", f"({self.name}.{fuName}) 需要搜索被移除的画廊，写入 fs_exp = 1")
                    queryParams["fs_exp"] = "1"
                elif not params["file"]["options"]["showExpunged"]:
                    queryParams["fs_exp"] = ""
                else:
                    pass
        waziLog.log("debug", f"({self.name}.{fuName}) 参数合成完毕，正在提交给 getFullURL 合成完整 URL。")
        url = self.URL.getFullURL(self.urls["main"], queryParams)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕，递交给 getBooks： {url}")
        return [{"url": url}, waziExHentai.getBooks(self, url)]

    def returnSoup(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得 Soup： {link}")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        waziLog.log("debug", f"({self.name}.{fuName}) 需要检查 URL 并进行处理。")
        if self.jumpWarn:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要跳过画廊警告，")
            tempHeaders["nw"] = "1"
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

    def getTorrent(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得其种子信息： {link}")
        url = self.urls["galleryTorrent"] + link.split("/")[4] + "&t=" + link.split("/")[5]
        waziLog.log("debug", f"({self.name}.{fuName}) 种子信息 URL： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziExHentai.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，进入分析。")
        torrents = []
        try:
            tempNum = len(soup.find_all("a")) - 1
        except:
            waziLog.log("warn", f"({self.name}.{fuName}) 无法获取种子信息，请检查 URL 或账号信息等排除问题。")
            return {"Error": "None"}
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 获取成功，等待遍历： {tempNum}")
            for tempInfo in range(tempNum):
                waziLog.log("debug", f"({self.name}.{fuName}) 进入 for in 循环，正在取出信息。")
                tempList = {
                    "time": soup.find_all("table")[tempInfo].tr.find_all("td")[0].get_text().split("Posted: ")[1],
                    "size": soup.find_all("table")[tempInfo].tr.find_all("td")[1].get_text().split("Size: ")[1],
                    "seeds": soup.find_all("table")[tempInfo].tr.find_all("td")[3].get_text().split("Seeds: ")[1],
                    "peers": soup.find_all("table")[tempInfo].tr.find_all("td")[4].get_text().split("Peers: ")[1],
                    "total": soup.find_all("table")[tempInfo].tr.find_all("td")[5].get_text().split("Downloads: ")[1],
                    "link": soup.find_all("table")[tempInfo].find_all("tr")[2].a.attrs["href"],
                    "name": soup.find_all("table")[tempInfo].find_all("tr")[2].a.get_text()
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 信息取出完毕： {tempList}")
                waziLog.log("debug", f"({self.name}.{fuName}) 追加至 torrents。")
                torrents.append(tempList)
            waziLog.log("info", f"({self.name}.{fuName}) 已跳出循环体，torrents 已获取： {torrents}")
            return torrents

    def getInfo(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得其画廊信息： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziExHentai.returnSoup(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，进入分析。")
        tags = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在遍历获取标签。")
        for tag in soup.find_all(id = "taglist")[0].find_all("a"):
            tagName = tag.attrs["onclick"].split("'")[1]
            waziLog.log("debug", f"({self.name}.{fuName}) 获取到： {tagName}")
            tags.append(tagName)
        waziLog.log("debug", f"({self.name}.{fuName}) 标签获取完毕： {tags}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取剩余信息。")
        info = {
            "title": soup.h1.get_text(),
            "jTitle": soup.find_all(id = "gj")[0].get_text(),
            "cat": soup.find_all(id = "gdc")[0].div.get_text(),
            "tags": tags,
            "time": soup.find_all(class_ = "gdt2")[0].get_text(),
            "father": soup.find_all(class_ = "gdt2")[1].get_text(),
            "viewable": soup.find_all(class_ = "gdt2")[2].get_text(),
            "language": soup.find_all(class_ = "gdt2")[3].get_text().split(" \xa0")[0],
            "tr": True if "TR" in soup.find_all(class_ = "gdt2")[3].get_text() else False,
            "rw": True if "RW" in soup.find_all(class_ = "gdt2")[3].get_text() else False,
            "size": soup.find_all(class_ = "gdt2")[4].get_text(),
            "pages": int(soup.find_all(class_ = "gdt2")[5].get_text().split(" ")[0]),
            "favTimes": soup.find_all(class_ = "gdt2")[6].get_text(),
            "uploader": soup.find_all(id = "gdn")[0].a.get_text(),
            "rate": soup.find_all(id = "rating_label")[0].get_text().split("Average: ")[1],
            "cover": soup.find_all(id = "gd1")[0].div.attrs["style"].split("(")[1].split(")")[0]
        }
        waziLog.log("info", f"({self.name}.{fuName}) 剩余信息和标签组合获取完毕： {info}")
        return info

    def getComments(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得其评论信息。")
        url = link
        if self.fullComments:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要完全的评论区。")
            if url.endswith("?"):
                url += "&hc=1#comments"
            else:
                url += "?hc=1#comments"
        waziLog.log("debug", f"({self.name}.{fuName}) 请求 URL 纠正： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziExHentai.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，进入分析。")
        comments = []
        for i in soup.find_all(id = "cdiv")[0].find_all(class_ = "c1"):
            waziLog.log("debug", f"({self.name}.{fuName}) 进入循环体，正在分析内容。")
            htmlComments = i.find_all(class_="c6")[0].prettify()
            waziLog.log("debug", f"({self.name}.{fuName}) 已获得评论内容（html 格式）")
            start = re.findall("<div.*?>", i.find_all(class_ = "c6")[0].prettify())[0]
            htmlComments = htmlComments.replace(start, "")
            htmlComments = htmlComments.replace("</div>", "")
            waziLog.log("debug", f"({self.name}.{fuName}) 评论内容获取完毕： {htmlComments}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试获取评分。")
            try:
                i.find(class_ = "c5 nosel").span.get_text()
            except:
                waziLog.log("debug", f"({self.name}.{fuName}) 该评论无法获取评分，或为上传者评论。")
                scores = "None / 不适用 | Uploader / 上传者"
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 该评论存在评分。")
                scores = i.find(class_ = "c5 nosel").span.get_text()
                waziLog.log("debug", f"({self.name}.{fuName}) 评分数据为： {scores}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在组合剩余数据。")
            tempComments = {
                "time": i.find(class_ = "c3").get_text().split(" by:")[0].split("Posted on ")[1],
                "uploader": i.find(class_ = "c3").a.attrs["href"],
                "uploaderName": i.find(class_ = "c3").a.get_text(),
                "scores": scores,
                "htmlComments": htmlComments
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 剩余数据组合完毕： {tempComments}")
            comments.append(tempComments)
            waziLog.log("debug", f"({self.name}.{fuName}) 评论数据已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 全部评论已获取： {comments}")
        return comments

    def apiInfo(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得其 API 返回信息： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 header。")
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.headers["Cookie"]
        }
        waziLog.log("debug", f"({self.name}.{fuName}) header 创建完毕： {headers}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 POST 数据。")
        body = {
            "method": "gdata",
            "gidlist": [
                [link.split("/")[4], link.split("/")[5]]
            ],
            "namespace": 1
        }
        waziLog.log("debug", f"({self.name}.{fuName}) POST 数据创建完毕： {body}")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 正在处理请求参数。")
        requestParams = self.request.handleParams(tempParams, "post", self.urls["api"], headers, self.proxies)
        requestParams["data"] = json.dumps(body).encode()
        waziLog.log("debug", f"({self.name}.{fuName}) 处理完毕，正在请求。")
        try:
            returnJson = json.loads(self.request.do(requestParams).data.decode("utf-8"))
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 获取失败，返回空字典。")
            return {}
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 已获取返回数据： {returnJson}")
            return returnJson

    def getPages(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得其页码信息： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziExHentai.returnSoup(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，进入分析。")
        try:
            pages = int(soup.find_all(class_ = "ptt")[0].find_all("a")[-2].get_text())
        except:
            waziLog.log("info", f"({self.name}.{fuName}) 无需翻页，返回 0。")
            return 0
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 需要 range： {pages}")
            return pages

    def parseSoupForLargeThumbnails(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息，开始分析。")
        thumbnails = []
        for i in soup.find(id = "gdt").find_all(class_ = "gdtl"):
            waziLog.log("debug", f"({self.name}.{fuName}) 进入遍历，正在组合信息。")
            tempThumbnails = {
                "url": i.a.img.attrs["src"],
                "style": i.attrs["style"],
                "alt": i.a.img.attrs["alt"],
                "title": i.a.img.attrs["title"],
                "text": i.a.get_text()
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完毕： {tempThumbnails}")
            thumbnails.append(tempThumbnails)
            waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 大尺寸缩略图获取完毕： {thumbnails}")
        return thumbnails
    
    def yieldGetLargeThumbnails(self, link):
        # Still need to be tested
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得其页码信息： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziExHentai.returnSoup(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，进入分析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getPages 获取页码数据。")
        page = waziExHentai.getPages(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {page}，开始获取大尺寸缩略图。")
        if page == 0:
            waziLog.log("debug", f"({self.name}.{fuName}) 单页模式。")
            data = waziExHentai.parseSoupForLargeThumbnails(self, soup)
            waziLog.log("debug", f"({self.name}.{fuName}) 数据已取得： {data}")
            yield data
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 多页模式。")
            for i in range(1, page + 1):
                url = link + "?p=" + str(i)
                waziLog.log("debug", f"({self.name}.{fuName}) 已进入循环，URL 已创建完毕： {url}，"
                                     f"通过 returnSoup 获取 Soup 数据。")
                soup = waziExHentai.returnSoup(self, url)
                waziLog.log("debug", f"({self.name}.{fuName}) 已取得 Soup 数据，进入大尺寸缩略图解析器。")
                data = waziExHentai.parseSoupForLargeThumbnails(self, soup)
                waziLog.log("debug", f"({self.name}.{fuName}) 单页大尺寸缩略图缩略图数据： {data}")
                yield data

    def getLargeThumbnails(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得其页码信息： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziExHentai.returnSoup(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getPages 获取页码数据。")
        page = waziExHentai.getPages(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {page}，开始获取大尺寸缩略图。")
        thumbnails = []
        if page == 0:
            waziLog.log("debug", f"({self.name}.{fuName}) 单页模式。")
            data = waziExHentai.parseSoupForLargeThumbnails(self, soup)
            waziLog.log("info", f"({self.name}.{fuName}) 数据已取得： {data}")
            return data
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 多页模式。")
            for i in range(page):
                url = link + "?p=" + str(i)
                waziLog.log("debug", f"({self.name}.{fuName}) 已进入循环，URL 已创建完毕： {url}，"
                                     f"通过 returnSoup 获取 Soup 数据。")
                soup = waziExHentai.returnSoup(self, url)
                waziLog.log("debug", f"({self.name}.{fuName}) 已取得 Soup 数据，进入大尺寸缩略图解析器。")
                data = waziExHentai.parseSoupForLargeThumbnails(self, soup)
                waziLog.log("debug", f"({self.name}.{fuName}) 单页大尺寸缩略图缩略图数据： {data}")
                thumbnails.append(data)
                waziLog.log("debug", f"({self.name}.{fuName}) 已追加到列表。")
            waziLog.log("info", f"({self.name}.{fuName}) 全部数据已取得： {thumbnails}")
            return thumbnails

    def parseSoupForNormalThumbnails(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息，开始分析。")
        thumbnails = []
        for i in soup.find_all(class_ = "gdtm"):
            waziLog.log("debug", f"({self.name}.{fuName}) 进入遍历，正在组合信息。")
            tempThumbnails = {
                "style": i.attrs["style"],
                "divMargin": i.div.attrs["style"].split("margin:")[1].split(";")[0],
                "divWidth": i.div.attrs["style"].split("width:")[1].split(";")[0],
                "divHeight": i.div.attrs["style"].split("height:")[1].split(";")[0],
                "url": i.div.attrs["style"].split("url(")[1].split(")")[0],
                "transparent": i.div.attrs["style"].split(") ")[1],
                "imgAlt": i.div.a.img.attrs["alt"],
                "imgTitle": i.div.a.img.attrs["title"],
                "imgWidth": i.div.a.img.attrs["style"].split("width:")[1].split(";")[0],
                "imgHeight": i.div.a.img.attrs["style"].split("height:")[1].split(";")[0],
                "imgMargin": i.div.a.img.attrs["style"].split("margin:")[1]
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 组合完毕： {tempThumbnails}")
            thumbnails.append(tempThumbnails)
        waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 正常尺寸缩略图获取完毕： {thumbnails}")
        return thumbnails
    
    def yieldGetNormalThumbnails(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得其页码信息： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziExHentai.returnSoup(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getPages 获取页码数据。")
        page = waziExHentai.getPages(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {page}，开始获取正常尺寸缩略图。")
        if page == 0:
            waziLog.log("debug", f"({self.name}.{fuName}) 单页模式。")
            data = waziExHentai.parseSoupForNormalThumbnails(self, soup)
            waziLog.log("info", f"({self.name}.{fuName}) 数据已取得： {data}")
            yield data
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 多页模式。")
            for i in range(page):
                url = link + "?p=" + str(i)
                waziLog.log("debug", f"({self.name}.{fuName}) 已进入循环，URL 已创建完毕： {url}，"
                                     f"通过 returnSoup 获取 Soup 数据。")
                soup = waziExHentai.returnSoup(self, url)
                waziLog.log("debug", f"({self.name}.{fuName}) 已取得 Soup 数据，进入正常尺寸缩略图解析器。")
                data = waziExHentai.parseSoupForNormalThumbnails(self, soup)
                waziLog.log("debug", f"({self.name}.{fuName}) 单页正常尺寸缩略图数据： {data}")
                yield data
        
    def getNormalThumbnails(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得其页码信息： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziExHentai.returnSoup(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在通过 getPages 获取页码数据。")
        page = waziExHentai.getPages(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {page}，开始获取正常尺寸缩略图。")
        thumbnails = []
        if page == 0:
            waziLog.log("debug", f"({self.name}.{fuName}) 单页模式。")
            data = waziExHentai.parseSoupForNormalThumbnails(self, soup)
            waziLog.log("info", f"({self.name}.{fuName}) 数据已取得： {data}")
            return data
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 多页模式。")
            for i in range(page):
                url = link + "?p=" + str(i)
                waziLog.log("debug", f"({self.name}.{fuName}) 已进入循环，URL 已创建完毕： {url}，"
                                     f"通过 returnSoup 获取 Soup 数据。")
                soup = waziExHentai.returnSoup(self, url)
                waziLog.log("debug", f"({self.name}.{fuName}) 已取得 Soup 数据，进入正常尺寸缩略图解析器。")
                data = waziExHentai.parseSoupForNormalThumbnails(self, soup)
                waziLog.log("debug", f"({self.name}.{fuName}) 单页正常尺寸缩略图数据： {data}")
                thumbnails.append(data)
                waziLog.log("debug", f"({self.name}.{fuName}) 已追加到列表。")
            waziLog.log("info", f"({self.name}.{fuName}) 全部数据已取得： {thumbnails}")
            return thumbnails

    def getTitle(self, link, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL 和参数，正在获得其标题。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {link}， 参数： {params}")
        if params["japanese"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要日语等其他语种标题，通过 getInfo 获取。")
            title = waziExHentai.getInfo(self, link)["jTitle"]
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要罗马音等标题，通过 getInfo 获取。")
            title = waziExHentai.getInfo(self, link)["title"]
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完毕： {title}，剔除字符。")
        title.strip().rstrip("\\")
        waziLog.log("info", f"({self.name}.{fuName}) 标题为： {title}")
        return title

    def createFolder(self, link, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL 和参数，正在创建文件夹。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {link}， 参数： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 通过 getTitle 获得标题。")
        title = waziExHentai.getTitle(self, link, params)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {title}")
        isExists = os.path.exists(os.path.join(params["path"], self.fileName.toRight(title)))
        if not isExists:
            os.makedirs(os.path.join(params["path"], self.fileName.toRight(title)))
        waziLog.log("info", f"({self.name}.{fuName}) 文件夹创建完成。")
    
    def yieldGetMPVImages(self, link, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL 和参数，正在获取 MPV 图像列表。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {link}， 参数： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合 URL。")
        mpvUrl = self.urls["mpv"] + link.split("/")[4] + "/" + link.split("/")[5]
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {mpvUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合 POST 请求参数。")
        post = {
            "method": "imagedispatch",
            "gid": int(link.split("/")[4]),
            "page": "",
            "imgkey": "",
            "mpvkey": ""
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {post}，正在通过 returnSoup 发起请求。")
        soup = waziExHentai.returnSoup(self, mpvUrl)
        waziLog.log("debug", f"({self.name}.{fuName}) 页面信息获取完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取页面中的 JavaScript 脚本。")
        scripts = str(soup.find_all("script")[1]).split("<script type=\"text/javascript\">")[1].split("</script>")[0]
        waziLog.log("debug", f"({self.name}.{fuName}) JS 脚本获取完成： {scripts}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 Image List 数据。")
        imgLists = eval(scripts.split("var imagelist = ")[1].split(";")[0])
        waziLog.log("debug", f"({self.name}.{fuName}) Image List 数据获取完毕： {imgLists}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 MPV Key 信息。")
        mpvkey = scripts.split("mpvkey = \"")[1].split("\"")[0]
        waziLog.log("debug", f"({self.name}.{fuName}) MPV Key 信息获取完毕： {mpvkey}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改请求参数和 Header。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        tempHeaders["Content-Type"] = "application/json"
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数和 Header 修改完毕。")
        i = 0
        waziLog.log("debug", f"({self.name}.{fuName}) 进入循环遍历。")
        for dic in imgLists:
            print(imgLists)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在修改 POST 请求参数。")
            i += 1
            post["page"] = i
            post["imgkey"] = dic["k"]
            post["mpvkey"] = mpvkey
            waziLog.log("debug", f"({self.name}.{fuName}) 修改完成： {post}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在处理请求参数。")
            requestParams = self.request.handleParams(tempParams, "post", self.urls["api"], tempHeaders, self.proxies)
            requestParams["data"] = json.dumps(post).encode()
            waziLog.log("debug", f"({self.name}.{fuName}) 请求参数处理完毕： {requestParams}， 准备发起请求。")
            lists = json.loads(self.request.do(requestParams).data.decode("utf-8"))
            waziLog.log("debug", f"({self.name}.{fuName}) 请求发起完毕，数据： {lists}")
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到获取模式，正在合成图像数据。")
            mpvList = {
                "name": dic["n"],
                "url": lists["i"]
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 图像数据： {mpvList}")
            yield mpvList

    def getMPVImages(self, link, method, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL, 方式和参数，正在获取 MPV 图像列表。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {link}， 方式： {method}， 参数： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合 URL。")
        mpvUrl = self.urls["mpv"] + link.split("/")[4] + "/" + link.split("/")[5]
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {mpvUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合 POST 请求参数。")
        post = {
            "method": "imagedispatch",
            "gid": int(link.split("/")[4]),
            "page": "",
            "imgkey": "",
            "mpvkey": ""
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {post}，正在通过 returnSoup 发起请求。")
        soup = waziExHentai.returnSoup(self, mpvUrl)
        waziLog.log("debug", f"({self.name}.{fuName}) 页面信息获取完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取页面中的 JavaScript 脚本。")
        scripts = str(soup.find_all("script")[1]).split("<script type=\"text/javascript\">")[1].split("</script>")[0]
        waziLog.log("debug", f"({self.name}.{fuName}) JS 脚本获取完成： {scripts}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 Image List 数据。")
        imgLists = eval(scripts.split("var imagelist = ")[1].split(";")[0])
        waziLog.log("debug", f"({self.name}.{fuName}) Image List 数据获取完毕： {imgLists}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 MPV Key 信息。")
        mpvkey = scripts.split("mpvkey = \"")[1].split("\"")[0]
        waziLog.log("debug", f"({self.name}.{fuName}) MPV Key 信息获取完毕： {mpvkey}")
        mpvLists = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改请求参数和 Header。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        tempHeaders["Content-Type"] = "application/json"
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数和 Header 修改完毕。")
        title = ""
        if method == "download":
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到下载请求，正在通过 createFolder 创建文件夹。")
            waziExHentai.createFolder(self, link, params)
            waziLog.log("debug", f"({self.name}.{fuName}) 文件夹创建完成，正在根据参数通过 getTitle 获取标题。")
            title = waziExHentai.getTitle(self, link, params)
            waziLog.log("debug", f"({self.name}.{fuName}) 标题获取完成： {title}")
        i = 0
        waziLog.log("debug", f"({self.name}.{fuName}) 进入循环遍历。")
        for dic in imgLists:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在修改 POST 请求参数。")
            i += 1
            post["page"] = i
            post["imgkey"] = dic["k"]
            post["mpvkey"] = mpvkey
            waziLog.log("debug", f"({self.name}.{fuName}) 修改完成： {post}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在处理请求参数。")
            requestParams = self.request.handleParams(tempParams, "post", self.urls["api"], tempHeaders, self.proxies)
            requestParams["data"] = json.dumps(post).encode()
            waziLog.log("debug", f"({self.name}.{fuName}) 请求参数处理完毕： {requestParams}， 准备发起请求。")
            lists = json.loads(self.request.do(requestParams).data.decode("utf-8"))
            waziLog.log("debug", f"({self.name}.{fuName}) 请求发起完毕，数据： {lists}")
            if method == "get":
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到获取模式，正在合成图像数据。")
                mpvList = {
                    "name": dic["n"],
                    "url": lists["i"]
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 图像数据： {mpvList}")
                mpvLists.append(mpvList)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
            if method == "download":
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到下载模式，准备合成请求参数。")
                requestParams = self.request.handleParams(tempParams, "get", lists["i"], self.headers, self.proxies)
                waziLog.log("debug", f"({self.name}.{fuName}) 请求参数处理完毕： {requestParams}， 准备发起请求。")
                fileData = self.request.do(requestParams).data
                waziLog.log("debug", f"({self.name}.{fuName}) 请求发起完毕，准备写入。")
                with open(os.path.join(params["path"], title, dic["n"]), "wb") as f:
                    f.write(fileData)
                waziLog.log("debug", f"({self.name}.{fuName}) 写入数据完成。")
                mpvLists.append(os.path.join(params["path"], title, dic["n"]))
                waziLog.log("debug", f"({self.name}.{fuName}) 文件路径已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 数据： {mpvLists}，结果返回。")
        return mpvLists

    def getImages(self, soup, method, title, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup， 方式和参数，标题，正在获取图像列表。")
        waziLog.log("debug", f"({self.name}.{fuName}) 方式： {method}， 参数： {params}，标题： {title}")
        images = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改请求 Header。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 请求 Header 修改完毕，正在从 Soup 中获取所有图像列表。")
        pics = soup.find_all(id = "gdt")[0].find_all("a")
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取，准备进入循环遍历。")
        for pic in pics:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取详细地址。")
            href = pic["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {href}，准备通过 returnSoup 获取 Soup。")
            soups = waziExHentai.returnSoup(self, href)
            waziLog.log("debug", f"({self.name}.{fuName}) 已获取，正在获取图像地址。")
            src = soups.find_all(id = "img")[0].attrs["src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 图像地址： {src}")
            if method == "get":
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到获取模式，追加数据。")
                images.append(src)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据追加完成。")
            if method == "download":
                waziLog.log("debug", f"({self.name}.{fuName}) 检测到下载模式，准备合成请求参数。")
                requestParams = self.request.handleParams(tempParams, "get", src, self.headers, self.proxies)
                waziLog.log("debug", f"({self.name}.{fuName}) 请求参数处理完毕： {requestParams}， 准备发起请求。")
                fileData = self.request.do(requestParams).data
                waziLog.log("debug", f"({self.name}.{fuName}) 请求发起完毕，准备写入。")
                with open(os.path.join(params["path"], title, src.split("/")[-1]), "wb") as f:
                    f.write(fileData)
                waziLog.log("debug", f"({self.name}.{fuName}) 写入数据完成。")
                images.append(os.path.join(params["path"], title, src.split("/")[-1]))
                waziLog.log("debug", f"({self.name}.{fuName}) 文件路径已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 数据： {images}，结果返回。")
        return images
    
    def yieldGetNormalImages(self, link, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和参数，正在获取图像列表。")
        waziLog.log("debug", f"({self.name}.{fuName}) 参数： {params}，URL： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取标题。")
        title = waziExHentai.getTitle(self, link, params)
        waziLog.log("debug", f"({self.name}.{fuName}) 标题获取成功： {title}")
        normalImages = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取页码信息。")
        page = waziExHentai.getPages(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 页码信息获取完成： {page}。")
        if page == 0:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无需翻页，正在通过 returnSoup 获取页面 Soup 信息。")
            soup = waziExHentai.returnSoup(self, link)
            waziLog.log("debug", f"({self.name}.{fuName}) Soup 信息获取完成，正在通过 getImages 获取。")
            data = waziExHentai.getImages(self, soup, "get", title, params)
            waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {data}")
            yield data
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页，进入 range 循环。")
            for i in range(page):
                waziLog.log("debug", f"({self.name}.{fuName}) 正在合成 URL。")
                url = link + "?p=" + str(i)
                waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕： {url}，正在通过 returnSoup 获取 Soup。")
                soup = waziExHentai.returnSoup(self, url)
                waziLog.log("debug", f"({self.name}.{fuName}) Soup 信息获取完成，正在通过 getImages 获取。")
                data = waziExHentai.getImages(self, soup, "get", title, params)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据获取完成： {data}")
                yield data

    def getNormalImages(self, link, method, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL， 方式和参数，正在获取图像列表。")
        waziLog.log("debug", f"({self.name}.{fuName}) 方式： {method}， 参数： {params}，URL： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取标题。")
        title = waziExHentai.getTitle(self, link, params)
        waziLog.log("debug", f"({self.name}.{fuName}) 标题获取成功： {title}")
        normalImages = []
        if method == "download":
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到下载模式，准备新建文件夹。")
            waziExHentai.createFolder(self, link, params)
            waziLog.log("debug", f"({self.name}.{fuName}) 文件夹新建完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取页码信息。")
        page = waziExHentai.getPages(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 页码信息获取完成： {page}。")
        if page == 0:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到无需翻页，正在通过 returnSoup 获取页面 Soup 信息。")
            soup = waziExHentai.returnSoup(self, link)
            waziLog.log("debug", f"({self.name}.{fuName}) Soup 信息获取完成，正在通过 getImages 获取。")
            data = waziExHentai.getImages(self, soup, method, title, params)
            waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {data}")
            return data
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到多页，进入 range 循环。")
            for i in range(page):
                waziLog.log("debug", f"({self.name}.{fuName}) 正在合成 URL。")
                url = link + "?p=" + str(i)
                waziLog.log("debug", f"({self.name}.{fuName}) URL 合成完毕： {url}，正在通过 returnSoup 获取 Soup。")
                soup = waziExHentai.returnSoup(self, url)
                waziLog.log("debug", f"({self.name}.{fuName}) Soup 信息获取完成，正在通过 getImages 获取。")
                data = waziExHentai.getImages(self, soup, method, title, params)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据获取完成： {data}")
                normalImages.append(data)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据追加完成。")
            waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {normalImages}")
            return normalImages

    def getArchivesHATH(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，正在 H@H 下载参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 发起请求。")
        soup = waziExHentai.returnSoup(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在获取 H@H 详情界面 URL。")
        url = soup.find_all(class_ = "g2 gsp")[0].a.attrs["onclick"].split("'")[1]
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完毕： {url}，正在通过 returnSoup 发起请求。")
        soup = waziExHentai.returnSoup(self, url)
        archiveLists = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取请求链接。")
        action = soup.find_all("form")[0].attrs["action"]
        waziLog.log("debug", f"({self.name}.{fuName}) 请求连接已获取： {action}，正在进入循环。")
        for i in soup.find_all("td"):
            if i.find_all("p")[1].get_text() == "N/A":
                sample = i.find_all("p")[0].get_text()
                waziLog.log("debug", f"({self.name}.{fuName}) 该分辨率 {sample} 不存在 H@H 下载代码，正在组合剩余数据。")
                archiveTemp = {
                    "sample": sample,
                    "size": i.find_all("p")[1].get_text(),
                    "cost": i.find_all("p")[2].get_text(),
                    "code": "N/A",
                    "url": "N/A"
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 组合完毕，数据如下： {archiveTemp}")
                archiveLists.append(archiveTemp)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
            else:
                sample = i.find_all("p")[0].get_text()
                waziLog.log("debug", f"({self.name}.{fuName}) 该分辨率 {sample} 存在 H@H 下载代码，正在组合剩余数据。")
                archiveTemp = {
                    "sample": sample,
                    "size": i.find_all("p")[1].get_text(),
                    "cost": i.find_all("p")[2].get_text(),
                    "code": i.find_all("p")[0].a.attrs["onclick"].split("'")[1],
                    "url": action
                }
                waziLog.log("debug", f"({self.name}.{fuName}) 组合完毕，数据如下： {archiveTemp}")
                archiveLists.append(archiveTemp)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 数据已完成获取： {archiveLists}")
        return archiveLists

    def toHATH(self, link, code):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和 H@H 下载代码，正在发起 H@H 下载请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {link}， H@H 下载代码： {code}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在合成请求数据。")
        forms = {
            "hathdl_xres": code
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 合成完毕： {forms}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改请求 Header。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 请求 Header 修改完成： {tempParams}，正在处理参数。")
        requestParams = self.request.handleParams(tempParams, "fieldsPost", link, self.headers, self.proxies)
        requestParams["data"] = forms
        waziLog.log("debug", f"({self.name}.{fuName}) 处理完成： {requestParams}，准备发起请求。")
        try:
            self.request.do(requestParams)
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 请求下载 H@H 失败，检查你的账号和网络配置。")
            return "Error, check your cookies and something balabala. / 错误，请检查你的 Cookies 或者其他乱七八糟的东西。"
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 请求下载 H@H 成功。")
            return "Done! / 完成！"

    def parseArchives(self, form, action):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求参数和请求地址，正在获取下载链接。")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数： {form}， 请求地址： {action}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改请求 Header。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 请求 Header 修改完成： {tempParams}，正在处理参数。")
        requestParams = self.request.handleParams(tempParams, "fieldsPost", action, self.headers, self.proxies)
        requestParams["data"] = form
        waziLog.log("debug", f"({self.name}.{fuName}) 处理完成： {requestParams}，准备发起请求。")
        soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求发送完成，已获取 Soup 信息，正在获取 JavaScript 内容。")
        tempUrl = soup.find_all("script")[0]
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，准备提取转跳链接。")
        try:
            tempUrl = str(tempUrl).split("document.location = \"")[1].split("\";")[0]
        except:
            waziLog.log("info", f"({self.name}.{fuName}) 无法提取任何转跳链接。")
            return "None / 无"
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 提取完成，准备处理请求参数。")
            requestParams = self.request.handleParams(tempParams, "get", tempUrl, self.headers, self.proxies)
            waziLog.log("debug", f"({self.name}.{fuName}) 处理完成： {requestParams}，准备发起请求。")
            soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
            waziLog.log("debug", f"({self.name}.{fuName}) 请求发送完成，已获取 Soup 信息，正在获取下载链接。")
            href = soup.find_all("a")[0].attrs["href"]
            downloadLink = urllib.parse.urljoin(tempUrl, href)
            waziLog.log("debug", f"({self.name}.{fuName}) 获取并拼接完成： {downloadLink}")
            return downloadLink

    def getArchives(self, link):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到画廊地址，正在获取所有压缩包下载地址。")
        waziLog.log("debug", f"({self.name}.{fuName}) 画廊地址： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup 信息。")
        soup = waziExHentai.returnSoup(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完毕，正在查找下载页面地址。")
        url = soup.find_all(class_ = "g2 gsp")[0]
        url = url.a.attrs["onclick"].split("'")[1]
        waziLog.log("debug", f"({self.name}.{fuName}) 查找完成： {url}，正在通过 returnSoup 获取 Soup 信息。")
        soup = waziExHentai.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在获取请求链接。")
        twoLists = []
        action = soup.find_all("form")[0].attrs["action"]
        waziLog.log("debug", f"({self.name}.{fuName}) 请求链接： {action}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建表单请求。")
        orgForms = {
            "dltype": "org",
            "dlcheck": "Download Original Archive"
        }
        resForms = {
            "dltype": "res",
            "dlcheck": "Download Resample Archive"
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 创建完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 原图尺寸： {orgForms}")
        waziLog.log("debug", f"({self.name}.{fuName}) 缩略尺寸： {resForms}")
        waziLog.log("debug", f"({self.name}.{fuName}) 查找原图和缩略尺寸的可用性。")
        orgExist = "disabled" in soup.find_all("form")[0].div.input.attrs
        resExist = "disabled" in soup.find_all("form")[1].div.input.attrs
        waziLog.log("debug", f"({self.name}.{fuName}) 查找完成，进入检查。")
        if not orgExist:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在原图尺寸的压缩包，正在通过 parseArchives 获取下载链接。")
            temp = {
                "type": "original",
                "link": waziExHentai.parseArchives(self, orgForms, action)
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 获取并组合完毕： {temp}")
            twoLists.append(temp)
            waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
        if not resExist:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在缩略尺寸的压缩包，正在通过 parseArchives 获取下载链接。")
            temp = {
                "type": "resample",
                "link": waziExHentai.parseArchives(self, resForms, action)
            }
            waziLog.log("debug", f"({self.name}.{fuName}) 获取并组合完成： {temp}")
            twoLists.append(temp)
            waziLog.log("debug", f"({self.name}.{fuName}) 数据已追加。")
        waziLog.log("info", f"({self.name}.{fuName}) 数据： {twoLists}")
        return twoLists

    def downloadArchives(self, link, params, sample):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到画廊地址，参数和清晰度，正在获取压缩包下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) 画廊地址： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 参数： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 清晰度： {sample}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改请求 Header。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 请求 Header 修改完成： {tempParams}，正在通过 getTitle 获取标题。")
        title = waziExHentai.getTitle(self, link, params)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {title}，正在创建文件夹。")
        waziExHentai.createFolder(self, link, params)
        waziLog.log("debug", f"({self.name}.{fuName}) 文件夹创建完成，正在获取压缩包下载链接。")
        links = waziExHentai.getArchives(self, link)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，压缩包下载链接： {links}")
        files = []
        if not links:
            waziLog.log("info", f"({self.name}.{fuName}) 没有返回任何压缩包下载地址。")
            return "No url return. / 没有返回 URL。"
        if sample != "":
            waziLog.log("debug", f"({self.name}.{fuName}) 存在指定分辨率。")
            for i in links:
                if not i == "None / 无":
                    if i["type"] == sample:
                        waziLog.log("debug", f"({self.name}.{fuName}) 分辨率： {i['type']}")
                        waziLog.log("debug", f"({self.name}.{fuName}) 正在处理请求参数。")
                        requestParams = self.request.handleParams(tempParams, "get", i["link"], self.headers,
                                                                  self.proxies)
                        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数处理完毕： {requestParams}， 准备请求下载。")
                        try:
                            temp = self.request.do(requestParams)
                        except:
                            waziLog.log("error", f"({self.name}.{fuName}) 无法请求下载。")
                        else:
                            waziLog.log("debug", f"({self.name}.{fuName}) 下载成功，正在获取画廊压缩包标题。")
                            try:
                                fileName = self.fileName.toRight(temp.headers["Content-Disposition"])
                            except:
                                waziLog.log("debug", f"({self.name}.{fuName}) 从 header 中获取失败，创建新文件名。")
                                fileName = self.fileName.toRight(i["type"] + "_" + title + ".zip")
                                waziLog.log("debug", f"({self.name}.{fuName}) 创建完成： {fileName}")
                            else:
                                waziLog.log("debug", f"({self.name}.{fuName}) 从 header 中获取完成： {fileName}，"
                                                     f"正在修改文件名。")
                                fileName = \
                                    self.fileName.toRight(fileName.split("filename=\"")[1][:-1]
                                                          .encode("latin1").decode("utf-8"))
                                waziLog.log("debug", f"({self.name}.{fuName}) 处理完成： {fileName}")
                            waziLog.log("debug", f"({self.name}.{fuName}) 正在写入文件。")
                            with open(os.path.join(params["path"], self.fileName.toRight(title),
                                                   i["type"] + "_" + self.fileName.toRight(fileName)), "wb") as f:
                                f.write(temp.data)
                            waziLog.log("info", f"({self.name}.{fuName}) 写入完成，下载文件路径已返回。")
                            return os.path.join(params["path"], self.fileName.toRight(title), i["type"] + "_"
                                                + self.fileName.toRight(fileName))
        waziLog.log("debug", f"({self.name}.{fuName}) 全尺寸下载。")
        for i in links:
            if not i == "None / 无":
                waziLog.log("debug", f"({self.name}.{fuName}) 分辨率： {i['type']} 存在下载地址。")
                waziLog.log("debug", f"({self.name}.{fuName}) 正在处理请求参数。")
                requestParams = self.request.handleParams(tempParams, "get", i["link"], self.headers, self.proxies)
                waziLog.log("debug", f"({self.name}.{fuName}) 请求参数处理完毕： {requestParams}， 准备请求下载。")
                try:
                    temp = self.request.do(requestParams)
                except:
                    waziLog.log("error", f"({self.name}.{fuName}) 无法请求下载。")
                else:
                    try:
                        fileName = self.fileName.toRight(temp.headers["Content-Disposition"])
                    except:
                        waziLog.log("debug", f"({self.name}.{fuName}) 从 header 中获取失败，创建新文件名。")
                        fileName = self.fileName.toRight(i["type"] + "_" + title + ".zip")
                        waziLog.log("debug", f"({self.name}.{fuName}) 创建完成： {fileName}")
                    else:
                        fileName = \
                            self.fileName.toRight(fileName.split("filename=\"")[1][:-1]
                                                  .encode("latin1").decode("utf-8"))
                        waziLog.log("debug", f"({self.name}.{fuName}) 处理完成： {fileName}")
                    waziLog.log("debug", f"({self.name}.{fuName}) 正在追加文件路径。")
                    files.append(os.path.join(params["path"], self.fileName.toRight(title),
                                              i["type"] + "_" + self.fileName.toRight(fileName)))
                    waziLog.log("debug", f"({self.name}.{fuName}) 追加完成，正在写入文件。")
                    with open(os.path.join(params["path"], self.fileName.toRight(title), i["type"] + "_"
                                           + self.fileName.toRight(fileName)), "wb") as f:
                        f.write(temp.data)
                    waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 下载文件路径： {files}")
        return files

    def downloadFile(self, url, orgName, path):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，文件名和路径，正在准备下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 文件名： {orgName}， 路径： {path}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取路径是否存在。")
        isExists = os.path.exists(path)
        waziLog.log("debug", f"({self.name}.{fuName}) 路径是否存在： {isExists}")
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到路径不存在，准备创建。")
            try:
                os.makedirs(path)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 创建失败。")
                return False
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 成功创建，继续执行。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在合成请求参数。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 合成完毕： {tempParams}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在处理请求参数。")
        requestParams = self.request.handleParams(tempParams, "get", url, self.headers, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 处理完毕，正在修正文件名。")
        fileName = os.path.join(path, self.fileName.toRight(orgName))
        waziLog.log("debug", f"({self.name}.{fuName}) 文件名修正完成： {fileName}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在请求： {url}")
        with open(fileName, "wb") as f:
            try:
                temp = self.request.do(requestParams)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 该文件无法下载！")
                return False
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在将数据写入。")
                f.write(temp.data)
                waziLog.log("debug", f"({self.name}.{fuName}) 数据写入完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 文件： {fileName}， 完成。")
        return True
