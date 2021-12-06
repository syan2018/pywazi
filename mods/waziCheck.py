import hmac
import time
import hashlib
from mods import waziFun
from ins.waziInsLog import waziLog

class waziCheck:
    # Separate checksum and crypto system for ExHentai search and PicAcg encryption and decryption processing.
    # 单独的校验和密码系统，针对 ExHentai 的搜索和 PicAcg 的加解密处理。
    def __init__(self):
        super(waziCheck, self).__init__()
        self.sha1 = hashlib.sha1()
        # These are ExHentai's tags.
        # 这些是 ExHentai 的标签。
        self.tags = [
            "Doujinshi",
            "Manga",
            "Artist CG",
            "Game CG",
            "Western",
            "Non-H",
            "Image Set",
            "Cosplay",
            "Asian Porn",
            "Misc"
        ]
        # These are the corresponding scores for the ExHentai tag.
        # You can see the values corresponding to all tags in table.itc of ExHentai.
        #
        # 这些是 ExHentai 标签的对应分数。
        # 在 ExHentai 的 table.itc 中可以看到所有标签对应的数值。
        self.tagsNumber = {
            "Doujinshi": 2,
            "Manga": 4,
            "Artist CG": 8,
            "Game CG": 16,
            "Western": 512,
            "Non-H": 256,
            "Image Set": 32,
            "Cosplay": 64,
            "Asian Porn": 128,
            "Misc": 1
        }
        # I've listed all the possible scoring displacement codes that can occur.
        # 我将所有可能出现的评分位移代码列举出来了。
        self.ratingPos = {
            "-80px -1px": 0,
            "-80px -21px": 0,
            "-64px -21px": 0.5,
            "-64px -1px": 1,
            "-48px -21px": 1.5,
            "-48px -1px": 2,
            "-32px -21px": 2.5,
            "-32px -1px": 3,
            "-16px -21px": 3.5,
            "-16px -1px": 4,
            "0px -21px": 4.5,
            "0px -1px": 5
        }
        self.name = self.__class__.__name__

    def returnHasTorrents(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息，正在分析。")
        try:
            torrentsImg = soup.attrs["src"]
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 并没有查找到任何 src 数据，返回 False。")
            return False
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 查找到 src 数据，进行分析。")
            # My idea is to compare whether the download icon address matches the download icon address of the existing
            # seed gallery Although it is more intuitive to use the title parameter for comparison But I think the URL
            # is a little more current and perhaps more reliable.
            #
            # 我的思路是对比下载图标地址是否与存在种子画廊的下载图标地址是否一致
            # 尽管使用 title 参数进行对比更加直观
            # 但我认为 URL 的资源时效性更高一点，或许更加可靠。
            if torrentsImg == "https://exhentai.org/img/t.png":
                hasTorrents = True
                waziLog.log("info", f"({self.name}.{fuName}) 检测到下载图标一致，存在种子，返回 True。")
            else:
                waziLog.log("info", f"({self.name}.{fuName}) 检测到下载图标不一致，存在不种子，返回 False。")
                hasTorrents = False
        return hasTorrents

    def returnRatingNum(self, pos):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到位移信息，正在分析： {pos}")
        if pos in self.ratingPos:
            waziLog.log("info", f"({self.name}.{fuName}) 成功获取位移对应评分： {self.ratingPos[pos]}。")
            return self.ratingPos[pos]
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取位移对应评分。")
            return "I can't get it, check your codes. / 我无法获取该评分，检查你的代码。"

    def getFileSHA1(self, path):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到路径信息，正在完成 SHA1 计算： {path}")
        self.sha1 = hashlib.sha1()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试打开文件： {path}。")
        try:
            temp = open(path, "rb")
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 文件无法打开，返回空字符串。")
            return ""
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 成功打开文件，正在计算 SHA1。")
            while True:
                temp2 = temp.read(128000)
                self.sha1.update(temp2)
                if not temp2:
                    break
            temp.close()
            waziLog.log("info", f"({self.name}.{fuName}) 成功获取 SHA1 值： {self.sha1.hexdigest()}")
        return self.sha1.hexdigest()

    def getSources(self, params):
        # You can see the values corresponding to all tags in table.itc of ExHentai,
        # and the calculation method in ehg_index.c.js.
        # 在 ExHentai 的 table.itc 中可以看到所有标签对应的数值，
        # 在 ehg_index.c.js 中可以看到计算方法。
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在完成计算： {params}")
        giveTags = [item for item in self.tags if item not in set(params["cats"])]
        waziLog.log("info", f"({self.name}.{fuName}) 应当计算的标签是： {giveTags}")
        if len(giveTags) == 0:
            sources = 0
        else:
            calc = 0
            for i in giveTags:
                calc = calc | int(self.tagsNumber[i])
            sources = calc
        waziLog.log("info", f"({self.name}.{fuName}) 完成计算，数值是： {sources}")
        return sources

    def signature(self, url, times, method, baseURL, uuids, apiKey, secretKey):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在计算签名。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 时间： {times}， 方法： {method}， 基准 URL： {baseURL}，"
                             f" UUID： {uuids}， API 访问密钥： {apiKey}， 密钥： {secretKey}")
        raw = url.replace(baseURL, "") + str(times) + uuids + method + apiKey
        raw = raw.lower()
        hc = hmac.new(secretKey.encode(), digestmod = hashlib.sha256)
        hc.update(raw.encode())
        waziLog.log("info", f"({self.name}.{fuName}) 完成计算： {hc.hexdigest()}")
        return hc.hexdigest()

    def construct(self, url, method, baseURL, uuids, apiKey, secretKey):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在计算签名和时间。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 方法： {method}， 基准 URL： {baseURL}，"
                             f" UUID： {uuids}， API 访问密钥： {apiKey}， 密钥： {secretKey}")
        times = int(time.time())
        waziLog.log("info", f"({self.name}.{fuName}) 已获取本地时间： {times}")
        sig = waziCheck.signature(self, url, times, method, baseURL, uuids, apiKey, secretKey)
        waziLog.log("info", f"({self.name}.{fuName}) 完成签名，时间： {times}， 签名： {sig}")
        return [sig, times]

    def needFilterIt(self, backJson, filters):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到需要过滤的数据和过滤标签。")
        waziLog.log("debug", f"({self.name}.{fuName}) 需要过滤的数据： {backJson}， 过滤标签： {filters}")
        returnDocs = []
        waziLog.log("debug", f"({self.name}.{fuName}) 进入数据遍历。")
        for i in backJson:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在处理数据： {i}")
            if len(list(set(i["categories"]) & set(filters))) == 0:
                waziLog.log("debug", f"({self.name}.{fuName}) 该数据可以通过，正在写入。")
                returnDocs.append(i)
                waziLog.log("debug", f"({self.name}.{fuName}) 该数据写入完成。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 该数据无法通过，拒绝写入。")
        waziLog.log("info", f"({self.name}.{fuName}) 写入数据如下： {returnDocs}")
        return returnDocs
