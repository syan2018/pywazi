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

该接口的参数是BeautifulSoup对象，可以是`link`字符串，返回值为视频基本信息，例如标题、播放数、标签等等。

#### parseGallery

> Please make love, not war. -A

该接口的参数是BeautifulSoup对象，可以是`link`字符串，返回值为图片信息，大致同`parseVideo`。

#### parsePerson

>查成分 -A

该接口的参数是BeautifulSoup对象，可以是`link`字符串，返回值为个人主页信息，同上两个接口。

#### parseRecommendImagesAndVideos

>政治和权利都只是别有用心的人的玩物罢了，不要过度相信推送 -A

该接口的参数是BeautifulSoup对象，`link`字符串，源码当中需要包含 ___`<div class="recommentBox"></div>`与`<div class="recommentBoxVideo"></div>`___ ，返回两个`list`，为推荐图片和视频，一个同`parseVideo`的返回值（大概），另一个同`parseGallery`的返回值（大概）。

#### parseImagesAndVideos

> 人类从不吸取教训 -A

该接口的参数是BeautifulSoup对象，`link`字符串，`link`可以是搜索结果也可以是单纯的页面，例如 _https://asiansiter.com/_；返回值与 ___`parseRecommendImagesAndVideos`___ 几乎完全相同，不再过多赘述。

#### getPage

> 相比魔怔人，我还是喜欢mmr，当然，像我一样做个不出声的乐子人也行 -A

接口参数是`page`基本整型，为页面数字（第一页即为1），返回值同样是两个`list`，不多赘述。

#### search

> 刚吃完午饭的下午可太困了 -A

该接口有两个参数，`keyword`字符串与`page`基本整型，返回值又又又是两个`list`。

#### tagsearch

> 定向研究 -A

该接口有两个参数，`tag`字符串与`page`基本整型，返回值又又又是两个`list`，基本同 ___`search`___。

#### personSearch

> 别查了，我什么成分都没有 -A

该接口参数为`person`字符串，返回三个`list`，相比之前多了对于个人信息的介绍。


#### getGallery

> 似乎快完了 -A

该接口参数是`gallery`字符串，返回一个`dict`，关于画册的基本信息。

#### getVideo

> 施法，施法 -A

该接口的参数为`video`字符串，返回一个含有视频信息的`dict`。

#### customParse

>“第一阶段战略目标实现”（笑） -A

该接口的参数为`content`字符串和`type`字符串，依据`type`的不同，返回值不同；返回值可能为 ___`parseImagesAndVideos()`，
`parsePerson()`
，`parseGallery()`
，`parseVideo()`___ 中的一种
