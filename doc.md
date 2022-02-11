# PyWazi 开发文档

> 1.3 Version

*我们总想安稳，以自己的方式掌握周遭的世界。*

在开始使用 PyWazi 之前，我有必要警告你：

1. 这是一个非常糟糕并且仅由一个人开发的爬虫框架，尽管它支持的功能较多但它效率低下；
2. 没有统一的返回格式和参数，包括大小写的统一；
3. 日志、请求系统均不采用流行的方式，不使用 requests, logging 等；
4. 它的日志系统过于繁琐，尽管你可以设置取消日志；
5. 可能较为脆弱的稳定性，因为测试并未完全进行。

在本开发文档中，我将不介绍所有基础模块，只介绍 `sites` 模块的使用。

## 配置环境

*给它所需要的水和食物，还有大三和弦。*

你需要：

1. Python >= 3.9
2. lxml >= 4.6.3
3. beautifulsoup4 >= 4.9.3

或许低版本也可以，只不过我没有进行测试。

## 导入 PyWazi

*开始一件伟大的事情的时候，手上得拿着一根棍子。*

```python
from pywazi import *
```

如果你只想导入部分模块则可以使用（事实上在 pywazi.py 中，它已经导入全部的模块）：

```python
from pywazi import waziXXX
```

目前存在的站点模块有：

+ `waziAsianSister` - 收集 AsianSister 中画廊和视频的模块
+ `waziDanbooru` - 获取或下载 Danbooru 类网站的图集、标签、图片等的模块
+ `waziExHentai` - 获取或下载 ExHentai 网站的图片、评论等的模块
+ `waziJavBus` - 获取 JavBus 番号磁力链接以及信息的模块
+ `waziNyaa` - 获取 waziNyaa 网站的磁力、信息等的模块
+ `waziPicAcg` - 基于官方 API 的获取 PicAcg 图片、信息等的模块

导入时自动读取目录下的 config.json 作为默认配置。

## 主模块教程

*我放弃了 init 文件，因为我是那样的无知。*

主模块存在两个函数，以用于读取配置并设置。

### 全局配置

*每个人都一样的集体社会，就像大统领得了 OCD 一样。*

使用 `globalParams` 以读取全局配置，会给所有模块传入同样的 `giveParams` 函数参数。

```python
from pywazi import *

globalParams("./config.json")
```

json 应当为如下格式：

```json
{
    "useProxies": true,
    "proxyAddress": "",
    "proxyPort": ""
}
```

### 单独读取配置

*我所热爱的，个人主义，所以我们死去。*

使用 `defConfig` 以读取各类配置，会给所有的模块以不同的配置函数。

```python
from pywazi import *

defConfig("./config.json") # 你的 JSON 文件目录
```

json 应当为如下格式：

```json
[{
	"name": "JavBus", // JavBus
	"params": {}, // 你的配置
    "url": "xxxx", // 镜像网站
    "eaUrl": "xxxx", // 欧美网站
    "type": 0, // 0 - mag 表示仅显示有磁力的影片 1 - all 表示全部显示
}, {
	"name": "PicAcg", // PicAcg
	"params": {}, // 你的配置
	"login": {
		"username": "xxxx",
		"password": "xxxx"
	}, // 账户名和密码
    "image": 0 // 0 1 2 3 分别对应 original low medium high
}, {
	"name": "Danbooru", // Danbooru
	"params": {}, // 账户名和密码
	"url": "https://konachan.com" // Danbooru 类网站
}, {
	"name": "ExHentai", // ExHentai
	"params": {}, // 账户名和密码
	"cookies": "xxxx", // 你的 Cookies
	"fullComment": true, // 是否需要完整评论
	"jump": true, // 是否跳过警告
    "parse": true, // 是否使用解析器
    "thumbType": "large" // large 大图模式 - normal 普通模式
}, {
    "name": "AsianSister", // AsianSister
    "params": {} // 你的配置
}, {
    "name": "Nyaa", // Nyaa
    "params": {} // 你的配置
}, {
	"name": "Config", // Config
	"save": true, // 是否保存日志
	"level": 5 // 日志显示等级
}]
```

## waziAsianSister 模块
