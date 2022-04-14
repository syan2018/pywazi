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

如果你想查询一个福利姬的信息，她的画廊、视频之类的，那么你可以这样：

```python
from pywazi import *

waziAsianSister.personSearch("m_1_Xidaidai___Misa_n")

# 如果一个福利姬的 URL 地址是： https://asiansister.com/m_1_Xidaidai___Misa_n
# 那么 m_1_Xidaidai___Misa_n 就是这个福利姬的 ID 填入即可
```

最后返回的是字典，格式如下：

```python
{
    "name": str,                                    # 福利姬叫啥
    "descriptionHTML": str,                         # 福利姬描述
    "views": int,                                   # 福利姬浏览数
    "tags": [{                                      # 福利姬标签
        "name": str,                                # 标签名
        "link": str                                 # 标签链接
    }],
    "galleries": [{                                 # 福利姬相关画廊
        "link": str,                                # 画廊链接
        "cover": str,                               # 画廊封面
        "alt": str,                                 # 画廊封面那个 IMG 标签的 ALT 属性
        "title": str,                               # 画廊标题
        "stars": str,                               # 画廊评分
        "VIP": bool                                 # 是否是 VIP 画廊
    }],
    "videos": [{                                    # 福利姬相关视频
        "data": str or None,                        # 视频的切割动图，你看了就知道了
        "link": str,                                # 视频链接
        "title": str,                               # 视频标题
        "cover": str,                               # 视频封面
        "VIP": bool                                 # 是否是 VIP 视频
    }]
}
```

### 获取一个画廊的详细信息

倘若你已经找到了一个满意的画廊了，你现在需要获取它的信息，那么你可以使用如下代码：

```python
from pywazi import *

waziAsianSister.getGallery("view_2096_Belle_Delphine__OnlyFans_Friendly_Neighborhoodn")

# 如果一个画廊的 URL 地址是： https://asiansister.com/view_2096_Belle_Delphine__OnlyFans_Friendly_Neighborhoodn
# 那么 view_2096_Belle_Delphine__OnlyFans_Friendly_Neighborhoodn 就是这个画廊的 ID 填入即可
```

最后返回的是字典，格式如下：

```python
{
    "title": str,                                       # 画廊标题
    "stars": str,                                       # 画廊评分
    "category": {"name": str, "link": str},             # 画廊分类
    "tags": [{"name": str, "link": str}],               # 画廊标签
    "description": str,                                 # 画廊描述
    "model": {"name": str, "link": str},                # 画廊福利姬
    "covers": [{"link": str, "alt": str}],              # 画廊封面
    "pictures": [{"link": str, "org": str}],            # 画廊图片
                                                        # org: 原图 link: 缩略图
    "pageNum": int,                                     # 画廊总页数
    "comments": [{                                      # 画廊评论
        "user": str,                                    # 评论者用户组
        "avatar": str,                                  # 评论者头像
        "name": str,                                    # 评论者名字
        "time": str,                                    # 评论时间
        "content": str                                  # 评论内容
    }],                                                 
    "galleries": [{                                     # 画廊相关推荐画廊
        "link": str,                                    # 画廊链接
        "cover": str,                                   # 画廊封面
        "alt": str,                                     # 画廊封面那个 IMG 标签的 ALT 属性
        "title": str,                                   # 画廊标题
        "stars": str,                                   # 画廊评分
        "VIP": bool                                     # 是否是 VIP 画廊
    }],
    "videos": [{                                        # 画廊相关推荐视频
        "data": str or None,                            # 视频的切割动图，你看了就知道了
        "link": str,                                    # 视频链接
        "title": str,                                   # 视频标题
        "cover": str,                                   # 视频封面
        "VIP": bool                                     # 是否是 VIP 视频
    }]
}
```

### 下载一个画廊

如果你想要下载一个画廊，那么你可以使用如下代码：

```python
from pywazi import *

waziAsianSister.downloadGallery(
    gallery   =   "view_2072____10Pn",               # 画廊 ID
    path      =   "./download",                      # 下载路径
    key       =   "org"                              # 默认是 org 控制下载链接选择的 org 表示原图 link 表示缩略图
)
```

其实下载 VIP 画廊也可以这么做，这个网站似乎没有任何鉴权。

最后返回的是元组，格式如下：

```python
(
    [str],                                          # 下载成功的文件名（包含路径）
    [str]                                           # 下载失败的图片地址
)
```

### 获取一个视频的详细信息

我可能以后再支持 https://sisterasian.com/ 这个视频站点吧，但是现在还没有支持。现在只能支持 AsianSister 站点内的视频，代码如下：

```python
from pywazi import *

waziAsianSister.getVideo("v_vide_348_Very_beautiful_pussy_girl_show_her_perfect_pussy_with_cosplay_suitn")

# 如果一个视频的 URL 地址是： https://asiansister.com/v_vide_348_Very_beautiful_pussy_girl_show_her_perfect_pussy_with_cosplay_suitn
# 那么 v_vide_348_Very_beautiful_pussy_girl_show_her_perfect_pussy_with_cosplay_suitn 就是这个视频的 ID 填入即可
```

最后返回的是字典，格式如下：

```python
{
    "title": str,                                   # 视频标题
    "views": int,                                   # 视频被观看的次数
    "tags": [{"name": str, "link": str}],           # 视频标签
    "cover": str,                                   # 视频封面
    "url": str,                                     # 视频文件 URL
    "comments": [{                                  # 视频评论
        "user": str,                                # 评论者用户组
        "avatar": str,                              # 评论者头像
        "name": str,                                # 评论者名字
        "time": str,                                # 评论时间
        "content": str                              # 评论内容
    }],                                             
    "recommends": [{                                # 视频相关推荐视频
        "title": str,                               # 视频标题
        "link": str,                                # 视频链接
        "cover": str,                               # 视频封面
        "views": int                                # 视频被观看的次数
    }]
}
```

### 下载一个视频

说实话，我不太支持你使用我内置的下载，因为速度实在是，令人汗颜，主要是我不想做多线程，写一个基础的下载模块，所以我建议你直接复制那个 url 地址，然后用浏览器打开，下载或者用什么 IDM 之类的。

总之代码就在这里：

```python
from pywazi import *

waziAsianSister.downloadVideo(
    video = "v_vide_348_Very_beautiful_pussy_girl_show_her_perfect_pussy_with_cosplay_suitn",       # 视频 ID
    path  = "./download"                                                                            # 保存路径
)
```

最后成功就返回文件名（包含路径），否则直接返回 `False`。

## Danbooru 站点模块

或许应该叫做 `Booru` 站点模块更为合适，因为现在可以适配很多类 Booru 站点。一开始只是想着支持以 `yande.re` 为主的 Danbooru，不过后来看到了更多的有趣的站点，提供了一个自定义的接口支持。

> 在一些网站中，一些功能可能不可用，建议在使用之前检查该站点的 API 文档的开放内容。

### 传入配置

如果你想自定义配置，可以这样：

```python
from pywazi import *

waziDanbooru.giveParams({
    "useProxies"    :        True,              # 是否使用代理
    "proxyAddress"  :        "127.0.0.1",       # 代理地址
    "proxyPort"     :        1080               # 代理端口
})
```

格式就如同上文的全局配置一致。

### 设置爬虫网站

程序一开始并不会设置默认的爬虫网站，你需要手动指定，比如 `yande.re` 之类的网站，应该是其相对 API 接口的根地址，比如 `https://yande.re/post.json` 那就是 `https://yande.re`。

```python
from pywazi import *

waziDanbooru.setApi("https://yande.re")
```

### 设置爬虫网站的 API 接口

默认的 API 接口配置如下：

```python
{
    "post": "/post.json",
    "tag": "/tag.json",
    "artist": "/artist.json",
    "comment": "/comment/show.json",
    "pool": "/pool.json",
    "poolShow": "/pool/show.json",
    "poolZip": "/pool/zip/"
}
```

与 `yande.re` 无异，如果你所爬取的网站的 API 接口（在你设置网站的 API 文档文档）不是这个样子，那么你可以这样设置：

```python
from pywazi import *

waziDanbooru.setApi("http://behoimi.org")

waziDanbooru.setPort("post", "/post/index.json")
```

### 获取 Posts 时间线内容

使用以下代码获取 Posts 时间线内容：

```python
from pywazi import *

waziDanbooru.getPosts(
    page  = 1,                               # 页码 从 1 开始
    tags  = "",                              # 标签 没有就写空字符串
    limit = 10                               # 每页显示的数量
)
```

最后会返回一个列表，包着一堆字典。主要的关键字有：

- `id` 表示图片 ID；
- `tags` 表示图片的标签，用空格隔开；
- `file_url` 表示图片的 URL；
- `preview_url` 表示图片的预览 URL；
- `sample_url` 表示图片的缩略 URL。

### 下载 Posts 时间线内容

使用以下代码进行一个 Posts 时间线内容的下载：

```python
from pywazi import *

waziDanbooru.downloadPosts(
    page  = 1,                               # 页码 从 1 开始
    tags  = "",                              # 标签 没有就写空字符串
    limit = 10,                              # 每页显示的数量
    path  = "./download",                    # 保存路径
    key   = "file_url",                      # 获取关键字 填写 file_url 就从 file_url 这个关键词对应的值拿到图片地址 即原图 同理 preivew_url 就是预览图 sample_url 就是缩略图 默认 file_url
    ext   = True                             # 爬取的时候是否带上 Referer 字段，用于绕过反爬虫 默认 False
)
```

最后返回格式如下：

```python
(
    [str],                                      # 下载成功的文件路径
    [{"fileURL": str, "id": int}]               # 下载失败的文件 URL 和图片 ID
)
```

### 获取这个网站的标签列表

使用以下代码获取这个网站的标签列表：

```python
from pywazi import *

waziDanbooru.getTags(
    page  = 1,                               # 页码 从 1 开始
    limit = 10,                              # 每页显示的数量
    order = "count"                          # 排序方式 count: 按创作数量排序 date: 按时间排序 name: 按名称排序
)
```

最后返回示例如下：

```python
[{
    "id": 45,
    "name": "long_hair",
    "count": 105004,
    "type": 0, 
    "ambiguous": False
}]
```

### 获取这个网站的艺术家列表

使用以下代码获取这个网站的艺术家列表：

```python
from pywazi import *

waziDanbooru.getArtists(
    page  = 1,                                # 页码 从 1 开始
    order = "name"                            # 排序方式 name: 按名称排序 date: 按时间排序
)
```

最后返回示例如下：

```python
[{
    "id": 4958,
    "name": "shashaki",
    "alias_id": None,
    "group_id": None,
    "urls": ["https://www.pixiv.net/en/users/9089874"]
}]
```

### 搜索图集

使用以下代码搜索图集：

```python
from pywazi import *

waziDanbooru.getPools(
    query = "Jack-O' Challenge",             # 搜索关键词
    page  = 1                                # 页码 从 1 开始
)
```

最后返回示例如下：

```python
[{
    "id": 509,
    "name": "Jack-O'_Challenge",
    "created_at": "2021-08-27T17:55:55.591Z",
    "updated_at": "2021-12-02T20:39:34.488Z",
    "user_id": 73632,
    "is_public": True,
    "post_count": 160,
    "description": "A Twitter meme where characters are drawn in an extreme top-down bottom-up resembling Jack-O' Valentine's crouch pose."
}]
```

### 通过图集 ID 获取图集详细信息

使用以下代码获取图集详细信息：

```python
from pywazi import *

waziDanbooru.getPoolFromId(
    poolId = 489,                            # 图集 ID
    page   = 1                               # 页码 从 1 开始
)
```

最后返回示例如下：

```python
{
    'id': 489,
    'name': 'Sailor_Moon_Redraw_2020',
    'created_at': '2020-05-20T18:50:05.132Z',
    'updated_at': '2021-04-19T18:24:09.842Z',
    'user_id': 73632,
    'is_public': True,
    'post_count': 26,
    'description': 'Art fad started in May 2020 wherein various artists redraw and parody a screenshot from the classic Sailor Moon anime.',
    'posts': [{...}]
}
```

### 下载图集

使用以下代码下载一页图集：

```python
from pywazi import *

waziDanbooru.downloadPool(
    poolId = 489,                            # 图集 ID
    page   = 1,                              # 页码 从 1 开始
    path   = "./pools",                      # 下载的文件夹路径
    key    = "file_url",                     # 获取字段 默认 file_url
    ext    = True                            # 爬取的时候是否带上 Referer 字段，用于绕过反爬虫 默认 False
)
```

最后返回格式如下：

```python
(
    [str],                                      # 下载成功的文件路径
    [{"fileURL": str, "id": int}]               # 下载失败的文件 URL 和图片 ID
)
```

### 下载打包图集

> 我记得似乎只有 Yande.re 存在这个功能

使用以下代码下载图集的压缩包：

```python
from pywazi import *

waziDanbooru.downloadPoolWithZip(
    poolId  = 111,                            # 图集 ID
    needJPG = True,                           # 是否需要 JPG 格式的图片
    path    = "./pools"                       # 下载的文件夹路径
)
```

最后返回布尔值表示下载是否成功。
