# PyWazi: 从入门到放弃

> PyWazi 参考文档
> 
> 正在编写...

该文档使用的版本是与 GitHub 同步（2022.02.22）的 1.4 版本，最近更新时间是 2022.02.22。

## 前言

> 废话，好多啊。

PyWazi 大抵是终于要写文档了。我思来想去，似乎 Markdown 已经离我远去了，每每打开 Typora 看到未激活的时候便觉得没有 Markdown 也无所谓，于是乎走上了写内嵌文档的不归路，只想用 `help()` 打发一下。

文档写得很慢，不过凌晨的时候也已搞定了。“啊，已经没有什么可做的了。”可并未如此，想来白日里觉得详细的文档还是要有的，用户看了便也大概知晓一二。内嵌文档写了，似乎也不明白究竟何时要用这个接口。打开 VS Code 一看，竟自己渲染了格式。思前想后，还是得写网络文档。

很久很久之前，也试着用过 LaTeX 去写文档的，用 morelull 那个模板，在 Overleaf 上，似乎很像教科书，也写得差不多了。当时使用的 PyWazi 版本都还是一个文件包四个模块上千行的那种。真正开始开源之后一直在用 Markdown 写文档，也有试过自己写一个静态 HTML 用上 Tailwind，但是一直写 class 确实难吃得消。

我似乎很想念 Typora 的所见即所得，LaTeX 需要编译后才能拿到 PDF 确实令我有些急躁，本地配置环境确实是令人头疼的感受。

像日记的废话先少说了，还是先说说我对于 PyWazi 的理解吧。我之前一直拿“爬虫”的噱头说这个项目，大抵是真的不对。如今想来，应该是自己实现了一个网络爬虫搞的一个网络抓取带数据处理的项目框架。
    
似乎在我潜意识（大抵就是刻板印象）里面，网络爬虫，基本都是用 Python 写的，多半都是自动下载互联网的媒体。可刻板印象终究是刻板印象，世界上也有很多种类型的爬虫。我的项目不光只是单单下载媒体的功能，还有数据处理，HTML 分析之类的。
    
可以直接 Clone 下来，用 PyWazi 来做一个小型的客户端了，或许可以用它开发 Web 服务，或者一个小软件也蛮不错的。尽管它大部分在我手上的时候就只是充当一个自动下载互联网媒体的相比于其他爬虫还要麻烦的工具罢了。

我已经记不清我究竟是把这个项目写成什么样了，个人感觉比较糟糕，但能用，功能还挺多的吧。如果我不是开发者只是一个普通用户的话，我大概会在某个夏天的午后，独自把玩这个项目，然后看源码看到头痛的感觉。
    
源码里面中英文混搭，充斥着拙劣的语法，VS Code 提示的标点符号混淆边框，以及在内嵌文档里写的各种骚话属实要把我弄窒息了。如果有机会的话，我不会把这个代码弄得这么脏，会尽量少一点功能，会试着去想怎么样才能做到高效且代码看着美观又逻辑清晰，大概会花上很多时间吧。
    
这个项目只是从去年开始，我自己花了一晚上时间做出来的，因为时差的缘故，我夜晚就相当于东八区的白天，便跟朋友瞎聊天，之后口嗨说我要写一个模块，能够采集一些 NSFW 网站的数据，不单单只是下载，我还要做数据收集，把能看到的都给采集下来。最后越说越激动，给我真的写出来了。不过一开始的版本，现在看来是真的很糟糕，使用 urllib 模块导致的连接 Close 问题使得一些情况下压根取不到 ExHentai 的数据，一个文件上千行，没有注释。一口气直接写下来，似乎很爽，但也管不了那么多了。

现在文档问题依旧存在，代码也依旧不能入眼，可是只要我还在用它，那我会一直更新下去的。

-- 2022 年 2 月 22 日， Yazawazi

## PyWazi 介绍

> 自我宣传。

PyWazi 是一个功能完备，不单单只有媒体下载功能的针对一些 NSFW 站点的带数据处理的网络抓取项目。它带了多个站点的基本解决方案，你可以使用它以进行针对特定网站的数据下载、收集、二次开发等。

项目主页：[GitHub - Yazawazi/pywazi: Internet Resource Crawler / 互联网资源爬虫](https://github.com/Yazawazi/pywazi)。

### 所支持的站点

> 其实也只是马马虎虎吧。

+ [AsianSister](https://asiansister.com/)
+ [Danbooru](https://danbooru.donmai.us/) *等一系列基于 Danbooru 的网站 (API 相近)*
+ [ExHentai](https://exhentai.org/) *没有 E-Hentai 的支持*
+ [JavBus](https://javbus.com/)
+ [Nyaa](https://nyaa.si/) *当然也有 sukebei 的支持*
+ [PicAcg](https://picacomic.xyz/)

未来会持续增加...

### 所需环境

> 房子需要地基，她也一样。

你需要 Python 版本大于 3.7，安装：

+ beautifulsoup4>=4.9.0
+ bs4>=0.0.1
+ certifi>=2021.10.8
+ lxml>=4.6.3
+ urllib3>=1.26.6

或许更低的版本同样可以正常使用，我未进行任何测试。

### 版权声明及致谢

> 总而言之，爱你啦。

程序源码以 GPL-3.0 许可协议开源，内嵌文档和网络文档则不以 GPL-3.0 许可开源。所有引用的歌词、名言、相关作品等版权由原作者享有。

本项目的开发离不开以下开源项目：

1. JavBus 代码参考：[WWILLV/iav: 可搜索javbus、btso的磁力链接和avgle的预览视频 (github.com)](https://github.com/WWILLV/iav)；
2. PicAcg 部分：[AnkiKong/picacomic: 哔咔漫画相关api (github.com)](https://github.com/AnkiKong/picacomic) 提供了大部分的 Api 链接；从 [tonquer/picacg-windows: 哔咔漫画，picacomic，bika，PC客户端。 (github.com)](https://github.com/tonquer/picacg-windows)  中获取了最新 headers；https://www.hiczp.com/wang-luo/mo-ni-bi-ka-android-ke-hu-duan.html 提供了一些想法（GitHub 地址：[czp3009/czp-blog (github.com)](https://github.com/czp3009/czp-blog)）。

感谢 [cloudwindy (github.com)](https://github.com/cloudwindy) 提供的 ExHentai 账号，得以我进行开发测试；感谢我的朋友 **The Galaxy~ Of Dick** 给我制作的 Banner。

### 相关警告

> 🛑 在使用之前，我有必要提醒你以下几点：

1. 尽管 PyWazi 支持的功能较多但它效率低下，尤其是 ExHentai 部分；
2. 没有统一的返回格式和参数，包括大小写的统一；
3. 日志、请求系统均不采用流行的方式，不使用 requests, logging，它使用自己抽象的日志，请求模块；
4. 它的日志系统过于繁琐，尽管你可以设置取消日志；
5. 可能较为脆弱的稳定性，因为测试并未完全进行。

### 开发配置

> 咕呣，其实非常敷衍的啦~

1. `git clone https://github.com/Yazawazi/pywazi`
2. `cd pywazi`
3. `vim [name].py` 或者其他你喜欢的编辑器，IDE 之类的
4. 开头使用 `from pywazi import *` 导入

其实你可以自己写一个 `setup.py` 把它变成库。

## 案例导入

> 大概只是一些简单的 Example 罢了。

假设你需要做一些比较机械重复的工作，非常的枯燥且耗时，比如每天从 Danbooru 类网站上找点 R18 图片看亦或者去 JavBus 从某个分类下面找点片看。

你或许会自己用 JavaScript 或者 Python 去写一个爬虫出来，亦或者去 GitHub 找找开源的解决方案。PyWazi 就非常适合你（大嘘），只需要进行配置就可以完成这些简单的基础任务。

```python
from pywazi import waziDanbooru    # 假设你只爬取 Danbooru 类网站

waziDanbooru.giveParams({
    "useProxies": True,	            # 是否使用代理
    "proxyAddress": "127.0.0.1",    # 代理地址
    "proxyPort": 7890               # 代理端口
})

waziDanbooru.setApi("https://konachan.com") # 设置你想爬的 Danbooru 类网站地址

for page in range(1, 101):
    # 爬一百页
    waziDanbooru.downloadPosts(
        page = page,                   # 指定页码
        tags = "rating:explicit",      # 标签
        limit = 40,                    # 每页限制几张图片，最多就 40 张
        path = "./download"            # 下载目录
    )
```

> 代码案例: 自动爬取 Konachan 100 页 R-18 图片

```python
from pywazi import waziJavBus	# JavBus 解决方案

waziJavBus.giveParams({
    "useProxies": True,             # 是否使用代理
    "proxyAddress": "127.0.0.1",    # 代理地址
    "proxyPort": 7890               # 代理端口
})

# 浏览
items = waziJavBus.browse(
    page = 1,           # 页码
    tag = "4u",         # 标签 ID 4u 表示 戲劇
    avType = 0          # AV 类型 0 是有码 1 是无码
)

for i in items:
    print(f"{i['avId']} - {i['title']}")    # 打印所有获取到的番号和标题
```

> 代码案例: 获取一个分类中第一页的 AV 番号和标题

如果你不单单只追求文件的下载，还想获取一些其他的信息，举个例子你对某一个 ExHentai 的本子的评论很感兴趣，又或者你需要以 RSS 格式获取 Nyaa 的数据，这些都是可以通过 PyWazi 来实现的。

PyWazi **尽可能**保证每个网站所能见到的信息都能被获取到（除了带 API 接口的 Danbooru 和 PicAcg 的聊天室），如果你觉得某个网站的信息不够，亦或者需要增加其他网站的接口，你可以直接写一个 Issue 来提出你的需求。

## 主模块教程

> 世界的大门，这里是 PyWazi 的主模块。

主模块是 `pywazi.py` 这个小家伙，它是一个模块，它的作用是负责管理所有的网站的接口，并且负责调用接口的具体实现。

好吧，你可能想问为什么不写一个 `__init__.py` 出来，答案是我不知道。

它内置了多个函数，以用于配置的读取，并且在导入时自动尝试读取配置。

在 PyWazi 中，它是门面，你可以通过它控制配置系统、日志系统和站点模块

### 配置系统

> 与文档无关，我觉得晚上就是该听 CityPop。

```python
from pywazi import waziConfig
```

使用以上代码，你可以获取到一个配置类，它原本的作用是每一个站点模块都能通过它获取配置，不过现在有了主模块，它基本就是个废物了。

你可以在下文中的基础模块配置模块找到对应的教程。

### 日志系统

> 世界上最烦人的就是你了。

```python
from pywazi import waziLog
```

使用以上代码，你可以获取到一个日志类，它可以让你控制单独的日志设置。

你可以在下文中的基础模块日志模块找到对应的教程。

### 站点模块

> 似乎你已经知道了，这里是最重要的了。

```python
from pywazi import waziAsianSister, waziDanbooru, waziExHentai, waziJavBus, waziPicAcg, waziNyaa
```
使用以上代码，导入所有站点模块。

+ `waziAsianSister` - 收集 AsianSister 中画廊和视频的模块；
+ `waziDanbooru` - 获取或下载 Danbooru 类网站的图集、标签、图片等的模块；
+ `waziExHentai` - 获取或下载 ExHentai 网站的图片、评论等的模块；
+ `waziJavBus` - 获取 JavBus 番号磁力链接以及信息的模块；
+ `waziNyaa` - 获取 waziNyaa 网站的磁力、信息等的模块；
+ `waziPicAcg` - 基于官方 API 的获取 PicAcg 图片、信息等的模块。

### 配置函数

> 蓝天的阳光，这里是风力发电机。

存在三个配置函数，以用于全局配置和配置文件导入。此外，在导入主函数时，程序会自动请求当前目录下的 `config.json` 文件以用于作为默认配置。

#### 读取全局配置文件

> 像大海一样。

如果你需要让所有的站点模块都用同一个 `params` 配置文件（记录了代理信息和请求头信息）的话，可以使用 `globalParamsByFile(filePath)` 函数以获取配置文件。

如：

```python
from pywazi import *

globalParamsByFile('./config.json')
```

文件的格式应当如下：

```python
{
    "useProxies": True,             # 要不要用代理
    "proxyAddress": "127.0.0.1",    # 代理地址
    "proxyPort": 7890,              # 代理端口（整数或者字符串）
    "useHeaders": True,             # 要不要用请求头（不需要写这个其实，程序会自己写好的）
    "headers": {}                   # 自定义请求头（字典，同样，程序会自动补全的）
}
```

#### 设置全局配置

> 没有重载函数，也不想自己造一个...

如果你不想要读取文件，而想直接写一个 `params` 字典传进去，你可以使用 `globalParams(params)` 函数。

举个例子：

```python
from pywazi import *

globalParams({
    "useProxies": True,
    "proxyAddress": "127.0.0.1",
    "proxyPort": 1080
})
```

#### 读取自定义配置文件

> 分析类型和可变参数也不是不行。

我们在案例中看到了一些配置类的代码，比如：

```python
waziDanbooru.giveParams({
    "useProxies": True,
    "proxyAddress": "127.0.0.1",
    "proxyPort": 7890
})

waziDanbooru.setApi("https://konachan.com")
```

那么我们能否把这些代码或者配置放到一个文件里，以便以后使用呢？事实上，这是可以的。PyWazi 主模块提供了一个接口：`defConfig(filePath)` 以用于读取这样的配置。

在导入主模块时会自动尝试 `defConfig('./config.json')` 以帮助用户进行配置。

这种配置文件的格式如下（内容都是可选的） ：

```jsonc
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

## 基础模块

> 碎石，构建我的人造地基。

总共有九个基础模块，事实上只用到了八个，它们有些会在 ins 中被实例化，有些则会在 sites 中实例化。

以下模块按照字母排序进行排列。提醒一下，关于模块的参数等内容，如果文档不够明晰，可以借助 `help()` 函数以进行查询。

### waziCheck

> 很糟糕，我的人造地基。

这是用于校验、计算、加解密的模块，它负责的有 PicAcg 的加密和过滤，ExHentai 的标签位运算、Nyaa 的 Class 翻译储存。

事实上，如 `waziFileName` 和 `waziURL` 这类模块可以直接被写入 `waziCheck` 但是我只能说，你得问问那时候我是怎么想的。

#### returnHasTorrents

> 非常神秘。

传入 `soup` 参数，即可获得一个布尔值，表示当前页面是否有磁力链接。

事实上，这个 `soup` 只是一个 `img` 标签（当然是 BeautifulSoup 类型）：

```html
<img src="https://exhentai.org/img/td.png" alt="T" title="No torrents available" />
```

函数将对比下载图标地址是否与存在种子画廊的下载图标地址是否一致，尽管使用 `title` 亦或者 `alt` 同样可以，但是我当时大概率比较优柔寡断，可能是觉得 URL 的资源时效性更高一些，可能更加可靠。

#### returnRatingNum

> 数字，也只是个数字。

传入 `pos` 字符串参数，以获得当前页面的评分数字。可能是浮点数，也可能是整数。

如：

```python
from mods import waziCheck as Wck
waziCheck = Wck.waziCheck()

waziCheck.returnRatingNum("-16px -1px")
```

即可取得返回值：`4`。这串 `pos` 字符串是 `div` 元素的 `style` 中的 `background-position` 的 CSS 属性值，如下所示：

```html
<div class="ir" style="background-position:-16px -1px;opacity:1"></div>
```

中的 `-16px -1px` 就是我们要取得的值，将它代入 `returnRatingNum` 函数即可取得对应的数字。我将所有可能出现的 `pos` 字符串和对应的数字写了一个字典，储存在 `ratingPos` 中。

#### getFileSHA1

> 指纹，唯一。

传入 `path` 字符串参数，即文件的路径（相对亦或者绝对都是可以接受的），以获得文件的 SHA1 摘要（之类的叫法）。

使用 `hashlib` 实现。


#### getSources

> Bit Wise.

传入一个 `params` 字典（格式在下面）计算出 `params` 内分类所对应的唯一数字。

这个参数的格式为：

```python
{
    "cats": ["Non-H"]  # ExHentai 分类
}
```

你可以通过 `tags` 获取所有储存的 ExHentai 分类。你可以在 `ehg_index.c.js` 中找到原始的计算函数：

```javascript
function toggle_category(b) {
    var a = document.getElementById("f_cats");
    var c = document.getElementById("cat_" + b);
    if (a.getAttribute("disabled")) {
        a.removeAttribute("disabled")
    }
    if (c.getAttribute("data-disabled")) {
        c.removeAttribute("data-disabled");
        a.value = parseInt(a.value) & (1023 ^ b)
    } else {
        c.setAttribute("data-disabled", 1);
        a.value = parseInt(a.value) | b
    }
}
```

#### signature

> 我用几行字形容你是我的谁 —— 周杰伦《七里香》

签名，非常重要，这个 PicAcg 的签名函数需要的参数还蛮多：

+ `url`: 字符串，表示请求的 URL；
+ `times`: 整数，表示请求时间戳，你可以使用构建函数以取消该参数；
+ `method`: 字符串，表示请求的方法；
+ `baseURL`: 字符串，表示请求的基础 URL，一般而言是 `https://picaapi.picacomic.com/`；
+ `uuids`: 字符串，表示请求的 UUID；
+ `apiKey`: 字符串，表示请求的 API Key，一般而言是 `C69BAF41DA5ABD1FFEDC6D2FEA56B`；
+ `secretKey`: 字符串，表示请求的 Secret Key，你可以在文档里面查看该字符串。

最后将会返回一个字符串，是该请求的签名。

#### construct

> 创造，创造，创造！

构建函数，事实上只构建了时间戳和签名，它需要的参数：

+ `url`: 字符串，表示请求的 URL；
+ `method`: 字符串，表示请求的方法；
+ `baseURL`: 字符串，表示请求的基础 URL，一般而言是 `https://picaapi.picacomic.com/`；
+ `uuids`: 字符串，表示请求的 UUID；
+ `apiKey`: 字符串，表示请求的 API Key，一般而言是 `C69BAF41DA5ABD1FFEDC6D2FEA56B`；
+ `secretKey`: 字符串，表示请求的 Secret Key，你可以在文档里面查看该字符串。

其实也称不上构建，最后返回列表，Index 0 为签名，Index 1 为时间戳。

#### needFilterIt

> 像个筛子一样过滤。

这是一个针对 PicAcg 的过滤接口，它模拟了 PicAcg 原生的分类过滤，需要两个参数：`backJson` 和 `filters`。

`backJson` 是一个列表，里面储存了所有的漫画，应当是漫画搜索结果的 `docs` 内容。`filters` 同样是一个接口，储存了你不想要的分类。

程序会自动处理这两个参数，并返回一个新的列表，里面储存了所有不在 `filters` 中的漫画。

### waziColor

> 油漆工。

世界上的颜色，每个人都有自己的颜色，但是我们的颜色，是不同的。（这段是 Copilot 生成的，总觉得它的 Temperature 有点高）

可以使用它打印 256 色的字符串，当然，我只支持 256 色终端，如果你的终端不支持，那我建议你直接关掉 `log` 显示，直接从保存文件里阅读。

#### HexToRGB

> 从一个表述到另一种表述。

终端可不收十六进制，它需要转换为 RGB，这个函数可以帮你转换。它是一个 static 函数，需要三个函数，分别是：`r`, `g`, `b`。如：`waziColor.HexToRGB(0x12, 0x34, 0x56)`。对应 R，G，B 的值。

将会拿到一个字典，格式如下，`{"R": str, "G": str, "B": str}`，这是一个适用于 `waziColor.print` 的字典。

#### print

> 好吧，考虑明天换成 `rich`。

打印，事实上，也是 static 的，它所能接受的参数 `jsons` 是一个字典，格式如下：

```python
{
    "color": {
        "R": 255,
        "G": 233,
        "B": 0
    },                      # 前景色
    "bgColor": {
        "R": 255,
        "G": 233,
        "B": 0
    },                      # 背景色
    "effects": {
        "normal": True,     # 正常显示 / 重置 | 就像你所看到的那样
        "highLight": True,  # 高亮或加粗 | 大概比较重要
        "lowLight": True,   # 浅色 | 可能是一个提示
        "itail": True,      # 斜体 | 像诗歌一样
        "underLine": True,  # 下划线 | a 标签 可惜我真的不喜欢下划线
        "slowShine": True,  # 闪烁 | 萤火虫
        "revWhite": True,   # 反白 | 白雪皑皑
        "hide": True,       # 隐藏 | 嘘...
        "delLine": True     # 删除线 | 这是机密
    },
    "text": "Text"          # 需要显示的文字
}
```

### waziConfig

> 宏大叙事崩塌了吗，那该来点无调性音乐了。

我原本把它计划地像一个码头，现在看来大概只是一个拉货的，额。本来应该承担配置的读写和设置的工作，结果主模块最合适设置，这个也不太想做写入，如果有写入的话，那应该就比现在大【指结构（包括 sites 内容）】了。

所以它只能读取配置文件并转换成对象，提供给主模块让它做设置。当然以后可能会做写入，会 `__init__.py` 写一个，那么那个时候很多想法都可以写入到这个模块里面了。

#### readConfig

> 只有我的王国！

只需要一个参数 `filePath`，是字符串，就可以读取配置文件，返回一个字典（只要你的配置文件存在并符合格式）。

### waziDebug

> 互联网，拯救我的不安。

如何处理一个错误：

1. 复制报错和代码；
2. Google 启动，在 stackoverflow 搜索；
3. 完事！

它是一个装饰器，并没有在任何地方使用，你可以使用：

```python
from mods import waziDebug as Wdb
debug = Wdb.waziDebug

@debug
def error():
    raise ValueError("This is a error!")

error()
```

类似这样的代码捕获错误，并打开对应的 `stackoverflow` 页面以快速了解该错误可能是什么以及触发的大致原因（它还是会使错误发生）。

### waziFileName

> 抹去你原有的历史。

为了使文件名在 Windows 下合法，你需要使用 `waziFileName` 模块以取得一个正常的过滤过的文件名（事实上，之前的有 BUG，我今天爬千恋万花的时候，发现 * 这个字符串我没给过滤，属于是谔谔了）。

#### toRight

> 扳回正轨，进入右派（大嘘）。

接受一个 `name` 字符串参数，函数会自动过滤其中的非法字符串：`\ / : * ? " < > |`，并返回一个新的字符串。如果没有啥需要过滤的，那么返回原来的字符串。

### waziFun

> 知道自己身处虚拟中。

在函数运行时获取函数的名称，并返回一个字符串。所以就别想着 `__name__` 了。

#### getFuncName

> 嘿。

透过 `inspect` 获取函数名称，并返回一个字符串。有些情况可能会导致 IndexError.

### waziLog

> 废话特别多的官方审查记录。

我只能说，日志系统无处不在，任何一条语句的上下都存在日志，已经代替了注释的存在，甚至对于赋值这类都要进行一个解释，我很想给当时的我一拳，他妈的，为什么要这么写。

大抵是当时还想着，追踪吧，万一哪天连赋值都会出错呢，一个完备的日志系统就可以解决这个问题。可惜现在看来，妈的，该报错还是报错，try catch 确实不知道该在那里用，日志系统也没能设计成我想的那样。

要是重新设计的话，我得换成 `logging` 顺便把各个模块的日志废话全给删了。

#### 被实例化时的操作

> 万物之初，宇宙还在载入地图。

在被实例化时，程序会自动执行创建日志文件夹和设置日志文件名的操作，见下文接口。

#### createLogsFolder

> 庇护所。

不需要任何参数，使用它会自动在当前目录下创建一个 `logs` 目录。

#### setSaveName

> 登记姓名，历史一样的。

设置日志文件名，不需要参数，同样会生成一个日志文件名，作为本次运行的日志文件名。格式是 `LOG_YYY-MM-DD HH.MM.SS.log`。

#### needSave

> 教科书上的历史需要校对。

设置是否需要保存日志，`boolean` 参数需要一个布尔值数据。程序一开始是设置成 `False` 的，所以默认不保存日志。

为什么不保存日志呢？因为日志文件是真他妈的大，一次简简单单地爬取一个 ExHentai 的本子，日志几个 MB。

#### setMinDisplayLevel

> 小心谨慎。

设置屏幕最低显示级别，需要一个整数参数 `levelNumber`。

+ -1 - 无日志
+ 0 - 只显示错误
+ 1 - 显示错误和警告
+ 2 - 显示错误、警告和信息
+ 3 - 显示错误、警告、信息和调试

-1 及以下，都表示不显示日志输出，3 及以上，都表示完全地显示日志输出。

#### outputLog

> 写，持续地写入，不断地写入。

用户可以通过 `outputLog` 接口输出日志，需要一个字符串参数 `text`，写入到目前所设置的日志文件中。

#### log

> FFDCA

通过 `log` 接口做到屏幕输出和日志写入，需要两个参数 `level` 和 `text`。

`level` 应当为如下几个 `debug, info, warn, error`，`text` 应当为一个字符串。程序会率先检查日志等级和设置的最低显示级别以决定是否通过 `color.print` 打印到屏幕，无论是否显示总是会通过 `outputLog` 把信息写入到日志文件中。

### waziRequest

> 当初，究竟是怀揣着什么样的心情去使用 `urllib` 的呢？

在 `urllib3` 更新到 1.26.4 亦或者附近的版本的时候，HTTPS 连接就必须用 HTTPS 方式进行，而不是 HTTP 方式。而 clash 所能支持的也只是 HTTP，当时我并不懂得这究竟如何，只是需要关闭系统代理就行。

可我尚不清楚那时的我为什么 `requests` 同样关闭代理之后也不能正常的使用，明明也是基于 `urllib3` 的，经过我 Google 半天，`verify = False` 参数也不行，设置代理也不行，关掉和开启系统代理也不行。我很奇怪，我也不知道为什么，也有可能是我的方式不对亦或者终端的环境有问题。再后来就是换系统了。

再再后来就给我造成了一个固定思维：以后别用 `requests` 了，自己去写一个请求模块。鉴于 Python 比较谔谔的模块混乱，于是我一开始使用了 `urllib`，因为它可以直接 https 填进去，到了后来发现这不行了，因为 ExHentai 长连接的需求，于是我换成了 `urllib3`。其实这中间我清楚，`requests` 在我这个新的环境下可以继续正常地使用了，结果奈何框架都写好了，所有的请求都靠着 `waziRequest` 这个模块来实现了，如果大费周章地把所有通过 `waziRequest` 的请求都换成 `requests` 的请求，那我确实是抖 M 属性了。如果把 `waziRequest` 的 `urllib3` 换成 `requests` 那同样没有必要，我所需求的范围，`urllib3` 和 `requests` 都可以，所以就先这样。

只能说，很神奇，很奇妙。

#### useProxies

> 代理，访问一些，不知道的网站。

通过该接口设置是否需要代理，需要一个布尔值参数 `isUse`，默认为 `False`。

#### editProxies

> 与文档无关的，我希求世界和平。

修改代理，需要两个参数 `http` 和 `port`，前者可以是一个字符串，后者可以是一个整数或字符串。你可以通过这个接口以设置代理，如果两个参数中有一方为 `None` 则设置为空的代理信息。

如果你在用户配置里面设置了开启代理，却没有指定代理地址，那么默认或会使用 `http://127.0.0.1:7890` 作为代理。

#### useHeaders

> 辨别我的身份，我需要守卫我的家园。

可以使用该接口设置是否需要设置请求头，需要一个布尔值参数 `isUse`，默认为 `False`。

事实上，基本上所有的站点模块都会把这个设置为真值。

#### editHeaders

> 献身。

如果你需要自定义请求头部，可以使用该接口进行设置，需要两个参数 `key` 和 `value`，前者是字符串，后者是任意对象。

#### overWriteHeaders

> 覆盖，使用敌军的武器。

如果你想直接替换当前的请求头，那么可以使用该接口以代替多个 `editHeaders` 方式。它需要一个参数 `headers`，这个参数是一个字典，程序会自动使用它替换掉当前的请求头。

#### delHeaders

> 为自由我们愿意献出灵魂和肉体。《乌克兰仍在人间》

删除一个请求头键值，需要一个字符串参数 `key`。这个接口同样可以被 `overWriteHeaders` 替换。如果你需要更多操作，可以直接修改 `headers` 变量。

#### get

> 我要拿起我的武器，保卫我的故土，保卫我的生活，保卫我的幸福。

该接口用来对一个地址发起 GET 请求，需要一个字符串参数 `url`，最后如果成功的话返回 `HTTPResponse` 对象。

#### post

> 报纸上，登记着战死的人们。

如果你需要发起一个 POST 请求，可以使用该接口，需要两个参数 `url` 和 `data`，前者是字符串，后者是字典，同样的，如果成功的话返回 `HTTPResponse` 对象。

#### fieldsPost

> 倘若战火继续，我也要轰轰烈烈地死去。

如果你需要发起一个带字段的 POST 请求，可以使用该接口，需要两个参数 `url` 和 `data`，前者是字符串，后者是字典，同样的，如果成功的话返回 `HTTPResponse` 对象。

#### put

> 或许以后会做人道救助相关的工作...

好吧，这个除了在 `PicAcg` 下，其他的模块都看不到，说起来啊，鸭鸭其实都是 `POST` 一梭子解决问题的，没有怎么做过 `RESTful API` 规范的 API 接口。

它需要需要两个参数 `url` 和 `data`，前者是字符串，后者是字典，重复的，如果成功的话返回 `HTTPResponse` 对象。

#### collectRequest

> 在那个时候，我们的世界就会变得更加美丽。

这个是综合请求，上文从 `get` 到 `put` 全都得通过这个接口实现，以减少每个函数对于代理池、新建请求等代码的再复制。它需要三个参数：`url` 表示请求地址，是一串字符串；`method` 是请求方法，是一个字符串；`data` 是请求数据，是一个字典。如果成功的话返回 `HTTPResponse` 对象，不成功返回空数据。

#### do

> 鼠鼠我啊，关于政治就讲到这里了。

这个接口用来分析传入的字典参数，根据参数需求设置代理和请求头并使用对应的请求接口，返回 `HTTPResponse` 对象。

这个字典参数的格式如下：

```python
{
    "useProxies": bool,
    "proxyAddress": str or None,
    "proxyPort": int, str or None,
    "useHeaders": bool,
    "headers": dict,
    "method": str,
    "url": str
}
```

#### handleParams

> 全面败北。

用来将用户的参数转换成 `do` 接口需要的参数（`data` 则需要你自己手动写入），返回一个字典。你需要五个参数：

+ `params` 表示用户的参数，是一个字典；
+ `method` 表示请求方法，是一个字符串；
+ `url` 表示请求地址，是一个字符串；
+ `deHeaders` 表示默认的请求头，是一个字典；
+ `deProxies` 表示默认的代理，是一个字典。

### waziURL

> ぼこぼこ

想来这个模块也是不必要的，因为看了看代码，很多时候也还是在手动拼接字符串，我大抵也想不到当时究竟为了什么而写的 waziURL，估计就是爬 ExHentai 的时候设置全参数比较舒服一点吧（尽管也没舒服到哪去）。

#### getFullURL

> 你的生活。

如果你需要拼接完整的 URL，那么这个可以使用这个接口，它需要两个参数：`url` 表示请求地址，是一个字符串；`params` 表示请求参数，是一个字典，返回 `str` 字符串。

#### getExHentaiAllURL

> Rest in peace.

好吧，这个只是给 ExHentai 用的，同样，它需要两个参数：`url` 表示请求地址，是一个字符串；`params` 表示请求参数，是一个字典，返回 `str` 字符串。只不过拼接时还会把过滤器关了，很多高级选项如搜索低能力（low-power）标签等都会被打开，搜索分类则是设置为全部。

## 站点模块

> 有时候，想了想，还是算了，还是摸了。

总共支持六个站点，所以存在六个站点模块，尽管它们都一个文件上千行，有考虑过拆分出来，但后来想想与其拆分，不如拿这个时间去陪陪自己的家人，出去走走，而不是对着我自己也不明白的代码看到头疼。

### waziAsianSister

> 哈哈。

我本来是想找一个 Cosplay 图集网站作为我下一次更新内容的，结果找了半天，我觉得还不如 PicAcg 和 ExHentai 的 Cosplay 区实在。然后我就看到了 AsianSister，还是可以用它水一个模块的，正好也当练练手了。（只不过它网站源码写的很抽象）（好吧，我也没有资格评价）

#### giveParams

> 伊始。

设置用户参数（即上文主模块的 `params`），参数是 `params` 字典，完成之后返回当前用户的参数，同样是字典。

格式如下：

```python
{
    "useProxies": True,             # 要不要用代理
    "proxyAddress": "127.0.0.1",    # 代理地址
    "proxyPort": 7890,              # 代理端口（整数或者字符串）
    "useHeaders": True,             # 要不要用请求头（不需要写这个其实，程序会自己写好的）
    "headers": {}                   # 自定义请求头（字典，同样，程序会自动补全的）
}
```

#### returnSoup

> Imagine all the people, living life in peace... --John Lennon

通过该接口获取一个网站的 BeautifulSoup 对象，参数是 `link` 字符串，如果无法获取到网页信息，则返回 `<html></html>` 的 BeautifulSoup 对象。

#### downloadFile

> Hopeless.

该接口需要三个参数以下载文件，`url`字符串、 `fileName`字符串、 `filePath`字符串，如果下载失败，则返回`False`；成功时返回`True`。

#### parseVideo

> 政客建立对立，人类祈求和平，所以黄色网站确实很和谐（笑） -A

该接口的参数是 `BeautifulSoup` 对象，应当是某个视频的地址，返回值为视频基本信息，例如标题、播放数、标签等等。更详细的格式如下：

```python
{
    "title": str,                                   # 视频的标题
    "views": int,                                   # 视频的播放量
    "tags": list[dict{"name": str, "link": str}],   # 视频的标签
    "cover": str,                                   # 视频的封面
    "url": str,                                     # 视频的文件地址
    "comments": list[dict{                          # 视频的评论
        "user": str,                                # 评论者的用户组
        "avatar": str,                              # 评论者的头像
        "name": str,                                # 评论者的名字
        "time": str,                                # 评论时间
        "content": str                              # 评论内容
    }],                                             
    "recommends": list[dict{                        # 该视频的有关推荐
        "title": str,                               # 推荐视频的标题
        "link": str,                                # 推荐视频的地址
        "cover": str,                               # 推荐视频的封面
        "views": int                                # 推荐视频的播放量
    }]
}
```

#### parseGallery

> Please make love, not war. -A

该接口的参数是 `BeautifulSoup` 对象，应当是某个画廊的地址，返回值为画廊信息，大致同 `parseVideo`，可以阅读下文的格式：

```python
{
    "title": str,                                       # 画廊的标题
    "stars": str,                                       # 画廊的评分，分数 / 总分
    "category": dict{"name": str, "link": str},         # 画廊的分类
    "tags": list[dict{"name": str, "link": str}],       # 画廊的分类
    "description": str,                                 # 画廊的描述
    "model": dict{"name": str, "link": str},            # 画廊中出演的任务
    "covers": list[dict{"link": str, "alt": str}],      # 画廊的封面
    "pictures": list[dict{"link": str, "org": str}],    # 画廊的图片
                                                        # org: 原图，link: 压缩图
    "pageNum": int,                                     # 画廊的页数
    "comments": list[dict{                              # 画廊的评论
        "user": str,                                    # 评论者的用户组
        "avatar": str,                                  # 评论者的头像
        "name": str,                                    # 评论者的名字
        "time": str,                                    # 评论时间
        "content": str                                  # 评论内容
    }],                                                 
    "galleries": list[dict{                             # 画廊的推荐画廊
        "link": str,                                    # 推荐画廊的地址
        "cover": str,                                   # 推荐画廊的封面
        "alt": str,                                     # 推荐画廊的 alt 属性
        "title": str,                                   # 推荐画廊的标题
        "stars": str,                                   # 推荐画廊的评分
        "VIP": bool                                     # 是否是 VIP 画廊
    }],
    "videos": list[dict{                                # 画廊的推荐视频
        "data": str or None,                            # 推荐视频的动画封面 没有就是 None 不是很清楚这个
        "link": str,                                    # 推荐视频的地址
        "title": str,                                   # 推荐视频的标题
        "cover": str,                                   # 推荐视频的封面
        "VIP": bool                                     # 是否是VIP视频
    }]
}
```

#### parsePerson

> 查成分 -A

该接口的参数是 `BeautifulSoup` 对象，应当是某个人物的地址，返回值为个人主页信息，同上两个接口。详细信息可以见：

```python
{
    "name": str,                                    # 名字
    "descriptionHTML": str,                         # 描述（使用 HTML 语言）
    "views": int,                                   # 浏览量
    "tags": list[dict{                              # 标签
        "name": str,                                # 标签名
        "link": str                                 # 标签链接
    }],
    "galleries": list[dict{                         # 相关推荐画廊
        "link": str,                                # 画廊的地址
        "cover": str,                               # 画廊的封面
        "alt": str,                                 # 画廊的 alt 属性
        "title": str,                               # 画廊的标题
        "stars": str,                               # 画廊的评分
        "VIP": bool                                 # 是否是 VIP 画廊
    }],
    "videos": list[dict{                            # 相关推荐视频
        "data": str or None,                        # 推荐视频的动画封面 没有就是 None 不是很清楚这个
        "link": str,                                # 推荐视频的地址
        "title": str,                               # 推荐视频的标题
        "cover": str,                               # 推荐视频的封面
        "VIP": bool                                 # 是否是 VIP 视频
    }]
}
```

#### parseRecommendImagesAndVideos

> 政治和权利都只是别有用心的人的玩物罢了，不要过度相信推送 -A

该接口的参数是 `BeautifulSoup` 对象。网页代码中需要包含 `<div class="recommentBox"></div>` 和 `<div class="recommentBoxVideo"></div>`，用于处理画廊等的推荐内容解析，详细返回格式可以见下文。

它返回的是元组，尽管我也不知道为什么我会这么设计。

```python
(
    list[dict{                                      # 推荐的画廊
        "link": str,                                # 画廊的地址
        "cover": str,                               # 画廊的封面
        "alt": str,                                 # 画廊的 alt 属性
        "title": str,                               # 画廊的标题
        "stars": str,                               # 画廊的评分
        "VIP": bool                                 # 是否是 VIP 画廊
    }],
    list[dict{                                      # 推荐的视频
        "data": str or None,                        # 推荐视频的动画封面 没有就是 None 不是很清楚这个
        "link": str,                                # 推荐视频的地址
        "title": str,                               # 推荐视频的标题
        "cover": str,                               # 推荐视频的封面
        "VIP": bool                                 # 是否是 VIP 视频
    }]
)
```

#### parseImagesAndVideos

> 人类从不吸取教训 -A

该接口的参数是 BeautifulSoup 对象，可以是搜索结果也可以是单纯的页面，例如 `https://asiansiter.com/`；返回值与 `parseRecommendImagesAndVideos` 几乎相同，但存在差异：

```python
(
    list[dict{
        "views": int,
        "link": str,
        "vip": bool,
        "cover": str,
        "alt": str,
        "title": str
    }],
    list[dict{
        "data": str or None,
        "views": int,
        "link": str,
        "vip": bool,
        "cover": str,
        "title": str
    }]
)
```

多了一个 `views` 字段，表示浏览量。

#### getPage

> 相比魔怔人，我还是喜欢 mmr，当然，像我一样做个不出声的乐子人也行 -A

使用该接口以获取第几页的内容解析，参数是 `page` 整数，为页面数字（第一页即为 1），返回值同样是一个元组包两个 `list` 的 `parseImagesAndVideos` 返回值，不多赘述。

#### search

> 刚吃完午饭的下午可太困了 -A

使用该接口以在该网站上进行搜索，该接口有两个参数，`keyword` 字符串与 `page` 基本整型，返回同样依赖 `parseImagesAndVideos` 返回值。

#### tagsearch

> 定向研究 -A

使用该接口以在该网站上进行标签搜索，该接口有两个参数，`tag` 字符串与 `page` 基本整型，返回还是同样跟 `parseImagesAndVideos` 无异。

#### personSearch

> 别查了，我什么成分都没有 -A

使用该接口以在该网站上进行人物搜索，该接口参数为 `person` 字符串，返回的是字典，它的格式与 `parsePerson` 的返回值相同。

#### getGallery

> 似乎快完了 -A

使用该接口获取一个画廊的信息，该接口参数是 `gallery` 字符串，应当是 `https://asiansister.com/...` 后面的内容，返回格式与 `parseGallery` 无异。

#### getVideo

> 施法，施法 -A

该接口的参数为 `video` 字符串，同样应当是 `https://asiansister.com/...`，后面的内容的返回格式是 `parseVideo` 的返回值。

#### customParse

> “第一阶段战略目标实现”（笑） -A

该接口的参数为 `content` 字符串和 `type` 字符串。如果 `type` 是 `main / tag / search` 的话会让 `parseImagesAndVideos` 去解析，如果是 `person` 的话会通过 `parsePerson` 去做，如果是 `gallery` 的话会通过 `parseGallery` 去做，如果是 `video` 的话会通过 `parseVideo` 去做。

`content` 字符串将与 `https://asiansister.com/` 进行拼接以获取完整的 URL。

### waziDanbooru

> 神明伟大，开放世界的创始逻辑和日志

`Danbooru` 和开源 API，你好 `Danbooru`，就喜欢和开源 API 的连，因为开源 API 确实比闭源 API 有点素质，不是夸你们开源 API 呢。

#### giveParams

> 白日做梦

设置用户参数，参数是 `params` 字典，完成之后返回当前用户的参数，同样是字典。这个在 `waziAsianSister` 中有写到，后面所有模块都有这个接口，所以不多赘述。

#### setApi

> 摸鱼去了

世界上有很多个 `Danbooru` 类网站，你可以通过这个接口设置当前所要爬取的 `Danbooru` 网站的主域名，参数是 `url` 字符串，返回值是你所设置的 `Danbooru` 网站的主域名。

#### toAPIJson

> 新的摆烂的一周 -A

该接口是会给 API 发送一个请求并返回 `json`，接口参数为 `port` 字符串（API 路径地址）与 `params` 字典，即请求数据参数，如：

```python
waziDanbooru.toAPIJson('/posts.json', {'tags': 'tag1 tag2'})
```

#### getPosts

> Simple, not harmonic, motion -A

用于获取 `Posts` 信息，该接口的参数是 `page` 字符串或整数，表示页码，从 1 数起；`tags` 字符串，表示标签；`limit` 整数或字符串（*上限是40，可能不同网站有不同的设置*），返回一个 `list`。

举例如下（Konachan）：

```python
[{
    'id': 334447,
    'tags': 'asamura_hiori bikini blush breasts brown_hair choker cleavage cross fang gradient green_eyes katana long_hair magic original skirt swimsuit sword thighhighs weapon zettai_ryouiki',
    'created_at': 1636920653,
    'creator_id': 73632,
    'author': 'otaku_emmy',
    'change': 2071516,
    'source': 'https://www.pixiv.net/en/artworks/94143720',
    'score': 32,
    'md5': 'a2e11789abfdd59830b33f2598b5de5e',
    'file_size': 4911373,
    'file_url': 'https://konachan.com/image/a2e11789abfdd59830b33f2598b5de5e/Konachan.com%20-%20334447%20bikini%20blush%20breasts%20brown_hair%20choker%20cleavage%20cross%20fang%20gradient%20green_eyes%20katana%20long_hair%20magic%20original%20skirt%20swimsuit%20sword%20thighhighs%20weapon.png',
    'is_shown_in_index': True,
    'preview_url': 'https://konachan.com/data/preview/a2/e1/a2e11789abfdd59830b33f2598b5de5e.jpg',
    'preview_width': 150,
    'preview_height': 89,
    'actual_preview_width': 300,
    'actual_preview_height': 179,
    'sample_url': 'https://konachan.com/sample/a2e11789abfdd59830b33f2598b5de5e/Konachan.com%20-%20334447%20sample.jpg',
    'sample_width': 1500,
    'sample_height': 893,
    'sample_file_size': 349306,
    'jpeg_url': 'https://konachan.com/jpeg/a2e11789abfdd59830b33f2598b5de5e/Konachan.com%20-%20334447%20bikini%20blush%20breasts%20brown_hair%20choker%20cleavage%20cross%20fang%20gradient%20green_eyes%20katana%20long_hair%20magic%20original%20skirt%20swimsuit%20sword%20thighhighs%20weapon.jpg',
    'jpeg_width': 3500,
    'jpeg_height': 2084,
    'jpeg_file_size': 615611,
    'rating': 's',
    'has_children': False,
    'parent_id': None,
    'status': 'active',
    'width': 5879,
    'height': 3500,
    'is_held': False,
    'frames_pending_string': '',
    'frames_pending': [],
    'frames_string': '',
    'frames': []
}]
```

#### downloadFile

> 许多杰出的行动都应归功于偶然， 然而将军和政客们却将掌声和欢呼占为己有。 ——亨利·霍姆 -A

该接口通过三个参数下载文件。参数是 `url` 字符串，代表下载的链接；`orgName` 字符串，代表文件的名称；`path` 字符串，代表保存文件的路径。如果下载成功，则返回 `True`，反之则返回 `False`。

#### download

> 或许人类根本没有自由意志，世间万物都是大脑放出的幻象罢了 -A

该接口用于从 `Posts` 列表中下载链接。分别是 `posts` 列表，代表 `post` 的信息；`path` 字符串，代表保存文件的路径，`key` 字符串，代表指定下载链接的 `key`，返回一个有下载信息的`tuple`，格式是：

```python
(
    list[str],                                      # 下载的文件
    list[dict{fileURL: str, id: int}]               # 下载失败的文件
)
```

#### downloadPosts

> 我们无法观测物自体，正如我们无法了解任何事件的绝对真相。我们能看到的东西或许都是别人想让我们看到的 -A

从 API 处下载 `posts` 图片，是 `download` 和 `getPosts` 的友善写法，接口有五个参数。依次是 `page` 字符串或整数，表示页码，从 1 开始；`tag` 是字符串，表示标签；`limit` 是整数或是字符串，表示 `posts` 的上限，最大为 `40`（不同网站或有不同的 limit）；`path` 字符串，代表文件保存的路径；`key` 字符串是下载文件地址对应的键，默认为 `file_url`，返回一个有下载信息的`tuple`，格式同上不多赘述。

#### getSizeLimit

> 拉普拉斯的超级存在体 -A

*作者声明未来可能移除该功能*

该接口用于生成尺寸搜索备忘单字符串，该接口的参数是 `size` 字典，形如：

```python
{
    "width": int or str,            # 宽度
    "height": int or str,           # 高度
    "limit": str                    # b 大于 s 小于 e 等于
}
```

所有生成搜索备忘单字符串的接口都会在末尾存在 ` `（即空格）以方便用户与其个人标签进行拼接。

#### getOrder

> 美好的每一天 -A

*作者声明未来可能移除该功能*

该接口用于生成排序搜索备忘单字符串，该接口的参数是 `order` 列表，支持的排序方式有：

```python
["score", "fav", "wide", "nonwide"] # 包括你可以自定义排序方式
# 按分数排序 | 收藏数排序 | 从大图排序 | 从小图排序
```

#### getRating

> 不知道写什么就只能写一点鄙人的见闻和拙见了（笑） -A

*作者声明未来可能移除该功能*

该接口的参数是 `ratingType` 列表，还适用于生成限制搜索备忘单字符串，支持的有：

```python
["safe", "questionable", "explicit", "questionableplus", "questionableless"] # 包括你可以自定义类型
# 安全 | 可能存在限制 | 限制 | 可能存在限制（包括限制） | 可能存在限制（包括安全）
```

#### getTags

> 不是因果逻辑，而是概率 -A

该接口用于获取一个 `Danbooru` 网站的 `tags` 内容，该接口的参数有 `page` 整数或字符串，表示从 1 到底的页面编号；`limit` 整数或字符串，表示上限，一些网站是 `50`，或每个网站都不一致；`order` 字符串，有 `date`, `name`, `count` 三种类型，允许你使用按日期排序、按名称排序和按数量排序，返回一个标签列表，格式（可能）如下：

```python
[{'id': int, 'name': str, 'count': int, 'type': int, 'ambiguous': bool}]
```

#### getArtists

> 无为而治 - 道德经

该接口用于获取一个 `Danbooru` 网站的艺术家内容，需要两个参数：`page` 表示页码，从 1 开始数起，可以是字符串或整数；`order` 字符串，有 `date`, `name` 三种类型，允许你使用按日期排序和按名称排序这两种方式进行请求，最后返回一个艺术家列表，格式（可能）如下：

```python
[{
    'id': int,
    'name': str,
    'alias_id': None or int or str,
    'group_id': None or int or str,
    'urls': [str]
}]
```

#### getComment

> 人生天地之间，若白驹过隙，忽然而已。 —— 庄子

该接口用于获取一个 `Danbooru` 的评论，它需要一个参数，即 `commentId` 可以是整数也可以是字符串，表示评论的 ID，返回一个评论字典，格式（可能）如下：

```python
{
    "id": int,
    "created_at": str,
    "post_id": int,
    "creator": str,
    "creator_id": int,
    "body": str
}
```

#### getPools

> 呜呼哀哉

如果你想搜索一个图集可以使用该接口，它需要两个参数：`query` 表示搜索内容，是字符串；`page` 表示页码，从 1 开始数起，可以是字符串或整数。最后返回一个图集列表，格式（可能）如下：

```python
[{
    'id': int,
    'name': str,
    'created_at': str,
    'updated_at': str,
    'user_id': int,
    'is_public': bool,
    'post_count': int,
    'description': str
}]
```

#### getPoolFromId

> 有考虑重新拿 JavaScipt 写一下这个项目

如果你获取到了一个图集的 ID，那么你可以通过该接口获取图集的详细信息，它需要两个个参数：`poolId` 可以是整数也可以是字符串，表示图集的 ID；`page` 同样可以是字符串或者整数，表示页码，从 1 数起，返回一个图集字典，举例（Konachan）如下：

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
    'posts': [{
        'id': 306979,
        'tags': 'aqua_eyes blonde_hair blush breasts choker cleavage close headband long_hair parody sailor_moon sailor_moon_(character) school_uniform tsukimaru tsukino_usagi twintails',
        'created_at': '2020-05-18T06:13:47.090Z',
        'creator_id': 257706,
        'author': 'Dreista',
        'change': 1845780,
        'source': 'https://www.pixiv.net/artworks/81661508',
        'score': 49,
        'md5': '8ce8b8db600fab17dc05bfc9c28157a5',
        'file_size': 6173818,
        'file_url': 'https://konachan.com/image/8ce8b8db600fab17dc05bfc9c28157a5/Konachan.com%20-%20306979%20aqua_eyes%20blonde_hair%20blush%20breasts%20choker%20cleavage%20close%20headband%20long_hair%20parody%20sailor_moon%20school_uniform%20tsukimaru%20tsukino_usagi%20twintails.png',
        'is_shown_in_index': True,
        'preview_url': 'https://konachan.com/data/preview/8c/e8/8ce8b8db600fab17dc05bfc9c28157a5.jpg',
        'preview_width': 150,
        'preview_height': 96,
        'actual_preview_width': 300,
        'actual_preview_height': 191,
        'sample_url': 'https://konachan.com/sample/8ce8b8db600fab17dc05bfc9c28157a5/Konachan.com%20-%20306979%20sample.jpg',
        'sample_width': 1500,
        'sample_height': 956,
        'sample_file_size': 586758,
        'jpeg_url': 'https://konachan.com/jpeg/8ce8b8db600fab17dc05bfc9c28157a5/Konachan.com%20-%20306979%20aqua_eyes%20blonde_hair%20blush%20breasts%20choker%20cleavage%20close%20headband%20long_hair%20parody%20sailor_moon%20school_uniform%20tsukimaru%20tsukino_usagi%20twintails.jpg',
        'jpeg_width': 4050,
        'jpeg_height': 2580,
        'jpeg_file_size': 1177937,
        'rating': 's',
        'has_children': False,
        'parent_id': None,
        'status': 'active',
        'width': 4050,
        'height': 2580,
        'is_held': False,
        'frames_pending_string': '',
        'frames_pending': [],
        'frames_string': '',
        'frames': []
    }]
}
```

#### downloadPool

> 额，后悔吗，好像没有

通过该接口以下载图集的单页，需要四个参数：`poolId` 可以是整数也可以是字符串，表示图集的 ID；`page` 同样可以是字符串或者整数，表示页码，从 1 数起；`path` 是字符串，表示下载目录；`key` 表示下载 URL 对应的键，默认为 `file_url`，也可以是其他键，如 `jpeg_url`，`sample_url` 等。最后返回元组表示下载情况：

```python
(
    list[str],                                      # 下载的文件
    list[dict{fileURL: str, id: int}]               # 下载失败的文件
)
```

#### downloadPoolWithZip

> 现在看来设计的太复杂了

通过压缩包的格式以下载完全的图集，一些网站如 `yande.re` 会提供这种功能，你使用它之前请确保你所爬取的网站是否存在这个功能，需要三个参数：`poolId` 可以是整数也可以是字符串，表示图集的 ID；`needJPG` 应当是布尔值，表示是否以 JPG 格式下载；`path` 应当是字符串，表示下载目录。最后如果返回 `True` 表示下载成功，否则下载失败。

#### customApi

> 快竣工了

自定义 API 接口请求，一些网站的请求接口可能不太一样，如果你还希望使用 `PyWazi` 的话，我提供给你了一个 `customApi` 接口以用于自行请求，它会帮助你最后得到一个对象，可能是字典也可能是列表，根据情况你自己进行解析，相对于 `toAPIJson` 来说，这个接口只是日志上显得好看一些。你需要两个参数：`port` 即请求 API 路径，跟在 URL 的后面的，是字符串；`params` 即请求数据，是字典或者列表，可以是单纯的 `{}`。

最后会返回一个字典或列表，如果成功的话。

### waziExHentai

> 近在咫尺

ExHentai 是 E-Hentai 的里站，提供了更多的画廊和图集，在 PyWazi 中，我们只支持 ExHentai 站点，或许在未来会尝试支持 E-Hentai 站点。

#### giveParams

> 个人内容消失，因为争议性的内容

设置用户参数，参数是 `params` 字典，完成之后返回当前用户的参数。在上文有更多说明，不做过多解释。

#### setParse

> 我会死去，你也会死去，我们都会死去。

设置是否使用自定义解析器，参数是 `boolean` 布尔值，完成之后返回当前设置。如果设置为 `true`，则使用自定义解析器，会根据当前账户的显示模式以设置对应的解析函数，否则强制使用默认解析器（即将账户强制使用 `Extended` 显示，会对你的正常浏览造成可能的影响）。

#### setCookies

> 脖子上的铁链，看客无动于衷。

设置你的账户 Cookies 信息，在进行任何操作之前，这个行为是必要的，参数是 `cookies` 字符串，完成之后返回当前设置。如何获取你的 `cookies` 可以见下文操作：

1. 使用已经登录好 ExHentai 的账号的浏览器访问 `exhentai.org`;
2. 打开 Console （不同的浏览器可能方式不一样，手机浏览器就，额，url 写 `javascript:` 把），输入 `document.cookie` 即可获得你的 `cookies` 信息；
3. 把 `cookies` 信息填入参数。

#### needFullComments

> “我们的终点是在这里，在这里，我们的终点是在这里。” —— 漫画家阿尔萨斯

设置是否需要完整的评论，参数是 `boolean` 布尔值，完成之后返回当前设置。如果设置为 `True`，则会在评论中显示完整的评论，否则只可能显示部分的评论。

#### changeThumbnailMode

> Copilot 创造了一个不存在的人类。

修改缩略图显示模式，参数是 `method` 字符串，完成之后返回当前设置。应当是 `normal` 或 `large` 之一，如果是 `normal` 则会使用普通的缩略图，如果是 `large` 则会使用大图。其他值会引发错误。

#### changeMethod

> （主语丢失）也从此作为普通人，幸福地生活下去便好…… —— 千恋 * 万花

修改画廊主页显示模式，参数是 `method` 字符串，完成之后返回当前设置。应当是 `Minimal, Minimal+, Compact, Extended, Thumbnail` 之一。其他值会保持现状，并报出日志警告。

#### setJump

> 警告明天的幸福，丧钟。

设置是否跳过画廊警告，需要一个布尔值参数 `jumpNeed`，完成之后返回当前设置。如果设置为 `True`，则会跳过画廊警告，否则不会。如果有些画廊存在警告但不跳过，程序在解析时可能会直接崩溃，你可以使用 `try` 语句来捕获错误，在以后会考虑支持默认跳过警告的功能。

#### getDisplayMode

> 身份证上的签名，签名上的身份证。

获取当前的显示模式，需要主页或搜索结果的 `soup` 参数，是 `BeautifulSoup` 对象，完成之后返回当前的显示模式。如果没有的话，会报错返回空字符串。

#### getMainInfo

> 我们都是精神病人 -A

该接口通过分析器来解析索引页或搜索页，参数为 `soup`，一个 `BeautifulSoup` 对象；`parserType`，为分析器种类，有 `Extended`, `Minimal`, `Minimal+`, `Compact`,`Thumbnail` 几种，分别会交由以下几个函数处理：

+ Extended -> waziExHentai.getExtendedMain
+ Minimal -> waziExHentai.getMinimalMain
+ Minimal+ -> waziExHentai.getMinimalPlusMain
+ Compact -> waziExHentai.getCompactMain
+ Thumbnail -> waziExHentai.getThumbnailMain

如果没有的话，会报错返回空字符串。

#### getRatingNum

> 骗人的 lifegame -A 

**Roleplay so hard, even in life.**  

**角色扮演太难了，即使是在现实生活中。**

该接口用于返回评分，参数是 `soup`，同样是 `BeautifulSoup` 对象，返回浮点数或是整数，代表评分。`soup` 对应的代码是：

```html
<div class="ir" style="background-position:-16px -1px;opacity:1"></div>
```

类似这种单 img 标签的 HTML 代码，要求存在 `style` 参数，并且要有 `background-position` CSS 内容。

#### getMinimalJSON

> 如果我们都是精神病，我们就不用为我们的错误承担责任了，因为，我们所做的事情都不受我们个人的控制；换言之，我们人类没有自由意志可言 -A

该接口用于分析 Minimal 的页面，接口参数为 `soup`，`BeautifulSoup` 对象，和一个 `parseType` 字符串，可以是 `normal` 或 `plus` 分别表示 `Minimal` 和 `Minimal+`，返回一个带有基本信息的字典文件。

普通格式：

```python
{
    "title": str,                               # 画廊标题
    "URL": str,                                 # 画廊地址
    "cat": str,                                 # 画廊分类
    "cover": str,                               # 画廊封面
    "uploader": str,                            # 画廊上传者
    "uploaderURL": str,                         # 画廊上传者地址
    "time": str,                                # 画廊上传时间
    "hasTorrents": bool,                        # 是否有种子
    "rating": int or float,                     # 画廊评分
    "pages": str                                # 画廊页数
}
```

Plus 格式：

```python
{
    "title": str,                               # 画廊标题
    "URL": str,                                 # 画廊地址
    "cat": str,                                 # 画廊分类
    "cover": str,                               # 画廊封面
    "uploader": str,                            # 画廊上传者
    "uploaderURL": str,                         # 画廊上传者地址
    "time": str,                                # 画廊上传时间
    "hasTorrents": bool,                        # 是否有种子
    "rating": int or float,                     # 画廊评分
    "pages": int,                               # 画廊页数
    "others": {                                 # 其他信息
        "type": "Minimal+ Own Information",     # 画廊特殊信息
        "has": ["markedTags"],                  # 是否有标记标签
        "markedTags": [{                        # 标记标签
            "title": str,                       # 标记标签标题
            "className": str,                   # 标记标签类名
            "style": str,                       # 标记标签样式
        }]
    }
}
```

#### itgGltmDel

> 生活就像强奸，如果不能反抗，那就尝试着去享受 -A

该接口的参数是 `soup`，`BeautifulSoup`；以及一个 `className` 字符串，返回一个含有 `BeautifulSoup` 对象的 `list`，包含所有搜索结果，会去除头内容，用于各类解析器中，`className` 通常是 `itg gltm`。

#### getMinimalMain

> 风沙

获取普通模式的 `Minimal` 下的主页或搜索内容，需要一个 `soup` 参数。透过 `itgGltmDel` 获取内容和使用 `getMinimalJSON` 进行解析。

返回格式同 `getMinimalJSON` 的普通模式。

#### getMinimalPlusMain

> 知晓自我

获取 `Minimal+` 即 `Plus` 模式的 `Minimal` 下的主页或搜索内容，需要一个 `soup` 参数。同样会透过 `itgGltmDel` 获取内容和使用 `getMinimalJSON` 进行解析。

返回格式同 `getMinimalJSON` 的 `Plus` 模式。

#### getCompactMain

> 我好想当个普通人，普通地读书，普通地工作，普通地生老病死 -A

获取 `Compact` 模式下的主页或搜索内容，还是需要一个 `soup` 参数。返回一个解析的结果列表。其返回格式如下：

```python
[{
    "title": str,                               # 画廊标题
    "URL": str,                                 # 画廊地址
    "cat": str,                                 # 画廊分类
    "cover": str,                               # 画廊封面
    "uploader": str,                            # 画廊上传者
    "uploaderURL": str,                         # 画廊上传者地址
    "time": str,                                # 画廊上传时间
    "hasTorrents": bool,                        # 是否有种子
    "rating": int or float,                     # 画廊评分
    "pages": int,                               # 画廊页数
    "others": {                                 # 其他信息
        "type": "Compact Own Information",      # 画廊特殊信息
        "has": ["tags"],                        # 画廊特殊信息存在的键
        "tags": [{                              # 画廊标签
            "title": str,                       # 画廊标签标题
            "className": str,                   # 画廊标签类名
            "style": str                        # 画廊标签样式
        }]
    }
}]
```

#### getThumbnailMain

> 钓鱼

获取 `Thumbnail` 模式下的主页或搜索内容，不管怎么说 `soup` 是一定需要的，同样的，还是会返回一个结果列表，但是相较于其他模式，它少了一些内容（上传者信息的丢失）：

```python
[{
    "title": str,                               # 画廊标题
    "URL": str,                                 # 画廊地址
    "cat": str,                                 # 画廊分类
    "cover": str,                               # 画廊封面
    "uploader": "Uploader information is not available in thumbnail mode. / 缩略模式下无法获取上传者信息。",
    "uploaderURL": "Uploader information is not available in thumbnail mode. / 缩略模式下无法获取上传者信息。",
    "time": str,                                # 画廊上传时间
    "hasTorrents": bool,                        # 画廊是否存在种子
    "rating": int or float,                     # 画廊评分
    "pages": int,                               # 画廊页数
    "others": {                                 # 其他信息
        "type": "Thumbnail Own Information",    # 画廊特殊信息
        "has": ["markedTags"],                  # 画廊特殊信息存在的键
        "markedTags": [{                        # 画廊标签
            "title": str,                       # 画廊标签标题
            "className": str,                   # 画廊标签类名
            "style": str                        # 画廊标签样式
        }]
    }
}]
```

#### getExtendedMain

> 每天五条推 抑郁远离我（

获取 `Extended` 模式下的主页或搜索内容，怎么说呢，还是需要 `soup`，返回如下：

```python
[{
    "title": str,                               # 画廊标题
    "URL": str,                                 # 画廊地址
    "cat": str,                                 # 画廊分类
    "cover": str,                               # 画廊封面
    "uploader": str,                            # 画廊上传者
    "uploaderURL": str,                         # 画廊上传者地址
    "time": str,                                # 画廊上传时间
    "hasTorrents": bool,                        # 画廊是否存在种子
    "rating": int or float,                     # 画廊评分
    "pages": int,                               # 画廊页数
    "others": {                                 # 其他信息
        "type": "Extended Own Information",     # 画廊特殊信息
        "has": ["tags"],                        # 画廊特殊信息存在的键
        "tags": [{                              # 画廊标签
            "title": str,                       # 画廊标签标题
            "className": str,                   # 画廊标签类名
            "style": str                        # 画廊标签样式
        }]
    }
}]
```

#### getBooks

> 距离结束需要很长一段时间

倘若你不想通过上面几个函数，你需要自己去通过接口获取 `soup` 然后再根据情况传入什么解析器或者别的乱七八糟的东西，不如直接使用 `getBooks` 接口传入 `url` 字符串参数，以进行解析。

格式会自动根据用户设置的解析器情况自动返回。

#### browse

> 知道那段历史

浏览主页的接口，会根据用户的默认设置进行浏览的哦。需要一个参数 `page` 可以是字符串或者整数，从 0 数起，表示页码。返回格式同 `getMainInfo` 接口。

#### allBrowse

> 资料库，对公众的完全开放

同样是浏览接口，但它会直接无视掉你的默认设置和过滤器，并启用可能会使你返回内容更多的选项。同样需要一个参数 `page` 可以是字符串或者整数，从 0 数起，表示页码，返回格式不再赘述。

选项一览：

```python
{
    "f_cats": "0",
    "advsearch": "1",
    "f_sname": "on",
    "f_stags": "on",
    "f_sh": "on",
    "f_sdt2": "on",
    "f_sfl": "on",
    "f_sfu": "on",
    "f_sft": "on"
}
```

#### search

> 谔谔

搜索接口，使用用户默认设置，需要两个参数：`page` 表示页码，从 0 数起，整数或字符串；`text` 表示搜索关键词，字符串。

#### allSearch

> 能量不足，前去摸鱼

同样表示搜索接口，但会与 `allBrowse` 一致，无视掉你的默认设置，需要两个参数：`page` 表示页码，从 0 数起，整数或字符串；`text` 表示搜索关键词，字符串。

#### tagSearch

> Epoch 13/50

使用该接口进行标签搜索，你需要两个参数：`page` 和 `tag`。前者是字符串或整数，从 0 数起，表示页码；后者是标签名，字符串，要求如 `artist:matsuriuta` 之类的格式。

#### tagAllSearch

> 雅

使用该接口进行全部标签搜索，emmm，我知道你想说什么，能不能不要这么多接口，似乎有点脱裤子放屁的意思，都一个方法，能不能凑一块写，其实我也不知道。总而言之，你需要两个参数：`page` 和 `tag`。前者是字符串或整数，从 0 数起，表示页码；后者是标签名，字符串，要求如 `artist:matsuriuta` 之类的格式。

#### uploaderSearch

> 这是一种错误。

使用该接口进行上传者搜索，好吧，请原谅一下我写这么多接口，下文会提供一个更不错的接口以代替的。需要 `page` 和 `uploader` 参数，前者不赘述，后者注意需要删除 `uploader:` 前缀。

#### uploaderAllSearch

> 进入了无可挽回的局面

使用该接口进行上传者全部搜索，参数同上，不重复赘述。

#### advancedSearch

> loss: 0.3474 - accuracy: 0.8619

这是提供高级搜索的接口，你需要一个字典参数：`params`，以下列出相关格式：

```python
{
    "cats": [str],                          # 需要搜索的分类，如 "Non-H"
    "search": str,                          # 需要搜索的内容
    "sgn": bool,                            # 是否搜索画廊名称
    "sgt": bool,                            # 是否搜索画廊标签
    "sgd": bool,                            # 是否搜索画廊描述
    "stf": bool,                            # 是否搜索种子名称
    "osgwt": bool,                          # 是否搜索只带有种子的画廊
    "slpt": bool,                           # 是否搜索带有 low-power 的标签
    "sdt": bool,                            # 是否搜索带有差评的标签
    "seg": bool,                            # 是否搜索被移除的标签
    "mr": bool,                             # 是否需要限定最低评分
    "mrs": int or str,                      # 最低评分，从 2 - 5
    "b": bool,                              # 是否需要限定搜索范围
    "b1": int or str,                       # 搜索范围的起始页码
    "b2": int or str,                       # 搜索范围的结束页码
    "dfl": bool,                            # 是否需要屏蔽语言过滤器
    "dfu": bool,                            # 是否需要屏蔽上传者过滤器
    "dft": bool,                            # 是否需要屏蔽标签过滤器
    "page": int or str                      # 页码，从 0 开始数起
}
```

#### imageSearch

> 第三拍，军鼓的声音，清脆

提供图片搜索的接口，你需要提供一个字典参数：`params`，以下列出相关格式：

给出图片的 `SHA-1` 值的做法：

```python
{
    "type": "sha1",                         # 填写 sha1 表示搜索 SHA-1 值
    "sha1": str,                            # 图片的 SHA-1 值
    "similar": bool,                        # 是否搜索相似图片
    "cover": bool,                          # 是否搜索封面图片
    "exp": bool                             # 是否搜索被移除的画廊
}
```

给出图片的本地路径值的做法：

```python
{
    "type": "path",                         # 填写 path 表示本地路径
    "path": str,                            # 图片的本地路径
    "similar": bool,                        # 是否搜索相似图片
    "cover": bool,                          # 是否搜索封面图片
    "exp": bool                             # 是否搜索被移除的画廊
}
```

#### customSearch

> 火柴盒

好了，如果你需要一个综合上面所有搜索接口的话，你可以使用这个接口，这大概就是大统一吧（尽管实现时是丑陋的），你需要提供一个字典参数：`params`，以下列出相关格式：

```python
waziExHentai.customSearch({
    "cats": ["Doujinshi", "Manga", "Artist CG", "Game CG"],
    # 需要搜索的分类，如果没有则程序不会指定搜索
    "uploaders": ["Pokom", "NekoHime27"],
    # 需要搜索的上传者，如果没有则程序不会指定搜索
    "tags": ["female:lolicon"],
    # 需要搜索的标签，如果没有则程序不会指定搜索
    "text": "",
    # 需要搜索的内容，如果没有则程序不会指定搜索
    "advanced": {  # 高级搜索参数，如果你需要的话
        "search": {
            "galleryName": True,  # 是否搜索画廊名称
            "galleryTags": True,  # 是否搜索画廊标签
            "galleryDescription": False,  # 是否搜索画廊描述
            "torrentFilenames": False,  # 是否搜索种子文件名
            "low-powerTags": False,  # 是否搜索 low-power 标签
            "downvotedTags": False,  # 是否搜索 downvoted 标签
            "expungedGalleries": False,  # 是否搜索被移除的画廊
        },
        "limit": {
            "onlyShowGalleriesWithTorrents": False,  # 是否只显示有种子的画廊
            "minimumRating": False,  # 是否限制最低评分
            "minimumRatingNumber": 2,  # 最低评分的值
            "between": False,  # 是否限制搜索范围
            "betweenPages": [0, 0]  # 搜索范围的页码，Index 0 表示起始页，Index 1 表示结束页
        },
        "disableFilters": {
            "language": False,  # 是否禁用语言过滤器
            "uploader": False,  # 是否禁用上传者过滤器
            "tags": False  # 是否禁用标签过滤器
        }
    },
    "file": {  # 文件搜索参数，如果你需要的话
        "main": {
            "type": "path",  # 文件类型，可选值为 path 和 sha1
            "value": "./a.jpg"  # 文件的本地路径或者 SHA-1 值
        },
        "options": {
            "useSimilarityScan": True,  # 是否使用相似度扫描
            "onlySearchCovers": False,  # 是否只搜索封面
            "showExpunged": False  # 是否显示被移除的画廊
        }
    }
})
```

#### returnSoup

> 谔谔，落枕了

通过该参数请求一个网页，并返回一个 `BeautifulSoup` 类型的对象，需要 `link` 字符串参数。如果请求失败了，则会返回 `<html></html>` 的 `BeautifulSoup` 对象。

#### getTorrent

> 倚音

通过该接口请求一个画廊的种子信息，返回列表，需要一个参数：`link`，应当是字符串，如 `https://exhentai.org/g/2011308/8263590d02/`。

返回列表的格式如下（可能会因为各种原因返回空列表）：

```python
[{
    "time": str,                            # 种子上传时间
    "size": str,                            # 种子内容大小
    "seeds": int,                           # 做种数
    "peers": int,                           # 下载数
    "total": int,                           # 总数
    "link": str,                            # 种子链接
    "name": str                             # 种子名称
}]
```

#### getInfo

> 序列化一切我所能见到的，然后浪费我的时间

通过该接口请求一个画廊的基本信息，返回字典，需要一个参数：`link`，应当是字符串，如 `https://exhentai.org/g/2011308/8263590d02/`。

返回字典的格式如下：

```python
{
    "title": str,                           # 画廊标题
    "jTitle": str,                          # 如果存在的话，画廊日文标题
    "cat": str,                             # 画廊分类
    "tags": list[str],                      # 画廊标签
    "time": str,                            # 画廊上传时间
    "father": str,                          # 画廊父画廊
    "viewable": str,                        # 画廊是否可见
    "language": str,                        # 画廊语言
    "tr": bool,                             # 画廊是否有翻译
    "rw": bool,                             # 画廊是否有重写
    "size": str,                            # 画廊大小
    "pages": int,                           # 画廊页数
    "favTimes": int,                        # 画廊收藏次数
    "uploader": str,                        # 画廊上传者
    "uploaderURL": str,                     # 画廊上传者链接
    "rate": float,                          # 画廊评分
    "cover": str                            # 画廊封面
}
```

#### getComments

> 落枕脖子比较难受，先摸了。

获取一个画廊的评论，根据用户设置的评论显示情况，返回列表，需要一个参数：`link`，应当是字符串，如 `https://exhentai.org/g/2011308/8263590d02/`。

列表格式如下：

```python
[{
    "time": str,                            # 评论时间
    "commenterURL": str,                    # 评论者 URL
    "commenter": str,                       # 评论者名称
    "scores": str,                          # 评论评分
    "htmlComments": str                     # 评论内容
}]
```

#### apiInfo

> 悲

通过官方 API 获取一个画廊的详细信息，速度更快，内容更全，返回字典，需要一个参数：`link`，应当是字符串，如 `https://exhentai.org/g/2011308/8263590d02/`。

字典格式如下（可能返回空字典）：

```python
{
    'gmetadata': [{
        'gid': int,
        'token': str,
        'archiver_key': str,
        'title': str,
        'title_jpn': str,
        'category': str,
        'thumb': str,
        'uploader': str,
        'posted': str,
        'filecount': str,
        'filesize': int,
        'expunged': bool,
        'rating': str,
        'torrentcount': str,
        'torrents': [{
            'hash': str,
            'added': str,
            'name': str,
            'tsize': str,
            'fsize': str
        }],
        'tags': [str]
    }]
}
```

#### getPages

> 适时

通过该接口，根据账户设置情况获取一个画廊需要的翻页次数，因为画廊的页数对每个账户而言是不确定的，你可以通过 `Hath` 购买解除相关限制的选项，所以需要一个参数：`link`，应当是字符串，如 `https://exhentai.org/g/2011308/8263590d02/`，最后返回数字表示翻页次数。

#### parseSoupForLargeThumbnails

> 名字就解释了一切

传入一个 `soup` 参数，取得页面中所有的缩略图（前提是你设置了 `large` 缩略图显示并且该 `soup` 中也使用了 `large` 模式），返回列表，列表的格式如下：

```python
[{
    "url": str,                             # 缩略图地址
    "style": str,                           # 缩略图 CSS 样式
    "alt": str,                             # 缩略图 alt 文字
    "title": str,                           # 缩略图 title 文字
    "text": str                             # 缩略图内容
}]
```

#### yieldGetLargeThumbnails

> ha na bi

一开始我是没有写生成器的，准确来说，压根没有想到，直到爬了一些比较大的画廊，才觉得一定要写一个生成器了，不然那他妈就是折磨人。你需要 `link` 参数，表示请求地址，如 `https://exhentai.org/g/2011308/8263590d02/`，一页一页来，取得页面中所有的缩略图，每次返回的格式如下：

```python
[{
    "url": str,                             # 缩略图地址
    "style": str,                           # 缩略图 CSS 样式
    "alt": str,                             # 缩略图 alt 文字
    "title": str,                           # 缩略图 title 文字
    "text": str                             # 缩略图内容
}]
```

#### getLargeThumbnails

> 如今再回头来看代码，简直像疯子一样的东西

这是一开始的接口，我不太推荐你用，我建议你使用 `yieldGetLargeThumbnails`，如果你的画廊比较大，那么请求时间会比较长。他需要一个参数：`link`，是字符串，如 `https://exhentai.org/g/2011308/8263590d02/`。返回格式如下：

```python
[[{
    "url": str,                             # 缩略图地址
    "style": str,                           # 缩略图 CSS 样式
    "alt": str,                             # 缩略图 alt 文字
    "title": str,                           # 缩略图 title 文字
    "text": str                             # 缩略图内容
}]]
```

二维数组注意，第一维是页数，第二维是缩略图列表。

#### parseSoupForNormalThumbnails

> 真的有必要吗

传入一个 `soup` 参数，取得页面中所有的普通模式缩略图（前提是你设置了 `normal` 缩略图显示并且该 `soup` 中也使用了 `normal` 模式），返回列表，列表的格式如下：

```python
[{
    "style": str,                           # 缩略图 CSS 样式
    "divMargin": str,                       # 缩略图 div 的 margin 属性
    "divWidth": str,                        # 缩略图 div 的 width 属性
    "url": str,                             # 缩略图地址
    "transparent": str,                     # 缩略图的 transparent 属性
    "imgAlt": str,                          # 缩略图的 alt 属性
    "imgTitle": str,                        # 缩略图的 title 属性
    "imgWidth": str,                        # 缩略图的 width 属性
    "imgHeight": str,                       # 缩略图的 height 属性
    "imgMargin": str                        # 缩略图的 margin 属性
}]
```

#### yieldGetNormalThumbnails

> 早上好 Python，现在我有生成器

通过该接口获取一个生成器，用于一页接一页地获取普通模式的缩略图信息，参数是 `link`，每次返回格式如下：

```python
[{
    "style": str,                           # 缩略图 CSS 样式
    "divMargin": str,                       # 缩略图 div 的 margin 属性
    "divWidth": str,                        # 缩略图 div 的 width 属性
    "url": str,                             # 缩略图地址
    "transparent": str,                     # 缩略图的 transparent 属性
    "imgAlt": str,                          # 缩略图的 alt 属性
    "imgTitle": str,                        # 缩略图的 title 属性
    "imgWidth": str,                        # 缩略图的 width 属性
    "imgHeight": str,                       # 缩略图的 height 属性
    "imgMargin": str                        # 缩略图的 margin 属性
}]
```

#### getNormalThumbnails

> 所以现在不是音乐时间

不是很推荐你使用，同样的，建议你使用 `yieldGetNormalThumbnails`，如果你的画廊比较大，那么请求时间会比较长。他需要一个参数：`link`，是字符串，如 `https://exhentai.org/g/2011308/8263590d02/`。返回格式如下：

```python
[[{
    "style": str,                           # 缩略图 CSS 样式
    "divMargin": str,                       # 缩略图 div 的 margin 属性
    "divWidth": str,                        # 缩略图 div 的 width 属性
    "url": str,                             # 缩略图地址
    "transparent": str,                     # 缩略图的 transparent 属性
    "imgAlt": str,                          # 缩略图的 alt 属性
    "imgTitle": str,                        # 缩略图的 title 属性
    "imgWidth": str,                        # 缩略图的 width 属性
    "imgHeight": str,                       # 缩略图的 height 属性
    "imgMargin": str                        # 缩略图的 margin 属性
}]]
```

二维数组注意，第一维是页数，第二维是缩略图列表。

#### getTitle

> Time Line

获取一个画廊的 `title` 信息，需要两个参数：`link` 和 `params`，前者是字符串，表示画廊链接；后者是字典，表示相关参数，格式如下：

```python
{
    "japanese": bool,               # 是否获取日文标题
}
```

最后返回字符串，表示标题。为什么这么设计呢，其实这个接口并不是给用户用的其实，其实是给其他接口用的（笑）

#### createFolder

> Ban

这是一个用于创建文件夹的接口，只是给内部接口用的，当然我没有把它设置为私有的，你可以使用。需要两个参数：`link` 和 `params`，前者是字符串，表示画廊链接；后者是字典，表示相关参数，格式如下：

```python
{
    "japanese": bool,               # 是否获取日文标题
    "path": str                     # 路径
}
```

将会获取画廊的标题，然后在指定的路径下创建一个同名的文件夹，如果文件夹已经存在，则不会创建。

#### yieldGetMPVImages

> 本来想摘一点古兰经的，但是这太谔谔了，算了。

通过该接口获取一个生成器以一张一张的获取方式获取 MPV 模式下的图片信息（前提是你的账户要有资格），需要的参数是 `link`，是字符串，表示画廊链接，每次返回格式如下：

```python
{
    'name': str,                    # 图片名
    'url': str                      # 图片地址
}
```

#### getMPVImages

> 過去 未来 ぼくら対せかい —— amazarashi ぼくら対せかい

通过该接口获取所有的 MPV 模式下的图片信息（前提是你的账户要有资格），建议使用 `yieldGetMPVImages`，这样可以提高效率。需要的参数有三个：`link`, `method` 和 `params`。`link` 表示字符串，是画廊地址；`method` 是字符串，应该是 `get` 或 `download`；`params` 是字典，是一些参数，格式如下：

```python
{
    "japanese": bool,               # 是否获取日文标题
    "path": str                     # 路径
}
```

如果 `method` 选择的是 `get`，那么最后返回的格式是：

```python
[{
    'name': str,                    # 图片名
    'url': str                      # 图片地址
}]
```

如果是 `download`，那么最后返回的格式是 `[str]`，表示下载的文件名列表。

#### getImages

> 或许

普通模式下获取单页图片的解析器，你需要四个参数：`soup`, `method`, `title` 和 `params`。`soup` 应当是 `https://exhentai.org/g/2011308/8263590d02/?p=0` 之类的 `BeautifulSoup` 对象；`method` 表示字符串，应当是 `get` 或 `download`；`title` 表示字符串，是标题；`params` 是字典，是一些参数，格式如下：

```python
{
    "japanese": bool,               # 是否获取日文标题
    "path": str                     # 路径
}
```

最后返回的结果格式都为：`[str]`，`get` 模式下是图片的地址，`download` 模式下是文件名。

#### yieldGetNormalImagesOneImageByOneImage

> 何だっていいだろ 君の話しをまずは聞かせてくれよ —— amazarashi 名前

这是一个生成器接口，用于获取普通模式下的图片，你可以吐槽这个名字，其实我是故意的，看起来就很玩世不恭。事实上，下文会写到 `yieldGetNormalImages` 这个生成器接口，但是呢，有些账号它一页展示的图片比较多，所以还是非常耗时的，干脆不如一张一张图片依次获取并返回吧。然后就直接取了这么一个好好玩的名字，需要一个参数：`link`，表示画廊地址，每次返回的内容格式是 `str`，表示一张图片的地址。

#### yieldGetNormalImages

> Fork

这是一个生成器接口，用于一页一页地获取普通模式下的图片，可是在一些账户下，一次返回的耗时还是太长了，推荐用上文的那个 `yieldGetNormalImagesOneImageByOneImage`。需要一个参数：`link`，表示画廊地址，每次返回的内容格式是 `str`，表示一张图片的地址。

#### getNormalImages

> 到点了，摸了

用于获取普通模式下所有图片的接口，耗时可能会比较长，建议看看 `yieldGetNormalImages` 和 `yieldGetNormalImagesOneImageByOneImage` 这些生成器。它需要三个参数：`link`, `method` 和 `params`。`link` 表示画廊地址，`method` 表示字符串，应当是 `get` 或 `download`；`params` 是字典，是一些参数，格式如下：

```python
{
    "japanese": bool,               # 是否获取日文标题
    "path": str                     # 路径
}
```

最终返回格式是：`[[str]]`，`get` 模式下是图片的地址，`download` 模式下是文件名。第一维表示页码，第二维是图片地址或文件名。

#### getArchivesHATH

> 你说的话 已开始蒸发 你造的梦 已开始崩塌 —— Chinese Football 世界悲

用于获取一个画廊的 `H@H` 下载信息的接口，说实话，作者我也没用过这个，需要一个参数：`link` 是字符串，表示画廊地址。返回格式如下：

```python
[{
    "sample": str,                                  # 图像分辨率
    "size": str,                                    # 压缩包大小
    "cost": str,                                    # 花费
    "code": str,                                    # 下载代码
    "url": str,                                     # 下载地址
}]
```

#### toHATH

> Call

发送一个 `H@H` 下载请求，需要两个参数：`link` 和 `code`，`link` 是字符串，表示请求地址，`code` 是字符串，表示 `H@H` 下载代码。返回格式如下：

如果成功：`Done! / 完成！`；如果失败：`Error, check your cookies and something balabala. / 错误，请检查你的 Cookies 或者其他乱七八糟的东西。`。

#### parseArchives

> 我还是太年轻，不知道这东西的严肃性不能被消解

通过该接口获取压缩包下载地址，它需要两个参数：`form` 和 `action`。前者是字典，表示压缩包请求数据；后者是字符串，表示请求地址。返回格式是字符串，表示下载地址。

`form` 的格式有 `Original` 和 `Resample` 两种：

`Orginial`：

```python
{
    "dltype": "org",
    "dlcheck": "Download Original Archive"
}
```

`Resample`：

```python
{
    "dltype": "res",
    "dlcheck": "Download Resample Archive"
}
```

#### getArchives

> 快结束了

获取一个画廊的所有压缩包下载地址的接口，需要一个参数：`link`，它是字符串，表示画廊地址。返回格式如下：

```python
[{
    "type": str,                                    # 压缩包类型
    "link": str,                                    # 压缩包下载地址
}]
```

#### downloadArchives

> 马上，就要到达彼岸

下载一个画廊的压缩包，它需要三个参数：`link`, `params` 和 `sample`。`link` 表示字符串，应该是画廊地址；`params` 是相关参数，格式下文会列出；`sample` 表示需要下载的图片分辨率，如果是空字符串则全部下载。返回格式是字符串，表示下载地址。

`params` 参数：

```python
{
    "japanese": bool,               # 是否获取日文标题
    "path": str                     # 路径
}
```

如果你指定了 `sample` 的话，最后只会返回字符串，表示本地文件，否则会返回一个列表，列表中的每一项都是字符串，表示本地文件。

#### downloadFile

> 暂时的中止

好了，这是最后一个 `ExHentai` 接口，用于下载文件，其实很多这种看起来没有意义的功能，其实对我而言，都是非常有用的，因为我做 Discord Bot 的时候发现没有一个下载接口简直想骂娘。

它需要三个参数：`url`, `orgName` 和 `path`。`url` 是字符串，表示下载地址；`orgName` 是字符串，表示文件名；`path` 是字符串，表示文件保存路径。返回格式是布尔值，表示是否成功。

### waziJavBus

> 无言投下

JavBus 是一个 AV 分享网站，在目前的版本中，我们支持镜像网站和对于欧美分区的单独的 `red` 网站。

#### giveParams

> 保持我的沉默

设置用户参数，参数是 `params` 字典，完成之后返回当前用户的参数。

#### changeType

> 我的心跳

修改获取视频的类型的接口，需要一个参数：`magType`，可以是字符串或整数，应当为 0 或 1，0 表示只显示有磁力链接的视频，1 表示显示所有视频。

#### setApiUrl

> 告诉我新的灯塔，我会跟紧你的步伐

设置 JavBus 镜像站地址，如果你需要的话，就可以使用这个接口。需要一个参数：`url`，应当是字符串，表示你的镜像地址。

#### setEAApiUrl

> 那可能是好的，但是一定是新的

设置 JavBus.red 镜像站地址（事实上不清楚有没有，这是一个欧美成人视频分享网站），如果你需要的话，就可以使用这个接口。需要一个参数：`url`，应当是字符串，表示你的镜像地址。

#### getPage

> 修改关于我对未来的回忆

该接口用于获取 `JavBus` 页面，因为 `urllib3` 导致的字典顺序问题，为了兼容，故单独使其使用 `urllib` 模块以暂时解决这个问题（如果可能，我会重写请求模块以解决这方面的问题）。你可以在 `https://stackoverflow.com/questions/62684468/pythons-requests-triggers-cloudflares-security-while-urllib-does-not` 中获取更多信息。

它需要三个参数: `url`, `headers` 和 `needOrg`。`url` 应当是字符串，表示请求地址；`headers` 表示请求头，应当是字典；`needOrg` 表示是否需要返回原始数据的字符串，否则返回解析后的数据。

#### getItems

> 千变万化

该接口用于从 `BeautifulSoup` 对象中解析相关内容，你需要三个参数以使用它：`soup`, `itemsType`, `ea`。`soup` 是 `BeautifulSoup` 对象，表示搜索结果等或其它内容；`itemsType` 是字符串，表示解析的类型，可以是 `normal`, `worker` 或 `eaWorker`；`ea` 是布尔值，表示是否是欧美分区。

最后返回列表，失败返回空列表，关于格式你应当检查使用了该接口的内容。事实上，很多都是私有的接口，包括这个也是，这只是一个实现，只是我也觉得可以写一个 `_` 区分一下，写文档的时候就不用写了，还比较方便，至少是明确的，告诉用户可以使用哪一个接口干活。

#### getTags

> 私有化进程很慢

该接口用于从 `BeautifulSoup` 对象中解析出标签，你需要一个参数：`soup`，表示网页。最后返回列表，格式如下：

```python
[{
    "tagType": str,             # Tag 分类
    "tags": list[str]           # Tag 列表
}]
```

#### getWorkers

> 农民力量，播种，生活；我们思考，大脑，程序；小姐肉体，夜晚，生活

需要四个参数 `soup`, `avType`, `avTypeFromWebSite` 和 `ea`，该接口用于从 `BeautifulSoup` 对象中解析出工作者列表。`soup` 是 `BeautifulSoup` 对象，表示搜索结果等或其它内容；`avType` 可以是字符串或整数，表示 AV 类型，0 表示有码，1 表示无码；`avTypeFromWebSite` 是布尔值，表示是否使用从网页中解析出的类型；`ea` 是布尔值，表示是否是欧美分区。

最后返回列表，格式如下：

```python
[{
    "link": str,                            # 工作者链接
    "frame": str,                           # 工作者封面
    "name": str,                            # 工作者姓名
    "workerId": str,                        # 工作者 ID
    "avType": str or int,                   # 出演 AV 类型
}]
```

#### getDetails

> もっと大袈裟に痛がろう —— MARETU うみたがり

获取一个 AV 的详细信息的接口，需要两个参数：`soup` 和 `ea`，`soup` 是 `BeautifulSoup` 对象，表示搜索结果等或其它内容；`ea` 是布尔值，表示是否是欧美分区。

最后返回字典，格式如下：

```python
{
    "title": str,                                   # AV 标题
    "cover": str,                                   # AV 视频封面地址
    "coverTitle": str,                              # AV 视频封面标题
    "avId": str,                                    # AV 番号
    "time": str,                                    # AV 发布时间
    "long": str,                                    # AV 时长
    "director": {                                   # AV 导演信息
        "name": str,                                # AV 导演姓名
        "id": str,                                  # AV 导演 ID
        "type": str or int                          # AV 导演类型
    },
    "studio": {                                     # AV 制作商信息
        "name": str,                                # AV 制作商名字
        "id": str,                                  # AV 制作商 ID
        "type": str or int                          # AV 制作商类型
    },
    "label": {                                      # AV 发行商信息
        "name": str,                                # AV 发行商名字
        "id": str,                                  # AV 发行商 ID
        "type": str or int                          # AV 发行商类型
    },
    "series": {                                     # AV 系列信息
        "name": str,                                # AV 系列名字
        "id": str,                                  # AV 系列 ID
        "type": str or int                          # AV 系列类型
    },
    "tags": [{                                      # AV 标签信息
        "name": str,                                # AV 标签名字
        "id": str,                                  # AV 标签 ID
        "type": str or int                          # AV 标签类型
    }],
    "workers": [{                                   # AV 工作者信息
        "name": str,                                # AV 工作者姓名
        "id": str,                                  # AV 工作者 ID
        "type": str or int                          # AV 工作者类型
    }],
    "samples": [{                                   # AV 展示图像信息
        "title": str,                               # AV 展示图像标题
        "url": str                                  # AV 展示图像地址
    }],
    "sameVideos": [{                                # AV 同类推荐视频信息
        "frame": str,                               # AV 同类推荐视频封面
        "title": str,                               # AV 同类推荐视频标题
        "img": str,                                 # AV 同类推荐视频封面
        "id": str                                   # AV 同类推荐视频 ID
    }],
    "hots": [{                                      # 论坛热门信息
        "url": str,                                 # 论坛热门信息地址
        "title": str,                               # 论坛热门信息标题
        "cover": str                                # 论坛热门信息封面
    }]
}
```

#### browse

> Last word

通过该接口以进行主页浏览，需要三个参数：`page`, `tag` 和 `avType`。`page` 表示页码，应当是字符串或整数，从 1 数起；`tag` 表示标签，应当是字符串，如果没有则填写空字符串；`avType` 表示 AV 类型，应当是字符串或整数，可以是以下值：0 表示有码，1 表示有码。

最后返回列表，格式如下：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### eaBrowse

> But not least

通过该接口以进行欧美分区浏览，需要两个参数：`page` 和 `tag`。`page` 表示页码，应当是字符串或整数，从 1 数起；`tag` 表示标签，应当是字符串，如果没有则填写空字符串。

最后返回列表，格式如下：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### withWorkerBrowse

> And finally

通过该接口进行 AV 工作者演出视频浏览，需要三个参数：`page`, `workerId` 和 `avType`。`page` 表示页码，应当是字符串或整数，从 1 数起；`workerId` 表示 AV 工作者 ID，应当是字符串；`avType` 表示 AV 类型，应当是字符串或整数，可以是以下值：0 表示有码，1 表示有码。

最后返回列表：

第 0 位：

```python
{
    "name": str,                    # 工作者姓名
    "img": str,                     # 工作者头像
    "basic" [{                      # 工作者基本信息
        "type": str,                # 工作者基本信息类型
        "content": str              # 工作者基本信息内容
    }]
}
```

第 1 位及以后：

```python
{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}
```

#### withEAWorkerBrowse

> 🥟

通过该接口进行欧美分区的 AV 工作者演出视频浏览，需要三个参数：`page` 和 `workerId`。`page` 表示页码，应当是字符串或整数，从 1 数起；`workerId` 表示 AV 工作者 ID，应当是字符串。

最后返回列表：

第 0 位：

```python
{
    "name": str,                    # 工作者姓名
    "img": str,                     # 工作者头像
    "basic" [{                      # 工作者基本信息
        "type": str,                # 工作者基本信息类型
        "content": str              # 工作者基本信息内容
    }]
}
```

第 1 位及以后：

```python
{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}
```

#### withDirectorBrowse

> Slap it

通过该接口进行导演导过的视频浏览（怎么那么怪），需要三个参数：`page`, `directorId` 和 `avType`。`page` 表示页码，应当是字符串或整数，从 1 数起；`directorId` 表示导演 ID，应当是字符串；`avType` 表示 AV 类型，应当是字符串或整数，可以是以下值：0 表示有码，1 表示有码。

最后返回列表，格式如下：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### withEADirectorBrowse

> 额，我为什么不能统一

通过该接口在欧美区浏览一个导演执导过的视频，需要两个参数：`page` 和 `directorId`。`page` 表示页码，应当是字符串或整数，从 1 数起；`directorId` 表示导演 ID，应当是字符串。

最后返回列表，格式如下：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### withStudioBrowse

> 摸了

通过该接口浏览一个工作室整的视频，需要三个参数：`page`, `studioId` 和 `avType`。`page` 表示页码，应当是字符串或整数，从 1 数起；`studioId` 表示工作室 ID，应当是字符串；`avType` 表示 AV 类型，应当是字符串或整数，可以是以下值：0 表示有码，1 表示有码。

最后返回列表，格式如下：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### withEAStudioBrowse

> 总是这样，为什么不能再和谐一点呢

通过该接口浏览一个欧美工作室整的视频，需要两个参数：`page` 和 `studioId`。`page` 表示页码，应当是字符串或整数，从 1 数起；`studioId` 表示工作室 ID，应当是字符串。

最后返回列表，格式如下：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### withLabelBrowse

> 透过未来的影子，窥见昨日的自己

通过该接口浏览一个发行商发行的视频，需要三个参数：`page`, `labelId` 和 `avType`。`page` 表示页码，应当是字符串或整数，从 1 数起；`labelId` 表示发行商 ID，应当是字符串；`avType` 表示 AV 类型，应当是字符串或整数，可以是以下值：0 表示有码，1 表示有码。

最后返回列表，格式如下：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### withEALabelBrowse

> 更加激进地

通过该接口浏览一个欧美发行商发行的视频，需要两个参数：`page` 和 `labelId`。`page` 表示页码，应当是字符串或整数，从 1 数起；`labelId` 表示发行商 ID，应当是字符串。

最后返回列表，格式，额，说了很多次了，不过我还是会复制的：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### withSeriesBrowse

> 恢弘的铜管乐，那样的主题我写不出来

通过该接口浏览一个系列下的视频，需要三个参数：`page`, `seriesId` 和 `avType`。`page` 表示页码，应当是字符串或整数，从 1 数起；`seriesId` 表示系列 ID，应当是字符串；`avType` 表示 AV 类型，应当是字符串或整数，可以是以下值：0 表示有码，1 表示有码。

最后返回列表：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### withEASeriesBrowse

> 我听到那段旋律的时候，听到那个铜管，一整个弦乐组的时候...

通过该接口浏览一个欧美的系列下的视频，只需要两个参数：`page` 和 `seriesId`。`page` 表示页码，应当是字符串或整数，从 1 数起；`seriesId` 表示系列 ID，应当是字符串。

最后返回列表：

```python
[{
    "link": str,                        # AV 链接
    "frame": str,                       # AV 封面
    "title": str,                       # AV 标题
    "avId": str,                        # AV 番号
    "others": {                         # 其他信息
        "type": str,                    # AV 其他信息类型
        "has": [str],                   # AV 其他信息内容
        "tags": [{                      # AV 其他信息标签
            "type": str,                # AV 其他信息标签类型
            "title": str                # AV 其他信息标签标题
        }]
    }
}]
```

#### getTagsList

> 换了

通过该接口获取标签列表，需要一个参数：`avType`，0 表示有码，1 表示无码。

最后返回列表，格式换了哦：

```python
[{
    "tagType": str,             # Tag 分类
    "tags": list[str]           # Tag 列表
}]
```

#### getEATagsList

> 大抵是自由的味道，跟鲜血一样

通过该接口获取欧美分区的标签列表，不需要任何参数。最后返回格式同上，但我再抄一遍：

```python
[{
    "tagType": str,             # Tag 分类
    "tags": list[str]           # Tag 列表
}]
```

#### getAVWorkersList

> 我愿意的话，我会考虑木管，那种金碧辉煌的质感，我已经好久没有接触过了...

通过该接口获取 AV 工作者列表，需要两个参数：`page` 和 `avType`，`page` 表示页码，应当是字符串或整数，从 1 数起；`avType` 表示 AV 类型，应当是字符串或整数，可以是以下值：0 表示有码，1 表示有码。最后返回列表：

```python
[{
    "link": str,                            # 工作者链接
    "frame": str,                           # 工作者封面
    "name": str,                            # 工作者姓名
    "workerId": str,                        # 工作者 ID
    "avType": str or int,                   # 出演 AV 类型
}]
```

#### getEAAVWorkersList

> 脚印

通过该接口获取欧美区的 AV 工作者列表，需要一个参数：`page` 表示页码，应当是字符串或整数，从 1 数起。最后返回列表：

```python
[{
    "link": str,                            # 工作者链接
    "frame": str,                           # 工作者封面
    "name": str,                            # 工作者姓名
    "workerId": str,                        # 工作者 ID
    "avType": str or int,                   # 出演 AV 类型
}]
```

#### getAVDetails

> 我有点看不下去了，RESTful 设计模式应该也得用在我这上面，我应该给我之前一拳。

通过该接口获取一个 AV 的详细信息，需要一个参数：`avId`，表示 AV 的 ID，应当是字符串。最后返回字典，格式如下：

```python
{
    "title": str,                                   # AV 标题
    "cover": str,                                   # AV 视频封面地址
    "coverTitle": str,                              # AV 视频封面标题
    "avId": str,                                    # AV 番号
    "time": str,                                    # AV 发布时间
    "long": str,                                    # AV 时长
    "director": {                                   # AV 导演信息
        "name": str,                                # AV 导演姓名
        "id": str,                                  # AV 导演 ID
        "type": str or int                          # AV 导演类型
    },
    "studio": {                                     # AV 制作商信息
        "name": str,                                # AV 制作商名字
        "id": str,                                  # AV 制作商 ID
        "type": str or int                          # AV 制作商类型
    },
    "label": {                                      # AV 发行商信息
        "name": str,                                # AV 发行商名字
        "id": str,                                  # AV 发行商 ID
        "type": str or int                          # AV 发行商类型
    },
    "series": {                                     # AV 系列信息
        "name": str,                                # AV 系列名字
        "id": str,                                  # AV 系列 ID
        "type": str or int                          # AV 系列类型
    },
    "tags": [{                                      # AV 标签信息
        "name": str,                                # AV 标签名字
        "id": str,                                  # AV 标签 ID
        "type": str or int                          # AV 标签类型
    }],
    "workers": [{                                   # AV 工作者信息
        "name": str,                                # AV 工作者姓名
        "id": str,                                  # AV 工作者 ID
        "type": str or int                          # AV 工作者类型
    }],
    "samples": [{                                   # AV 展示图像信息
        "title": str,                               # AV 展示图像标题
        "url": str                                  # AV 展示图像地址
    }],
    "sameVideos": [{                                # AV 同类推荐视频信息
        "frame": str,                               # AV 同类推荐视频封面
        "title": str,                               # AV 同类推荐视频标题
        "img": str,                                 # AV 同类推荐视频封面
        "id": str                                   # AV 同类推荐视频 ID
    }],
    "hots": [{                                      # 论坛热门信息
        "url": str,                                 # 论坛热门信息地址
        "title": str,                               # 论坛热门信息标题
        "cover": str                                # 论坛热门信息封面
    }]
}
```

#### getEAAVDetails

> 写文档给我写成了大海

通过该接口获取一个欧美 AV 的详细信息，需要一个参数：`avId`，表示 AV 的 ID，应当是字符串。最后返回字典，格式就不复制了。

#### getAVDetailsWithMagnet

> 像 E 一样

通过该接口获取一个 AV 的相信信息并附带磁力链接，需要一个参数：`avId`，表示 AV 的 ID，应当是字符串。最后返回字典，格式如下：

```python
{
    "title": str,                                   # AV 标题
    "cover": str,                                   # AV 视频封面地址
    "coverTitle": str,                              # AV 视频封面标题
    "avId": str,                                    # AV 番号
    "time": str,                                    # AV 发布时间
    "long": str,                                    # AV 时长
    "director": {                                   # AV 导演信息
        "name": str,                                # AV 导演姓名
        "id": str,                                  # AV 导演 ID
        "type": str or int                          # AV 导演类型
    },
    "studio": {                                     # AV 制作商信息
        "name": str,                                # AV 制作商名字
        "id": str,                                  # AV 制作商 ID
        "type": str or int                          # AV 制作商类型
    },
    "label": {                                      # AV 发行商信息
        "name": str,                                # AV 发行商名字
        "id": str,                                  # AV 发行商 ID
        "type": str or int                          # AV 发行商类型
    },
    "series": {                                     # AV 系列信息
        "name": str,                                # AV 系列名字
        "id": str,                                  # AV 系列 ID
        "type": str or int                          # AV 系列类型
    },
    "tags": [{                                      # AV 标签信息
        "name": str,                                # AV 标签名字
        "id": str,                                  # AV 标签 ID
        "type": str or int                          # AV 标签类型
    }],
    "workers": [{                                   # AV 工作者信息
        "name": str,                                # AV 工作者姓名
        "id": str,                                  # AV 工作者 ID
        "type": str or int                          # AV 工作者类型
    }],
    "samples": [{                                   # AV 展示图像信息
        "title": str,                               # AV 展示图像标题
        "url": str                                  # AV 展示图像地址
    }],
    "sameVideos": [{                                # AV 同类推荐视频信息
        "frame": str,                               # AV 同类推荐视频封面
        "title": str,                               # AV 同类推荐视频标题
        "img": str,                                 # AV 同类推荐视频封面
        "id": str                                   # AV 同类推荐视频 ID
    }],
    "hots": [{                                      # 论坛热门信息
        "url": str,                                 # 论坛热门信息地址
        "title": str,                               # 论坛热门信息标题
        "cover": str                                # 论坛热门信息封面
    }],
    "magnets": [{                                   # AV 磁力链接
        "title": str,                               # 磁力链接标题
        "tags": [{                                  # 磁力链接标签
            "title": str,                           # 磁力链接标签标题
            "type": str or None                     # 磁力链接标签类型
        }],
        "size": str,                                # 磁力链接大小
        "date": str,                                # 磁力链接发布时间
        "magnet": str                               # 磁力链接地址
    }]
}
```

#### getEAAVDetailsWithMagnet

> 八度

通过该接口获取一个欧美的 AV 的相信信息并附带磁力链接，需要一个参数：`avId`，表示 AV 的 ID，应当是字符串。最后返回字典，格式同上。

#### search

> 管钟的感觉，就非常宏大叙事，我很喜欢。

搜索接口，需要三个参数：`searchType`, `keyWord` 还有 `page`。`searchType` 应当是字符串或整数，表示搜索类型，可以是 0 到 6 的其中一个，具体如下：

+ 0 - 搜索有码影片
+ 1 - 搜索无码影片
+ 2 - 搜索工作者
+ 3 - 搜索导演
+ 4 - 搜索制作商
+ 5 - 搜索发行商
+ 6 - 搜索系列（可能坏了）

`keyWord` 应该是字符串，表示搜索内容；`page` 应当是整数或字符串，表示搜索结果的页数，从 1 开始数起。

如果 `searchType` 为 2 的话，使用和返回的接口是 `getWorkers`，其余则是 `getItems`。

#### eaSearch

> 定音鼓

欧美的搜索接口，需要三个参数：`searchType`, `keyWord` 还有 `page`。`searchType` 应当是字符串或整数，表示搜索类型，应当是 0 或 1，0 表示搜索影片，1 表示搜索工作者；`keyWord` 应当是字符串，表示搜索内容；`page` 应当是整数或字符串，表示搜索结果的页数，从 1 开始数起。同样的，如果 `searchType` 为 1 的话，使用和返回的接口是 `getWorkers`，其余则是 `getItems`。

#### getAjax

> 用沙子堆成的砖头

通过该接口获取一个 AV 的信息 AJAX 获取地址，需要两个参数：`avId` 和 `isEa`。`avId` 应当是字符串，表示 AV 的 ID；`isEa` 应当是布尔值，表示是否是欧美分区的。

最后返回字符串，是 AJAX 请求地址。

#### getMagnet

> Beat Per Minute

通过该接口获取一个 AV 的磁力链接，需要一个参数：`avId`，需要两个参数：`avId` 和 `isEa`。`avId` 应当是字符串，表示 AV 的 ID；`isEa` 应当是布尔值，表示是否是欧美分区的。

最后返回的是列表，格式如下：

```python
[{
    "title": str,                               # 磁力链接标题
    "tags": [{                                  # 磁力链接标签
        "title": str,                           # 磁力链接标签标题
        "type": str or None                     # 磁力链接标签类型
    }],
    "size": str,                                # 磁力链接大小
    "date": str,                                # 磁力链接发布时间
    "magnet": str                               # 磁力链接地址
}]
```

#### downloadFile

> 它终于要死去了，我为它热烈地欢呼

通过该接口下载一个文件，额好吧，真的只是给我的 Bot 用的，你需要三个参数：`url`, `orgName` 和 `path`。`url` 是字符串，表示下载地址；`orgName` 是字符串，表示文件名；`path` 是字符串，表示文件保存路径。返回格式是布尔值，表示是否成功。

### waziNyaa

> 一直都在开始，一直都不会结束

Nyaa 是一个二次元的磁力链接分享网站，在目前的版本中，我们还支持 `sukebei` 分区。

#### giveParams

> 只剩一次

设置用户参数，参数是 `params` 字典，完成之后返回当前用户的参数。

#### getFiles

> 知晓

一个递归函数，用于从 `ul` 获取所有的文件，并将文件储存在 `self.tempFiles` 列表中。

#### returnSoup

> 即将起程

通过该接口获取一个网站的 BeautifulSoup 对象，为了支持 RSS，现在需要两个参数：`link` 和 `xml`。`link` 应当是字符串，表示网站的链接；`xml` 应当是布尔值，表示是否是 RSS 的链接。如果失败了，则返回 `<html></html>` 的 BeautifulSoup 对象。

#### parsePage

> 竖琴也很雅，那个琶音

解析一个磁力链接的详情主页，需要两个参数：`soup` 和 `site`。前者是 BeautifulSoup 对象，后者是整数，表示什么网站，0 表示 Nyaa，1 表示 Sukebei。最后返回字典，格式如下：

```python
{
    "type": str,                                        # 磁力链接类型
    "title": str,                                       # 磁力链接标题
    "category": {                                       # 磁力链接分类
        "fatherCategory": str,                          # 父分类
        "fatherCategoryId": str,                        # 父分类 ID
        "subCategory": str,                             # 子分类
        "subCategoryId": str                            # 子分类 ID
        "category": str,                                # 分类
    },
    "time": str,                                        # 磁力链接发布时间
    "timeStamp": int,                                   # 磁力链接发布时间戳
    "uploader": str,                                    # 磁力链接发布者
    "uploaderLink": str,                                # 磁力链接发布者链接
    "seeders": int,                                     # 磁力链接种子数
    "information": str,                                 # 磁力链接信息
    "informationLink": str,                             # 磁力链接信息链接
    "leechers": int,                                    # 磁力链接吸血鬼数
    "size": str,                                        # 磁力链接大小
    "completes": int,                                   # 磁力链接完成数
    "hash": str,                                        # 磁力链接哈希值
    "torrent": str or None,                             # 磁力链接种子链接，如果没有则为 None
    "magnet": str,                                      # 磁力链接的 magnet 链接
    "description": str,                                 # 磁力链接的简介
    "files": str or list[str],                          # 磁力链接的文件列表
    "comments": [{                                      # 磁力链接的评论列表
        "name": str,                                    # 评论者名字
        "link": str,                                    # 评论者链接
        "extra": str,                                   # 评论者额外信息
        "time": str,                                    # 评论时间
        "timeStamp": int,                               # 评论时间戳
        "editTime": str,                                # 编辑时间
        "editTimeStamp": float,                         # 编辑时间戳
    }]
}
```

#### parseRSS

> 需要进一步的观望

该接口用于获取 RSS 中的信息，需要一个参数：`rss`，应当是 `BeautifulSoup` 对象，是 RSS 的内容。最后返回列表，格式如下：

```python
[{
    "type": str,                        # 磁力链接类型
    "category": str,                    # 磁力链接分类
    "categoryId": str,                  # 磁力链接分类 ID
    "comments": int,                    # 磁力链接评论数
    "title": str,                       # 磁力链接标题
    "link": str,                        # 磁力链接链接
    "id": int,                          # 磁力链接 ID
    "torrent": str or None,             # 磁力链接种子链接，如果没有则为 None
    "magnet": str,                      # 磁力链接的 magnet 链接
    "size": str,                        # 磁力链接大小
    "time": str,                        # 磁力链接发布时间
    "seeders": int,                     # 磁力链接种子数
    "leechers": int,                    # 磁力链接吸血鬼数
    "completes": int                    # 磁力链接完成数
}]
```

#### parseSearch

> 解析，序列化，睡觉

该接口用于解析一个搜索结果页面，需要两个参数：`soup` 和 `site`。前者是 BeautifulSoup 对象，后者是整数，表示什么网站，0 表示 Nyaa，1 表示 Sukebei。最后返回列表，格式如下：

```python
[{
    "type": str,                        # 磁力链接类型
    "typeExtra": str,                   # 磁力链接类型额外信息（若有）
    "category": str,                    # 磁力链接分类
    "categoryId": str,                  # 磁力链接分类 ID
    "comments": int,                    # 磁力链接评论数
    "title": str,                       # 磁力链接标题
    "link": str,                        # 磁力链接链接
    "id": int,                          # 磁力链接 ID
    "torrent": str,                     # 磁力链接种子链接，如果没有则为 None
    "magnet": str,                      # 磁力链接的 magnet 链接
    "size": str,                        # 磁力链接大小
    "time": str,                        # 磁力链接发布时间
    "timeStamp": int,                   # 磁力链接发布时间戳
    "seeders": int,                     # 磁力链接种子数
    "leechers": int,                    # 磁力链接吸血鬼数
    "completes": int                    # 磁力链接完成数
}]
```

#### search

> 正在激活扩展

该接口是搜索接口，用于搜索磁力链接，需要一个参数：`params`，格式如下：

```python
{
    "page": int or str,             # 页码，从 1 开始
    "keyword": str,                 # 搜索关键词
    "category": str,                # 分类
    "filter": str,                  # 过滤器： No / No Remakes / Trusted Only （不过滤 / 不 Remake / 只信任）
    "order": str,                   # 评分： Comments / Size / Date / Seeders / Leechers / Completed Downloads
                                    # 评论 / 大小 / 日期 / 种子数 / 吸血鬼数 / 完成下载数
    "site": str or int,             # 网站. 0 是 https://nyaa.si/, 1 是 https://sukebei.nyaa.si/
                                    # 这个是必须的，其余都是可选的
    "orderBy": str                  # 排序 asc / desc （正序 / 倒序）
}
```

最后返回列表，格式同 `parseSearch`。

#### searchRSS

> 犯罪活动

该接口是 RSS 搜索接口，用于搜索磁力链接，需要一个参数：`params`，格式同上，最后返回也是列表，格式同 `parseRSS`。

#### getViewFromId

> 签出分支

该接口用于获取一个磁力链接的详细信息，需要两个参数：`id` 和 `site`，前者是整数或字符串，表示磁力链接 ID，后者是整数，表示什么网站，0 表示 Nyaa，1 表示 Sukebei。最后返回字典，格式同 `parsePage`。

### waziPicAcg

> 即将结束这种荒诞的活动

PicAcg 是一个让你可以轻松看到不同的本子的程式，据说官方不是很欢迎第三方，如果有冒犯的话，我可能将会中止维护 PicAcg 的活动。

#### 被实例化时的操作

> 一定需要一些条件

在被实例化时，会自动设置请求头，详情见下文。

#### giveParams

> 完结

设置用户参数，参数是 `params` 字典，完成之后返回当前用户的参数。

#### editHeaders

> 27 秒钟之前

在实例化时该接口将被调用，用于设置请求头，将生成 `uuid` 填入请求头的 `nonce`，并也将 `api-key` 填入。

#### sign

> 海关

该接口用于签名一个请求，在任何请求之前都需要使用该函数进行签名，签名的结果将被放在请求头中。你需要两个参数：`url` 和 `method`。`url` 表示请求的 URL，`method` 表示请求的方法，可以是 `GET`、`POST`、`PUT`、`DELETE` 之类的。

最后将透过 `self.check.construct` 签名，获取签名字符串和时间戳填入自定义请求头。

#### up

> 过门的时候我也喜欢加两个 Clap

该接口用于发送一个请求，将会自动签名，无需用户签名。需要五个参数：

+ `url`：请求的 URL，应当是字符串；
+ `needAuth`：是否需要验证，应当是布尔值；
+ `data`：请求的数据，应当是字典；
+ `method`：请求的方法，应当是字符串；
+ `jsonNeed`：是否需要 JSON 格式，应当是布尔值。

（`jsonNeed` / `needAuth` 这两个，谔谔，算了）最后如果 `jsonNeed` 是 `True`，则会自动将 `data` 转换为 JSON 格式，否则直接返回：`urllib3.response.HTTPResponse` 格式。

#### justUP

> Amore

该接口用于发送一个不带签名和验证的请求（事实上，是不带自定义请求头），通常用在获取文件上，需要四个参数：

+ `url`：请求的 URL，应当是字符串；
+ `data`：请求的数据，应当是字典；
+ `method`：请求的方法，应当是字符串；
+ `jsonNeed`：是否需要 JSON 格式，应当是布尔值。

最后如果 `jsonNeed` 是 `True`，则会自动将 `data` 转换为 JSON 格式，否则直接返回：`urllib3.response.HTTPResponse` 格式。

#### normalUP

> 斟酌

不知道封装了多少次，总而言之 `up` 和 `justUP` 都通过 `normalUP` 实现，大抵就是多次封装，层层套娃，脱裤子放屁的设计思想吧（大嘘）。需要五个参数：

+ `tempParams`：用户自定义参数，应当是字典；
+ `url`：请求的 URL，应当是字符串；
+ `data`：请求的数据，应当是字典；
+ `method`：请求的方法，应当是字符串；
+ `jsonNeed`：是否需要 JSON 格式，应当是布尔值。

最后如果 `jsonNeed` 是 `True`，则会自动将 `data` 转换为 JSON 格式，否则直接返回：`urllib3.response.HTTPResponse` 格式。

#### login

> 前提

使用该接口进行登录，是大部分操作的前提，需要两个参数：`username` 和 `password`。登录成功后将自动写入 `token` 到请求头并返回，否则报错。

#### getCategories

> 分治

使用该接口获取分类列表，不需要任何参数。最后返回字典：

```python
{
    "code": int,                            # 返回状态码
    "message": str,                         # 返回信息
    "data": {                               # 返回数据
        "categories": [{                    # 分类列表
            "title": str,                   # 分类名称
            "thumb": {                      # 分类图标
                "originalName": str,        # 原始文件名
                "path": str,                # 图标路径
                "fileServer": str           # 图标服务器
            },
            "isWeb": bool,                  # 是否是网页分类
            "active": bool,                 # 是否激活
            "link": str,                    # 分类链接
            "_id": str,                     # 分类 ID
            "description": str,             # 分类描述
        }]
    }
}
```

#### getComicsWithFullParams

> 非常神必

这个接口用于获取漫画，作者还没有试过，所以我不清楚到底会咋样，需要八个参数：

+ `page`：页码，应当是整数，从 1 开始；
+ `c`：分类，应当是字符串；
+ `t`：标签，应当是字符串，大部分时候应该使用繁体中文；
+ `a`：作者，应当是字符串；
+ `f`：是否完结，应当是布尔值；
+ `s`：排序，应当是字符串，对应格式如下：
    + `ua`：默认排序；
    + `dd`：从新到旧；
    + `vd`：绅士指名；
    + `ld`：最多喜欢。
+ `ct`：中文翻译组，应当是字符串；
+ `ca`：漫画作者 ID，应当是字符串。

最后返回字典，但是我这失效了就很神必。

#### getComics

> 因为顺序吗？

这个接口估计失效了，同样用于获取漫画，但它的所需参数较少，你需要四个参数：`page`，`c`，`t`，`s`。参数格式同上，最后依旧返回字典，不知道为啥就失效了。

#### search

> 可是我还有办法

这个接口用于搜索漫画，同样失效了，但在下文我将提供一个可以代替 `getComics` 等的高级搜索接口。

你需要两个参数：`page` 和 `keyword`。前者可以是字符串或者整数，从 1 开始数起，后者表示搜索关键字，是字符串。

#### getComic

> 希望我能够在你写完之前帮你（笑），过段时间估计要封校了，上海疫情有点严重。 -A

该接口用于获取漫画的信息，需要一个参数：`comicId`，应当是字符串，表示漫画的 ID。最后返回字典：

```python
{
    "code": int,                                            # 返回状态码
    "message": str,                                         # 返回信息
    "data": {                                               # 返回数据
        "comic": {                                          # 漫画信息
            "_id": str,                                     # 漫画 ID
            "_creator": {                                   # 漫画上传者
                "_id": str,                                 # 漫画上传者 ID
                "gender": str,                              # 漫画上传者性别
                "name": str,                                # 漫画上传者姓名
                "verified": bool,                           # 漫画上传者是否可行
                "exp": int,                                 # 漫画上传者经验
                "level": int,                               # 漫画上传者等级
                "characters": list[str],                    # 漫画上传者角色
                "role": str,                                # 漫画上传者角色
                "title": str,                               # 漫画上传者头衔
                "avatar": {                                 # 漫画上传者头像
                    "originalName": str,                    # 漫画上传者头像原始名称
                    "path": str,                            # 漫画上传者头像路径
                    "fileServer": str                       # 漫画上传者头像文件服务器
                },
                "slogan": str,                              # 漫画上传者签名
                "character": str                            # 漫画上传者角色
            },
            "title": str,                                   # 漫画标题
            "description": str,                             # 漫画描述
            "thumb": {                                      # 漫画缩略图
                "originalName": str,                        # 漫画缩略图原始名称
                "path": str,                                # 漫画缩略图路径
                "fileServer": str                           # 漫画缩略图文件服务器
            },
            "author": str or may be other object,           # 漫画作者
            "chineseTeam": str or may be other object,      # 漫画汉化组
            "categories": list[str],                        # 漫画分类
            "tags": list[str],                              # 漫画标签
            "pagesCount": int,                              # 漫画页数
            "epsCount": int,                                # 漫画集数
            "finished": bool,                               # 漫画是否完结
            "updated_at": str,                              # 漫画更新时间
            "created_at": str,                              # 漫画创建时间
            "allowDownload": bool,                          # 漫画是否允许下载
            "allowComment": bool,                           # 漫画是否允许评论
            "totalLikes": int,                              # 漫画点赞数
            "totalViews": int,                              # 漫画浏览数
            "viewsCount": int,                              # 漫画浏览数
            "likesCount": int,                              # 漫画点赞数
            "isFavorite": bool,                             # 漫画是否被用户收藏
            "isLiked": bool,                                # 漫画是否被用户喜欢
            "commentsCount": int                            # 漫画评论数
        }
    }
}
```

#### getComicEps

> 谢谢你，不过快完事了

通过该接口获取漫画的分页信息，需要两个参数：`comicId` 和 `page`，应当是字符串，表示漫画的 ID，后者表示分页页码，可以是字符串或者整数。返回字典，格式如下：

```python
{
    "code": int,                                            # 返回状态码
    "message": str,                                         # 返回信息
    "data": {                                               # 返回数据
        "eps": {                                            # 漫画分页信息
            "docs": [{                                      # 漫画分页列表
                "_id": str,                                 # 漫画集 ID
                "title": str,                               # 漫画集标题
                "order": int,                               # 漫画集顺序
                "updated_at": str,                          # 漫画集更新时间
                "id": str                                   # 漫画集 ID
            }],
            "total": int,                                   # 漫画集总数
            "limit": int,                                   # 漫画集每页限制
            "page": int,                                    # 漫画集当前页码
            "pages": int                                    # 漫画集总页数
        }
    }
}
```

#### advancedSearch

> 就很棒

一个高级搜索，用于代替漫画获取等的接口，需要四个参数：`categories`, `keyword`, `sort` 和 `page`。`categories` 应当是带字符串的列表，表示漫画分类，如果没有则直接设置空列表即可；`keyword` 表示搜索关键词；`sort` 表示排序方式，上文有写该内容；`page` 表示分页页码，可以是字符串或者整数，从 1 开始。返回字典，格式如下：

```python
{
    "code": int,                                            # 返回状态码
    "message": str,                                         # 返回信息
    "data": {                                               # 返回数据
        "comics": {                                         # 漫画信息
            "total": int,                                   # 漫画总数
            "page": int,                                    # 当前页面
            "pages": int,                                   # 总页面数
            "docs": [{                                      # 漫画列表
                "updated_at": str,                          # 漫画更新时间
                "thumb": {                                  # 漫画缩略图
                    "originalName": str,                    # 漫画缩略图原始名称
                    "path": str,                            # 漫画缩略图路径
                    "fileServer": str                       # 漫画缩略图文件服务器
                },
                "author": str,                              # 漫画作者
                "description": str,                         # 漫画描述
                "chineseTeam": str or may other object,     # 漫画汉化组
                "created_at": str,                          # 漫画创建时间
                "finished": bool,                           # 漫画是否完结
                "categories": [str],                        # 漫画分类
                "title": str,                               # 漫画标题
                "tags": [str],                              # 漫画标签
                "_id": str,                                 # 漫画 ID
                "likesCount": int                           # 漫画点赞数
            }],
            "limit": int                                    # 搜索每页限制
        }
    }
}
```

#### getComicPages

> 这里不是补充说明

使用该接口用于获取一个漫画分页的内容，你需要三个参数：`comicId`, `eps` 和 `page`。`comicId` 表示漫画 ID，应当是字符串；`eps` 表示漫画章节或分页量，是整数；`page` 表示分页页码，可以是字符串或者整数，从 1 开始。返回字典，格式如下：

```python
{
    "code": int,                                            # 返回状态码
    "message": str,                                         # 返回信息
    "data": {                                               # 返回数据
        "pages": {                                          # 分页小节信息
            "docs": [{                                      # 分页小节列表
                "_id": str,                                 # 分页小节 ID
                "media": {                                  # 分页小节媒体信息
                    "originalName": str,                    # 分页小节媒体原始名称
                    "path": str,                            # 分页小节媒体路径
                    "fileServer": str                       # 分页小节媒体文件服务器
                },
                "id": str                                   # 分页小节 ID
            }],
            "total": int,                                   # 分页小节总数
            "limit": int,                                   # 分页小节每页限制显示量
            "page": int,                                    # 分页小节当前页面
            "pages": int                                    # 分页小节总页面数
        },
        "ep": {                                             # 漫画章节信息
            "_id": str,                                     # 漫画章节 ID
            "title": str                                    # 漫画章节标题
        }
    }
}
```

#### getComicRecommend

> 破旧的齿轮

使用该接口获取一个漫画的相关推荐，需要一个参数：`comicId`，返回字典，格式如下：

```python
{
    "code": int,                                        # 返回状态码
    "message": str,                                     # 返回信息
    "data": {                                           # 返回数据
        "comics": [{                                    # 漫画列表
            "_id": str,                                 # 漫画 ID
            "title": str,                               # 漫画标题
            "author": str,                              # 漫画作者
            "pagesCount": int,                          # 漫画总页数
            "epsCount": int,                            # 漫画总章节数
            "finished": bool,                           # 漫画是否完结
            "categories": [str],                        # 漫画分类
            "thumb": {                                  # 漫画封面
                "originalName": str,                    # 漫画封面原始名称
                "path": str,                            # 漫画封面路径
                "fileServer": str                       # 漫画封面文件服务器
            },
            "likesCount": int                           # 漫画喜欢数
        }]
    }
}
```

#### getKeywords

> 钥匙

使用该接口获取当前搜索热词，不需要任何参数，返回字典，格式如下：

```python
{
    "code": int,                                        # 返回状态码
    "message": str,                                     # 返回信息
    "data": {                                           # 返回数据
        "keywords": [str]                               # 热词列表
    }
}
```

#### getMyComments

> 查看你的黑历史发言

使用该接口获取当前用户所有评论内容，你需要一个参数：`page`，从 1 开始，表示页码，应当是字符串或者整数，返回字典，格式如下：

```python
{
    "code": int,                                        # 返回状态码
    "message": str,                                     # 返回信息
    "data": {                                           # 返回数据
        "comments": {                                   # 用户评论数据
            "docs": [],                                 # 里面就是你的评论了 可是我一条都没发表过 这边我就不说了
            "total": int,                               # 评论总数
            "limit": int,                               # 每页限制
            "page": str,                                # 当前页码
            "pages": int                                # 总页码
        }
    }
}
```

#### getMyFavourites

> 你所热爱的 就是你的生活 —— 陈睿

使用该接口获取当前用户收藏夹内容，你需要两个参数：`page` 和 `s`。`page` 表示页码，是字符串或整数，从 1 开始；`s` 表示排序，只能允许 `ua`, `dd` 和 `da`。最后返回字典，格式如下：

```python
{
    "code": int,                                    # 返回状态码
    "message": str,                                 # 返回信息
    "data": {                                       # 返回数据
        "comics": {                                 # 收藏夹内容
            "pages": int,                           # 收藏夹总页数
            "total": int,                           # 收藏夹内容总数
            "docs": [{                              # 收藏夹内容列表
                "_id": str,                         # 漫画 ID
                "title": str,                       # 漫画标题
                "author": str,                      # 漫画作者
                "pagesCount": int,                  # 漫画总页数
                "epsCount": int,                    # 漫画总章节数
                "finished": bool,                   # 漫画是否完结
                "categories": [str],                # 漫画分类
                "thumb": {                          # 漫画封面
                    "fileServer": str,              # 漫画封面文件服务器
                    "path": str,                    # 漫画封面路径
                    "originalName": str             # 漫画封面原始名称
                },
                "totalViews": int,                  # 漫画总浏览数
                "totalLikes": int,                  # 漫画总喜欢数
                "likesCount": int                   # 漫画喜欢数
            }],
            "page": int,                            # 当前页码
            "limit": int                            # 每页限制
        }
    }
}
```

#### getMyProfile

> 突然想起来，唢呐的哨片，不知道给我放到哪里去了。

使用该接口获取当前用户个人信息，你不需要任何参数，返回字典，格式如下：

```python
{
    "code": int,                                    # 返回状态码
    "message": str,                                 # 返回信息
    "data": {                                       # 返回数据
        "user": {                                   # 用户信息
            "_id": str,                             # 用户 ID
            "birthday": str,                        # 用户生日
            "email": str,                           # 用户邮箱
            "gender": str,                          # 用户性别
            "name": str,                            # 用户名
            "slogan": str,                          # 用户签名
            "title": str,                           # 用户头衔
            "verified": bool,                       # 用户是否已经验证
            "exp": int,                             # 用户经验值
            "level": int,                           # 用户等级
            "characters": [str],                    # 用户角色
            "created_at": str,                      # 用户创建时间
            "avatar": {                             # 用户头像
                "fileServer": str,                  # 用户头像文件服务器
                "path": str,                        # 用户头像路径
                "originalName": str                 # 用户头像原始名称
            },
            "isPunched": bool,                      # 用户是否已经签到
            "character": str                        # 用户当前角色
        }
    }
}
```

#### getGames

> Do

使用该接口获取游戏区内容，需要一个参数：`page`，表示页码，应当是字符串或者整数，从 1 开始数起。最后返回字典，格式如下：

```python
{
    "code": int,                                    # 返回状态码
    "message": str,                                 # 返回信息
    "data": {                                       # 返回数据
        "games": {                                  # 游戏区内容
            "docs": [{                              # 游戏区内容列表
                "_id": str,                         # 游戏 ID
                "title": str,                       # 游戏标题
                "version": str,                     # 游戏版本
                "publisher": str,                   # 游戏发行商
                "suggest": bool,                    # 是否被推荐
                "adult": bool,                      # 是否是 R-18
                "android": bool,                    # 是否支持 Android
                "ios": bool,                        # 是否支持 iOS
                "icon": {                           # 游戏图标
                    "originalName": str,            # 游戏图标原始名称
                    "path": str,                    # 游戏图标路径
                    "fileServer": str               # 游戏图标文件服务器
                }
            }],
            "total": int,                           # 游戏区内容总数
            "limit": int,                           # 每页限制
            "page": int,                            # 当前页码
            "pages": int                            # 总页数
        }
    }
}
```

#### getGameInfo

> 告诉我它的一切

使用该接口获取一个游戏的详细信息，需要一个参数：`gameId`，表示游戏 ID，应当是字符串。最后返回字典，格式如下：

```python
{
    "code": int,                                    # 返回状态码
    "message": str,                                 # 返回信息
    "data": {                                       # 返回数据
        "game": {                                   # 游戏信息
            "_id": str,                             # 游戏 ID
            "title": str,                           # 游戏标题
            "description": str,                     # 游戏描述
            "version": str,                         # 游戏版本
            "icon": {                               # 游戏图标
                "fileServer": str,                  # 游戏图标文件服务器
                "path": str,                        # 游戏图标路径
                "originalName": str                 # 游戏图标原始名称
            },
            "publisher": str,                       # 游戏发布者
            "ios": bool,                            # 是否支持 iOS
            "iosLinks": [str],                      # iOS 下载链接
            "android": bool,                        # 是否支持 Android
            "androidLinks": [str],                  # Android 下载链接
            "adult": bool,                          # 是否是 R-18
            "suggest": bool,                        # 是否被推荐
            "downloadsCount": int,                  # 下载次数
            "screenshots": [{                       # 游戏截图
                "originalName": str,                # 截图原始名称
                "path": str,                        # 截图路径
                "fileServer": str                   # 截图文件服务器
            }],
            "androidSize": int,                     # Android 游戏大小
            "iosSize": int,                         # iOS 游戏大小
            "updateContent": str,                   # 更新内容
            "updated_at": str,                      # 更新时间
            "created_at": str,                      # 创建时间
            "likesCount": int,                      # 喜欢数
            "isLiked": bool,                        # 用户是否喜欢
            "commentsCount": int                    # 评论数
        }
    }
}
```

#### likeOrUnLikeGame

> 你的热爱

使用该接口喜欢或者取消喜欢一个游戏，需要一个参数：`gameId`，表示游戏 ID，应当是字符串。原本喜欢，使用该接口后就取消喜欢；原本没有喜欢，使用该接口后就喜欢。最后返回字典，格式如下：

```python
{
    "code": int,                                    # 返回状态码
    "message": str,                                 # 返回信息
    "data": {                                       # 返回数据
        "action": str                               # 动作，喜欢或者取消喜欢 (like or unlike)
    }
}
```

#### favOrUnFavComic

> 购物车

使用该接口收藏或取消收藏一个漫画，需要一个参数：`comicId`，表示漫画 ID，应当是字符串。最后返回字典，格式如下：

```python
{
    "code": int,                                    # 返回状态码
    "message": str,                                 # 返回信息
    "data": {                                       # 返回数据
        "action": str                               # 动作，收藏或取消收藏 (favorite or un_favorite)
    }
}
```

#### likeOrUnLikeComic

> 热

使用该接口喜欢或取消喜欢一个漫画，需要一个参数：`comicId`，表示漫画 ID，应当是字符串。最后返回字典，格式同 `likeOrUnLikeGame` 一致。

#### likeOrUnLikeComment

> 😔

使用该接口喜欢或取消喜欢一个评论，需要一个参数：`commentId`，表示评论 ID，应当是字符串。最后返回字典，格式同 `likeOrUnLikeGame` 一致。

#### hideOrUnHideComment

> 4536251

使用该接口隐藏或取消隐藏一个评论，需要一个参数：`commentId`，表示评论 ID，应当是字符串。最后我不清楚返回什么，我只能拿到 1005 权限错误。

#### getCommentsChildren

> 啮齿目

使用该接口获取一个评论下的子评论，需要两个参数：`commentId`，表示评论 ID，应当是字符串；`page`，表示页码，应当是整数或字符串，从 1 开始。最后返回字典，格式如下：

```python
{
    "code": int,                                    # 返回状态码
    "message": str,                                 # 返回信息
    "data": {                                       # 返回数据
        "comments": {                               # 评论内容
            "docs": [{                              # 评论列表
                "_id": str,                         # 评论 ID
                "content": str,                     # 评论内容
                "_user": {                          # 评论者信息
                    "_id": str,                     # 用户 ID
                    "gender": str,                  # 用户性别
                    "name": str,                    # 用户名
                    "title": str,                   # 用户头衔
                    "verified": bool,               # 用户是否被验证
                    "exp": int,                     # 用户经验值
                    "level": int,                   # 用户等级
                    "characters": [str],            # 用户角色
                    "role": str,                    # 用户角色
                    "avatar": {                     # 用户头像
                        "originalName": str,        # 头像原始名称
                        "path": str,                # 头像路径
                        "fileServer": str,          # 头像文件服务器
                    },
                    "slogan": str,                  # 用户签名
                    "character": str                # 用户头像框
                },
                "_parent": str,                     # 父评论 ID
                "_comic": str,                      # 漫画 ID
                "_game": str,                       # 游戏 ID
                "isTop": bool,                      # 是否置顶
                "hide": bool,                       # 是否隐藏
                "created_at": str,                  # 创建时间
                "id": str,                          # 评论 ID
                "likesCount": int,                  # 喜欢数
                "isLiked": bool                     # 是否喜欢
            }],
            "total": int,                           # 评论总数
            "limit": int,                           # 每页评论数
            "page": str,                            # 当前页码
            "pages": int                            # 总页数
        }
    }
}
```

#### replyComment

> 告知我的内心

使用该接口进行一个评论的回复，你需要两个参数：`commentId` 和 `content`。`commentId` 表示评论 ID，应当是字符串；`content` 表示回复内容，应当是字符串。

最后返回格式鉴于我没有进行测试故不得而知。

#### reportComment

> 春生被他们打倒在地，身体搁在那块木牌上，一只脚踢在他脑袋上，春生的脑袋像是被踢出个洞似的咚的一声响，整个人趴在了地上。 —— 余华 活着

使用该接口进行一个评论的举报，好像不需要理由的样子，你需要一个参数：`commentId`，表示评论 ID，应当是字符串。

最后返回格式鉴于我没有进行测试故不得而知。

#### topOrUnTopComment

> 领头的红卫兵是个女的，他们来到了我们跟前，那女的朝我们喊：“这里为什么没有标语，没有大字报？队长呢？队长是谁？” —— 余华 活着

使用该接口进行一个评论的置顶，似乎普通用户也可以完成这个操作？你需要一个参数：`commentId`，表示评论 ID，应当是字符串。最后返回是字典，格式如下：

```python
{
    "code": int,                                    # 返回状态码
    "message": str,                                 # 返回信息
    "data": {                                       # 返回数据
        "isTop": bool                               # 是否置顶
    }          
}
```

#### getGameComments

> 获取反对派的声明

使用该接口获取一个游戏的评论区，你需要两个参数：`gameId` 和 `page`。前者是字符串，表示游戏 ID；后者是整数或字符串，表示页码，从 1 数起，最后返回是字典，格式如下：

```python
{
    "code": int,                                    # 返回状态码
    "message": str,                                 # 返回信息
    "data": {                                       # 返回数据
        "comments": {                               # 评论
            "docs": [{                              # 评论列表
                "_id": str,                         # 评论 ID
                "content": str,                     # 评论内容
                "_user": {                          # 用户信息
                    "_id": str,                     # 用户 ID
                    "gender": str,                  # 用户性别
                    "name": str,                    # 用户名
                    "title": str,                   # 用户头衔
                    "verified": bool                # 是否认证
                    "exp": int,                     # 用户经验值
                    "level": int,                   # 用户等级
                    "characters": list[str],        # 用户角色
                    "role": str,                    # 用户角色
                    "avatar": {                     # 用户头像
                        "originalName": str,        # 原始文件名
                        "path": str,                # 头像路径
                        "fileServer": str           # 文件服务器
                    },
                    "slogan": str,                  # 用户签名
                    "character": str                # 用户头像框
                },
                "_game": str,                       # 游戏 ID
                "isTop": bool,                      # 是否置顶
                "hide": bool,                       # 是否隐藏
                "created_at": str,                  # 创建时间
                "id": str,                          # 评论 ID
                "likesCount": int,                  # 点赞数
                "commentsCount": int,               # 评论数
                "isLiked": bool                     # 是否已点赞
            }],
            "total": int,                           # 评论总数
            "limit": int,                           # 每页数量
            "page": str,                            # 当前页码
            "pages": int                            # 总页码数
        },
        "topComments": [{                           # 置顶评论
            "_id": str,                             # 评论 ID
            "content": str,                         # 评论内容
            "_user": {                              # 用户信息
                "_id": str,                         # 用户 ID
                "gender": str,                      # 用户性别
                "name": str,                        # 用户名
                "title": str,                       # 用户头衔
                "verified": bool                    # 是否认证
                "exp": int,                         # 用户经验值
                "level": int,                       # 用户等级
                "characters": list[str],            # 用户角色
                "role": str,                        # 用户角色
                "avatar": {                         # 用户头像
                    "originalName": str,            # 原始文件名
                    "path": str,                    # 头像路径
                    "fileServer": str               # 文件服务器
                },
                "slogan": str,                      # 用户签名
                "character": str                    # 用户头像框
            },
            "ip": str,                              # IP 地址
            "_game": str,                           # 游戏 ID
            "isTop": bool,                          # 是否置顶
            "hide": bool,                           # 是否隐藏
            "created_at": str,                      # 创建时间
            "likesCount": int,                      # 点赞数
            "commentsCount": int,                   # 评论数
            "isLiked": bool                         # 是否已点赞
        }]
    }
}
```

#### postGameComment

> 勇敢



