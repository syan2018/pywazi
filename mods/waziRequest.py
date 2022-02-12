"""
mods/waziRequest.py

class: waziRequest
"""

import urllib3
from mods import waziFun
from ins.waziInsLog import waziLog

class waziRequest:
    """
    waziRequest
    *Bitter lemon juice, no sugar.*

    A class for requesting web pages.

    Attributes:
        isUseProxies: bool
            If True, use proxies.
            default: True
        
        proxies: str
            The proxy address like: http://ip:port
            default: ""
        
        isUseHeaders: bool
            If True, use custom headers.
            default: False
        
        headers: dict
            The custom headers.
            default: A chrome user-agent header.
    
    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziRequest.__init__(self)
        *Bittersweet*

        Initialize the class.

        Parameters:
            None
        """
        super(waziRequest, self).__init__()
        self.isUseProxies = True
        self.proxies = ""
        self.isUseHeaders = False
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/93.0.4577.82 Safari/537.36"
        }
        self.name = self.__class__.__name__

    def useProxies(self, isUse):
        """
        waziRequest.useProxies(self, isUse)
        *It will probably always be like this.*

        Set the use of proxies.

        Parameters:
            isUse: bool
                If True, use proxies.
        
        Return:
            Type: bool
            Current proxies status.
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到代理使用信息，正在写入配置。")
        self.isUseProxies = isUse
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.isUseProxies}")
        return self.isUseProxies

    def editProxies(self, http, port):
        """
        waziRequest.editProxies(self, http, port)
        *Scavenging for supplies in a post-apocalyptic world.*

        Set the proxy Address.

        Parameters:
            http: str or None
                The http proxy address.
            
            port: str or int or None
                The http proxy port.
        
        Return:
            Type: str or None
            Current proxy address.
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到代理信息，正在写入配置。")
        if http is None or port is None:
            self.proxies = None
        else:
            self.proxies = f"http://{http}:{port}"
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.proxies}")
        return self.proxies

    def useHeaders(self, isUse):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到自定义 Header 使用信息，正在写入配置。")
        self.isUseHeaders = isUse
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.isUseHeaders}")
        return self.isUseHeaders

    def editHeaders(self, key, value):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到自定义 Header 字段定义信息，正在写入配置。")
        waziLog.log("debug", f"({self.name}.{fuName}) 字段： {key}， 数值： {value}")
        self.headers[key] = value
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，全局配置为： {self.headers}")
        return self.headers

    def overWriteHeaders(self, headers):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到自定义 Header 信息，正在覆盖写入配置。")
        self.headers = headers
        waziLog.log("info", f"({self.name}.{fuName}) 覆写完成，全局配置为： {self.headers}")
        return self.headers

    def delHeaders(self, key):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到删除 Header 字段定义信息，正在写入配置。")
        waziLog.log("debug", f"({self.name}.{fuName}) 需求删除字段： {key}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试删除字段。")
        try:
            self.headers.pop(key)
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 删除失败。")
        waziLog.log("info", f"({self.name}.{fuName}) 最终全局配置为： {self.headers}")
        return self.headers

    def get(self, url):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 信息，准备发起 GET 请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL 信息为： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        temp = waziRequest.collectRequest(self, url, "get", None)
        waziLog.log("debug", f"({self.name}.{fuName}) 请求发送完毕，相关数据已返回。")
        return temp

    def post(self, url, data):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和 Data 信息，准备发起 POST 请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL 信息为： {url}， Data 信息为： {data}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        temp = waziRequest.collectRequest(self, url, "post", data)
        waziLog.log("debug", f"({self.name}.{fuName}) 请求发送完毕，相关数据已返回。")
        return temp

    def fieldsPost(self, url, data):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和 Data 信息，准备通过 collectRequest 发起 fieldsPost 请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL 信息为： {url}， Data 信息为： {data}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        temp = waziRequest.collectRequest(self, url, "fieldspost", data)
        waziLog.log("debug", f"({self.name}.{fuName}) 请求发送完毕，相关数据已返回。")
        return temp

    def put(self, url, data):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和 Data 信息，准备通过 collectRequest 发起 PUT 请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL 信息为： {url}， Data 信息为： {data}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        temp = waziRequest.collectRequest(self, url, "put", data)
        waziLog.log("debug", f"({self.name}.{fuName}) 请求发送完毕，相关数据已返回。")
        return temp

    def collectRequest(self, url, method, data):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL， METHOD 和 DATA 信息，准备发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL 信息为： {url}， 请求方式为： {method}， 数据为： {data}")
        temp = None
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查是否需要代理。")
        if self.isUseProxies:
            waziLog.log("debug", f"({self.name}.{fuName}) 检查到需要代理，使用 ProxyManager。")
            http = urllib3.ProxyManager(self.proxies)
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 未检查到需要代理，使用 PoolManager。")
            http = urllib3.PoolManager()
        waziLog.log("debug", f"({self.name}.{fuName}) 创建 HTTP 管理器完成，正在检查是否需要自定义 Header 并发起对应请求。")
        if self.isUseHeaders:
            waziLog.log("debug", f"({self.name}.{fuName}) 检查到需要自定义 Header，正在发起对应请求。")
            try:
                if method.lower() == "get":
                    temp = http.request("GET", url, headers = self.headers)
                elif method.lower() == "post":
                    temp = http.request("POST", url, body = data, headers = self.headers)
                elif method.lower() == "fieldspost":
                    temp = http.request("POST", url, headers = self.headers, fields = data)
                elif method.lower() == "put":
                    temp = http.request("PUT", url, body = data, headers=self.headers)
                else:
                    temp = None
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 无法发起请求或请求错误，请检查代码。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 请求发送完成。")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 未检查到需要自定义 Header，正在发起对应请求。")
            try:
                if method.lower() == "get":
                    temp = http.request("GET", url)
                elif method.lower() == "post":
                    temp = http.request("POST", url, body = data)
                elif method.lower() == "fieldsPost":
                    temp = http.request("POST", url, fields = data)
                elif method.lower() == "put":
                    temp = http.request("PUT", url, body = data)
                else:
                    temp = None
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 无法发起请求或请求错误，请检查代码。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 请求发送完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 相关数据已返回。")
        return temp

    def do(self, params):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数信息，准备分析后分配到对应函数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 参数信息： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备检查代理。")
        if "useProxies" in params:
            waziRequest.useProxies(self, params["useProxies"])
            waziLog.log("debug", f"({self.name}.{fuName}) 是否使用代理信息写入成功。")
            if params["useProxies"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在写入代理信息。")
                if "proxyAddress" in params and "proxyPort" in params:
                    waziRequest.editProxies(self, params["proxyAddress"], params["proxyPort"])
                    waziLog.log("debug", f"({self.name}.{fuName}) 代理信息写入完成。")
                else:
                    waziLog.log("warn", f"({self.name}.{fuName}) 不存在代理信息，无法写入。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 不使用代理，不写入代理信息。")
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 不存在是否使用代理信息，无法写入。")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备检查 Header。")
        if "useHeaders" in params:
            waziRequest.useHeaders(self, params["useHeaders"])
            waziLog.log("debug", f"({self.name}.{fuName}) 是否使用 Header 信息写入成功。")
            if params["useHeaders"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在写入 Header 信息。")
                if "headers" in params:
                    waziRequest.overWriteHeaders(self, params["headers"])
                    waziLog.log("debug", f"({self.name}.{fuName}) Header 信息写入完成。")
                else:
                    waziLog.log("warn", f"({self.name}.{fuName}) 不存在代理信息，无法写入。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 不使用 Header，不写入 Header 信息。")
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 不存在是否使用 Header 信息。")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备检查请求方式。")
        if "method" in params:
            if params["method"].lower() == "get":
                waziLog.log("info", f"({self.name}.{fuName}) 检测到 GET 模式，递交给 GET 函数处理。")
                return waziRequest.get(self, params["url"])
            elif params["method"].lower() == "post":
                waziLog.log("info", f"({self.name}.{fuName}) 检测到 POST 模式，递交给 POST 函数处理。")
                return waziRequest.post(self, params["url"], params["data"])
            elif params["method"].lower() == "fieldspost":
                waziLog.log("info", f"({self.name}.{fuName}) 检测到带表单的 POST 模式，递交给 FIELDSPOST 函数处理。")
                return waziRequest.fieldsPost(self, params["url"], params["data"])
            elif params["method"].lower() == "put":
                waziLog.log("info", f"({self.name}.{fuName}) 检测到 PUT 模式，递交给 PUT 函数处理。")
                return waziRequest.put(self, params["url"], params["data"])
            else:
                waziLog.log("error", f"({self.name}.{fuName}) 未检测到任何请求模式。")
                return "Sorry, method must be get, post or put. / 对不起，模式一定得是 GET, POST 或者 PUT 呜呜呜。"
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 不存在请求模式。")
            return "Sorry, please input method. / 对不起，请填写请求模式。"

    def handleParams(self, params, method, url, deHeaders, deProxies):
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到信息，准备合成 Params。")
        waziLog.log("debug", f"({self.name}.{fuName}) 基础参数： {params}， 请求方式： {method}， 访问地址： {url}， "
                             f"自定义 Header： {deHeaders}， 自定义代理： {deProxies}")
        temp = {}
        waziLog.log("debug", f"({self.name}.{fuName}) 准备检查代理。")
        if "useProxies" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 基础参数存在使用代理信息。")
            temp["useProxies"] = params["useProxies"]
            waziLog.log("debug", f"({self.name}.{fuName}) 写入代理使用信息成功。")
            if temp["useProxies"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在写入代理信息。")
                if "proxyAddress" in params:
                    waziLog.log("debug", f"({self.name}.{fuName}) 基础参数中存在代理地址，正在写入。")
                    temp["proxyAddress"] = params["proxyAddress"]
                    waziLog.log("debug", f"({self.name}.{fuName}) 代理地址写入完成。")
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 基础参数中不存在代理地址，正在检查自定义代理。")
                    if deProxies is None:
                        waziLog.log("warn", f"({self.name}.{fuName}) 自定义代理为空，自动设置空代理地址。")
                        temp["proxyAddress"] = None
                        waziLog.log("debug", f"({self.name}.{fuName}) 空代理地址设置完成。")
                    else:
                        waziLog.log("debug", f"({self.name}.{fuName}) 自定义代理不为空，正在获取自定义代理。")
                        if "proxyAddress" in deProxies:
                            waziLog.log("debug", f"({self.name}.{fuName}) 自定义代理存在代理地址，正在写入。")
                            temp["proxyAddress"] = deProxies["proxyAddress"]
                            waziLog.log("debug", f"({self.name}.{fuName}) 代理地址写入成功。")
                        else:
                            waziLog.log("warn", f"({self.name}.{fuName}) 自定义代理的代理地址不存在，自动设置空代理地址。")
                            temp["proxyAddress"] = None
                            waziLog.log("debug", f"({self.name}.{fuName}) 代理地址写入成功。")
                if "proxyPort" in params:
                    waziLog.log("debug", f"({self.name}.{fuName}) 基础参数中存在代理端口，正在写入。")
                    temp["proxyPort"] = params["proxyPort"]
                    waziLog.log("debug", f"({self.name}.{fuName}) 代理端口写入完成。")
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 基础参数中不存在代理端口，正在检查自定义代理。")
                    if deProxies is None:
                        waziLog.log("warn", f"({self.name}.{fuName}) 自定义代理为空，自动设置空代理端口。")
                        temp["proxyPort"] = None
                        waziLog.log("debug", f"({self.name}.{fuName}) 空代理端口设置完成。")
                    else:
                        waziLog.log("debug", f"({self.name}.{fuName}) 自定义代理不为空，正在获取自定义代理。")
                        if "proxyPort" in deProxies:
                            waziLog.log("debug", f"({self.name}.{fuName}) 自定义代理存在代理端口，正在写入。")
                            temp["proxyPort"] = deProxies["proxyPort"]
                            waziLog.log("debug", f"({self.name}.{fuName}) 代理端口写入成功。")
                        else:
                            waziLog.log("warn", f"({self.name}.{fuName}) 自定义代理的代理端口不存在，自动设置空代理端口。")
                            temp["proxyPort"] = None
                            waziLog.log("debug", f"({self.name}.{fuName}) 空代理端口写入成功。")
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 基础参数中不存在代理信息，自动设置无代理请求模式。")
            temp["useProxies"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 不使用代理模式已写入。")
        if "useHeaders" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) 基础参数中存在使用 Header 信息。")
            temp["useHeaders"] = params["useHeaders"]
            waziLog.log("debug", f"({self.name}.{fuName}) 写入 Header 使用信息成功。")
            if temp["useHeaders"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在写入 Header。")
                if "headers" in params:
                    waziLog.log("debug", f"({self.name}.{fuName}) 基础参数中存在 Header，正在写入。")
                    temp["headers"] = params["headers"]
                    waziLog.log("debug", f"({self.name}.{fuName}) Header 写入成功。")
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 基础参数中不存在 Header，正在检查自定义 Header。")
                    if deHeaders is None:
                        waziLog.log("warn", f"({self.name}.{fuName}) 自定义 Header 不存在，自动设置默认 Header。")
                        temp["headers"] = self.headers
                        waziLog.log("debug", f"({self.name}.{fuName}) 默认 Header 写入成功。")
                    else:
                        waziLog.log("debug", f"({self.name}.{fuName}) 存在自定义 Header，正在写入。")
                        temp["headers"] = deHeaders
                        waziLog.log("debug", f"({self.name}.{fuName}) 自定义 Header 写入成功。")
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 基础参数中不存在 Header 信息，自动设置无 Header 请求模式。")
            temp["useHeaders"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 不使用 Header 模式已写入。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在更新 Params 信息。")
        temp.update(method = method, url = url)
        waziLog.log("info", f"({self.name}.{fuName}) 处理完成，数据为： {temp}， 已返回。")
        return temp
