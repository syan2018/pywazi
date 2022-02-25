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

1. 这个项目仅有一个人负责，尽管它支持的功能较多但它效率低下，尤其是 ExHentai 部分；
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
    "useProxies": True,				# 是否使用代理
    "proxyAddress": "127.0.0.1",	# 代理地址
    "proxyPort": 7890				# 代理端口
})

waziDanbooru.setApi("https://konachan.com") # 设置你想爬的 Danbooru 类网站地址

for page in range(1, 101):
    # 爬一百页
    waziDanbooru.downloadPosts(
        page = page,					# 指定页码
        tags = "rating:explicit",		# 标签
        limit = 40, 					# 每页限制几张图片，最多就 40 张
        path = "./download"				# 下载目录
    )
```

> 代码案例: 自动爬取 Konachan 100 页 R-18 图片

```python
from pywazi import waziJavBus	# JavBus 解决方案

waziJavBus.giveParams({
    "useProxies": True,				# 是否使用代理
    "proxyAddress": "127.0.0.1",	# 代理地址
    "proxyPort": 7890				# 代理端口
})

# 浏览
items = waziJavBus.browse(
    page = 1,			# 页码
    tag = "4u",			# 标签 ID 4u 表示 戲劇
    avType = 0			# AV 类型 0 是有码 1 是无码
)

for i in items:
    print(f"{i['avId']} - {i['title']}")	# 打印所有获取到的番号和标题
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

以下按照字母排序进行排列。提醒一下，关于模块的参数等内容，如果文档不够明晰，可以借助 `help()` 函数以进行查询。

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

> 给这个世界上的颜色加上一点点阳光。

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