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
    
    def parseImagesAndVideos(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 提取页面中所有画廊信息。")
        galleries = soup.find_all("div", class_ = "itemBox")
        waziLog.log("debug", f"({self.name}.{fuName}) 画廊提取完成，正在进行解析。")
        galleriesBox = []
        videosBox = []
        for i in galleries:
            gallery = {}
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取浏览数量。")
            gallery["views"] = int(i.find("div", class_ = "viewCountBox").text)
            waziLog.log("debug", f"({self.name}.{fuName}) 浏览数量为： {gallery['views']}。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊链接。")
            gallery["link"] = "https://asiansister.com/" + i.find("a")["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 画廊链接为： {gallery['link']}。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该画廊是否需要 VIP。")
            if i.find("img", class_ = "vip_cover"):
                waziLog.log("debug", f"({self.name}.{fuName}) 该画廊需要 VIP 权限。")
                gallery["vip"] = True
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 该画廊不需要 VIP 权限。")
                gallery["vip"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面。")
            gallery["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 画廊封面为： {gallery['cover']}。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面的顶替字符串。")
            gallery["alt"] = i.find("img", class_ = "lazyload").attrs["alt"]
            waziLog.log("debug", f"({self.name}.{fuName}) 画廊封面的顶替字符串为： {gallery['alt']}。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊标题。")
            gallery["title"] = i.find("div", class_ = "titleName").text.strip()
            waziLog.log("debug", f"({self.name}.{fuName}) 画廊标题为： {gallery['title']}。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到画廊列表。")
            galleriesBox.append(gallery)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 提取页面中所有视频信息。")
        videos = soup.find_all("div", class_ = "itemBox_video")
        for i in videos:
            video = {}
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频是否存在 data 标签。")
            if i.attrs["data"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 视频存在 data 标签。")
                video["data"] = i.attrs["data"]
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 视频不存在 data 标签。")
                video["data"] = None
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频播放量。")
            video["views"] = int(i.find("div", class_ = "viewCountBox").text)
            waziLog.log("debug", f"({self.name}.{fuName}) 视频播放量为： {video['views']}。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频链接。")
            video["link"] = "https://asiansister.com/" + i.find("a")["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 视频链接为： {video['link']}。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该视频是否需要 VIP。")
            if i.find("img", class_ = "vip_cover"):
                waziLog.log("debug", f"({self.name}.{fuName}) 该视频需要 VIP 权限。")
                video["vip"] = True
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 该视频不需要 VIP 权限。")
                video["vip"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频封面。")
            if i.find("img", class_ = "lazyload").attrs["data-src"].startswith("http"):
                video["cover"] = i.find("img", class_ = "lazyload").attrs["data-src"]
            else:
                video["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 视频封面为： {video['cover']}。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频标题。")
            video["title"] = i.find("div", class_ = "titleName_video").text.strip()
            waziLog.log("debug", f"({self.name}.{fuName}) 视频标题为： {video['title']}。")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到视频列表。")
            videosBox.append(video)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 提取页面中所有信息完成，图像信息： {galleriesBox}, 视频信息： {videosBox}。")
        return galleriesBox, videosBox

    def getPage(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在生成 URL： {page}。")
        url = "https://asiansister.com/_page" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        return waziAsianSister.parseImagesAndVideos(self, soup)
