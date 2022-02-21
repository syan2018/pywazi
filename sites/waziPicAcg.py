"""
sites/waziPicAcg.py

class: waziPicAcg
"""

import os
import json
import uuid
import base64
from mods import waziFun
from ins.waziInsLog import waziLog
from mods.waziCheck import waziCheck
from mods.waziRequest import waziRequest
from mods.waziFileName import waziFileName

class waziPicAcg:
    """
    waziPicAcg
    *Hardcore Game.*

    A class for crawling the PicAcg.

    Attributes:
        imageQuality: list
            The quality of the image.
            ["original", "low", "medium", "high"]
        
        name: str
            The name of the class.
        
        headers: dict
            The headers of the request.
            Will be modified in the class.
        
        info: dict
            A dict of the information of the request.
            Save request's secret key, api key, base url, uuid.
            Will be modified in the class.
        
        params: dict
            A dict of user params for requests. User can set the params in config.json.
        
        proxies: dict
            The proxy for the request.
            Default: {'proxyAddress': '127.0.0.1', 'proxyPort': '7890'}
        
        token: str
            The token for the request.
            The user's token will be filled in the login method.
        
        urls: dict
            The urls for the request.
        
        request: waziRequest
            A waziRequest object.
        
        check: waziCheck
            A waziCheck object.
        
        fileName: waziFileName
            A waziFileName object.
        
    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziPicAcg.__init__(self)
        *su be te mi se ta i.*

        Initialize the class.

        Parameters:
            None
        
        Actions:
            + Set the headers: waziPicAcg.editHeaders(self)
        """
        super(waziPicAcg, self).__init__()
        self.imageQuality = ["original", "low", "medium", "high"]
        self.name = self.__class__.__name__
        self.headers = {
            "api-key": "",
            "accept": "application/vnd.picacomic.com.v1+json",
            "app-channel": "3",
            "time": "0",
            "nonce": "",
            "signature": "0",
            "app-version": "2.2.1.3.3.4",
            "app-uuid": "418e56fb-60fb-352b-8fca-c6e8f0737ce6",
            "app-platform": "android",
            "Content-Type": "application/json; charset=UTF-8",
            "User-Agent": "okhttp/3.8.1",
            "app-build-version": "45",
            "image-quality": "original"
        }
        self.info = {
            "secretKey": "~d}$Q7$eIni=V)9\\RK/P.RM4;9[7|@/CA}b~OW!3?EV`:<>M7pddUBL5n|0/*Cn",
            "baseUrl": "https://picaapi.picacomic.com/",
            "uuid": "",
            "apiKey": "C69BAF41DA5ABD1FFEDC6D2FEA56B"
        }
        self.params = {}
        self.proxies = {
            "proxyAddress": "127.0.0.1",
            "proxyPort": "7890"
        }
        self.token = ""
        self.urls = {
            "login": "https://picaapi.picacomic.com/auth/sign-in",
            "register": "https://picaapi.picacomic.com/auth/register",
            "categories": "https://picaapi.picacomic.com/categories",
            "search": "https://picaapi.picacomic.com/comics/search",
            "comics": "https://picaapi.picacomic.com/comics",
            "comicId": "https://picaapi.picacomic.com/comics/{comicId}",
            "comicEps": "https://picaapi.picacomic.com/comics/{comicId}/eps",
            "comicPages": "https://picaapi.picacomic.com/comics/{comicId}/order/{order}/pages",
            "comicRecommend": "https://picaapi.picacomic.com/comics/{comicId}/recommendation",
            "keywords": "https://picaapi.picacomic.com/keywords",
            "myComments": "https://picaapi.picacomic.com/users/my-comments",
            "myFavourites": "https://picaapi.picacomic.com/users/favourite",
            "profile": "https://picaapi.picacomic.com/users/profile",
            "games": "https://picaapi.picacomic.com/games",
            "comicFavourite": "https://picaapi.picacomic.com/comics/{comicId}/favourite",
            "comicLike": "https://picaapi.picacomic.com/comics/{comicId}/like",
            "comicComments": "https://picaapi.picacomic.com/comics/{comicId}/comments",
            "advSearch": "https://picaapi.picacomic.com/comics/advanced-search",
            "punchIn": "https://picaapi.picacomic.com/users/punch-in",
            "gameLike": "https://picaapi.picacomic.com/games/{gameId}/like",
            "gameComments": "https://picaapi.picacomic.com/games/{gameId}/comments",
            "avatar": "https://picaapi.picacomic.com/users/avatar",
            "userTitle": "https://picaapi.picacomic.com/users/{userId}/title",
            "forgotPassword": "https://picaapi.picacomic.com/auth/forgot-password",
            "resetPassword": "https://picaapi.picacomic.com/auth/reset-password",
            "adjustExp": "https://picaapi.picacomic.com/utils/adjust-exp",
            "password": "https://picaapi.picacomic.com/users/password",
            "updateId": "https://picaapi.picacomic.com/users/update-id",
            "updateQA": "https://picaapi.picacomic.com/users/update-qa",
            "removeComment": "https://picaapi.picacomic.com/utils/remove-comment",
            "leaderBoard": "https://picaapi.picacomic.com/comics/leaderboard",
            "knight": "https://picaapi.picacomic.com/comics/knight-leaderboard",
            "randomComic": "https://picaapi.picacomic.com/comics/random",
            "collections": "https://picaapi.picacomic.com/collections",
            "banners": "https://picaapi.picacomic.com/banners",
            "init": "http://68.183.234.72/init",
            "initAndroid": "https://picaapi.picacomic.com/init?platform=android",
            "commentsChildren": "https://picaapi.picacomic.com/comments/{commentId}/childrens?page={page}",
            "replyComment": "https://picaapi.picacomic.com/comments/{commentId}",
            "chat": "https://picaapi.picacomic.com/chat",
            "apps": "https://picaapi.picacomic.com/pica-apps",
            "androidAPPs": "https://picaapi.picacomic.com/applications?platform=android&page={page}",
            "blockUser": "https://picaapi.picacomic.com/utils/block-user",
            "notifications": "https://picaapi.picacomic.com/users/notifications?page={page}",
            "announcements": "https://picaapi.picacomic.com/announcements?page={page}",
            "dirty": "https://picaapi.picacomic.com/users/{userId}/dirty",
            "userProfile": "https://picaapi.picacomic.com/users/{userId}/profile",
            "commentLike": "https://picaapi.picacomic.com/comments/{commentId}/like",
            "commentHide": "https://picaapi.picacomic.com/comments/{commentId}/hide",
            "commentReport": "https://picaapi.picacomic.com/comments/{commentId}/report",
            "commentTop": "https://picaapi.picacomic.com/comments/{commentId}/top"
        }
        self.request = waziRequest()
        self.check = waziCheck()
        self.fileName = waziFileName()
        waziLog.log("debug", f"({self.name}.__init__) 正在初始化 Headers。")
        self.editHeaders()

    def giveParams(self, params):
        """
        waziPicAcg.giveParams(self, params)
        *Oops!*

        Give params to this class. Controled by user.
        Proxy and headers are controlled by self.params.

        Parameters:
            params: dict
                A dict of params, user given.
        
        Return:
            None
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到配置信息，正在写入。")
        self.params = params
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.params}")
        return self.params

    def editHeaders(self):
        """
        waziPicAcg.editHeaders(self)
        *Into the Vault!*

        Edit headers.
        Generate a new uuid, and fill in the headers with other params.
        Called in __init__.

        Parameters:
            None
        
        Return:
            None
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 接到 __init__ 指令，正在创建 headers。")
        self.info["uuid"] = str(uuid.uuid4()).replace("-", "")
        self.headers["nonce"] = self.info["uuid"]
        self.headers["api-key"] = self.info["apiKey"]
        waziLog.log("debug", f"({self.name}.{fuName}) 创建完成，header 已写入： {self.headers}")

    def sign(self, url, method):
        """
        waziPicAcg.sign(self, url, method)
        *Keep it secret, keep it safe!*

        Signature request.
        Use self.check.construct to construct the request headers.

        Parameters:
            url: str
                The url of request.
            
            method: str
                The method of request.
        
        Return:
            None
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和请求方式，正在签名。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 请求方式： {method}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 construct 获取签名。")
        sig = self.check.construct(url, method, self.info["baseUrl"], self.info["uuid"], self.info["apiKey"],
                                   self.info["secretKey"])
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {sig}，正在写入。")
        self.headers["signature"] = sig[0]
        self.headers["time"] = str(sig[1])
        waziLog.log("debug", f"({self.name}.{fuName}) 写入完成： {self.headers}")

    def up(self, url, needAuth, data, method, jsonNeed):
        """
        waziPicAcg.up(self, url, needAuth, data, method, jsonNeed)
        *Eee.*

        Send a request.

        Parameters:
            url: str
                The url of request.
            
            needAuth: bool
                Whether need auth.
            
            data: object
                The data of request.
            
            method: str
                The method of request.
            
            jsonNeed: bool
                Whether need return json.
        
        Return:
            jsonNeed: True
                Type: list or dict Object.
            
            jsonNeed: False
                Type: urllib3.response.HTTPResponse
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，是否验证信息，数据，请求方式和是否返回 JSON 信息，正在请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 是否验证信息： {needAuth}， 数据： {data}")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求方式： {method}， 是否返回 JSON 信息： {jsonNeed}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改用户配置。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 修改完成，正在通过 sign 签名。")
        waziPicAcg.sign(self, url, method)
        waziLog.log("debug", f"({self.name}.{fuName}) 签名完成。")
        if needAuth:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要验证用户信息，authorization 写入 {self.token}")
            self.headers["authorization"] = self.token
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不需要验证用户信息，authorization 为空。")
            self.headers["authorization"] = ""
        waziLog.log("debug", f"({self.name}.{fuName}) 递交至 normalUP 处理。")
        return waziPicAcg.normalUP(self, tempParams, url, data, method, jsonNeed)

    def justUP(self, url, data, method, jsonNeed):
        """
        waziPicAcg.justUP(self, url, data, method, jsonNeed)
        *Wanna be the first one?*

        Send a request without sign and auth.

        Parameters:
            url: str
                The url of request.
            
            data: object
                The data of request.
            
            method: str
                The method of request.
            
            jsonNeed: bool
                Whether need return json.
        
        Return:
            jsonNeed: True
                Type: list or dict Object.
            
            jsonNeed: False
                Type: urllib3.response.HTTPResponse
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，数据，请求方式和是否返回 JSON 信息，正在请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 数据： {data}， 请求方式： {method}")
        waziLog.log("debug", f"({self.name}.{fuName}) 是否返回 JSON 信息： {jsonNeed}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改用户参数。")
        tempParams = self.params
        tempParams["useHeaders"] = False
        waziLog.log("debug", f"({self.name}.{fuName}) 修改完成： {tempParams}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交至 normalUP 处理。")
        return waziPicAcg.normalUP(self, tempParams, url, data, method, jsonNeed)

    def normalUP(self, tempParams, url, data, method, jsonNeed):
        """
        waziPicAcg.normalUP(self, tempParams, url, data, method, jsonNeed)
        *Night.*

        Re-abstraction of the request method.
        The base request method in this class.

        Parameters:
            tempParams: dict
                The params of request. User-defined.
            
            url: str
                The url of request.
            
            data: object
                The data of request.
            
            method: str
                The method of request.
            
            jsonNeed: bool
                Whether need return json.
        
        Return:
            jsonNeed: True
                Type: list or dict Object.
            
            jsonNeed: False
                Type: urllib3.response.HTTPResponse
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数，URL，数据，请求方式和是否返回 JSON 信息，正在请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户参数： {tempParams}， URL： {url}， 数据： {data}")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求方式： {method}， 是否返回 JSON 信息： {jsonNeed}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 mods.waziRequest.handleParams 处理用户参数。")
        requestParams = self.request.handleParams(tempParams, method.lower(), url, self.headers, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 处理完成： {requestParams}")
        if method.lower() != "get":
            waziLog.log("debug", f"({self.name}.{fuName}) 非 get 请求，正在检查数据。")
            if data is None:
                waziLog.log("debug", f"({self.name}.{fuName}) 数据为空，写入空字典。")
                requestParams["data"] = json.dumps({}).encode()
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 数据不为空，写入数据。")
                requestParams["data"] = json.dumps(data).encode()
        if jsonNeed:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在请求并 JSON 格式化结果。")
            jsons = json.loads(self.request.do(requestParams).data.decode("utf-8"))
            waziLog.log("info", f"({self.name}.{fuName}) 格式化完成： {jsons}， 数据返回。")
            return jsons
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 请求完成后，数据自动返回。")
            return self.request.do(requestParams)

    def login(self, username, password):
        """
        waziPicAcg.login(self, username, password)
        *Pepper Salt.*

        Login in the account.
        If success, will use your token to request.
        So you have to use this method once to get your token before any authorization request is needed.

        Parameters:
            username: str
                The username of account.
            
            password: str
                The password of account.
        
        Return:
            Type: str
            The token of account.
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Logs:
                Error:
                    + Login failed.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户名和密码，正在发起登录请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户名： {username}， 密码： {password}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "email": username,
            "password": password
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试请求。")
        try:
            self.token = waziPicAcg.up(self, self.urls["login"], False, body, "POST", True)["data"]["token"]
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 错误，无法获取账号。")
            return "Account not available. / 无法获取账号。"
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 已获取 token： {self.token}")
            return self.token

    def getCategories(self):
        """
        waziPicAcg.getCategories(self)
        *Fear.*

        Get all categories.

        Parameters:
            None
        
        Return:
            Type: dict
            The categories.
            May like (Some categories may not have these information):
            {
                "code": int,                            # The status code of request.
                "message": str,                         # The message of request.
                "data": {                               # The data of request.
                    "categories": [{                    # The categories.
                        "title": str,                   # The title of category.
                        "thumb": {                      # The thumbnail of category.
                            "originalName": str,        # The original name of thumb.
                            "path": str,                # The path of thumb.
                            "fileServer": str           # The file server of thumb.
                        },
                        "isWeb": bool,                  # Whether the category is web.
                        "active": bool,                 # Whether the category is active.
                        "link": str,                    # The link of category.
                        "_id": str,                     # The id of category.
                        "description": str,             # The description of category.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["categories"], True, None, "GET", True)

    def getComics(self, page, c, t, s):
        """
        ?Why cannot get comics?
        waziPicAcg.getComics(self, page, c, t, s)
        *Go listen to VOY@GER.*

        Get comics with page, category, tag and sort.

        Parameters:
            page: int or str
                The page of comics. Start from 1.
            
            c: str
                Category of comics. Can be string from getCategories.
            
            t: str
                Tag of comics. Please use traditional Chinese.
            
            s: str
                Sorting of comics.
                    ua: Default.
                    dd: From newest to oldest.
                    da: From oldest to newest.
                    vd: From users named most to users named least. (What is that? Hot?)
                    ld: From users liked most to users liked least.
        
        Return:
            Type: dict
            The comics.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码、分区、标签和排序，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 分区： {c}， 标签： {t}， 排序： {s}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comics"] + "?page=" + str(page) + "&c=" + c
        newUrl += "&t=" + t + "&s=" + s
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def search(self, page, keyword):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和关键词，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 关键词： {keyword}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["search"] + "?page=" + str(page) + "&q=" + keyword
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getComic(self, comicId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicId"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getComicEps(self, comicId, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和分 P 数据，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 分 P 数据： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicEps"].replace("{comicId}", comicId) + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def advancedSearch(self, categories, keyword, sort, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到分类、关键词、排序和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 分类： {categories}， 关键词： {keyword}， 排序： {sort}， "
                             f"页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["advSearch"] + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "categories": categories,
            "keyword": keyword,
            "sort": sort
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, body, "POST", True)

    def getComicPages(self, comicId, eps, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID、分 P 数据和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 分 P 数据： {eps}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicPages"].replace("{comicId}", comicId).replace("{order}", eps) + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getComicRecommend(self, comicId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicRecommend"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getKeywords(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["keywords"], True, None, "GET", True)

    def getMyComments(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["myComments"] + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getMyFavourites(self, page, s):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和排序，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 排序： {s}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["myFavourites"] + "?page=" + str(page) + "&s=" + s
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getMyProfile(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["profile"], True, None, "GET", True)

    def getGames(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["games"] + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getGameInfo(self, gameId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到游戏 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 游戏 ID： {gameId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["games"] + "/" + str(gameId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def likeOrUnLikeGame(self, gameId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到游戏 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 游戏 ID： {gameId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["gameLike"].replace("{gameId}", gameId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def favOrUnFavComic(self, comicId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicFavourite"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def likeOrUnLikeComic(self, comicId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicLike"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def likeOrUnLikeComment(self, commentId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentLike"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def hideOrUnHideComment(self, commentId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentHide"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def getCommentsChildren(self, commentId, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID 和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentsChildren"].replace("{commentId}", commentId).replace("{page}", str(page))
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def replyComment(self, commentId, content):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID 和内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}， 内容： {content}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["replyComment"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "content": content
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, body, "POST", True)

    def reportComment(self, commentId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentReport"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def topOrUnTopComment(self, commentId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentTop"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def getGameComments(self, gameId, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到游戏 ID 和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 游戏 ID： {gameId}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["gameComments"].replace("{gameId}", gameId) + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def postGameComment(self, gameId, content):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到游戏 ID 和内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 游戏 ID： {gameId}， 内容： {content}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["gameComments"].replace("{gameId}", gameId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "content": content
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, body, "POST", True)

    def getComicComments(self, comicId, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicComments"].replace("{comicId}", comicId) + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def postComicComment(self, comicId, content):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 内容： {content}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicComments"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "content": content
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, body, "POST", True)

    def getSinglePage(self, fileServer, path):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到头部（文件地址）和尾部（文件名），正在组合。")
        url = fileServer + "/static/" + path
        waziLog.log("info", f"({self.name}.{fuName}) 组合完成： {url}")
        return url

    def punchIn(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["punchIn"], True, None, "POST", True)

    def register(self, loginName, password, birthday, gender, displayName, qa):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到登录名、密码、生日、性别、昵称和问答信息，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 登录名： {loginName}， 密码： {password}， 生日： {birthday}")
        waziLog.log("debug", f"({self.name}.{fuName}) 性别： {gender}， 昵称： {displayName}， 问答信息： {qa}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合数据。")
        data = {
            "email": loginName,
            "password": password,
            "birthday": birthday,
            "gender": gender,
            "name": displayName,
            "answer1": qa[0]["answer"],
            "answer2": qa[1]["answer"],
            "answer3": qa[2]["answer"],
            "question1": qa[0]["question"],
            "question2": qa[1]["question"],
            "question3": qa[2]["question"]
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["register"], False, data, "POST", True)

    def uploadAvatar(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 参数： {params}")
        if params["type"] == "base64":
            waziLog.log("debug", f"({self.name}.{fuName}) 用户给出 base64 信息，正在写入。")
            upload = "data:image/" + params["format"] + ";base64," + params["data"]
            waziLog.log("debug", f"({self.name}.{fuName}) 写入完成： {upload}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 用户给出文件路径，正在获取文件扩展名。")
            fileFormat = os.path.splitext(params["path"])[-1][1:]
            if fileFormat == "jpg":
                waziLog.log("debug", f"({self.name}.{fuName}) 自动修正 jpg 为 jpeg")
                fileFormat = "jpeg"
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {fileFormat}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取文件 base64。")
            with open(params["path"], "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在写入。")
            upload = "data:image/" + fileFormat + ";base64," + data
            waziLog.log("debug", f"({self.name}.{fuName}) 写入完成： {upload}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合数据。")
        data = {
            "avatar": upload
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["avatar"], True, data, "PUT", True)

    def setTitle(self, userId, title):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID 和头衔内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}， 头衔内容： {title}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["userTitle"].replace("{userId}", userId)
        waziLog.log("debug", f"({self.name}.{fuName}) 创建完成： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "title": title
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, data, "PUT", True)

    def resetPassword(self, loginName, questionNo, answer):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到登录名，问题编号，答案，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 登录名： {loginName}， 问题编号： {questionNo}， 答案： {answer}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "email": loginName,
            "questionNo": int(questionNo),
            "answer": answer
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["resetPassword"], False, data, "POST", True)

    def forgotPassword(self, loginName):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到登录名，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 登录名： {loginName}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "email": loginName
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["forgotPassword"], False, data, "POST", True)

    def adjustExp(self, userId, exp):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID 和经验值，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}， 经验值： {exp}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "exp": int(exp),
            "userId": userId
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["adjustExp"], True, data, "POST", True)

    def changePassword(self, oldPassword, newPassword):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到旧密码和新密码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 旧密码： {oldPassword}， 新密码： {newPassword}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "old_password": oldPassword,
            "new_password": newPassword
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["password"], True, data, "PUT", True)

    def changeDisplayName(self, loginName, newDisplayName):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到登录名和新昵称，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 登录名： {loginName}， 新昵称： {newDisplayName}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "email": loginName,
            "name": newDisplayName
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["updateId"], True, data, "PUT", True)

    def changeSlogan(self, newSlogan):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到新签名，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 新签名： {newSlogan}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "slogan": newSlogan
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["profile"], True, data, "PUT", True)

    def changeQA(self, qa):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到新问答内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 问答： {qa}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "question1": qa[0]["q"],
            "question2": qa[1]["q"],
            "question3": qa[2]["q"],
            "answer1": qa[0]["a"],
            "answer2": qa[1]["a"],
            "answer3": qa[2]["a"]
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["updateQA"], True, data, "PUT", True)

    def removeUserComments(self, userId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "userId": userId
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["removeComment"], True, data, "POST", True)

    def getH24LeaderBoard(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["leaderBoard"] + "?tt=H24&ct=VC"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getD7LeaderBoard(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["leaderBoard"] + "?tt=D7&ct=VC"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getD30LeaderBoard(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["leaderBoard"] + "?tt=D30&ct=VC"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def knightLeaderBoard(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["knight"], True, None, "GET", True)

    def getRandomComics(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["randomComic"], True, None, "GET", True)

    def getCollections(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["collections"], True, None, "GET", True)

    def getBanners(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["banners"], True, None, "GET", True)

    def init(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.justUP(self, self.urls["init"], None, "GET", True)

    def initAndroid(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["initAndroid"], True, None, "GET", True)

    def changeImageQuality(self, number):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图片素质信息，正在写入。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图片素质信息： {number}")
        self.headers["image-quality"] = self.imageQuality[number]
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成： {self.headers['image-quality']}")

    def createFolder(self, path, title):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到创建文件夹请求，已悉知路径和标题信息，正在创建。")
        waziLog.log("debug", f"({self.name}.{fuName}) 路径： {path}， 标题信息： {title}")
        isExists = os.path.exists(os.path.join(path, self.fileName.toRight(title)))
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在该文件夹，正在创建。")
            os.makedirs(os.path.join(path, self.fileName.toRight(title)))
            waziLog.log("debug", f"({self.name}.{fuName}) 创建完成。")

    def createFolderEps(self, path, title, docTitle):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到创建子文件夹请求，已悉知路径、标题信息和分页标题信息，正在创建。")
        waziLog.log("debug", f"({self.name}.{fuName}) 路径： {path}， 标题信息： {title}， 分页标题信息： {docTitle}")
        isExists = os.path.exists(os.path.join(path, self.fileName.toRight(title), docTitle))
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在该文件夹，正在创建。")
            os.makedirs(os.path.join(path, self.fileName.toRight(title), docTitle))
            waziLog.log("debug", f"({self.name}.{fuName}) 创建完成。")

    def getThumbImageLink(self, comicId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在获取封面地址和标题。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getComic 获取漫画信息。")
        comicInfo = waziPicAcg.getComic(self, comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在获取原始文件名和文件路径及标题。")
        originalName = comicInfo["data"]["comic"]["thumb"]["originalName"]
        filePath = comicInfo["data"]["comic"]["thumb"]["path"]
        comicName = comicInfo["data"]["comic"]["title"]
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在组合 URL。")
        fileURL = "https://storage.wikawika.xyz/static/" + filePath
        waziLog.log("debug", f"({self.name}.{fuName}) URL 组合完成： {fileURL}")
        data = [originalName, comicName, fileURL]
        waziLog.log("info", f"({self.name}.{fuName}) 数据： {data}， 返回。")
        return data

    def getThumbImage(self, comicId, path):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和下载路径，正在下载封面。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 下载路径： {path}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getThumbImage 获取封面及信息。")
        thumbs = waziPicAcg.getThumbImageLink(self, comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {thumbs}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建文件夹。")
        waziPicAcg.createFolder(self, path, thumbs[1])
        waziLog.log("debug", f"({self.name}.{fuName}) 创建完成，正在发起请求。")
        temp = waziPicAcg.justUP(self, thumbs[2], None, "GET", False)
        waziLog.log("debug", f"({self.name}.{fuName}) 发起完成，正在写入。")
        filePath = os.path.join(path, self.fileName.toRight(thumbs[1]), "thumb_" + self.fileName.toRight(thumbs[0]))
        with open(filePath, "wb") as f:
            f.write(temp.data)
        waziLog.log("info", f"({self.name}.{fuName}) 已写入到： {filePath}")
        return filePath

    def getChat(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["chat"], True, None, "GET", True)

    def getAPPs(self):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["apps"], True, None, "GET", True)
    
    def getComicImageURLs(self, pageDict):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到分 P 分页字典，正在获取漫画图片地址: {pageDict}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
        urls = []
        for i in pageDict["data"]["pages"]["docs"]:
            if "fileServer" in i["media"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在 fileServer，使用返回值。")
                fileServer = i["media"]["fileServer"]
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 不存在 fileServer，已填入默认值。")
                fileServer = "https://storage1.picacomic.com"
            waziLog.log("debug", f"({self.name}.{fuName}) fileServer 为 {fileServer}")
            url = waziPicAcg.getSinglePage(self, fileServer, i["media"]["path"])
            urls.append(url)
        return urls

    def singleDownloadComicImage(self, pageDict, path, comicName, docTitle):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到分 P 分页字典，路径，漫画 ID 和分页标题，正在下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) 分 P 分页字典： {pageDict}， 路径： {path}， 漫画 ID： {comicName}， "
                             f"分页标题： {docTitle}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
        for i in pageDict["data"]["pages"]["docs"]:
            if "fileServer" in i["media"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在 fileServer，使用返回值。")
                fileServer = i["media"]["fileServer"]
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 不存在 fileServer，已填入默认值。")
                fileServer = "https://storage1.picacomic.com"
            waziLog.log("debug", f"({self.name}.{fuName}) fileServer 为 {fileServer}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
            temp = waziPicAcg.justUP(self, waziPicAcg.getSinglePage(self, fileServer, i["media"]["path"]),
                                     None, "GET", False)
            waziLog.log("debug", f"({self.name}.{fuName}) 请求发起完成，正在写入。")
            with open(os.path.join(path, self.fileName.toRight(comicName), self.fileName.toRight(docTitle),
                                   self.fileName.toRight(i["media"]["originalName"])), "wb") as f:
                f.write(temp.data)
            waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
    
    def getComicFilesList(self, comicId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getThumbImage 获取封面。")
        thumbs = waziPicAcg.getThumbImageLink(self, comicId)
        yield thumbs
        waziLog.log("debug", f"({self.name}.{fuName}) 下载完成，正在获取漫画信息。")
        comicInfo = waziPicAcg.getComic(self, comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在获取分页。")
        comicName = comicInfo["data"]["comic"]["title"]
        eps = int(comicInfo["data"]["comic"]["epsCount"])
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画吗： {comicName}， 分页数： {eps}")
        waziLog.log("debug", f"({self.name}.{fuName}) 进入 for in range。")
        for i in range(1, eps + 1):
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取分 P 内容。")
            newEps = waziPicAcg.getComicEps(self, comicId, str(i))
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进入遍历。")
            for j in newEps["data"]["eps"]["docs"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在获取分 P 的分页。")
                newPage = waziPicAcg.getComicPages(self, comicId, str(i), str(j["order"]))
                waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在检查是否为单页。")
                if newPage["data"]["pages"]["pages"] == 1:
                    waziLog.log("debug", f"({self.name}.{fuName}) 单页，通过 getComicImageURLs 获取。")
                    yield waziPicAcg.getComicImageURLs(self, newPage)
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 多页，正在进入 for in range。")
                    for q in range(1, newPage["data"]["pages"]["pages"] + 1):
                        waziLog.log("debug", f"({self.name}.{fuName}) 正在请求 {str(q)} 页。")
                        newPage = waziPicAcg.getComicPages(self, comicId, str(i), str(q))
                        waziLog.log("debug", f"({self.name}.{fuName}) 请求完成，正在通过 getComicImageURLs 获取。")
                        yield waziPicAcg.getComicImageURLs(self, newPage)

    def downloadComic(self, comicId, path):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和下载路径，正在开始下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getThumbImage 获取封面。")
        waziPicAcg.getThumbImage(self, comicId, path)
        waziLog.log("debug", f"({self.name}.{fuName}) 下载完成，正在获取漫画信息。")
        comicInfo = waziPicAcg.getComic(self, comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在获取漫画名和分页。")
        comicName = comicInfo["data"]["comic"]["title"]
        eps = int(comicInfo["data"]["comic"]["epsCount"])
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画吗： {comicName}， 分页数： {eps}")
        waziLog.log("debug", f"({self.name}.{fuName}) 进入 for in range。")
        for i in range(1, eps + 1):
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取分 P 内容。")
            newEps = waziPicAcg.getComicEps(self, comicId, str(i))
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进入遍历。")
            for j in newEps["data"]["eps"]["docs"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在创建文件夹。")
                waziPicAcg.createFolderEps(self, path, comicName, j["title"])
                waziLog.log("debug", f"({self.name}.{fuName}) 创建完成，正在获取分 P 的分页。")
                newPage = waziPicAcg.getComicPages(self, comicId, str(i), str(j["order"]))
                waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在检查是否为单页。")
                if newPage["data"]["pages"]["pages"] == 1:
                    waziLog.log("debug", f"({self.name}.{fuName}) 单页，通过 singleDownloadComicImage 下载。")
                    waziPicAcg.singleDownloadComicImage(self, newPage, path, comicName, j["title"])
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 多页，正在进入 for in range。")
                    for q in range(1, newPage["data"]["pages"]["pages"] + 1):
                        waziLog.log("debug", f"({self.name}.{fuName}) 正在请求 {str(q)} 页。")
                        newPage = waziPicAcg.getComicPages(self, comicId, str(i), str(q))
                        waziLog.log("debug", f"({self.name}.{fuName}) 请求完成，正在通过 singleDownloadComicImage 下载。")
                        waziPicAcg.singleDownloadComicImage(self, newPage, path, comicName, j["title"])
                        waziLog.log("debug", f"({self.name}.{fuName}) 下载完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 全部下载完成。")
        return "Done! / 完工！"

    def getAndroidAPPs(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["androidAPPs"].replace("{page}", str(page))
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def blockUser(self, userId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "userId": userId
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["blockUser"], True, data, "POST", True)

    def getNotifications(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["notifications"].replace("{page}", str(page))
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getAnnouncements(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["announcements"].replace("{page}", str(page))
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getUserDirty(self, userId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["dirty"].replace("{userId}", userId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def getUserProfile(self, userId):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["userProfile"].replace("{userId}", userId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def latestUpdate(self, page):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 已递交至 advancedSearch 处理。")
        return waziPicAcg.advancedSearch(self, [], "", "dd", page)

    def filterIt(self, backJson, filters):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到需要过滤的内容和过滤标签，正在通过 needFilterIt 完成过滤。")
        returnJson = backJson
        returnJson["data"]["comics"]["docs"] = self.check.needFilterIt(backJson["data"]["comics"]["docs"], filters)
        waziLog.log("info", f"({self.name}.{fuName}) 过滤完成： {returnJson}")
        return returnJson
