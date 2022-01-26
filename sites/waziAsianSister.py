from markupsafe import re
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

    def parsePerson(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        person = {}
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取个人信息。")
        person["name"] = soup.find("center").find("h1").text
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取个人描述。")
        person["descriptionHTML"] = str(soup.find("div", {"class": "detailBox"})).replace("<br>", "\n")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取个人浏览量。")
        person["views"] = int(soup.find("div", {"class": "detailBox"}).find("div").text.split(": ")[1].split("标签")[0])
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取个人标签。")
        person["tags"] = []
        for i in soup.find("div", {"class": "detailBox"}).find("div").find("h4").find_all("a"):
            if i.attrs["href"] == "tag.php?tag=":
                pass
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 个人标签： {i.text}。")
                person["tags"].append({"name": i.text, "link": i.attrs["href"]})
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取相关推荐。")
        person["galleries"] = waziAsianSister.parseRecommendImagesAndVideos(self, soup)[0]
        person["videos"] = waziAsianSister.parseRecommendImagesAndVideos(self, soup)[1]
        waziLog.log("info", f"({self.name}.{fuName}) 解析完成，个人信息返回中。")
        return person
    
    def parseRecommendImagesAndVideos(self, soup):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取推荐画廊和视频。")
        recommendGalleries = []
        recommendVideos = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取推荐画廊。")
        for i in soup.find_all("div", {"class": "recommentBox"}):
            gallery = {}
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊地址。")
            gallery["link"] = i.find("a").attrs["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面。")
            gallery["cover"] = i.find("img", {"class": "lazyload"}).attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面缺省字符串。")
            gallery["alt"] = i.find("img", {"class": "lazyload"}).attrs["alt"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊标题。")
            gallery["title"] = i.find("a").attrs["title"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊星级。")
            gallery["stars"] = len(i.find_all("img", {"class": "recommentStar"}))
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该画廊是否需要 VIP。")
            if i.find("img", {"class": "rec_vip_cover"}):
                gallery["VIP"] = True
            else:
                gallery["VIP"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到画廊列表。")
            recommendGalleries.append(gallery)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取推荐视频。")
        for i in soup.find_all("div", {"class": "recommentBoxVideo"}):
            video = {}
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频是否存在 data 标签。")
            if i.attrs["data"]:
                video["data"] = i.attrs["data"]
            else:
                video["data"] = ""
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频地址。")
            video["link"] = i.find("a").attrs["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频标题。")
            video["title"] = i.find("a").attrs["title"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频封面。")
            if i.find("img", class_ = "lazyload").attrs["data-src"].startswith("http"):
                video["cover"] = i.find("img", class_ = "lazyload").attrs["data-src"]
            else:
                video["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该视频是否需要 VIP。")
            if i.find("img", {"class": "rec_vip_cover"}):
                video["VIP"] = True
            else:
                video["VIP"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到视频列表。")
            recommendVideos.append(video)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 提取页面中所有信息完成，图像信息： {recommendGalleries}, 视频信息： {recommendVideos}。")
        return recommendGalleries, recommendVideos

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
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊链接。")
            gallery["link"] = "https://asiansister.com/" + i.find("a")["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该画廊是否需要 VIP。")
            if i.find("img", class_ = "vip_cover"):
                gallery["vip"] = True
            else:
                gallery["vip"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面。")
            gallery["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面的顶替字符串。")
            gallery["alt"] = i.find("img", class_ = "lazyload").attrs["alt"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊标题。")
            gallery["title"] = i.find("div", class_ = "titleName").text.strip()
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到画廊列表。")
            galleriesBox.append(gallery)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 提取页面中所有视频信息。")
        videos = soup.find_all("div", class_ = "itemBox_video")
        for i in videos:
            video = {}
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频是否存在 data 标签。")
            if i.attrs["data"]:
                video["data"] = i.attrs["data"]
            else:
                video["data"] = None
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频播放量。")
            video["views"] = int(i.find("div", class_ = "viewCountBox").text)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频链接。")
            video["link"] = "https://asiansister.com/" + i.find("a")["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该视频是否需要 VIP。")
            if i.find("img", class_ = "vip_cover"):
                video["vip"] = True
            else:
                video["vip"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频封面。")
            if i.find("img", class_ = "lazyload").attrs["data-src"].startswith("http"):
                video["cover"] = i.find("img", class_ = "lazyload").attrs["data-src"]
            else:
                video["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频标题。")
            video["title"] = i.find("div", class_ = "titleName_video").text.strip()
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到视频列表。")
            videosBox.append(video)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 提取页面中所有信息完成，图像信息： {galleriesBox}, 视频信息： {videosBox}。")
        return galleriesBox, videosBox

    def getPage(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在生成 URL： {page}。")
        url = "https://asiansister.com/_page" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        return waziAsianSister.parseImagesAndVideos(self, soup)

    def search(self, keyword, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到关键字和页码，正在生成 URL： {keyword}， {page}。")
        url = "https://asiansister.com/search.php?q=" + keyword + "&page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        return waziAsianSister.parseImagesAndVideos(self, soup)

    def tagSearch(self, tag, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到标签和页码，正在生成 URL： {tag}， {page}。")
        url = "https://asiansister.com/tag.php?tag=" + tag + "&page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        return waziAsianSister.parseImagesAndVideos(self, soup)

    def customParse(self, content, type):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到补充 URL 和类型，正在生成 URL： {content}， {type}。")
        url = "https://asiansister.com/" + content
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        if type == "main":
            waziLog.log("debug", f"({self.name}.{fuName}) 解析主页，已提交至 parseImagesAndVideos。")
            return waziAsianSister.parseImagesAndVideos(self, soup)
        elif type == "person":
            waziLog.log("debug", f"({self.name}.{fuName}) 解析角色主页，已提交至 parsePerson。")
            return waziAsianSister.parsePerson(self, soup)
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 无法识别的类型，已返回空列表。")
            return []
