# PyWazi: 不可明说的资源爬虫框架

> 做一点玩具项目就足以打发我那漫长的时间了。 —— 可能是我想说的

上帝花了 6 天时间创造了整个世界，而我花了一年的时间写了压根不可能跟人谈起的爬取色情资源的玩具项目，令人感慨。

**⚠ 这里是来自作者的警告，他希望你在使用时少一点偏头痛：**

1. 尽管 PyWazi 支持的功能较多但它效率低下，尤其是 ExHentai 部分（事实上，还有一堆 BUG）；
2. 没有统一的返回格式和参数，包括大小写的统一（URL, Url, url, link, href）；
3. 日志、请求系统均不采用流行的方式，不使用 requests, logging，它使用自己抽象的日志，请求模块（然后窒息）；
4. 它的日志系统过于繁琐，尽管你可以设置取消日志（可能会对硬盘造成不可知的伤害）；
5. 可能较为脆弱的稳定性，因为测试并未完全进行（能不能运行是一个未知数）。

## 进行一个了解

```python
from pywazi import *

info = [*waziExHentai.allSearch(0, "ボクの理想の異世界生活"), 
        *waziExHentai.allSearch(1, "ボクの理想の異世界生活")]

for i in info:
    waziExHentai.getNormalImages(i["URL"], "download", {
        "japanese": True,
        "path": "./download"
    })
```

> 使用 PyWazi 的 waziExHentai 下载一些本子

```python
from pywazi import *

for page in range(1, 54):
    info = waziAsianSister.getPage(page)
    for i in info[0]:
        waziAsianSister.downloadGallery(
            gallery = i["link"].split("/")[-1],
            path = "./download"
        )
```

> 使用 PyWazi 的 waziPicAcg 下载一些福利姬的画廊

尽管看起来不够简洁，也不够优雅，甚至似乎连这种小驼峰式的写法也显得十分粗糙和丑陋，有时候一些接口像极了 JSON RPC，一个很长的方法名和一堆参数，有时候则像极了 REST，一个可能会带动词的方法名，但只有一个字典参数。

只能说很古怪了，不过话就先说到这里，我们先开始进行教程吧。

## 安装

首先它不能被 `pip install` 安装，因为它是一个玩具项目，不是一个完整的可以被值得谈论的模块；第二我没写 `__init.py__` 文件，如果你想的话，你可以试着写一下；第三我不太想把它发布到 `pypi` 上，或许有朝一日它也会在 `GitHub` 上消失。

所以你的安装方式是：

1. `git clone https://github.com/Yazawazi/pywazi`;
2. `cd pywazi`;
3. `pip install -r .\requirements.txt`。

至此，你可以开始使用了，新建一个文件如下：

```python
import pywazi

print(pywazi)
```

如果显示 `<module 'pywazi' from 'xxxxx'>` 至此，你已经完成了这个项目的安装了。

## 主模块教程

主模块叫 `waziMain`，它有三个静态接口，你可以完全不实例化它直接使用，都是用于配置。

### 设置全局配置

如果你真试了上面的了解中的代码，很有可能因为在这个围城里面因为各种各样的原因而取得一些错误返回。很有可能是因为你需要一个通往全球互联网的逻辑链路，说人话就是你需要一个代理。此时，你可以设置一个全局代理给所有的模块使用：

基础的 HTTP 代理设置：

```python
from pywazi import *

waziMain.globalParams({
    "useProxies"    :        True,              # 是否使用代理
    "proxyAddress"  :        "127.0.0.1",       # 代理地址
    "proxyPort"     :        1080               # 代理端口
})
```

如果你的代理是全局的，那我建议你把 `useProxies` 设置为 `False` 以避免一些错误；或者你的代理是 SOCK5 或者需要账号密码，没有问题，现在这个版本我们推出了一项全新的参数（大嘘，其实本来就该做的，只不过我用的是 HTTP 代理）：

```python
from pywazi import *

waziMain.globalParams({
    "useProxies": True,                     # 是否使用代理
    "advancedProxies": {                    # 高级代理设置
        "protocol": "socks5",               # 代理协议（必须）
        "username": "yazawazi",             # 代理账号（爱填不填）
        "password": "kyomoitenki",          # 代理密码（爱填不填）
        "host": "127.0.0.1",                # 代理地址（必须）
        "port": 1080                        # 代理端口（爱填不填）
    }
})
```

事实上，我将打算把 `Tor` 的 `socks5h` 代理写入默认参数，以方便以后可能要做 `ExHentai` 暗网爬虫，我还在想怎么绕过那个充满噪点，我自己都难以分辨的验证码和 Cookies 过期时效。

此外，它还可以设置请求头的使用，在一些情况下，确实你需要手动设置，但我依旧不推荐你玩火，毕竟到时候你可能会因为缺少一些请求头字段被一些网站拒绝：

```python
from pywazi import *

waziMain.globalParams({
    "useHeaders": True,                    # 是否使用请求头
    "headers": {                           # 请求头设置
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
})
```

### 从文件读取全局配置

谁愿意每次新建一个项目就直接在代码里面重写，不如把它变成文件然后让程序设置。这样做的好处是，你可以在不增加代码的情况下更改配置，不用担心代码长得太丑：

```python
from pywazi import *

waziMain.globalParamsByFile("./params.json")
```

就是这样，文件的内容的格式应该和上文一致。

### 从文件读取特定配置

我的很多模块都会要求你设置一些内容，好让他们知道要做什么。比如 `waziDanbooru` 需要你设置 `api` 信息，`waziExHentai` 需要你设置 `cookies` 之类的，你在下文可以看到这些代码。

现在想象一下，你有一个项目，或者一堆，亦或者无数个文件，这个要做 Web 服务，这个要当爬虫，这个每天的七点自动执行 PicAcg 打卡任务，我可不愿意在代码里面写各种配置，不如我们都让他们读取一个特定配置好了，于是有了这个：

```python
from pywazi import *

waziMain.defConfig("./main.json")
```

其格式如下：

```json
[{
    "name": "JavBus",         // 即表示这是 JavBus 的配置
    "params": {},             // 这里是 Params 内容，跟前文一致
    "url": "",                // 设置 JavBus 的镜像站地址
    "eaUrl": "",              // 设置 JavBus.red 的镜像站地址
    "type": 0                 // 设置 JavBus 的类型，0 为仅显示有磁力的影片，1 为显示所有影片
}, {
    "name": "PicAcg",         // 即表示这是 PicAcg 的配置
    "params": {},             // 这里是 Params 内容，跟前文一致
    "login": {
        "username": "",       // 设置登录用户名
        "password": ""        // 设置登录密码
    },
    "image": 0                // 设置图片素质，0 为原图，1 为 low，2 为 medium，3 为 high
}, {
    "name": "Danbooru",       // 即表示这是 Danbooru 的配置
    "params": {},             // 这里是 Params 内容，跟前文一致
    "url": "",                // 设置 Danbooru 类网站地址
    "ports": [{               // 设置请求 API 路由，可以设置多个
        "key": "",            // 设置 key
        "value": ""           // 设置 value 可见 `waziDanbooru.setPort` 相关内容
    }]
}, {
    "name": "ExHentai",       // 即表示这是 ExHentai 的配置
    "params": {},             // 这里是 Params 内容，跟前文一致
    "cookies": "",            // 设置 ExHentai 的 Cookies
    "fullComment": true,      // 设置是否显示全部评论
    "jump": true,             // 是否跳过画廊警告
    "parse": true,            // 是否解析画廊
    "thumbType": "large"      // 设置缩略图类型，large 是大图，normal 是普通模式
}, {
    "name": "AsianSister",    // 即表示这是 AsianSister 的配置
    "params": {}              // 这里是 Params 内容，跟前文一致
}, {
    "name": "Nyaa",           // 即表示这是 Nyaa 的配置
    "params": {}              // 这里是 Params 内容，跟前文一致
}, {
    "name": "Log",            // 即表示这是 Log 的配置
    "save": true,             // 是否保存日志
    "level": 5                // 设置日志屏幕输入等级，-1 不显示，0 是错误，1 是警告，2 是信息，3 是调试，更高级别则与 3 同步
}]
```

此外，如果你也不愿意每个文件都加一句 `waziMain.defConfig("./main.json")` 之类的，你可以把这个配置文件命名为 `config.json` 它将会自动加载，实在是贴心。

## 日志模块教程

日志模块是 `waziLog`，你可以通过这个模块设置是否需要保存日志或者日志屏幕输出级别。

尽管在一开始的设计中，我想象中的它是完美的，可追踪的，直到我写了半天 try catch 没把错误信息传进去，才发现它不是那么完美。再后来发现它是个垃圾日志生成器，消耗你的硬盘读写寿命的，我就不太愿意再继续了，甚至修改它。

### 设置保存日志

如果你需要保存这些没用的废话然后出 BUG 了提一个 issue 的话，那就请：

```python
from pywazi import *

waziLog.needSave(True)
```

同理，使用 `False` 可以关闭日志保存。

### 设置日志屏幕输出级别

有时候你需要在控制台进行代码追踪或者想让它显示错误日志之类的（如果你觉得这个配色好看的话），你就可以使用这个接口：

```python
from pywazi import *

waziLog.setMinDisplayLevel(-1)
```

`-1` 表示什么都不打印，什么都不会在屏幕上显示；`0` 表示显示错误的日志输出；`1` 表示显示错误、警告的日志输出；`2` 表示显示错误、警告、信息的日志输出；`3` 表示显示全部，包括调试级别的（会非常的多，大部分其实是追踪级别的）。

## AsianSister 站点模块

哈，终于要讲到这个了吗，这个模块是用来获取 `AsianSister` 站点的，如果你不清楚 `AsianSister` 的话，我推荐你访问一下：https://asiansister.com/

总而言之，你能在上面看福利姬的照片和视频，以及一个叫「少年维特」的用户。

### 传入配置

如果你想自定义配置，可以这样：

```python
from pywazi import *

waziAsianSister.giveParams({
    "useProxies"    :        True,              # 是否使用代理
    "proxyAddress"  :        "127.0.0.1",       # 代理地址
    "proxyPort"     :        1080               # 代理端口
})
```

格式就如同上文的全局配置一致。

### 下载单个文件

试着想象一下，你拿到了一个 AsianSister 站点中的图片下载地址，现在你需要把它保存到本地，那么你可以这样：

```python
from pywazi import * 

waziAsianSister.downloadFile(
    url  = "https://asiansister.com/images/cover/20/R735AeWiX1J77.jpg",          # 文件地址
    name = "1.jpg",                                                              # 保存文件名（可不要觉得我会设置的）
    path = "./download"                                                          # 保存路径
)
```

这样就可以下载一个文件了，试着运行一下，如果成功的话会返回 True 的哦，否则就是 False。

### 进行一个浏览

假设只是想随便逛逛 AsianSister，随便翻翻页，看看有没有好玩的，那么你可以这样：

```python
from pywazi import *

waziAsianSister.getPage(1)
```

这样就可以获取第一页的内容了，返回的是一个字典，格式是这样的：

```python
(                                                       # 这是元组
    [{                                                  # 画廊信息 这是一个列表 列表中每一个都是一个字典 表示一个画廊
        "views": int,                                   # 画廊浏览数
        "link": str,                                    # 画廊链接
        "vip": bool,                                    # 是否是 VIP 画廊
        "cover": str,                                   # 画廊封面
        "alt": str,                                     # 画廊封面那个 IMG 标签的 ALT 属性
        "title": str                                    # 画廊标题
    }],
    [{                                                  # 视频信息 这是一个列表 列表中每一个都是一个字典 表示一个画廊
        "data": str or None,                            # 视频的切割动图，你看了就知道了
        "views": int,                                   # 视频浏览数
        "link": str,                                    # 视频链接
        "vip": bool,                                    # 是否是 VIP 视频
        "cover": str,                                   # 视频封面
        "title": str                                    # 视频标题
    }]
)
```

### 进行一个搜索

如果你有目的的话，比如搜索一些福利姬的画廊或者视频，亦或者一些关键词，那么你可以这样：

```python
from pywazi import *

waziAsianSister.search(
    keyword = "Cosplay",                                # 搜索关键词
    page    = 1                                         # 搜索第几页 从 1 开始数起哦
)
```

这样子就完成了一次搜索，格式同上哦！

### 进行一个标签搜索

如果你想搜一些标签，比如 `Cosplay` 这个标签的话，那么你可以这样：

```python
from pywazi import *

waziAsianSister.tagSearch(
    tag = "Cosplay",                                    # 标签名
    page = 1                                            # 搜索第几页 从 1 开始数起哦
)
```

格式还是同上，就是那个元组哦。

### 查看一个福利姬的信息

> 💤(～﹃～)~zZ 睡了，明天写
