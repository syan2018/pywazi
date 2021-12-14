# PyWazi 前置文档

针对 ExHentai, JavBus, Danbooru, PicAcg 的模块。

## 设计哲学

PyWazi 的设计哲学为以下几点：

1. 没有；
1. 从来没有设计哲学。

## 关于与声明

<a href="https://www.python.org/"><img src="https://shields.io/badge/Python-3-green?style=flat-square" /></a> <a href="https://github.com/Yazawazi/pywazi/tree/1.1.9-dev"><img src="https://shields.io/badge/Version-1.2-green?style=flat-square" /></a>

PyWazi 是一个针对 ExHentai, JavBus, Danbooru, PicAcg 的数据采集、处理和操作模块，使用 Python 语言。目前版本为 1.2，如果你有想法或在使用中出现问题了，欢迎提出 issue。

本模块完全开放源代码，仅供大家学习参考使用，不鼓励一切在中国大陆境内的使用该模块的商业行为。

## 感谢

1. ExHentai 部分：感谢 [cloudwindy](https://github.com/cloudwindy) 提供了 ExHentai 账号得以我进行测试；
2. JavBus 部分：感谢 [WWILLV 的 iav](https://github.com/WWILLV/iav) 和 [akkuman 的 Javbus_crawler](https://github.com/akkuman/Javbus_crawler) 这两个项目，我在代码中或多或少使用到了他们；
3. Danbooru 部分：感谢 [Danbooru 项目](https://github.com/danbooru/danbooru) 和 [Moebooru 项目](https://github.com/moebooru/moebooru)；
4. PicAcg 部分：感谢 [AnkiKong 分享的部分 PicAcg 的 API](https://github.com/AnkiKong/picacomic)；[PicAcg-Windows 项目](https://github.com/tonquer/picacg-windows)，提供了其他的 API 接口和最新的 Header，以及感谢 [czp 的有关 PicAcg 的内容](https://www.hiczp.com/wang-luo/mo-ni-bi-ka-android-ke-hu-duan.html) 得以让我有了想法并反编译 PicAcg 获得其他的 API 接口以及请求方式，最后感谢一位我已经记不得的 GitHub 用户，早期我的 PicAcg 模块有使用过他的代码，但他的项目我已无法寻找；
5. 其他部分：感谢我的朋友 **The Galaxy~ Of Dick** 制作了横幅图片。

## 配置
如果你是 Windows 用户请前往 Python 官网下载 Python 3 代的安装包或通过 Microsoft Store 下载 Python 3 代，然后可以再下载一个 Git 使用 clone 指令将该模块下载到本地，或者直接 Download ZIP 本项目。

如果你是非 Windows 用户，请检查你的系统是否自带 Python 3 代和 Git，否则请使用 apt yum pacman 等包管理器安装，并使用 Git 克隆本项目或直接 Download ZIP 本项目。

参考前置库：
- beautifulsoup4
- lxml
- urllib3

（或许可能有其他前置库并未囊括，请用户在提示导入错误时自行安装）

## 一些说明
有时候我的想法比较混乱，并且我不遵守 PEP 8，所以部分代码你可能看不懂。如果你有问题的话，可以找我谈谈或者自己修改一下。如果出现以下问题了，请试着解答以下问题找找原因：

1. 前置环境有安装吗？Python 是 3 代的吗？
2. 配置对了吗，代理类型不要搞混；
3. 账号密码或 Cookies 请保证正确，账号确保不受限；
4. 查看说明文档找找相关内容或百度、谷歌等相关内容。

如果这些都解决不了问题，请发表 issue 并提供上下文，可能的代码，前置库版本等有关信息。

## 有什么用
你可以单独使用 PyWazi 来开发爬虫，也可以使用该模块开发其他项目。

## 联系我
我很累，请不要联系我。

# PyWazi 说明文档

## 测试环境

Windows 11 - Python 3.9.6

- beautifulsoup4 4.9.3
- certifi 2021.5.30
- lxml 4.6.3
- urllib3 1.26.6

PyWazi 1.2

## 更新内容

1. 有针对 PicAcg 的聊天室需求的，可以前往 [PicAcg-Windows 项目](https://github.com/tonquer/picacg-windows)；

2. 删除了取消证书检查的请求模块；
3. 日志系统；
4. JavBus 的欧美分区和搜索；
5. ExHentai 的标签，数据等有增加；
6. 其他的 `Danbooru` 类网站的 API，和自定义接口；
7. 自动导入配置。

After Hours 是一种美学标签，其作品的主要灵感来自于看到一个通常应该有人但实际上环境空无一人的感觉和印象。[^1]

## 下次更新

我也不知道。

## 开始

### 导入 PyWazi

使用这行代码导入所有内容：

```python
from pywazi import *
```

如果只想导入部分则：

```python
from pywazi import waziXXXX, waziXXXX
```

目前存在以下站点模块：

1. `waziJavBus` - 帮助获取 JavBus 番号磁力链接以及信息的模块。
2. `waziPicAcg` - 涵盖了大部分 PicAcg 功能（除去聊天、程序的具体功能）的模块。
3. `waziDanbooru` - 获取或下载 Danbooru 类型网站的图片和标签。
4. `waziExHentai` - 涵盖了大部分 ExHentai 功能（除去给予评分、发送评论等功能）的模块。

导入时自动读取目录下的 `config.json` 作为默认配置。

### 高级导入

以下为高级导入教程，以方便用户导入自己所需要的或需要开发的模块。

#### 站点模块

```python
from sites.wazi站点名 import wazi站点名 [as xxx]
```

并且实例化它：

```python
aaa = xxx()
```

接着你就可以通过 `aaa` 来访问该站点模块的所有接口了。

#### 基础模块

如果你仅需要使用 `pywazi` 中的 `waziRequest` 等模块来开发自己的项目，那么可以这么做。以下我给出几个最好不使用我基础模块的理由：

1. 这些基础模块具有仅针对我程序的局限性，如果需要在你的程序中使用请修改相关内容或格式；
2. `waziRequest` 基础模块使用的是 `urllib3` ，这是一个简单但繁琐的模块以处理用户参数并发动网络请求的模块，它的逻辑我看一次忘一次，如果你只是需要网络请求为何不试试同样基于 `urllib3` 的 `requests`；
3. 好像除了 `waziRequest` ，其他基础模块在别的项目中似乎没有作用或者都可以找到替代品了。

导入：

```python
from mods.wazi基础模块名 import wazi基础模块名 [as xxx]
```

同样，你需要实例化它。

#### 实例化模块

>[重要] 我不建议你导入任何实例化模块：
>
>1. 如果你仅需要通过我的基础模块开发自己的项目，你最好导入抽象的模块；
>2. 如果你需要使用 PyWazi，你应该修改或导入 `pywazi` 主模块，并通过主模块允许的接口以操控实例化模块；
>3. 如果你开发 PyWazi，那么你可以导入实例化模块以控制配置，日志和其他内容（尽管现在不存在）。
>
>实例化模块是唯一一个合法实例化的抽象模块，用于统一配置等，使用时注意对全局的影响。

导入：

```python
from ins.wazi实例化模块名 import wazi实例化模块名
```

## 主模块教程

主模块存在两个函数，以用于读取配置并设置。

### 全局配置

使用 `globalParams` 以读取全局配置，会给所有模块传入同样的 `giveParams` 函数。

```python
from pywazi import *

globalParams("./config.json") # 你的 JSON 文件目录
```

json 应该是类似 `params` 的以下内容：

```json
{
    "useProxies": true,
    ...
}
```

### 读取配置

使用 `defConfig` 以读取各类配置，会给所有的模块以不同的配置函数。

```python
from pywazi import *

defConfig("./config.json") # 你的 JSON 文件目录
```

json 应该是类似的以下内容（没有的可以不写）：

```json
[{
	"name": "JavBus", // JavBus
	"params": {
		"useProxies": true,
		"proxyAddress": "127.0.0.1",
		"proxyPort": "7890"
	}, // 你的配置
    "url": "xxxx", // 镜像网站
    "eaUrl": "xxxx", // 欧美网站
    "type": 0, // 0 - mag 表示仅显示有磁力的影片 1 - all 表示全部显示
}, {
	"name": "PicAcg", // PicAcg
	"params": {
		"useProxies": true,
		"proxyAddress": "127.0.0.1",
		"proxyPort": "7890"
	}, // 你的配置
	"login": {
		"username": "xxxx",
		"password": "xxxx"
	}, // 账户名和密码
    "image": 0 // 0 1 2 3 分别对应 original low medium high
}, {
	"name": "Danbooru", // Danbooru
	"params": {
		"useProxies": true,
		"proxyAddress": "127.0.0.1",
		"proxyPort": "7890"
	}, // 账户名和密码
	"url": "https://konachan.com" // Danbooru 类网站
}, {
	"name": "ExHentai", // ExHentai
	"params": {
		"useProxies": true,
		"proxyAddress": "127.0.0.1",
		"proxyPort": "7890"
	}, // 账户名和密码
	"cookies": "xxxx", // 你的 Cookies
	"fullComment": true, // 是否需要完整评论
	"jump": true, // 是否跳过警告
    "parse": true, // 是否使用解析器
    "thumbType": "large" // large 大图模式 - normal 普通模式
}, {
	"name": "Config", // Config
	"save": true, // 是否保存日志
	"level": 5 // 日志显示等级
}]
```

在导入 `pywazi` 的时候会默认尝试 `deConfig` 当前目录下的 `config.json`。

## waziDanbooru 教程

Danbooru 是一个开源的图集展示系统，而且它开放 Api，目前比较广为人知的有：https://yande.re/ https://konachan.com/ 等，但是各种 Danbooru 类型的网站有不同的 Api 返回格式，我只是基于 Yande 和 Konachan 完成，仍未清楚其他使用 Danbooru 网站的适配性。

说实话，我对于 Danbooru 提供的部分接口有点搞不清楚，XD。

### 配置

譬如 https://yande.re/ 这种 Danbooru 网站在国内可能无法访问，所以你需要进行配置，让 PyWazi 使用代理访问，包括其他类型的网站也是一样，在国内访问可能或多或少都受到阻拦。

并且你需要配置 Danbooru 图库网站，这个世界上存在着很多使用 Danbooru 或 Moebooru 的网站，比如 konachan 之类的。你需要提供一个网站告知 PyWazi 到底去访问哪个网站。

```python
from pywazi import waziDanbooru

waziDanbooru.giveParams({
    "useProxies": True,  # 是否使用代理
    "proxyAddress": "127.0.0.1",  # HTTPS / HTTP 代理地址
    "proxyPort": "7890",  # HTTPS / HTTP 代理端口
    "useHeaders": False,  # 是否用自定义头部 （不建议填写，程序自动补充）
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.164 Safari/537.36"
    }  # 自定义头部内容 （不建议填写，程序自动补充，自己填写可能导致部分程序错误）
})

waziDanbooru.setApi("https://konachan.com")  # 设置图库网址
```

> 如果你提供了 `useProxies` 为 `True` 但是没有给予 `proxyAddress` 和 `proxyPort` 的话，程序会默认设置为 `127.0.0.1:7890`。但事实上，在小部分情况下这是无效的，所有的模块同理。

### Post 时间线

访问接口是：`URL/post.json`（当然也可以是 `URL/post.xml`）不同的网站有不同的返回格式，但是大体上基本一致。

#### 获取

```python
waziDanbooru.getPosts(0, "", 40)

# 第一位参数表示页码，从 0 数起
# 第二位参数表示标签，仅允许英文字符和下划线，如果没有标签则使用空字符串代替，多标签请在引号里面使用“+”号连接（可以使用空格或%20）
# 第三位参数表示显示数量限制，正常是 40 个，如果没有特别需求则输入 40 即可
```

返回列表（仅取一例）：

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

因为篇幅受限和各个 Danbooru 类网站返回的 JSON 格式都不一致，故无法详细解读。

#### 下载

```python
waziDanbooru.downloadPosts(0, "", 40, "./")

# 第一位参数表示页码，从 0 数起
# 第二位参数表示标签，仅允许英文字符和下划线，如果没有标签则使用空字符串代替，多标签请在引号里面使用“+”号连接（可以使用空格或%20）
# 第三位参数表示显示数量限制，正常是 40 个，如果没有特别需求则输入 40 即可
# 第四位参数表示下载路径，可以是相对的，也可以是绝对的
```

下载未作优化，如果有多线程需求可以查看：[cloudwindy/yander: Yande.re 爬虫 (github.com)](https://github.com/cloudwindy/yander)

完成后返回元组，包含下载文件和无法下载的图片：

```python
(['./334447.png', './334446.jpg', './334445.png', './334444.jpg', './334443.png', './334442.png', './334441.png', './334440.png', './334439.jpg', './334438.jpg', './334437.jpg', './334436.jpg', './334435.png', './334434.png', './334433.png', './334432.png', './334431.png', './334430.png', './334429.jpg', './334428.png', './334427.png', './334426.png', './334425.png', './334424.png', './334423.png', './334422.png', './334421.png', './334420.png', './334419.png', './334418.png', './334417.png', './334415.png', './334414.png', './334413.jpg', './334412.jpg', './334411.png', './334410.jpg', './334409.jpg', './334408.jpg', './334407.jpg'], [])
```

> 无法下载的图片列表返回格式如下：
>
> ```python
> [
>     {
>         "fileURL": "",			# 文件下载 URL
>         "id": ""				# 图片ID
>     }
> ]
> ```

### Pools 获取

`Pools` 是将图片组合起来的一种图集，你可以通过 `url/pool.json` 获取图集。

#### 搜索

```python
waziDanbooru.getPools("Jack-O'_Challenge", 0)

# 第一位参数表示图集名称
# 第二位参数表示页码 从 0 数起
```

返回列表：

```python
[{'id': 509, 'name': "Jack-O'_Challenge", 'created_at': '2021-08-27T17:55:55.591Z', 'updated_at': '2021-12-02T20:39:34.488Z', 'user_id': 73632, 'is_public': True, 'post_count': 160, 'description': "A Twitter meme where characters are drawn in an extreme top-down bottom-up resembling Jack-O' Valentine's crouch pose."}]
```

#### 获取图像

```python
waziDanbooru.getPoolsFromId(489, 0)

# 第一位参数表示图集 ID
# 第二位参数表示页码 从 0 数起
```

返回字典：

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

### 获取艺术家

获取全部艺术家的接口是：`url/artist.json`，同样也可以是 `url/artist.xml`。

```python
waziDanbooru.getArtists(0, "date")

# 第一位参数表示页码，从 0 数起
# 第二位参数表示排序方式：
# 	date - 日期
# 	name - 名称
```

返回列表：

```python
[{
	'id': 4958,
	'name': 'shashaki',
	'alias_id': None,
	'group_id': None,
	'urls': ['https://www.pixiv.net/en/users/9089874']
}]
```

### 获取标签

获取全部标签的接口是：`url/tag.json`，同样也可以是 `url/tag.xml`。

```python
waziDanbooru.getTags(0, 50, "count")

# 第一位参数表示页码，从 0 数起
# 第二位参数表示显示数量限制，正常是 50 个，如果没有特别需求则输入 50 即可
# 第三位参数表示排序模式，存在三种排序模式：
#     按创建日期排序的 - date
#     按图片数量排序的 - count
#     按标签名称排序的 - name
```

返回列表（取其中一例）：

```python
[{'id': 45, 'name': 'long_hair', 'count': 105004, 'type': 0, 'ambiguous': False}]
```

### 自定义接口

我允许用户自己访问自定义接口获取数据，并会返回符合的字典和列表。

```python
waziDanbooru.customApi("/post.json", {"page": "1"})

# 参数1：接口地址
# 参数2：GET 请求参数，如果无则使用 {} 代替
```

### 自定义搜索字符串

我提供了三种自定义搜索字符串生成函数，分别为：`getSizeLimit`, `getOrder`, `getRating` 这三个。

分别生成：尺寸限定搜索字符串、排序限定搜索字符串、评级限定搜索字符串。

其返回后总会存在一个空格，以方便用户拼接其他标签或字符串等。

#### 尺寸限定

```python
waziDanbooru.getSizeLimit({
    "limit": "b",
    "width": 1920,
    "height": 1080
})

# 第一位参数表示尺寸限定字典
#    limit 表示限定模式： e 表示正好符合该尺寸 / b 表示大于该尺寸 / s 表示小于该尺寸
#    width 表示宽 单位像素
#    height 表示高 单位像素
```

返回字符串：

```python
'width:1920.. height:1080.. '
```

#### 排序限定

```python
waziDanbooru.getOrder(["score", "fav"])

# 第一位参数表示排序限定列表
#    存在以下几种排序方式：
#        score - 评分 | fav - 收藏数 | wide - 大图 | nonwide - 小图
```

返回字符串：

```python
'order:score order:fav '
```

#### 评级限定

```python
waziDanbooru.getRating(["safe"])

# 第一位参数表示评级限定列表
#    存在以下几种评级模式：
#        safe | 表示完全可以给家长看的那种
#        questionable | 表示家长看了可能会恼火的那种
#        explicit | 表示完全不可以给家长看的那种
#        questionableplus | questionable + explicit
#        questionableless | questionable + safe
```

返回字符串：

 ```python
 'rating:safe '
 ```

### 关于你阅读代码时的疑惑

我知道你肯定会认为 `customApi` 和 `toAPIJson` 这两个接口就是脱裤子放屁，感到非常的疑惑，但是我不是解答你的这个问题的。

我是想说，为什么 `getComments` 这个接口没说，其实，很简单，因为这个接口我无论如何都无法取出数据，都是 `404`。

## waziJavBus 教程

> 因为 JavBus 存在 Cloudflare 反 BOT 机制，所以我使用了 `urllib` 模块，但是部分信息依旧无法获取。
>
> https://stackoverflow.com/questions/62684468/pythons-requests-triggers-cloudflares-security-while-urllib-does-not
>
> 事实发现，还存在一种对代理的检查，如果你无法获取到信息，试着更换代理。

### 配置

JavBus 在大陆大抵是真的无法直接访问了，除去几个镜像网站。

```python
from pywazi import waziJavBus

waziJavBus.giveParams({
    "useProxies": True,  # 是否使用代理
    "proxyAddress": "127.0.0.1",  # HTTPS / HTTP 代理地址
    "proxyPort": "7890",  # HTTPS / HTTP 代理端口
    "useHeaders": False,  # 是否用自定义头部 （不建议填写，程序自动补充）
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.164 Safari/537.36"
    }  # 自定义头部内容 （不建议填写，程序自动补充，自己填写可能导致部分程序错误）
})

waziJavBus.changeType(0) # 修改你的磁力链接显示模式 0 表示只显示有磁力链接的 1 表示显示全部
waziJavBus.setApiUrl("xxxxxxx") # 设置镜像站 没有可以不写
waziJavBus.setEAApiUrl("xxxxxxxxxx") # 设置欧美镜像站 没有可以不写
```

### 浏览

如果你是想像平常一样，一页一页翻，那么可以使用自带的默认浏览。除此之外，PyWazi 还存在 AV 工作者、导演、工作室、发行公司和系列浏览模式。

#### 默认

```python
waziJavBus.browse(1, "", 0)

# 第一位参数表示页码，从 1 数起
# 第二位参数表示标签 ID，可以从标签获取中找到 ID 填入
# 第三位参数表示 AV 类型，0 表示有码，1 表示无码
```

返回列表（取其中一例）：

```python
[{
	'link': 'https://www.javbus.com/ZOCM-011',
	'frame': 'https://www.javbus.com/pics/thumb/8j67.jpg',
	'title': '地味子な教え子と相部屋ラブホで生中出し子作り不倫セックスに明け暮れた私。色白美肌美少女 まいちゃん 花狩まい',
	'avId': 'ZOCM-011',
	'time': '2021-11-13',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': [{
			'type': '高清',
			'title': '包含高清HD的磁力連結'
		}, {
			'type': '今日新種',
			'title': '包含最新出種的磁力連結'
		}]
	}
}]
```

`link` 表示该 AV 的详细信息页面，`frame` 表示封面，`title` 表示 AV 标题，`avId` 表示 AV 番号，`time` 表示上传时间，`others` 表示附加内容，`tags` 里面存在 `type` 和 `title`。

##### 欧美

```python
waziJavBus.eaBrowse(1, "")

# 第一位参数表示页码，从 1 数起
# 第二位参数表示标签 ID，可以从标签获取中找到 ID 填入
```

返回列表（取其中一例）：

```python
[{
	'link': 'https://www.javbus.red/BrazzersExxtra-21-02-01',
	'frame': 'https://images.javbus.red/thumb/10si.jpg',
	'title': 'Lickity Stick, Blow Up Doll Trick',
	'avId': 'BrazzersExxtra.21.02.01',
	'time': '2021-02-01',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': []
	}
}]
```

#### 工作者

```python
waziJavBus.withWorkerBrowse(1, "p6v", 0)

# 第一位参数表示页码，从 1 数起
# 第二位参数表示工作者 ID，可以从工作者获取中找到 ID 填入
# 第三位参数表示 AV 类型，0 表示有码，1 表示无码
```

返回列表（取其中一例）：

```python
[{
	'name': '桃乃木かな',
	'img': 'https://www.javbus.com/pics/actress/p6v_a.jpg',
	'basic': [{
		'type': '生日',
		'content': '1996-12-24'
	}, {
		'type': '年齡',
		'content': '24'
	}, {
		'type': '身高',
		'content': '153cm'
	}, {
		'type': '罩杯',
		'content': 'F'
	}, {
		'type': '胸圍',
		'content': '80cm'
	}, {
		'type': '腰圍',
		'content': '54cm'
	}, {
		'type': '臀圍',
		'content': '80cm'
	}, {
		'type': '出生地',
		'content': '東京都'
	}, {
		'type': '愛好',
		'content': 'カラオケ、大食い'
	}]
}, {
	'link': 'https://www.javbus.com/IPX-778',
	'frame': 'https://www.javbus.com/pics/thumb/8nh3.jpg',
	'title': '洗脳 服従セラピーで肉体を完全征服された人気女子アナ。 催●療法 強●失禁・潮噴射・イキ我慢で耐える堕ちない屈強女子アナ凌●。 桃乃木かな',
	'avId': 'IPX-778',
	'time': '2021-12-10',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': [{
			'type': '高清',
			'title': '包含高清HD的磁力連結'
		}, {
			'type': '3天前新種',
			'title': '包含最新出種的磁力連結'
		}]
	}
}]
```

##### 欧美

```python
waziJavBus.withEAWorkerBrowse(1, "57x")

# 第一位参数表示页码，从 1 数起
# 第二位参数表示工作者 ID，可以从工作者获取中找到 ID 填入
```

返回列表（取其中一例）：

```python
[{
	'name': 'Jessy Jones',
	'img': 'https://images.javbus.red/actress/57x_a.jpg',
	'basic': []
}, {
	'link': 'https://www.javbus.red/BrazzersExxtra-20-06-09',
	'frame': 'https://images.javbus.red/thumb/10j5.jpg',
	'title': 'Best Of Brazzers: Sharing Stepsiblings',
	'avId': 'BrazzersExxtra.20.06.09',
	'time': '2020-06-09',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': [{
			'type': '高清',
			'title': '包含高清HD的磁力連結'
		}]
	}
}]
```

#### 导演

```python
waziJavBus.withDirectorBrowse(1, "j1", 0)

# 第一位参数表示页码，从 1 数起
# 第二位参数表示导演 ID，可以从网站中找到 ID 填入
# 第三位参数表示 AV 类型，0 表示有码，1 表示无码
```

返回列表（取其中一例）：

```python
{
	'link': 'https://www.javbus.com/ZOCM-011',
	'frame': 'https://www.javbus.com/pics/thumb/8j67.jpg',
	'title': '地味子な教え子と相部屋ラブホで生中出し子作り不倫セックスに明け暮れた私。色白美肌美少女 まいちゃん 花狩まい',
	'avId': 'ZOCM-011',
	'time': '2021-11-13',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': [{
			'type': '高清',
			'title': '包含高清HD的磁力連結'
		}, {
			'type': '今日新種',
			'title': '包含最新出種的磁力連結'
		}]
	}
}]
```

##### 欧美

```python
waziJavBus.withEADirectorBrowse(1, "")
```



#### 工作室

```python
waziJavBus.withStudioBrowse(1, "3or", 0)

# 第一位参数表示页码，从 1 数起
# 第二位参数表示制造商 ID，可以从网站中找到 ID 填入
# 第三位参数表示 AV 类型，0 表示有码，1 表示无码
```

返回列表（取其中一例）：

```python
[{
	'link': 'https://www.javbus.com/ZOCM-011',
	'frame': 'https://www.javbus.com/pics/thumb/8j67.jpg',
	'title': '地味子な教え子と相部屋ラブホで生中出し子作り不倫セックスに明け暮れた私。色白美肌美少女 まいちゃん 花狩まい',
	'avId': 'ZOCM-011',
	'time': '2021-11-13',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': [{
			'type': '高清',
			'title': '包含高清HD的磁力連結'
		}, {
			'type': '今日新種',
			'title': '包含最新出種的磁力連結'
		}]
	}
}]
```

##### 欧美

```python
waziJavBus.withEAStudioBrowse(1, "4")

# 第一位参数表示页码，从 1 数起
# 第二位参数表示制造商 ID，可以从网站中找到 ID 填入
```

返回列表（取其中一例）：

```python
[{
	'link': 'https://www.javbus.red/BrazzersExxtra-21-02-01_10sj',
	'frame': 'https://images.javbus.red/thumb/10sj.jpg',
	'title': 'Post Party Cumdown',
	'avId': 'BrazzersExxtra.21.02.01',
	'time': '2021-02-01',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': []
	}
}]
```

#### 发行公司

```python
waziJavBus.withLabelBrowse(1, "1so", 0)

# 第一位参数表示页码，从 1 数起
# 第二位参数表示发行公司 ID，可以从网站中找到 ID 填入
# 第三位参数表示 AV 类型，0 表示有码，1 表示无码
```

返回列表（取其中一例）：

```python
[{
	'link': 'https://www.javbus.com/STARS-475',
	'frame': 'https://www.javbus.com/pics/thumb/8kco.jpg',
	'title': '青空ひかりデビュー2周年記念 輪姦アリ!早抜きアリ!逆レイプアリ!22本ニ…',
	'avId': 'STARS-475',
	'time': '2021-11-11',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': [{
			'type': '高清',
			'title': '包含高清HD的磁力連結'
		}, {
			'type': '5天前新種',
			'title': '包含最新出種的磁力連結'
		}]
	}
}]
```

##### 欧美

恕我直言，我暂时没有找到欧美发行公司的接口。

#### 系列

```python
waziJavBus.withSeriesBrowse(1, "ckx", 0)

# 第一位参数表示页码，从 1 数起
# 第二位参数表示系列 ID，可以从网站中找到 ID 填入
# 第三位参数表示 AV 类型，0 表示有码，1 表示无码
```

返回列表（取其中一例）：

```python
[{
	'link': 'https://www.javbus.com/NTRD-095',
	'frame': 'https://www.javbus.com/pics/thumb/8iah.jpg',
	'title': 'ネトラレーゼ 部下とまさか… 池谷佳純',
	'avId': 'NTRD-095',
	'time': '2021-10-28',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': [{
			'type': '高清',
			'title': '包含高清HD的磁力連結'
		}, {
			'type': '字幕',
			'title': '包含字幕的磁力連結'
		}]
	}
}]
```

##### 欧美

```python
waziJavBus.withEASeriesBrowse(1, "1y")

# 第一位参数表示页码，从 1 数起
# 第二位参数表示系列 ID，可以从网站中找到 ID 填入
```

返回列表（取其中一例）：

```python
[{
	'link': 'https://www.javbus.red/TeensLikeItBig-21-01-31',
	'frame': 'https://images.javbus.red/thumb/10sl.jpg',
	'title': 'Save My Pussy, Fuck My Ass',
	'avId': 'TeensLikeItBig.21.01.31',
	'time': '2021-01-31',
	'others': {
		'type': 'Item Tag',
		'has': ['tags'],
		'tags': []
	}
}]
```

### 搜索

```python
waziJavBus.search(0, "a", 1)

# 第一位参数表示搜索类型
#	0 - 有码
#	1 - 无码
#	2 - 工作者
#	3 - 导演
#	4 - 制作商
#	5 - 发行商
#	6 - 系列
# 第二位参数表示搜索关键词
# 第三位参数表示页码
```

#### 欧美

```python
waziJavBus.eaSearch(0, "a", 1)

# 第一位参数表示搜索类型
#	0 - AV 搜索
# 	1 - 工作者搜索
# 第二位参数表示搜索关键词
# 第三位参数表示页码
```

### 获取列表

存在两种列表获取函数：`getTagsList` 和 `getAVWorkersList`，分别获取标签和工作者的列表。

#### 标签

```python
waziJavBus.getTagsList(0)

# 第一位参数表示 AV 类型，0 表示有码，1 表示无码
```

返回列表（取其中一例）：

```python
{
	'tagType': '主題',
	'tags': [{
		'name': '折磨',
		'tagId': '62'
	}, {
		'name': '嘔吐',
		'tagId': '5g'
	}, {
		'name': '觸手',
		'tagId': '59'
	}, {
		'name': '蠻橫嬌羞',
		'tagId': '57'
	}, {
		'name': '處男',
		'tagId': '52'
	}, {
		'name': '正太控',
		'tagId': '4y'
	}, {
		'name': '出軌',
		'tagId': '4r'
	}, {
		'name': '瘙癢',
		'tagId': '4e'
	}, {
		'name': '運動',
		'tagId': '4d'
	}, {
		'name': '女同接吻',
		'tagId': '4a'
	}, {
		'name': '性感的',
		'tagId': '49'
	}, {
		'name': '美容院',
		'tagId': '44'
	}, {
		'name': '處女',
		'tagId': '41'
	}, {
		'name': '爛醉如泥的',
		'tagId': '40'
	}, {
		'name': '殘忍畫面',
		'tagId': '3x'
	}, {
		'name': '妄想',
		'tagId': '3w'
	}, {
		'name': '惡作劇',
		'tagId': '3v'
	}, {
		'name': '學校作品',
		'tagId': '3t'
	}, {
		'name': '粗暴',
		'tagId': '3r'
	}, {
		'name': '通姦',
		'tagId': '3g'
	}, {
		'name': '姐妹',
		'tagId': '3e'
	}, {
		'name': '雙性人',
		'tagId': '3d'
	}, {
		'name': '跳 舞',
		'tagId': '3c'
	}, {
		'name': '性奴',
		'tagId': '3b'
	}, {
		'name': '倒追',
		'tagId': '37'
	}, {
		'name': '性騷擾',
		'tagId': '35'
	}, {
		'name': '其他',
		'tagId': '2y'
	}, {
		'name': '戀腿癖',
		'tagId': '2x'
	}, {
		'name': '偷窥',
		'tagId': '2v'
	}, {
		'name': '花癡',
		'tagId': '2t'
	}, {
		'name': '男同性恋',
		'tagId': '2r'
	}, {
		'name': '情侶',
		'tagId': '2e'
	}, {
		'name': '戀乳癖',
		'tagId': '2d'
	}, {
		'name': '亂倫',
		'tagId': '20'
	}, {
		'name': '其他戀物癖',
		'tagId': '1y'
	}, {
		'name': '偶像藝人',
		'tagId': '1u'
	}, {
		'name': '野外・露出',
		'tagId': '1i'
	}, {
		'name': '獵豔',
		'tagId': '1e'
	}, {
		'name': '女同性戀',
		'tagId': '1d'
	}, {
		'name': '企畫',
		'tagId': '11'
	}, {
		'name': '10枚組',
		'tagId': '6h'
	}, {
		'name': '科幻',
		'tagId': '61'
	}, {
		'name': '女優ベスト・総集編',
		'tagId': '6i'
	}, {
		'name': '温泉',
		'tagId': '6j'
	}, {
		'name': 'M男',
		'tagId': '6k'
	}, {
		'name': '原作コラボ',
		'tagId': '6l'
	}, {
		'name': '16時間以上作品',
		'tagId': '6n'
	}, {
		'name': 'デカチン・巨根',
		'tagId': '6o'
	}, {
		'name': 'ファン感謝・訪問',
		'tagId': '6p'
	}, {
		'name': '動画',
		'tagId': '6q'
	}, {
		'name': '巨尻',
		'tagId': '6r'
	}, {
		'name': 'ハーレム',
		'tagId': '6s'
	}, {
		'name': '日焼け',
		'tagId': '6t'
	}, {
		'name': '早漏',
		'tagId': '6u'
	}, {
		'name': 'キス・接吻',
		'tagId': '6v'
	}, {
		'name': '汗だく',
		'tagId': '6w'
	}, {
		'name': 'スマホ専用縦動画',
		'tagId': '77'
	}, {
		'name': 'Vシネマ',
		'tagId': '7d'
	}, {
		'name': "Don Cipote's choice",
		'tagId': '7c'
	}, {
		'name': 'アニメ',
		'tagId': '7f'
	}, {
		'name': 'アクション',
		'tagId': '7g'
	}, {
		'name': 'イメージビデオ（男性）',
		'tagId': '7h'
	}, {
		'name': '孕ませ',
		'tagId': '7i'
	}, {
		'name': 'ボーイズラブ',
		'tagId': '7j'
	}, {
		'name': 'ビッチ',
		'tagId': '7t'
	}, {
		'name': '特典あり（AVベースボール）',
		'tagId': '7u'
	}, {
		'name': 'コミック雑誌',
		'tagId': '7v'
	}, {
		'name': '時間停止',
		'tagId': '7w'
	}]
}
```

##### 欧美

```python
waziJavBus.getEATagsList()
```

#### 工作者

```python
waziJavBus.getAVWorkersList(1, 0)

# 第一位参数表示页码，从 1 数起
# 第二位参数表示 AV 类型，0 表示有码，1 表示无码
```

取其中一例：

```python
[{'link': 'https://www.javbus.com/star/okq', 'frame': 'https://www.javbus.com/pics/actress/okq_a.jpg', 'name': '三上悠亜', 'workerId': 'okq', 'avType': 0}]
```

##### 欧美

```python
waziJavBus.getEAAVWorkersList(1)

# 第一位参数表示页码，从 1 数起
```

取其中一例：

```python
[{'link': 'https://www.javbus.red/star/4hv', 'frame': 'https://images.javbus.red/actress/4hv_a.jpg', 'name': 'Danny D', 'workerId': '4hv', 'avType': 1}]
```

### AV

PyWazi 存在两种获取 AV 详细信息的方式，但实际上后一种完全依照前一种本体，请看文档：

#### 信息

```python
waziJavBus.getAVDetails("STARS-471")

# 第一位参数表示 AV ID
```

返回字典：

```python
{
	'title': 'STARS-471 147cmミニマム巨乳Gカップ美少女がナマ本番解禁!感度倍増イキまくり初め…',
	'cover': 'https://www.javbus.com/pics/cover/8nr9_b.jpg',
	'coverTitle': '147cmミニマム巨乳Gカップ美少女がナマ本番解禁!感度倍増イキまくり初め…',
	'avId': 'STARS-471',
	'time': '2021-11-11',
	'long': '130',
	'director': {
		'name': 'ザック荒井',
		'id': 'lw',
		'type': 0
	},
	'studio': {
		'name': 'SODクリエイト',
		'id': 'ca',
		'type': 0
	},
	'label': {
		'name': 'SODstar',
		'id': '1so',
		'type': 0
	},
	'series': {
		'name': '中出し解禁',
		'id': 'pv6',
		'type': 0
	},
	'tags': [{
		'name': '中出',
		'id': '4',
		'type': 0
	}, {
		'name': '巨乳',
		'id': 'e',
		'type': 0
	}, {
		'name': '無毛',
		'id': '22',
		'type': 0
	}],
	'workers': [{
		'name': '朝田ひまり',
		'id': 'x5e',
		'type': 0
	}],
	'samples': 'None. / 无。',
	'sameVideos': [{
		'frame': 'https://www.javbus.com/NITR-172',
		'title': 'マゾの宅配便 4',
		'img': 'https://www.javbus.com/pics/thumb/56un.jpg'
	}, {
		'frame': 'https://www.javbus.com/EKDV-670',
		'title': '百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。',
		'img': 'https://www.javbus.com/pics/thumb/8is1.jpg'
	}, {
		'frame': 'https://www.javbus.com/HDKA-245',
		'title': 'はだかの家政婦 全裸家政婦紹介所 夏音いおり',
		'img': 'https://www.javbus.com/pics/thumb/8jga.jpg'
	}, {
		'frame': 'https://www.javbus.com/AMBI-143',
		'title': '血の繋がりのない妹と二人っきりの3日間！ここぞとばかりにセックスしまくった！！ 紺野みいな',
		'img': 'https://www.javbus.com/pics/thumb/8jge.jpg'
	}, {
		'frame': 'https://www.javbus.com/DANDAN-010',
		'title': '出会って速攻！チェンジする暇を与えない下品テクで若い精子を何度も搾り取るグイグイおばさんデリヘル嬢',
		'img': 'https://www.javbus.com/pics/thumb/8jgi.jpg'
	}, {
		'frame': 'https://www.javbus.com/NASH-595',
		'title': '五十路の性癖 おばさんのいやらしい日常 熟年女性が隠し持っている性癖とは・・熟年女性の下品な性癖 五十路女4人の性癖中出し性行為ドキュメント',
		'img': 'https://www.javbus.com/pics/thumb/8hzu.jpg'
	}],
	'hots': 'None. / 无。'
}
```

无法获取 `hots` 的内容，我表示毫无头绪。

##### 欧美

```python
waziJavBus.getEAAVDetails("TeensLikeItBig-21-01-31")
```

返回字典：

```python
{
	'title': 'TeensLikeItBig.21.01.31 Save My Pussy, Fuck My Ass',
	'cover': 'https://images.javbus.red/cover/10sl_b.jpg',
	'coverTitle': 'Save My Pussy, Fuck My Ass',
	'avId': 'TeensLikeItBig.21.01.31',
	'time': '2021-01-31',
	'long': '0',
	'director': 'None. / 无。',
	'studio': {
		'name': 'Brazzers',
		'id': '4',
		'type': 0
	},
	'label': 'None. / 无。',
	'series': {
		'name': 'TeensLikeItBig',
		'id': '1y',
		'type': 0
	},
	'tags': 'None. / 无。',
	'workers': [{
		'name': 'Lil D',
		'id': 'd0c',
		'type': 0
	}, {
		'name': 'Adriana Maya',
		'id': 'd6p',
		'type': 0
	}],
	'samples': 'None. / 无。',
	'sameVideos': [{
		'frame': 'https://www.javbus.red/BrazzersExxtra-20-09-21',
		'title': 'Best Of Brazzers: Luna Star',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10l2.jpg'
	}, {
		'frame': 'https://www.javbus.red/BrazzersExxtra-20-09-07',
		'title': 'Best of Brazzers Pantyhose',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10lg.jpg'
	}, {
		'frame': 'https://www.javbus.red/BrazzersExxtra-20-10-31',
		'title': 'Best of Brazzers Happy Halloween',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10nn.jpg'
	}, {
		'frame': 'https://www.javbus.red/BrazzersExxtra-20-09-14',
		'title': 'Best Of Brazzers: Soaking Wet',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10l9.jpg'
	}, {
		'frame': 'https://www.javbus.red/TeensLikeItBig-20-08-14',
		'title': 'The Cocksuckers Club: Remastered',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10m5.jpg'
	}, {
		'frame': 'https://www.javbus.red/BrazzersExxtra-21-01-03',
		'title': 'Spitting Image In Her Ass',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10qy.jpg'
	}],
	'hots': 'None. / 无。'
}
```

#### 信息与磁力链接

相比于普通信息获取，它多出了磁力链接的获取。

```python
waziJavBus.getAVDetailsWithMagnet("EKDV-670")

# 第一位参数表示 AV ID
```

返回字典：

```python
{
	'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。',
	'cover': 'https://www.javbus.com/pics/cover/8is1_b.jpg',
	'coverTitle': '百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕 メイドとのなんともうらやましい日常。',
	'avId': 'EKDV-670',
	'time': '2021-11-06',
	'long': '108',
	'director': 'None. / 无。',
	'studio': {
		'name': 'クリスタル映像',
		'id': '72',
		'type': 0
	},
	'label': {
		'name': 'e-kiss',
		'id': 's5',
		'type': 0
	},
	'series': 'None. / 无。',
	'tags': [{
		'name': '高畫質',
		'id': '4o',
		'type': 0
	}, {
		'name': '女上位',
		'id': '42',
		'type': 0
	}, {
		'name': '舔陰',
		'id': '3q',
		'type': 0
	}, {
		'name': '乳交',
		'id': '1s',
		'type': 0
	}, {
		'name': '口交',
		'id': '1o',
		'type': 0
	}, {
		'name': '無毛',
		'id': '22',
		'type': 0
	}, {
		'name': '女傭',
		'id': 'j',
		'type': 0
	}, {
		'name': '巨乳',
		'id': 'e',
		'type': 0
	}, {
		'name': '中出',
		'id': '4',
		'type': 0
	}, {
		'name': '苗條',
		'id': '1f',
		'type': 0
	}, {
		'name': 'DMM獨家',
		'id': 'g',
		'type': 0
	}, {
		'name': '單體作品',
		'id': 'f',
		'type': 0
	}],
	'workers': [{
		'name': '百永さ りな',
		'id': 'xl9',
		'type': 0
	}],
	'samples': [{
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕 メイドとのなんともうらやましい日常。 - 樣品圖像 - 1',
		'url': 'https://www.javbus.com/pics/sample/8is1_1.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 2',
		'url': 'https://www.javbus.com/pics/sample/8is1_2.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 3',
		'url': 'https://www.javbus.com/pics/sample/8is1_3.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピ ストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 4',
		'url': 'https://www.javbus.com/pics/sample/8is1_4.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 5',
		'url': 'https://www.javbus.com/pics/sample/8is1_5.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 6',
		'url': 'https://www.javbus.com/pics/sample/8is1_6.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 7',
		'url': 'https://www.javbus.com/pics/sample/8is1_7.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 8',
		'url': 'https://www.javbus.com/pics/sample/8is1_8.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち 追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 9',
		'url': 'https://www.javbus.com/pics/sample/8is1_9.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 10',
		'url': 'https://www.javbus.com/pics/sample/8is1_10.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 11',
		'url': 'https://www.javbus.com/pics/sample/8is1_11.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 12',
		'url': 'https://www.javbus.com/pics/sample/8is1_12.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 13',
		'url': 'https://www.javbus.com/pics/sample/8is1_13.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメ イドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 14',
		'url': 'https://www.javbus.com/pics/sample/8is1_14.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 15',
		'url': 'https://www.javbus.com/pics/sample/8is1_15.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 16',
		'url': 'https://www.javbus.com/pics/sample/8is1_16.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 17',
		'url': 'https://www.javbus.com/pics/sample/8is1_17.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 18',
		'url': 'https://www.javbus.com/pics/sample/8is1_18.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 19',
		'url': 'https://www.javbus.com/pics/sample/8is1_19.jpg'
	}, {
		'title': 'EKDV-670 百永さりな 乳首責めが大好きなTバックメイドに返り討ち追撃ピストン！！ボクの事を好き過ぎるご奉仕メイドとのなんともうらやましい日常。 - 樣品圖像 - 20',
		'url': 'https://www.javbus.com/pics/sample/8is1_20.jpg'
	}],
	'sameVideos': [{
		'frame': 'https://www.javbus.com/EKDV-667',
		'title': '北野未奈 出張先のホテルで苦手な上司とまさかの相部屋…巨大な上司のアレに寝る間も惜しんで犯●れた屈辱的な夜',
		'img': 'https://www.javbus.com/pics/thumb/8haw.jpg'
	}, {
		'frame': 'https://www.javbus.com/EKDV-661',
		'title': 'オイルボイン吉根ゆりあ神乳Mカップパイズリ密着中出しセックス！！',
		'img': 'https://www.javbus.com/pics/thumb/89mt.jpg'
	}, {
		'frame': 'https://www.javbus.com/CRNX-018',
		'title': 'ショートカットで剛毛…お尻が素敵な新人メイドと調教FUCK！ 月城らん',
		'img': 'https://www.javbus.com/pics/thumb/86cp.jpg'
	}, {
		'frame': 'https://www.javbus.com/GNAX-038',
		'title': '夫には絶対見せられない白昼の絶叫 逢見リカ',
		'img': 'https://www.javbus.com/pics/thumb/7xmq.jpg'
	}, {
		'frame': 'https://www.javbus.com/WANZ-726',
		'title': 'うっかり滑って生挿入！パイパン素股メイド 真白ここ',
		'img': 'https://www.javbus.com/pics/thumb/6fqa.jpg'
	}, {
		'frame': 'https://www.javbus.com/EKDV-668',
		'title': '永野いち夏 甘えん坊メイドの密着耳元ささやき！ボクのことを好き過ぎるご奉仕メイ ドとのなんともうらやましい日常。',
		'img': 'https://www.javbus.com/pics/thumb/8hav.jpg'
	}],
	'hots': 'None. / 无。',
	'magnets': [{
		'title': 'EKDV-670_2K',
		'tags': [],
		'size': '1.77GB',
		'date': '2021-11-08',
		'magnet': 'magnet:?xt=urn:btih:31AEBB7BB355A28F7E79DC2F2857D13FB224E2E9&dn=EKDV-670_2K'
	}, {
		'title': '-EKDV670',
		'tags': [],
		'size': '1.54GB',
		'date': '2021-11-07',
		'magnet': 'magnet:?xt=urn:btih:ABDA69D89E7FB19E5EAAEBC8F973AE18CB55C803&dn=-EKDV670'
	}, {
		'title': 'ekdv-670',
		'tags': [{
			'title': '包含高清HD的磁力連結',
			'type': None
		}],
		'size': '4.64GB',
		'date': '2021-11-07',
		'magnet': 'magnet:?xt=urn:btih:2C9C45536A52347005E7AB366B62AE1CE119FD67&dn=ekdv-670'
	}, {
		'title': 'EKDV-670',
		'tags': [{
			'title': '包含高清HD的磁力連結',
			'type': None
		}],
		'size': '4.48GB',
		'date': '2021-11-06',
		'magnet': 'magnet:?xt=urn:btih:D1C5EA3E07B4976DF6CF9759FFB34CEF10C201C9&dn=EKDV-670'
	}]
}
```

##### 欧美

```python
waziJavBus.getEAAVDetailsWithMagnet("")
```

返回字典：

```python
{
	'title': 'TeensLikeItBig.21.01.31 Save My Pussy, Fuck My Ass',
	'cover': 'https://images.javbus.red/cover/10sl_b.jpg',
	'coverTitle': 'Save My Pussy, Fuck My Ass',
	'avId': 'TeensLikeItBig.21.01.31',
	'time': '2021-01-31',
	'long': '0',
	'director': 'None. / 无。',
	'studio': {
		'name': 'Brazzers',
		'id': '4',
		'type': 0
	},
	'label': 'None. / 无。',
	'series': {
		'name': 'TeensLikeItBig',
		'id': '1y',
		'type': 0
	},
	'tags': 'None. / 无。',
	'workers': [{
		'name': 'Lil D',
		'id': 'd0c',
		'type': 0
	}, {
		'name': 'Adriana Maya',
		'id': 'd6p',
		'type': 0
	}],
	'samples': 'None. / 无。',
	'sameVideos': [{
		'frame': 'https://www.javbus.red/BrazzersExxtra-20-09-21',
		'title': 'Best Of Brazzers: Luna Star',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10l2.jpg'
	}, {
		'frame': 'https://www.javbus.red/BrazzersExxtra-20-09-07',
		'title': 'Best of Brazzers Pantyhose',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10lg.jpg'
	}, {
		'frame': 'https://www.javbus.red/BrazzersExxtra-20-10-31',
		'title': 'Best of Brazzers Happy Halloween',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10nn.jpg'
	}, {
		'frame': 'https://www.javbus.red/BrazzersExxtra-20-09-14',
		'title': 'Best Of Brazzers: Soaking Wet',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10l9.jpg'
	}, {
		'frame': 'https://www.javbus.red/TeensLikeItBig-20-08-14',
		'title': 'The Cocksuckers Club: Remastered',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10m5.jpg'
	}, {
		'frame': 'https://www.javbus.red/BrazzersExxtra-21-01-03',
		'title': 'Spitting Image In Her Ass',
		'img': 'https://www.javbus.comhttps://images.javbus.red/thumb/10qy.jpg'
	}],
	'hots': 'None. / 无。',
	'magnets': [{
		'title': 'TeensLikeItBig - Adriana Maya - Save My Pussy Fuck My Ass 31.01.2021 480p mp4',
		'tags': [],
		'size': '317.24MB',
		'date': '2021-01-31',
		'magnet': 'magnet:?xt=urn:btih:8ff79dc1218285a690853a9a971c5fa71e8332c2&dn=TeensLikeItBig+-+Adriana+Maya+-+Save+My+Pussy+Fuck+My+Ass+31.01.2021+480p+mp4'
	}, {
		'title': 'TeensLikeItBig.21.01.31.Adriana.Maya.Save.My.Pussy.Fuck.My.Ass.XXX.SD.MP4-KLEENEX',
		'tags': [],
		'size': '310.86MB',
		'date': '2021-01-31',
		'magnet': 'magnet:?xt=urn:btih:707635c3f87d4de6b7a27d8114cff2dc3a4e911e&dn=TeensLikeItBig.21.01.31.Adriana.Maya.Save.My.Pussy.Fuck.My.Ass.XXX.SD.MP4-KLEENEX'
	}, {
		'title': 'TeensLikeItBig.21.01.31.Adriana.Maya.Save.My.Pussy.Fuck.My.Ass.XXX.1080p.MP4-WRB',
		'tags': [],
		'size': '1.00GB',
		'date': '2021-01-31',
		'magnet': 'magnet:?xt=urn:btih:af26e492d4a20b795cc3ee5761ae06c05697d278&dn=TeensLikeItBig.21.01.31.Adriana.Maya.Save.My.Pussy.Fuck.My.Ass.XXX.1080p.MP4-WRB'
	}]
}
```

### 磁力链接

如果你单单只需要磁力链接的话，可以使用 `getMagnet` 来获取。

```python
waziJavBus.getMagnet("STARS-471", False)

# 第一位参数表示 AV ID
# 第二位参数表示是否是欧美分区
```

返回列表：

```python
[{
	'title': 'stars-471',
	'tags': [],
	'size': '',
	'date': '2021-11-11',
	'magnet': 'magnet:?xt=urn:btih:58BF7B307EE14C806E4AC92407F5D22AFD7E8AD5&dn=stars-471'
}, {
	'title': 'STARS-471_2K',
	'tags': [],
	'size': '',
	'date': '2021-11-10',
	'magnet': 'magnet:?xt=urn:btih:0B995192153272D8DE0D5D0E831AD242DCB56399&dn=STARS-471_2K'
}, {
	'title': 'STARS-471',
	'tags': [],
	'size': '',
	'date': '2021-11-09',
	'magnet': 'magnet:?xt=urn:btih:5196095E8BC162CB8777CDCE05C979A46ED537CB&dn=STARS-471'
}]
```

## waziExHentai 教程

ExHentai 是 E-Hentai 的里站，需要有权限的账户才能进入（本人不提供）。最好在使用本程序前，您的显示方式设置为 `Extended`，虽然该程序有针对其他显示模式的适配，但还需额外的代码配置（虽然仅需一行）。

### 配置

```python
from pywazi import waziExHentai

waziExHentai.giveParams({
    "useProxies": True,  # 是否使用代理
    "proxyAddress": "127.0.0.1",  # HTTPS / HTTP 代理地址
    "proxyPort": "7890",  # HTTPS / HTTP 代理端口
    "useHeaders": False,  # 是否用自定义头部 （不建议填写，程序自动补充）
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.164 Safari/537.36"
    }  # 自定义头部内容 （不建议填写，程序自动补充，自己填写可能导致部分程序错误）
})

waziExHentai.setCookies("xxxxxx=xxxxxxxxxx;xxxxxxx=xxxxxxxxxxxxxxx;xxxxxx=xxxxxxx")  # 设置你的 Cookies
```

#### 如何获取你账号的 Cookies

1. 打开 https://exhentai.org/ 如果你没有登录的话，那就先登录一下
2. 右键 -> 检查 / 审查元素 -> 控制台 （或者 F12）
3. 输入 `document.cookie` 并回车
4. 复制返回内容，这就是你的 Cookies

#### 额外的解析器

启用后将自动检查当前的显示模式，并使用适配它的解析函数，如果不启用则默认以 `Extended` 显示模式。

默认启用。

```python
waziExHentai.setParse(True)

# 第一位参数表示是否打开额外的解析器
```

##### 如果不启用

则调用 `changeMethod("Extended")` 强制设置为 `Extended` 模式。

#### 画廊警告跳过

有些时候，画廊会显示警告，程序默认不跳过并且触发错误，如果你想跳过，那么可以按以下方法打开警告跳过：

```python
waziExHentai.setJump(True)

# 第一位参数表示是否打开画廊警告跳过
```

#### 全评论需要

如果你想要在解析时看到更多的评论，或者全部评论，你应该使用：

```python
waziExHentai.needFullComments(True)

# 第一位参数表示请求全评论
```

#### 显示模式

存在两种可供设置的显示模式。

##### 首页显示模式

```python
waziExHentai.changeMethod("Extended")

# 第一位参数表示首页显示模式 有：
# Minimal Minimal+ Compact Extended Thumbnail
```

##### 缩略图显示模式

```python
waziExHentai.changeThumbnailMode("normal")

# 第一位参数表示缩略图显示模式 有：
# normal large
```

### 浏览

首页浏览模式，内置两种浏览模式。

#### 普通浏览

使用默认设置下的首页显示内容，以 `Extended` 显示模式为例。

```python
waziExHentai.browse(0)

# 第一位参数表示页码，从 0 数起
```

返回列表（取其中一例）：

```python
[{
	'title': '[Beruzumi-M] Charlotte and Vampire Vincent [Castlevania]',
	'URL': 'https://exhentai.org/g/2085145/c920c6838c/',
	'cat': 'Artist CG',
	'cover': 'https://exhentai.org/t/ee/5c/ee5c2c44aa3d4b7fbf111d388faeb617415352f9-1565921-1900-1400-jpg_250.jpg',
	'uploader': 'Xotoj',
	'uploaderURL': 'https://exhentai.org/uploader/Xotoj',
	'time': '2021-12-14 16:43',
	'hasTorrents': False,
	'rating': 2,
	'pages': 24,
	'others': {
		'type': 'Extended Own Information',
		'has': ['tags'],
		'tags': [{
			'title': 'parody:castlevania',
			'className': ['gtl']
		}, {
			'title': 'character:astarte',
			'className': ['gtl']
		}, {
			'title': 'character:charlotte aulin',
			'className': ['gtl']
		}, {
			'title': 'female:netorare',
			'className': ['gt'],
			'style': 'color:#090909;border-color:#FFFF00;background:radial-gradient(#FFFF00,#dfdf00) !important'
		}, {
			'title': 'female:big breasts',
			'className': ['gtl']
		}, {
			'title': 'female:kissing',
			'className': ['gtl']
		}, {
			'title': 'female:mind control',
			'className': ['gtl']
		}, {
			'title': 'female:paizuri',
			'className': ['gtl']
		}, {
			'title': 'male:hairy',
			'className': ['gtl']
		}, {
			'title': 'artist:belmond uozumi',
			'className': ['gtl']
		}]
	}
}]
```

`title` 表示该画廊的日文标题，`URL` 表示该画廊的链接，`cat` 表示该画廊的分类，`cover` 表示该画廊的封面地址，`uploader` 表示该画廊的上传者，`uploaderURL` 表示该画廊的上传者地址，`time` 表示该画廊的上传时间，`rating` 表示该画廊的评分，`pages` 表示该画廊的页码。

`others` 表示该显示模式下的附加信息，`type` 表示信息类型，`has` 表示存在什么内容，`tags` 表示标签。

#### 全部浏览

使用该模式将会无视你的默认设置，关闭你的过滤器，并展示更多内容，如：被删除的画廊、低分标签等。

```python
waziExHentai.allBrowse(0)

# 第一位参数表示页码，从 0 数起
```

格式同**普通浏览**一致。

### 搜索

内置多种搜索模式，搜索返回格式均同浏览一致，不再赘述。

#### 普通模式

使用默认设置进行搜索。

```python
waziExHentai.search(0, "maid")

# 第一位参数表示页码，从 0 数起
# 第二位参数表示搜索内容，多内容请在引号里面使用“+”连接
```

#### 全部模式

无视你的默认模式并允许其他内容。

```python
waziExHentai.allSearch(0, "dress")

# 第一位参数表示页码，从 0 数起
# 第二位参数表示搜索内容，多内容请在引号里面使用“+”连接
```

#### 标签模式

使用默认设置进行标签搜索。

```python
waziExHentai.tagSearch(0, "language:chinese")

# 第一位参数表示页码，从 0 数起
# 第二位参数表示标签，包括 : 前的内容（若有）
```

多标签普通搜索请使用普通模式，标签全部搜索请使用全部模式。

#### 上传者模式

使用默认设置进行上传者搜索。

```python
waziExHentai.uploaderSearch(0, "如歌的行板")

# 第一位参数表示页码，从 0 数起
# 第二位参数表示上传者名，无需带上 uploader: 前缀
```

多上传者普通搜索请使用普通模式，多上传者全部搜索请使用全部模式，记得带上 `uploader:` 前缀。

#### 上传者全部模式

无视你的默认模式并允许其他内容进行上传者搜索。

```python
waziExHentai.uploaderAllSearch(0, "如歌的行板")

# 第一位参数表示页码，从 0 数起
# 第二位参数表示上传者名，无需带上 uploader: 前缀
```

#### 高级模式

> 不推荐使用，因为这个东西的参数内容不是那么直观，建议使用自定义搜索。

```python
waziExHentai.advancedSearch({
    "cats": ["Non-H"],  # 需要搜索的分类
    "search": "",  # 搜索内容
    "sgn": True,  # 是否搜索画廊名称
    "sgt": True,  # 是否搜索画廊标签
    "sgd": False,  # 是否搜索画廊描述
    "stf": False,  # 是否搜索种子名称
    "osgwt": False,  # 是否只查看那些带有种子的画廊
    "slpt": False,  # 搜索冷门标签或低评分标签
    "sdt": False,  # 搜索投票过差的标签
    "seg": False,  # 搜索被移除的画廊
    "mr": True,  # 是否限定最低评分
    "mrs": 5,  # 最低评分 范围是 2 - 5
    "b": False,  # 搜索限定范围
    "b1": "",  # 起始范围
    "b2": "",  # 结束范围
    "dfl": False,  # 关掉默认或设置对语言的过滤
    "dfu": False,  # 关掉默认或设置对上传者的过滤
    "dft": False,  # 关掉默认或设置对标签的过滤
    "page": 0  # 页码 从 0 计数
})
```

#### 图片模式

> 不推荐使用，因为这个东西的参数内容不是那么直观，建议使用自定义搜索。

通过默认模式进行图片搜索。

##### 给出图片的 SHA-1

```python
waziExHentai.imageSearch({
    "type": "sha1",
    "sha1": "C75774D8D2F003C8337F1EA57BA3184A9A4FD515",
    "similar": True,  # 是否搜索相似的图片
    "cover": True,  # 是否搜索封面
    "exp": True  # 是否搜索被移除的画廊
})
```

##### 给出图片的路径

```python
waziExHentai.imageSearch({
    "type": "file",
    "path": "./11.jpg", # 绝对和相对均可
    "similar": True, # 是否搜索相似的图片
    "cover": True, # 是否搜索封面
    "exp": True # 是否搜索被移除的画廊
})
```

#### 自定义模式

我非常推荐开发者使用自定义搜索来构建一个更为严谨的搜索请求。

```python
waziExHentai.customSearch({
	"cats": ["Doujinshi", "Manga", "Artist CG", "Game CG"],  # 搜索需要的分类 不提供表示全搜索
	"uploaders": ["Pokom", "NekoHime27"],  # 是否搜索上传者 不提供表示不搜索
	"tags": ["female:lolicon"],  # 是否搜索标签 不提供表示不搜索
	"text": "",  # 是否搜索关键词 不提供表示不搜索 三者互相制约
	"advanced": {  # 高级搜索 不提供表示不进行高级搜索
		"search": {
			"galleryName": True,  # 是否搜索画廊名称
			"galleryTags": True,  # 是否搜索画廊标签
			"galleryDescription": False,  # 是否搜索画廊描述
			"torrentFilenames": False,  # 是否搜索种子名
			"low-powerTags": False,  # 是否搜索低能标签
			"downvotedTags": False,  # 是否搜索投票给差的标签
			"expungedGalleries": False,  # 是否搜索被移除的画廊
		},
		"limit": {
			"onlyShowGalleriesWithTorrents": False,  # 是否只搜索带种子的画廊
			"minimumRating": False,  # 是否启用最低评分
			"minimumRatingNumber": 2,  # 最低评分 2 - 5
			"between": False,  # 范围
			"betweenPages": [0, 0]  # 起始与结束
		},
		"disableFilters": {
			"language": False,  # 是否关闭语言过滤器
			"uploader": False,  # 是否关闭上传者过滤器
			"tags": False  # 是否关闭标签过滤器
		}
	},
	"file": {  # 文件搜索，不提供表示不进行文件搜索
		"main": {
			"type": "path",  # type 可以是 sha1 或者 path
			"value": "./a.jpg"  # 如果 type 是 sha1 那么这里填写文件的 SHA1 值
		},
		"options": {
			"useSimilarityScan": True,  # 是否启用相似搜索
			"onlySearchCovers": False,  # 是否只搜索封面
			"showExpunged": False  # 查看被移除的画廊
		}
	}
})
```

### 信息获取

包含种子信息，基础信息，评论内容三大要素。

#### 种子信息

```python
waziExHentai.getTorrent("https://exhentai.org/g/2011308/8263590d02/")

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
```

返回列表：

```python
[{'time': '2021-09-15 17:48', 'size': '39.93 MB', 'seeds': '8', 'peers': '3', 'total': '268', 'link': 'https://exhentai.org/torrent/2011308/dcfecda8d01d5f928ed0a03d44a20bd753b86d92.torrent', 'name': '[Ramchi] 【巫女服を着た】茶髪ちゃん.zip'}]
```

`time` 表示上传时间，`size` 表示文件大小，`seeds` 表示做种数，`peers` 表示用户数，`total` 表示下载总量，`link` 表示种子下载地址，`name` 表示文件名。

#### 基础信息

分了两个获取方式出来：

1. 通过网页端；
2. 通过 API 接口。

##### 通过网页端

```python
waziExHentai.getInfo("https://exhentai.org/g/2011308/8263590d02/")

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
```

返回字典：

```python
{'title': '[Ramchi] [Mikofuku o Kita] Chapatsu-chan', 'jTitle': '[らむち] 【巫女服を着た】茶髪ちゃん', 'cat': 'Artist CG', 'tags': ['artist:ramchi', 'male:sole male', 'male:first person perspective', 'female:sole female', 'female:miko', 'other:variant set', 'other:mosaic censorship'], 'time': '2021-09-15 16:27', 'father': 'None', 'viewable': 'Yes', 'language': 'Japanese', 'tr': False, 'rw': False, 'size': '40.02 MB', 'pages': 24, 'favTimes': '257 times', 'uploader': 'RepStormy', 'rate': '4.54', 'cover': 'https://exhentai.org/t/6f/4c/6f4ce969fb06df5c588d0c608325dd51b6c80e6a-1775767-1152-2048-png_250.jpg'}
```

`title` 表示罗马字/英文标题，`jTitle` 表示日文或其他语种标题，`cat` 表示分类，`tags` 表示标签，`time` 表示上传时间，`father` 表示父级图集，`viewable` 表示是否可见，`language` 表示语言，`size` 表示大小，`pages` 表示页码，`favTimes` 表示被收藏次数，`uploader` 表示上传者，`rate` 表示评分，`cover` 表示封面。

##### 通过 API 接口

```python
waziExHentai.apiInfo("https://exhentai.org/g/2011308/8263590d02/")

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
```

返回字典：

```python
{'gmetadata': [{'gid': 2011308, 'token': '8263590d02', 'archiver_key': '453359--2db256904a5e9dfedee04cb1fad9229abc723e43', 'title': '[Ramchi] [Mikofuku o Kita] Chapatsu-chan', 'title_jpn': '[らむち] 【巫女服を着た】茶髪ちゃん', 'category': 'Artist CG', 'thumb': 'https://exhentai.org/t/6f/4c/6f4ce969fb06df5c588d0c608325dd51b6c80e6a-1775767-1152-2048-png_l.jpg', 'uploader': 'RepStormy', 'posted': '1631723255', 'filecount': '24', 'filesize': 41959880, 'expunged': False, 'rating': '4.36', 'torrentcount': '1', 'torrents': [{'hash': 'dcfecda8d01d5f928ed0a03d44a20bd753b86d92', 'added': '1631728106', 'name': '[Ramchi] 【巫女服 を着た】茶髪ちゃん.zip', 'tsize': '13243', 'fsize': '41871590'}], 'tags': ['artist:ramchi', 'male:first person perspective', 'male:sole male', 'female:miko', 'female:sole female', 'mosaic censorship', 'variant set']}]}
```

`archiver_key` 是压缩包下载地址的后缀, `title` 是标题，`title_jpn` 是日文标题，`category` 是分类，`thumb` 是封面，`uploader` 是上传者, `posted` 是秒级别的时间戳，`filecount` 是文件数量，`filesize` 是文件大小，`expunged` 是否被移除状态，`rating` 是评分，`torrentcount` 是种子数量，`hash` 是种子哈希值，`added` 是秒级别的时间戳，`name` 是种子文件名，`tsize` 和 `fszie` 我不清楚，`tags` 是标签。

#### 评论内容

```python
waziExHentai.getComments("https://exhentai.org/g/1948847/f81687b96e/")

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
```

返回列表：

```python
[{'time': '02 July 2021, 17:41', 'uploader': 'https://exhentai.org/uploader/%E9%82%A3%E7%8F%82%E3%81%A1%E3%82%83%E3%82%93', 'uploaderName': '那珂ちゃん', 'scores': 'None / 不适用', 'htmlComments': '\n https://fantia.jp/posts/615177\n <br/>\n <br/>\n <a href="https://exhentai.org/s/0dcc07ddde/1948847-1">\n  001~010 文字あり\n </a>\n <br/>\n <a href="https://exhentai.org/s/0e34105f9a/1948847-11">\n  011~020 文字なし\n </a>\n\n'}, {'time': '30 July 2021, 04:56', 'uploader': 'https://exhentai.org/uploader/pop9', 'uploaderName': 'pop9', 'scores': '+76', 'htmlComments': '\n https://ehwiki.org/wiki/japanese\n <br/>\n <br/>\n Default language flag;\n <strong>\n  do NOT use this tag\n </strong>\n outside of legitimate dual-language galleries and translations to Japanese.\n\n'}]
```

`time` 表示评论时间，`uploader` 表示评论者主页，`uploaderName` 表示评论者昵称，`scores` 表示评分，`htmlComments` 表示 html 版本的评论。

### 图片

分为缩略图和普通图片。

#### 缩略图

缩略图给了两种模式：Large（大图模式） 跟 Normal（正常模式）。

##### 大图模式

```python
waziExHentai.getLargeThumbnails("https://exhentai.org/g/1948847/f81687b96e/")

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
```

返回列表：

```python
[{'url': 'https://exhentai.org/t/0d/cc/0dcc07ddde12dd84a128ae83f9ff48375e32f768-5456884-2921-4112-png_l.jpg', 'style': 'height:302px', 'alt': '01', 'title': 'Page 1: cien_2102_01_full.png', 'text': '01'}, ...]
```

`url` 表示缩略图下载地址，`style` 表示这张图的叠层样式表信息，`alt` 表示缺失时内容，`title` 表示图片信息，`text` 表示图片位置等其他内容。

##### 普通模式

> 不推荐使用普通模式，因为在显示时需要做图片切割。

```python
waziExHentai.getNormalThumbnails("https://exhentai.org/g/1948847/f81687b96e/")

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
```

返回列表：

```python
[{'style': 'height:161px', 'divMargin': '1px auto 0', 'divWidth': '100px', 'divHeight': '141px', 'url': 'https://exhentai.org/m/001948/1948847-00.jpg', 'transparent': '-0px 0 no-repeat', 'imgAlt': '01', 'imgTitle': 'Page 1: cien_2102_01_full.png', 'imgWidth': '100px', 'imgHeight': '140px', 'imgMargin': '-1px 0 0 -1px'}, ...]
```

对于内容的解释，我建议你去阅读去看 Normal 模式下的网站源码，因为这涉及到边框、位移、切分、范围等信息，我能理解，却不能正常又简洁地表述出来。

#### 画廊图片

##### 列出下载地址或下载

```python
waziExHentai.getNormalImages("https://exhentai.org/g/1948847/f81687b96e/", "get", {"path": "./download", "japanese": True})

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
# 第二位参数表示方式 get 表示列出下载地址 download 表示下载
# 第三位参数是一个字典，表示详细信息，path 表示你的下载路径，japanese 表示是否使用日文标题
```

get 返回列表：

```python
['https://psnnstn.svbhzynmthvg.hath.network:6643/h/9a46b72d4e41e2cb71904e3f47a3a225041614f6-702136-2400-3379-jpg/keystamp=1627754700-3893ea4f9c;fileindex=94546547;xres=2400/cien_2102_01_full.jpg', ...]
```

包含所有画廊的图片地址。

download 返回列表：

```python
['./download\\[tokunocin (徳之ゆいか)] 妄想少女キクリちゃん #1\\cien_2102_01_full.jpg', ...]
```

包含所有下载的文件。

##### MPV 权限用户

```python
waziExHentai.getMPVImages("https://exhentai.org/g/1948847/f81687b96e/", "get", {"path": "./download", "japanese": True})

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
# 第二位参数表示方式 get 表示列出下载地址 download 表示下载
# 第三位参数是一个字典，表示详细信息，path 表示你的下载路径，japanese 表示是否使用日文标题
```

get 返回列表：

```python
[{'name': 'cien_2102_01_full.png', 'url': 'https://vzwiuar.bgjtsezaekpi.hath.network:9880/h/219a879c79dddf63c230e02408ccebceebd9cccb-283462-1280-1802-jpg/keystamp=1627755900-c26b737547;fileindex=94546547;xres=1280/cien_2102_01_full.jpg'}, ...]
```

`name` 表示文件名，`url` 表示下载链接。

download 返回列表：

```python
['./download\\[tokunocin (徳之ゆいか)] 妄想少女キクリちゃん #1\\cien_2102_01_full.jpg', ...]
```

包含所有下载的文件。

### 压缩包下载

分三个：H@H、链接、下载

#### H@H

分两个：获取和下载

##### H@H 获取

```python
waziExHentai.getArchivesHATH("https://exhentai.org/g/1948847/f81687b96e/")

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
```

返回列表：

```python
[{'sample': '780x', 'size': '1.42 MB', 'cost': 'Free', 'code': '780', 'url': 'https://exhentai.org/archiver.php?gid=1948847&token=f81687b96e&or=452154-1c41df26535532bfc35cff7874319017afed3418'}, ...]
```

`sample` 表示分辨率，`size` 表示大小，`cost` 表示花费点数，`code` 表示代码，`url` 表示 H@H 请求链接。

##### H@H 下载

```python
waziExHentai.toHATH("https://exhentai.org/archiver.php?gid=1948847&token=f81687b96e&or=452154-1c41df26535532bfc35cff7874319017afed3418", "780")

# 第一位参数表示 H@H 返回的 URL
# 第二位参数表示 H@H 返回的代码
```

如果返回 `Done! / 完成！` 就表示成了，否则，按照提示做。

#### 链接获取

```python
waziExHentai.getArchives("https://exhentai.org/g/1948847/f81687b96e/")

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
```

返回列表：

```python
[{'type': 'original', 'link': 'https://plprhexcngkbxoopaqlx.hath.network/archive/1948847/1d0756978bba0f6166cc5eafa1b05cc33257a77d/cxltzmu9ovu/2?start=1'}, {'type': 'resample', 'link': 'https://plprhexcngkbxoopaqlx.hath.network/archive/1948847/1d0756978bba0f6166cc5eafa1b05cc33257a77d/cxltzmu9ovu/3?start=1'}]
```

`type` 表示压缩包类型，`link` 表示下载地址。

#### 下载压缩包

```python
waziExHentai.downloadArchives("https://exhentai.org/g/1948847/f81687b96e/", {"path": "./download", "japanese": True}, "")

# 第一位参数表示画廊的地址，要求 “https://” 开头 “/” 结尾 
# 第二位参数是一个字典，表示详细信息，path 表示你的下载路径，japanese 表示是否使用日文标题
# 第三位参数表示下载的分辨率，如果为空字符串表示全部下载
```

返回列表，但我无法正常返回，因为我只能下载原图尺寸。

## waziPicAcg 教程

### 配置

```python
from pywazi import waziPicAcg

waziPicAcg.giveParams({
    "useProxies": True,  # 是否使用代理
    "proxyAddress": "127.0.0.1",  # HTTPS / HTTP 代理地址
    "proxyPort": "7890",  # HTTPS / HTTP 代理端口
    "useHeaders": False,  # 是否用自定义头部 （不建议填写，程序自动补充）
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.164 Safari/537.36"
    }  # 自定义头部内容 （你填了我估计没法访问）
})

waziPicAcg.login("你的用户名", "你的密码")
```

正常登陆后返回一串 token，如果失败了，大概率是：

1. 网络问题，检查代理；
2. 时间同步问题，尤其是双系统的电脑；
3. 账号密码不对或不存在；
4. PicAcg 更新了。

### 获取分区

```python
waziPicAcg.getCategories()
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'categories': [{
			'title': '援助嗶咔',
			'thumb': {
				'originalName': 'help.jpg',
				'path': 'help.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': True,
			'active': True,
			'link': 'https://donate.wikawika.xyz'
		}, {
			'title': '嗶咔小禮物',
			'thumb': {
				'originalName': 'picacomic-gift.jpg',
				'path': 'picacomic-gift.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': True,
			'link': 'https://gift-web.wikawika.xyz',
			'active': True
		}, {
			'title': '小電影',
			'thumb': {
				'originalName': 'av.jpg',
				'path': 'av.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': True,
			'link': 'https://av.wikawika.xyz',
			'active': True
		}, {
			'title': '小里番',
			'thumb': {
				'originalName': 'h.jpg',
				'path': 'h.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': True,
			'link': 'https://h.wikawika.xyz',
			'active': True
		}, {
			'title': '嗶咔畫廊',
			'thumb': {
				'originalName': 'picacomic-paint.jpg',
				'path': 'picacomic-paint.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': True,
			'link': 'https://paint-web.wikawika.xyz',
			'active': True
		}, {
			'title': '嗶咔鍋貼',
			'thumb': {
				'originalName': 'picacomic-post.jpg',
				'path': 'picacomic-post.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': True,
			'link': 'https://post-web.wikawika.xyz',
			'active': True
		}, {
			'title': '嗶咔商店',
			'thumb': {
				'originalName': 'picacomic-shop.jpg',
				'path': 'picacomic-shop.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': True,
			'link': 'https://online-shop-web.wikawika.xyz',
			'active': True
		}, {
			'title': '大家都在看',
			'thumb': {
				'originalName': 'every-see.jpg',
				'path': 'every-see.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': False,
			'active': True
		}, {
			'title': '下雨了呢',
			'thumb': {
				'originalName': 'recommendation.jpg',
				'path': '829847d3-36ab-4357-834f-676411041554.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			},
			'isWeb': False,
			'active': True
		}, {
			'title': '那年今天',
			'thumb': {
				'originalName': 'old.jpg',
				'path': 'old.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': False,
			'active': True
		}, {
			'title': '官方都在看',
			'thumb': {
				'originalName': 'promo.jpg',
				'path': 'promo.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': False,
			'active': True
		}, {
			'title': '嗶咔運動',
			'thumb': {
				'originalName': 'picacomic-move-cat.jpg',
				'path': 'picacomic-move-cat.jpg',
				'fileServer': 'https://wikawika.xyz/static/'
			},
			'isWeb': True,
			'active': True,
			'link': 'https://move-web.wikawika.xyz'
		}, {
			'_id': '5821859b5f6b9a4f93dbf6e9',
			'title': '嗶咔漢化',
			'description': '未知',
			'thumb': {
				'originalName': 'translate.png',
				'path': 'f541d9aa-e4fd-411d-9e76-c912ffc514d1.png',
				'fileServer': 'https://storage1.picacomic.com'
			}
		}, {
			'_id': '5821859b5f6b9a4f93dbf6d1',
			'title': '全彩',
			'description': '未知',
			'thumb': {
				'originalName': '全彩.jpg',
				'path': '8cd41a55-591c-424c-8261-e1d56d8b9425.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			}
		}, {
			'_id': '5821859b5f6b9a4f93dbf6cd',
			'title': '長篇',
			'description': '未知',
			'thumb': {
				'originalName': '長篇.jpg',
				'path': '681081e7-9694-436a-97e4-898fc68a8f89.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			}
		}, ...
		}]
	}
}
```

### 获取热词

```python
waziPicAcg.getKeywords()
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'keywords': ['乳汁', '短髮', '全彩', '自慰', '吞精', '橫切面', '無修正', '短篇合集', '校園', '人外娘', '開大車']}}
```

### 获取神魔推荐

```python
waziPicAcg.getCollections()
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'collections': [{'title': '本子神推薦', 'comics': [{'_id': '5f9e7e417193765a84d387c1', 'title': 'ナイショの夜ふかし(High☆Speed! -Free! Starting Days-)', 'author': 'B-LUSH(カウカウ)', 'totalViews': 136228, 'totalLikes': 8393, 'pagesCount': 40, 'epsCount': 1, 'finished': True, 'categories': ['短篇', '同人', '純愛', '耽美花園'], 'thumb': {'originalName': 'title 副本.jpg', 'path': 'eb9ccaf7-24f5-42ea-8f11-d57b1249718f.jpg', 'fileServer': 'https://storage1.picacomic.com'}}]}, {'title': '本子魔推薦', 'comics': [{'_id': '6072a5621397b71d7b466432', 'title': 'Lusty radroach', 'author': 'Chobonolly', 'totalViews': 498033, 'totalLikes': 7498, 'pagesCount': 27, 'epsCount': 3, 'finished': True, 'categories': ['短篇', '非人類', '重口地帶', '全彩', 'CG雜圖', '生肉'], 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': '5baeb887-2bb3-4fb9-a2dd-cbb42c21b45f.jpg', 'originalName': '1.jpg'}}, {'_id': '612628dbaa7eee38665221ce', 'title': '비밀유지보안법丨维持秘密的保安法', 'author': '팀딱콩', 'totalViews': 204856, 'totalLikes': 9110, 'pagesCount': 109, 'epsCount': 2, 'finished': False, 'categories': ['全彩', 'WEBTOON'], 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': 'b3b4d5c1-6413-40f4-9d15-6d76b7b351e2.jpg', 'originalName': 'E0H2BCCVUAAtxaA.jpg'}}]}]}}
```

### 获取首页横幅

```python
waziPicAcg.getBanners()
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'banners': [{'_id': '601d3abdcfeaee28f8d8cb72', 'title': '逆王傳說: 入侵女兒國', 'shortDescription': '想幹就幹！', '_game': '601d3abdcfeaee28f8d8cb72', 'type': 'game', 'thumb': {'fileServer': 'https://pica-pica.wikawika.xyz', 'path': 'banner_game.gif?v=1', 'originalName': 'banner_game.gif'}}, {'_id': 'qkwejqkwe', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '完美嫩乳!', 'type': 'web', 'link': 'https://ad-channel.wikawika.xyz/redirect/zone_3', 'thumb': {'fileServer': 'https://ad-channel.wikawika.xyz', 'path': 'TPl-6fggnqnd5qb_AgUvT.jpg', 'originalName': 'image.jpg'}}, {'_id': 'dsfsdf', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '😘 ', 'type': 'ads', 'link': 'https://ad-channel.wikawika.xyz/android/home_banner', 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': '369ca47f-e015-4acf-b2e3-cb4800c876f7.jpg', 'originalName': 'image.jpg'}}, {'_id': 'dsfsdf1', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '😘 ', 'type': 'ads', 'link': 'https://ad-channel.wikawika.xyz/android/home_banner_2', 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': '369ca47f-e015-4acf-b2e3-cb4800c876f7.jpg', 'originalName': 'image.jpg'}}, {'_id': 'fjg1', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '點就對了!', 'type': 'web', 'link': 'https://ad-channel.wikawika.xyz/redirect/zone_4', 'thumb': {'fileServer': 'https://ad-channel.wikawika.xyz', 'path': 'ANECmINT-izcsF208QM2y.jpg', 'originalName': 'image.jpg'}}, {'_id': 'toBe3', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '😘 ', 'type': 'ads', 'link': 'https://ad-channel.wikawika.xyz/android/home_banner_4', 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': '369ca47f-e015-4acf-b2e3-cb4800c876f7.jpg', 'originalName': 'image.jpg'}}, {'_id': 'toBe4', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '來征服我吧!', 'type': 'web', 'link': 'https://ad-channel.wikawika.xyz/redirect/zone_5', 'thumb': {'fileServer': 'https://ad-channel.wikawika.xyz', 'path': 'bI8uZ7Pdycuet_IBuh64O.jpg', 'originalName': 'image.jpg'}}]}}
```

### 获取通知

```python
waziPicAcg.getNotifications(1)

# 第一位参数表示页码，从 1 数起
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'notifications': {'docs': [], 'total': 0, 'limit': 10, 'page': 1, 'pages': 1}}}
```

我仍不清楚 `docs` 里面会有什么东西。

### 获取公告

```python
waziPicAcg.getAnnouncements(1)

# 第一位参数表示页码，从 1 数起
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'announcements': {'docs': [{'_id': '6142e0880dac716f6aa09d01', 'content': '「Master，我快要抑制不住了魔主之力了，嗚、嗚啊——！」\n少女英靈卸除胸甲，展示腹部泛起的黑色旋渦\n她脫下身上皮甲和長裙，絲襪接連扯下，背對勇士翹起圓臀——\n「Master……？不快點的話，我就……嗯…♡」\n面對少女的挑逗，立即解開蠢蠢欲動的褲檔，插進你的「聖劍♂」，以高濃度魔力侵吞英靈的驅體！\n\n安卓及iOS下載連接:\nhttps://fgoatt13.star1818.net\n\n其餘遊戲請到嗶咔遊戲區下載！\n\n－－－－－－－－－－－－－－－－－－\n\n宅男成人社區，海量美圖視頻免費觀看 https://new-apk.99gezi.com/package/android/30_nlzljq_3.1.6.apk\n\n蘑菇加速器，翻牆看本子，再也不怕掉隊。牆外的世界很精彩！https://3.mogu91.com/\n\n騎士開發，老司機帶你看片子 https://dw.xiacangku.xyz/\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡有優惠哦~ http://mtw.so/5Urt0j\n\n視訊玩法，點擊下載送現金! https://down.sxshiye.com/gamecenter-release-android-shanhe-500019-7bb5d875dd0fe7d4939cad9b283d24a1.apk\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n91短視頻 記錄性福生活 https://app.dsppro.me/chan-1005/aff-Ghyw\n\n極速翻牆看嗶咔速度秒殺老王 https://VPN.bika.page\n\n－－－－－－－－－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j\n\n！！！！！\n由於嗶咔的淑女會員愈來愈多，為了了解淑女對本子的喜好，我們在 telegram 開了一個淑女群，希望透過交流了解淑女對嗶咔的感覺和意見，歡迎淑女們加入我們的群。進入群後你必須證實你是淑女，否則會被踢出群和封鎖喔😊\nhttps://t.me/joinchat/y7Q6G3n-Y_NhYzNl', 'title': '命運王座', 'created_at': '2021-09-16T06:13:28.578Z', 'thumb': {'originalName': '0915_FGO_800_1200.jpg', 'path': '304c55e0-a8cc-4fa9-a414-466a068e3393.jpg', 'fileServer': 'https://storage1.picacomic.com'}}, {'_id': '613a1dfcff488f6f443a54a7', 'content': '夕陽西下，浴場內有一女子洗濯 的背影\n豈料風一吹，藏匿在草叢的你馬上現形！\n「逆王大人，都看過我的身體了，還能就此作罷嘛♡～？」\n少女僅以薄布包裹半身 ，外露的北半球在夕照和水面的映襯下顯得碧波蕩漾\n她靠近輕撫你的褲檔，身上乳液混雜著少女體香，實在叫人欲罷不能！\n還不一手扯掉她的浴巾，盡情享受魚水之歡？\n立即降臨女兒國，以身下大炮廣結淫緣！\n\n安卓及iOS下載連接:\nhttp://xratt13.thejierou.net\n\n其餘遊戲請到嗶咔遊戲區下載！\n\n－－－－－－－－－－－－－－－－－－\n\n宅男成人社區，海量美圖視頻免費觀看 https://new-apk.99gezi.com/package/android/30_nlzljq_3.1.6.apk\n\n蘑菇加速器，翻牆看本子，再也不怕掉隊。牆外的世界很精彩！https://3.mogu91.com/\n\n騎士開發，老司機帶你看片子 https://dw.xiacangku.xyz/\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡 有優惠哦~ http://mtw.so/5Urt0j\n\n視訊玩法，點擊下載送現金! https://down.sxshiye.com/gamecenter-release-android-shanhe-500019-7bb5d875dd0fe7d4939cad9b283d24a1.apk\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n91短視頻 記錄性福生活 https://app.dsppro.me/chan-1005/aff-Ghyw\n\n極速翻牆看嗶咔速度秒殺老王 https://VPN.bika.page\n\n－－－－－－－ －－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j\n\n！！！！！\n由於嗶咔的淑女會員愈來愈多，為了了解淑女對本子的喜好，我們在 telegram 開了一個淑女群，希望透過交流了解淑女對嗶咔的感覺和意見，歡迎淑女們加入我們的群。進入群後你必須證實你是淑女，否則會被踢出群和封鎖喔😊\nhttps://t.me/joinchat/y7Q6G3n-Y_NhYzNl', 'title': '逆王傳說', 'created_at': '2021-09-09T14:45:16.557Z', 'thumb': {'originalName': 'Artboard 1.jpg', 'path': 'ad2c7950-e2f1-459f-b0a8-7bbd90cf3b51.jpg', 'fileServer': 'https://storage1.picacomic.com'}}, {'_id': '6081771007edd91d5adbfbdd', 'title': '棋牌公告', 'content': '盛夏燥熱無比？快來貼緊冰涼爆乳為你降溫！\n下載游戲，拯救bika~\n視訊發牌再升級，夏季限定比基尼爆乳荷官，冰冰涼涼貼緊你～同城真人陪玩，主人，約嗎？\n每晚整點准時抽獎，現金6666、iPhone12pro Max等，獎品upupup再up！\n刺激爽翻 天，安全公平，24小時客服服務，隨叫隨到，全新趨勢分析參考助你走上人生巔峰！\n實時聯網競技，盡享競技快感，爆乳在測波濤洶湧，助你今晚高潮！\n山河棋牌，2021年最新最火爆棋牌。真人在线，提款秒到！\n一秒開局萬人在線，德州撲克大佬互搏，今晚就要贏到人生高潮！還有豐富的游戲種類！\n主人快來～乳醬陪你激情一夏～～\n\n下載連結:\nhttps://down.sxshiye.com/gamecenter-release-android-shanhe-500019-7bb5d875dd0fe7d4939cad9b283d24a1.apk\n\n－－－－－－－－－－－－－－－－－－\n\n宅男成人社區，海 量美圖視頻免費觀看 https://new-apk.99gezi.com/package/android/30_nlzljq_3.1.6.apk\n\n蘑菇加速器，翻牆看本子，再也不怕掉 隊。牆外的世界很精彩！https://3.mogu91.com/\n\n騎士開發，老司機帶你看片子  https://dw.xiacangku.xyz/\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡有優惠哦~ http://mtw.so/5Urt0j\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n91短視頻 記錄性福生活 https://app.dsppro.me/chan-1005/aff-Ghyw\n\n極速翻牆看嗶咔速度秒殺老王 https://VPN.bika.page\n\n—－－－－－－－－－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j\n', 'created_at': '2021-04-22T13:16:00.766Z', 'thumb': {'originalName': '组1(9).jpg', 'path': '6585d1ee-0a6a-48dc-9075-5d22358d34f5.jpg', 'fileServer': 'https://storage1.picacomic.com'}}, {'_id': '5bf235bbd158ce4e17b8d09a', 'title': '嗶咔漫畫鳳凰計劃・一 順利完成 ！', 'content': '----------請注意個人衞生，配戴口罩，保護自己，努力活下去-------------\n\n嗶咔漫畫鳳凰計劃・一\n\n\n鳳凰計劃第一階行動雖然遇上一點點困難，但最後也順利完成，十分感謝大家的耐心等候。\n快與穩能夠同時存在！\n晚上的戒擼時段已經成為歷史！\n\n・・・\n\n要來的，總會來\n嗶咔漫畫會蛻變成鳳凰\nhttps://countdown.picacomic.com\n\n-----《特別公告》-----\n 遊戲區部份H遊暫停至1月25日！\n\n－－－－－－－－－－－－－－－－－－\n\n宅男成人社區，海量美圖視頻免費觀看 https://new-apk.99gezi.com/package/android/30_nlzljq_3.1.6.apk\n\n蘑菇加速器，翻牆看本子，再也不怕掉隊。牆外的世界很精彩！https://3.mogu91.com/\n\n騎士開發，老司機帶你看片子  https://dw.xiacangku.xyz/\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡有優惠哦~ http://mtw.so/5Urt0j\n\n91短视频 记录性福生活 https://app.dsppro.me/chan-1005/aff-Ghyw\n\n極速翻牆看嗶咔速度秒殺老王 https://VPN.bika.page\n\n\n—－－－－－－－－－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j', 'created_at': '2018-11-19T04:02:03.067Z', 'thumb': {'originalName': '34789.png', 'path': 'e7b7ea62-2ede-4521-92bc-7a044d4b3f07.png', 'fileServer': 'https://storage1.picacomic.com'}}, {'_id': '5acc60d0bc6b3779f41f681f', 'title': '漢化組及群組聲明公告', 'content': '嗶咔漢化組出現危機！\n\n漢化 組原話：\n" 勇士们哟！欢迎来到我的酒馆！快找个位子随便座~≧▽≦ 就像招募页里一样的啦，哔咔哔咔汉化组的图源酱不小心操劳过度 被沉到大西洋了，在这里向各位有志之士发出邀请òᆺó，欢迎新图源酱的到来哦！"\n\n請多多支持！詳細請看圖！ \n\n另外，又發現一 個冒認吾等的群組收錢賣免費軟件，在此聲明，無論你付不付款，你要用梯子就是要用，不需要用就是不需要用，並沒有付款後會增加的功能，我們也不會從任何的群收取任何金錢，以上！\n\n－－－－－－－－－－－－－－－－－－－－\n\n玩機動戰隊，告別枯燥回合操作\n安卓下載請去: http://package.jdzd.gameduchy.cn/jdzd_c10___.apk\n\n獲取禮包碼\x08:\n安卓: http://jdzd.gameduchy.cn:9152/get_code/?key=dujia\niOS: http://jdzd.gameduchy.cn:9252/get_code/?key=dujia\n\n－－－－－－－－－－－－－－－－－－\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n蘑菇加速器，翻牆看本子，再也不怕掉隊。牆外的世界很精彩！https://3.mogu86.com/\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡有優惠哦~ http://t.cn/AiQS1jH0\n\n91短视频 记录性福生活 http://invited.91porn005.me:2082/chan-1005/aff-Ghyw\n\n萝莉喷水裸聊 加微信一夜情约炮  http://www.yyuucity.com/index.html?id=kch64\n\n極速翻牆看本子看油管玩外服遊戲 https://bika.lsj.world\n\n—－－－－－－－－－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j', 'created_at': '2018-04-10T06:59:28.003Z', 'thumb': {'originalName': 'sell_and_chinese_team.jpg', 'path': 'be75c212-0de4-40a7-bbc3-7e4369184e2b.jpg', 'fileServer': 'https://storage1.picacomic.com'}}], 'total': 30, 'limit': 5, 'page': '1', 'pages': 6}}}
```

### 获取随机漫画

```python
waziPicAcg.getRandomComics()
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'comics': [{
			'_id': '5d976c19ba83807016b899bf',
			'title': '私のかわいい丸腹の悪魔の姉妹',
			'author': 'はくじら海猫団 (しむー)',
			'totalViews': 17716,
			'totalLikes': 67,
			'pagesCount': 92,
			'epsCount': 1,
			'finished': True,
			'categories': ['全彩', '長篇', 'CG雜圖', '姐姐系', '妹妹系', '生肉'],
			'thumb': {
				'originalName': '1.jpg',
				'path': 'tobeimg/N0fVttx3OsKFPk5td3WEGk_awHMUO-DiS00mo7JS--M/fill/300/400/sm/0/aHR0cHM6Ly9zdG9yYWdlMS5waWNhY29taWMuY29tL3N0YXRpYy9jYmExMWFkZi01YWQ5LTQ5OGQtYjQwNy0xYTUyN2NlZmIzNTEuanBn.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			},
			'likesCount': 67
		}, ...]
	}
}
```

### 修改请求图片质量

```python
waziPicAcg.changeImageQuality(0)

# 第一位参数表示质量，0 表示原图，1 表示低质量，2 表示中等，3 表示高质量
```

### 最近更新（特殊）

```python
waziPicAcg.latestUpdate(1)

# 第一位参数表示页码，从 1 计数
```

### 过滤器

```python
waziPicAcg.filterIt(waziPicAcg.getComics("1", "足の恋", "全彩", "ua"), ["純愛"])

# 第一位参数表示返回的字典，建议直接使用 getComics 等
# 第二位参数表示需要过滤的分类，是列表
```

### 分流系

存在两类：普通分流、安卓分流。

#### 普通分流

```python
waziPicAcg.init()
```

返回字典：

```python
{'status': 'ok', 'addresses': ['104.20.180.50', '104.20.181.50'], 'waka': 'https://ad-channel.wikawika.xyz', 'adKeyword': 'wikawika'}
```

#### 安卓分流

```python
waziPicAcg.initAndroid()
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'isPunched': True, 'latestApplication': {'_id': '5dc58b151e103c60e7663b12', 'downloadUrl': 'https://download.wikawika.xyz/apps/2.2.1.3.3.4_collections.apk', 'updateContent': '【一般更新】\n\n1・ 新增漫畫推薦欄\n\n2・修改部份版本閃退問題\n\n後備下載連結\nhttps://download.wikawika.xyz/apps/2.2.1.3.3.4_collections.apk', 'version': '2.2.1.3.3.4', 'updated_at': '2019-11-08T15:38:45.706Z', 'created_at': '2019-11-08T15:34:45.163Z', 'apk': {'originalName': '2.2.1.3.3.4_collections.apk', 'path': '4da05b12-3534-4b4d-b9bf-804de301d2e0.apk', 'fileServer': 'https://storage1.picacomic.com'}}, 'imageServer': 'https://storage.wikawika.xyz/static/', 'apiLevel': 22, 'minApiLevel': 22, 'categories': [{'_id': '5821859b5f6b9a4f93dbf6e9', 'title': '嗶咔漢化'}, {'_id': '5821859b5f6b9a4f93dbf6d1', 'title': '全彩'}, {'_id': '5821859b5f6b9a4f93dbf6cd', 'title': '長篇'}, {'_id': '5821859b5f6b9a4f93dbf6ca', 'title': '同人'}, {'_id': '5821859b5f6b9a4f93dbf6ce', 'title': '短篇'}, {'_id': '584ea1f45a44ac4f7dce3623', 'title': '圓神領域'}, {'_id': '58542b601b8ef1eb33b57959', 'title': '碧藍幻想'}, {'_id': '5821859b5f6b9a4f93dbf6e5', 'title': 'CG雜圖'}, {'_id': '5821859b5f6b9a4f93dbf6e8', 'title': '英語 ENG'}, {'_id': '5821859b5f6b9a4f93dbf6e0', 'title': '生肉'}, {'_id': '5821859b5f6b9a4f93dbf6de', 'title': '純愛'}, {'_id': '5821859b5f6b9a4f93dbf6d2', 'title': '百合花園'}, {'_id': '5821859b5f6b9a4f93dbf6e2', 'title': '耽美花園'}, {'_id': '5821859b5f6b9a4f93dbf6e4', 'title': '偽娘哲學'}, {'_id': '5821859b5f6b9a4f93dbf6d3', 'title': '後宮閃光'}, {'_id': '5821859b5f6b9a4f93dbf6d4', 'title': '扶他樂園'}, {'_id': '5abb3fd683111d2ad3eecfca', 'title': '單行本'}, {'_id': '5821859b5f6b9a4f93dbf6da', 'title': '姐姐系'}, {'_id': '5821859b5f6b9a4f93dbf6db', 'title': '妹妹系'}, {'_id': '5821859b5f6b9a4f93dbf6cb', 'title': 'SM'}, {'_id': '5821859b5f6b9a4f93dbf6d0', 'title': '性轉換'}, {'_id': '5821859b5f6b9a4f93dbf6df', 'title': '足の恋'}, {'_id': '5821859b5f6b9a4f93dbf6cc', 'title': '人妻'}, {'_id': '5821859b5f6b9a4f93dbf6d8', 'title': 'NTR'}, {'_id': '5821859b5f6b9a4f93dbf6d9', 'title': '強暴'}, {'_id': '5821859b5f6b9a4f93dbf6d6', 'title': '非人類'}, {'_id': '5821859b5f6b9a4f93dbf6cf', 'title': '艦隊收藏'}, {'_id': '5821859b5f6b9a4f93dbf6d7', 'title': 'Love Live'}, {'_id': '5821859b5f6b9a4f93dbf6dc', 'title': 'SAO 刀劍神域'}, {'_id': '5821859b5f6b9a4f93dbf6e1', 'title': 'Fate'}, {'_id': '5821859b5f6b9a4f93dbf6dd', 'title': '東方'}, {'_id': '59041d54ccc747074b47dae4', 'title': 'WEBTOON'}, {'_id': '5821859b5f6b9a4f93dbf6e3', 'title': '禁書目錄'}, {'_id': '5bd66e7e8ff47f7c46cf999d', 'title': '歐美'}, {'_id': '5821859b5f6b9a4f93dbf6e6', 'title': 'Cosplay'}, {'_id': '5821859b5f6b9a4f93dbf6d5', 'title': '重口地帶'}], 'notification': None, 'isIdUpdated': True}}
```

### 漫画搜索

分了三类：`Comics` 模式、关键字模式和高级模式。

#### Comics 模式

```python
waziPicAcg.getComics("1", "足の恋", "全彩", "ua")

# 第一位参数表示页码，从 1 计数。
# 第二位参数表示分区名字，应当为 categories 里面的 title。
# 第三位参数表示标签名字，由 info 返回数据里面的 tags 获得。
# 第四位参数表示排序依据，分别为：
# 	ua -> 默认排序
#	dd -> 从新到旧
#	da -> 从旧到新
#	vd -> 最多绅士指名
#	ld -> 最多爱心
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'comics': {
			'docs': [{
				'_id': '610399ae3a8a1824a38ec6d2',
				'title': ' How to use dolls RE',
				'author': 'ooyun',
				'totalViews': 138134,
				'totalLikes': 2122,
				'pagesCount': 35,
				'epsCount': 1,
				'finished': True,
				'categories': ['短篇', '同人', '全彩', '足の恋', '純愛', '後宮閃光'],
				'thumb': {
					'originalName': '00.jpg',
					'path': 'tobeimg/qjKm0jTW70tSw0IyEa-hSI5aMgTLre9aDOa-0nqriSU/fill/300/400/sm/0/aHR0cHM6Ly9zdG9yYWdlMS5waWNhY29taWMuY29tL3N0YXRpYy9kYmQ3MDkyZi01ZjJiLTQ0Y2EtODMyZC01M2NlZjM1MzAxZDkuanBn.jpg',
					'fileServer': 'https://storage1.picacomic.com'
				},
				'id': '610399ae3a8a1824a38ec6d2',
				'likesCount': 2122
			}, ...],
			'total': 83,
			'limit': 20,
			'page': 1,
			'pages': 5
		}
	}
}
```

#### 关键词模式

```python
waziPicAcg.search("1", "伪娘")

# 第一位参数表示页码，从 1 计数。
# 第二位参数表示关键词。
```

格式同上，高级模式的格式也完全一致。

#### 高级模式

```python
waziPicAcg.advancedSearch(["純愛"], "女僕", "ld", 1)

# 第一位表示分区，支持多个分区，应当为列表类型，若不想要可以直接填写 []
# 第二位表示搜索的关键词
# 第三位表示排序方式
# 第四位表示页码，从 1 计数
```

### 漫画系

#### 获取漫画的基础信息

```python
waziPicAcg.getComic("60f5aab6e239c4708507c5d9")

# 第一位参数表示漫画 ID，_id 中可见
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'comic': {'_id': '60f5aab6e239c4708507c5d9', '_creator': {'_id': '58b2fe52288c3778fcbaba4d', 'gender': 'f', 'name': 'Selestial', 'verified': False, 'exp': 4586, 'level': 7, 'characters': ['knight'], 'role': 'knight', 'title': '萌新', 'avatar': {'originalName': 'avatar.jpg', 'path': 'f959bc38-94c0-4793-bc02-b1465d74f0bc.jpg', 'fileServer': 'https://storage1.picacomic.com'}, 'slogan': '......', 'character': 'https://pica-web.wakamoment.tk/images/halloween_f.png'}, 'title': 'ホクロ流星群せかんど [中国翻訳] [DL版]', 'description': '早该好好学学了\n（05 后别看05后别看05后别看）', 'thumb': {'originalName': 'QQ图片20210718224515.png', 'path': 'tobeimg/Gxkeem7A4h_VvYKYnIJbQx3ZCAcWFNj38-CFbeOfhZ4/fill/300/400/sm/0/aHR0cHM6Ly9zdG9yYWdlMS5waWNhY29taWMuY29tL3N0YXRpYy9jMjJjODVjNi0yYzUzLTQxMWQtYmIwNi1jZjg0NzBmZGVmZmEucG5n.png', 'fileServer': 'https://storage1.picacomic.com'}, 'author': '書肆マガジンひとり (ホクロ流 星群)', 'chineseTeam': '观星能治颈椎病个人渣翻', 'categories': ['偽娘哲學', '全彩', '短篇'], 'tags': ['偽娘', '口交', ' 制服', '雌墜', '女裝'], 'pagesCount': 30, 'epsCount': 1, 'finished': True, 'updated_at': '2021-07-19T16:39:18.121Z', 'created_at': '2021-07-18T15:12:14.015Z', 'allowDownload': True, 'allowComment': True, 'totalLikes': 438, 'totalViews': 51574, 'viewsCount': 51574, 'likesCount': 438, 'isFavourite': False, 'isLiked': False, 'commentsCount': 97}}}
```

#### 获取漫画的分页

```python
waziPicAcg.getComicEps("60f5aab6e239c4708507c5d9", "1")

# 第一位参数表示漫画 ID
# 第二位参数表示获取第几个分页
#   返回的 epsCount 中注明了有几个分页
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'eps': {'docs': [{'_id': '60f5aab6e239c4708507c5da', 'title': '第1話', 'order': 1, 'updated_at': '2021-07-18T15:17:47.711Z', 'id': '60f5aab6e239c4708507c5da'}], 'total': 1, 'limit': 40, 'page': 1, 'pages': 1}}}
```

#### 获取漫画的分页内容

```python
waziPicAcg.getComicPages("60f5aab6e239c4708507c5d9", "1", "1")

# 第一位参数表示漫画 ID
# 第二位参数表示获取第几个分页
# 第三位参数表示获取第几页
#   返回的 pages 注明了全部页码 / page 表示现在是第几页
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'pages': {
			'docs': [{
				'_id': '60f5aab6e239c4708507c5db',
				'media': {
					'originalName': '00.jpg',
					'path': 'tobeimg/wHyKO5BdzvRZkBugyFPJV0PsDVWI0a6_jDL6FuYISJE/fit/800/800/ce/0/aHR0cHM6Ly9zdG9yYWdlMS5waWNhY29taWMuY29tL3N0YXRpYy8xODU4MzQ0YS1jNTA3LTRhNWYtODYzMC0zYmFiZDYyYWM1ODUuanBn.jpg',
					'fileServer': 'https://storage1.picacomic.com'
				},
				'id': '60f5aab6e239c4708507c5db'
			}, ...],
			'total': 31,
			'limit': 40,
			'page': 1,
			'pages': 1
		},
		'ep': {
			'_id': '60f5aab6e239c4708507c5da',
			'title': '第1話'
		}
	}
}
```

#### 获取漫画推荐

```python
waziPicAcg.getComicRecommend("60f5aab6e239c4708507c5d9")

# 第一位参数表示漫画 ID
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'comics': []}}
```

如果能返回 comics 的话，应该同：[AnkiKong/picacomic: 哔咔漫画相关api (github.com)](https://github.com/AnkiKong/picacomic#recommend-看了這本子的人也在看) 一致。

#### 喜欢/取消喜欢这个漫画

```python
waziPicAcg.likeOrUnLikeComic("60f5aab6e239c4708507c5d9")

# 第一位参数表示漫画 ID
```

返回字典：

```python
{'code': 200, 'message': 'success'}
```

第一次是喜欢，第二次是取消喜欢。

#### 收藏/取消收藏这个漫画

```python
waziPicAcg.favOrUnFavComic("60f5aab6e239c4708507c5d9")

# 第一位参数表示漫画 ID
```

返回字典：

```python
{'code': 200, 'message': 'success'}
```

同上；第一次是收藏，第二次是取消收藏。

#### 获取漫画的评论

```python
waziPicAcg.getComicComments("60f5aab6e239c4708507c5d9", "1")

# 第一位参数表示漫画 ID
# 第二位表示评论页码 从 1 数起
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'comments': {
			'docs': [{
				'_id': '612b191cb3a8b0f946b87139',
				'content': '我擦，这玩意真不好说',
				'_user': {
					'_id': '5cf34b93fefcb53c0df2e833',
					'gender': 'm',
					'name': 'loli赛高ovo',
					'title': '萌新',
					'verified': False,
					'exp': 1410,
					'level': 4,
					'characters': [],
					'role': 'member',
					'avatar': {
						'fileServer': 'https://storage1.picacomic.com',
						'path': 'e862029c-efdd-48b4-8c7e-3bac89a15b19.jpg',
						'originalName': 'avatar.jpg'
					},
					'character': 'https://pica-web.wakamoment.tk/images/halloween_m.png'
				},
				'_comic': '60f5aab6e239c4708507c5d9',
				'isTop': False,
				'hide': False,
				'created_at': '2021-08-29T05:20:28.124Z',
				'id': '612b191cb3a8b0f946b87139',
				'likesCount': 1,
				'commentsCount': 0,
				'isLiked': False
			}, ...],
			'total': 68,
			'limit': 20,
			'page': '1',
			'pages': 4
			'topComments': []
		}
	}
}
```

#### 发表对漫画的评论

```python
waziPicAcg.postComicComment("60f5aab6e239c4708507c5d9", "支持")

# 第一位参数表示漫画 ID
# 第二位参数表示评论内容
```

我不清楚会返回什么，我没那个勇气发表高见。

### 排行系

分为四类：日排行榜、周排行榜、月排行榜和骑士榜。

#### 获取日排行榜

```python
waziPicAcg.getH24LeaderBoard()
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'comics': [{
			'_id': '6121d0c0075ed94fbc1ee749',
			'title': '画师Kidmo作品集 2019-2021.03',
			'author': 'Kidmo',
			'totalViews': 3120864,
			'totalLikes': 20953,
			'pagesCount': 2004,
			'epsCount': 74,
			'finished': False,
			'categories': ['全彩', '同人', '生肉', 'NTR', 'CG雜圖', '長篇'],
			'thumb': {
				'fileServer': 'https://storage1.picacomic.com',
				'path': 'tobeimg/VQ_3ksmsIETh5HPN1uIu2Cqo_Vs9fh3SjrT4d_MlWxU/fill/300/400/sm/0/aHR0cHM6Ly9zdG9yYWdlMS5waWNhY29taWMuY29tL3N0YXRpYy9kOWQ2Mjg0ZC0yMmQzLTQxNzctYmViZC1iNGI4N2IwNTE3NWIuanBn.jpg',
				'originalName': 'QQ截图20210819133942_compressed.jpg'
			},
			'viewsCount': 3120864,
			'leaderboardCount': 320876
		}, ...]
	}
}
```

#### 获取周排行榜

```python
waziPicAcg.getD7LeaderBoard()
```

返回格式同上，月排行榜也是。

#### 获取月排行榜

```python
waziPicAcg.getD30LeaderBoard()
```

#### 获取骑士榜

```python
waziPicAcg.knightLeaderBoard()
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'users': [{
			'_id': '593019d53f532059f297efa7',
			'gender': 'm',
			'name': '黎欧',
			'slogan': '二八七六八七八三九二（QQ代传邮箱，请标注来意不然我只能无视了 。来私自要本的还请歇歇吧，我不会提供转售服务。）代传传的，如果急着要上的说一声。',
			'title': '萌新',
			'verified': False,
			'exp': 2585049,
			'level': 161,
			'characters': ['knight'],
			'role': 'knight',
			'avatar': {
				'fileServer': 'https://storage1.picacomic.com',
				'path': 'bad6a292-27e6-49a1-ae87-c29f91f36bd2.jpg',
				'originalName': 'avatar.jpg'
			},
			'comicsUploaded': 17352,
			'character': 'https://pica-web.wakamoment.tk/images/halloween_m.png'
		}, ...]
	}
}
```

### 个人系

#### 登录

```python
waziPicAcg.login("用户名", "密码")
```

返回一串 token。

#### 注册

```python
waziPicAcg.register("pywazi2022", "pywazi2022520", 0, "m", "深空時計", [{"question": "是为了什么而流着血", "answer": "是为了谁而流眼泪"}, {"question": "我躲在夜里取笑着黑", "answer": "因为没有人能杀死鬼"}, {"question": "鬼", "answer": "草东没有派对"}])

# 第一个参数表示用户名，要求符合正则表达式：/^(?!.*\\.\\.)(?!.*\\.$)[^\\W][\\w.]{0,29}$/i
# 第二个参数表示明文账号密码
# 第三个参数表示生日 暂且不清楚是否精确到秒
# 第四个参数表示性别 支持 m（女） f（男） bot（机器人）
# 第五个参数表示昵称
# 第六个参数是一个列表，要求有三个字典，只有 question 和 answer 这两个 key，对应的是三个密保问题
```

成功返回字典：

```python
{'code': 200, 'message': 'success'}
```

#### 签到

```python
waziPicAcg.punchIn()
```

成功返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'res': {'status': 'ok', 'punchInLastDay': '2021-08-04'}}}
```

#### 获取发表过的评论

```python
waziPicAcg.getMyComments(1)

# 第一个参数表示页码，从 1 数起
```

成功返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'comments': {'docs': [], 'total': 0, 'limit': 20, 'page': '1', 'pages': 1}}}
```

#### 获取收藏的漫画

```python
waziPicAcg.getMyFavourites(1, "ld")

# 第一个参数表示页码，从 1 数起
# 第二个参数表示排序方式 似乎只有从新到旧 或者 从旧到新
```

成功返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'comics': {
			'pages': 18,
			'total': 348,
			'docs': [{
				'_id': '59c29060b9cbc06484f4ff35',
				'title': 'JCマニュアル',
				'author': '雪雨こん',
				'pagesCount': 206,
				'epsCount': 1,
				'finished': True,
				'categories': ['長篇', '妹妹系'],
				'thumb': {
					'originalName': 'JC_manual_0000.jpg',
					'path': '7caf8d14-203e-42ef-8897-7e03207ae2be.jpg',
					'fileServer': 'https://storage1.picacomic.com'
				},
				'totalViews': 352693,
				'totalLikes': 5275,
				'likesCount': 5275
			}, ...],
			'page': 1,
			'limit': 20
		}
	}
}
```

#### 获取个人资料

```python
waziPicAcg.getMyProfile()
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'user': {'_id': '5f92f94fa94c02192e0d5c6a', 'birthday': '1999-10-08T00:00:00.000Z', 'email': 'yazawazi520', 'gender': 'f', 'name': '鸭杂袜子', 'slogan': '你所热爱的，就是你的生活。', 'title': '萌新', 'verified': False, 'exp': 720, 'level': 3, 'characters': ['dirty'], 'created_at': '2020-10-23T15:39:59.824Z', 'avatar': {'originalName': 'avatar.jpg', 'path': '1e649daf-9f96-4a8f-9a95-4a77a7f84f00.jpg', 'fileServer': 'https://storage1.picacomic.com'}, 'isPunched': True, 'character': 'https://pica-pica.wikawika.xyz/special/frame-dirty.png?r=3'}}}
```

#### 上传头像

```python
waziPicAcg.uploadAvatar({"type": "file", "path": "./avatar.jpeg"})
waziPicAcg.uploadAvatar({"type": "base64", "format": "jpeg", "data": "qwertyuiopasdfghjklzxcvbnm"})

# 第一种是通过文件上传 type 输入 file path 输入 你的头像文件路径
# 第二种是直接通过 base64 上传 type 输入 base64 format 输入你头像文件的类型 data 输入你头像文件的 base64 值
```

成功了返回：

```python
{'code': 200, 'message': 'success'}
```

#### 重置密码

```python
waziPicAcg.resetPassword("用户名", 1, "答案")

# 第一位参数表示用户名
# 第二位参数表示问题的编号
# 第三位参数表示该问题的答案
```

我测试返回：

```python
{'code': 400, 'error': '1015', 'message': 'invalid request', 'detail': ':('}
```

#### 忘记密码

```python
waziPicAcg.forgotPassword("用户名")

# 第一位参数表示用户名
```

我测试返回：

```python
{'code': 400, 'error': '1015', 'message': 'invalid request', 'detail': ':('}
```

#### 修改密码

```python
waziPicAcg.changePassword("旧密码", "新密码")

# 第一位参数表示你的旧密码
# 第二位参数表示你的新密码
```

成功后返回：

```python
{'code': 200, 'message': 'success'}
```

#### 修改昵称

```python
waziPicAcg.changeDisplayName("用户名", "新昵称")

# 第一位参数表示你的用户名
# 第二位参数表示你的新昵称
```

官方说现在还不能用。

#### 修改签名

```python
waziPicAcg.changeSlogan("新的签名")

# 第一位参数表示你的新签名
```

成功后返回：

```python
{'code': 200, 'message': 'success'}
```

#### 修改问答

```python
waziPicAcg.changeQA([{"q": "第一个问题", "a": "第一个答案"}, {"q": "第二个问题", "a": "第二个答案"}, {"q": "第三个问题", "a": "第三个答案"}])
```

成功后返回：

```python
{'code': 200, 'message': 'success'}
```

### 游戏系

#### 获取游戏

```python
waziPicAcg.getGames(1)

# 第一位参数表示页码，从 1 数起
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'games': {
			'docs': [{
				'_id': '60f6a6cf77a54e70a918f3d4',
				'title': '機甲戰姬',
				'version': '1.0.0',
				'publisher': 'JG Game',
				'suggest': False,
				'adult': False,
				'android': True,
				'ios': False,
				'icon': {
					'originalName': 'gumdam_APP - 250.png',
					'path': '90ac9d84-e8d5-456e-a805-3dce8449dad3.png',
					'fileServer': 'https://storage1.picacomic.com'
				}
			}, {
				'_id': '5ded08947cd2ce4ed0f5e101',
				'title': '真愛の百合は赤く染まる',
				'version': '1.0.0',
				'publisher': 'バグシステム',
				'suggest': False,
				'adult': True,
				'android': True,
				'ios': True,
				'icon': {
					'originalName': '2019-12-09 23.29.05.jpg',
					'path': '260034ca-77b3-458a-99c1-1eb11b3a05a4.jpg',
					'fileServer': 'https://storage1.picacomic.com'
				}
			}, ...],
			'total': 133,
			'limit': 100,
			'page': 1,
			'pages': 2
		}
	}
}
```

#### 获取游戏信息

```python
waziPicAcg.getGameInfo("5ded08947cd2ce4ed0f5e101")

# 第一位参数表示游戏 ID，在 _id 中可见
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'game': {
			'_id': '5ded08947cd2ce4ed0f5e101',
			'title': '真愛の百合は赤く染まる',
			'description': '----------團長特別警告!!----------\n\n純愛大作，厄夜良心推薦。\n親自測試，絕對無雷!\n(๑•̀ᄇ•́)و ✧\n\n物語的主人公「真奈美」最近剛搬到了一個新的小鎮裡，而身為蕾絲的她暗地裡對同班同學的「愛實」抱有著愛意。\n\n一直嘗試隱藏的這份感情卻被對方輕易看穿，而真奈美也從她那聽到了令人驚愕的發言——\n\n「我其實也……喜歡女孩子」\n\n心意相通的兩人很快便確立了關系，然而這份關系卻隨著時間的流逝漸漸變質得不可名狀。「MANAMI」到底能滿足「MANAMI」到什麼程度呢。不久，這份異常的緣分便將她們以外的人們也卷入了事件的漩渦當中，而本應純情的物語也開始大幅度地產生扭曲……\n\n請用zarchiver解壓，用krkr2玩耍。',
			'version': '1.0.0',
			'icon': {
				'originalName': '2019-12-09 23.29.05.jpg',
				'path': '260034ca-77b3-458a-99c1-1eb11b3a05a4.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			},
			'publisher': 'バグシステム',
			'ios': True,
			'iosLinks': ['https://game.eroge.xyz/hhh.php?id=106'],
			'android': True,
			'androidLinks': ['https://game.eroge.xyz/hhh.php?id=106'],
			'adult': True,
			'suggest': False,
			'downloadsCount': 0,
			'screenshots': [{
				'originalName': '2019-12-09 23.29.10.jpg',
				'path': 'ad636f7b-cbbd-474a-81f4-ce1509eda319.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			}, {
				'originalName': '2019-12-09 23.29.14.jpg',
				'path': '11ccbab5-8673-4be6-b1bd-f8f9c5687fa9.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			}, {
				'originalName': '2019-12-09 23.29.18.jpg',
				'path': '36d49e43-36b6-4075-9447-1d7ebe460f6e.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			}, {
				'originalName': '2019-12-09 23.29.22.jpg',
				'path': '142140b8-b5bf-47d7-bc0e-4648c79a9290.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			}, {
				'originalName': '2019-12-09 23.29.25.jpg',
				'path': '8e0d66c7-daf9-4dc6-8479-7492bd2fddfd.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			}, {
				'originalName': '2019-12-09 23.29.29.jpg',
				'path': '33eb34ae-e21e-4c4d-a131-bc4bc14fadb0.jpg',
				'fileServer': 'https://storage1.picacomic.com'
			}],
			'androidSize': 632.23,
			'iosSize': 632.23,
			'updated_at': '2020-06-03T14:27:27.042Z',
			'created_at': '2019-12-08T14:28:36.369Z',
			'likesCount': 8870,
			'isLiked': False,
			'commentsCount': 1291
		}
	}
}
```

#### 喜欢/取消喜欢这个游戏

```python
waziPicAcg.likeOrUnLikeGame("5ded08947cd2ce4ed0f5e101")

# 第一位参数表示游戏 ID
```

同漫画喜欢：第一次是喜欢，第二次是取消喜欢，返回内容不再赘述。

#### 获取游戏的评论

```python
waziPicAcg.getGameComments("5ded08947cd2ce4ed0f5e101", "1")

# 第一位参数表示游戏 ID
# 第二位参数表示评论区分页，从 1 数起
```

同漫画的获取评论一致，返回内容不再赘述。

#### 发表对这个游戏的评论

```python
waziPicAcg.postGameComment("5ded08947cd2ce4ed0f5e101", "非常支持")

# 第一位参数表示游戏 ID
# 第二位参数表示评论内容
```

我说白了，我不敢评论，不敢测试，你们自己试试看。

### 评论系

#### 喜欢/取消喜欢评论

```python
waziPicAcg.likeOrUnLikeComment("612b191cb3a8b0f946b87139")

# 第一位参数表示评论 ID
```

我不敢测试，你们测试吧（逃）

#### 隐藏/取消隐藏评论

```python
waziPicAcg.hideOrUnHideComment("612b191cb3a8b0f946b87139")

# 第一位参数表示评论 ID
```

我没有权限，返回 1005。

#### 获取评论的子评论

```python
waziPicAcg.getCommentsChildren("60fc1228af308a2d7d7c2991")

# 第一位参数表示评论 ID
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'comments': {'docs': [{'_id': '60feee91b2ce8a24cbed7cae', 'content': '天…天堂…', '_user': {'_id': '5d048a078297f2110498899c', 'gender': 'f', 'name': 'Blue Pink', 'title': '萌新', 'verified': False, 'exp': 1640, 'level': 4, 'characters': [], 'role': 'member', 'avatar': {'originalName': 'avatar.jpg', 'path': '77b6f4c6-3681-4332-9ef2-ecd6cd15b598.jpg', 'fileServer': 'https://storage1.picacomic.com'}, 'slogan': '1', 'character': 'https://pica-web.wakamoment.tk/images/halloween_f.png'}, '_parent': '60fc1228af308a2d7d7c2991', '_comic': '60f5aab6e239c4708507c5d9', 'isTop': False, 'hide': False, 'created_at': '2021-07-26T17:19:13.003Z', 'id': '60feee91b2ce8a24cbed7cae', 'likesCount': 4, 'isLiked': False}, {'_id': '60fd1d70eacb85326231bf73', 'content': '有就怪了', '_user': {'_id': '5b744884d179b4579b3c5b22', 'gender': 'm', 'name': '离殇ボ', 'title': '萌新', 'verified': False, 'exp': 590, 'level': 2, 'characters': [], 'role': 'member', 'avatar': {'fileServer': 'https://storage1.picacomic.com', 'path': '3d3f9619-a386-4a46-9ca7-49fe8db8b4cd.jpg', 'originalName': 'avatar.jpg'}, 'slogan': 'null', 'character': 'https://pica-web.wakamoment.tk/images/halloween_m.png'}, '_parent': '60fc1228af308a2d7d7c2991', '_comic': '60f5aab6e239c4708507c5d9', 'isTop': False, 'hide': False, 'created_at': '2021-07-25T08:14:40.035Z', 'id': '60fd1d70eacb85326231bf73', 'likesCount': 0, 'isLiked': False}], 'total': 2, 'limit': 5, 'page': '1', 'pages': 1}}}
```

#### 回复评论

```python
waziPicAcg.replyComment("60fc1228af308a2d7d7c2991", "真的会有吗")

# 第一位参数表示评论 ID
# 第二位参数表示评论内容
```

我不敢测试，你们测试吧。

#### 举报评论

```python
waziPicAcg.reportComment("60fc1228af308a2d7d7c2991")

# 第一位参数表示评论 ID
```

我不敢测试，你们测试吧。

#### 置顶评论

```python
waziPicAcg.topComment("60fc1228af308a2d7d7c2991")

# 第一位参数表示评论 ID
```

可能返回 1005。

### 管理系

#### 设置称号

```python
waziPicAcg.setTitle("5f92f94fa94c02192e0d5c6a", "awa")

# 第一位参数表示用户 ID
# 第二位参数表示称号名
```

我测试返回：

```python
{'code': 400, 'error': '1015', 'message': 'invalid request', 'detail': ':('}
```

#### 修改经验值

```python
waziPicAcg.adjustExp("5f92f94fa94c02192e0d5c6a", 7200)

# 第一位参数表示用户 ID
# 第二位参数表示经验值
```

我测试返回：

```python
{'code': 404, 'error': '1007', 'message': 'not found', 'detail': ':('}
```

#### 移除用户评论

```python
waziPicAcg.removeComment("5f92f94fa94c02192e0d5c6a")

# 第一位参数表示用户 ID
```

我测试返回：

```python
{'code': 401, 'error': '1007', 'message': 'not found', 'detail': ':('}
```

#### 封禁用户

```python
waziPicAcg.blockUser("5f92f94fa94c02192e0d5c6a")

# 第一位参数表示用户 ID
```

我测试返回：

```python
{'code': 404, 'error': '1007', 'message': 'not found', 'detail': ':('}
```

#### getUserDirty

```python
waziPicAcg.getUserDirty("5f92f94fa94c02192e0d5c6a")

# 第一位参数表示用户 ID
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'dirty': False}}
```

#### 获取用户个人资料

```python
waziPicAcg.getUserProfile("5f92f94fa94c02192e0d5c6a")

# 第一位参数表示用户 ID
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'user': {'_id': '5f92f94fa94c02192e0d5c6a', 'gender': 'f', 'name': '鸭杂袜子', 'slogan': '你所热爱的，就是你的生活。', 'title': '萌新', 'verified': False, 'exp': 720, 'level': 3, 'avatar': {'originalName': 'avatar.jpg', 'path': '1e649daf-9f96-4a8f-9a95-4a77a7f84f00.jpg', 'fileServer': 'https://storage1.picacomic.com'}}}}
```

### 下载系

#### 下载封面

```python
waziPicAcg.getThumbImage("60f5aab6e239c4708507c5d9", "./")

# 第一位参数表示漫画 ID
# 第二位参数表示下载路径
```

返回字符串：

```python
'./ホクロ流星群せかんど [中国翻訳] [DL版]\\thumb_QQ图片20210718224515.png'
```

#### 下载漫画

```python
waziPicAcg.downloadComic("60f5aab6e239c4708507c5d9", "./")

# 第一位参数表示漫画 ID
# 第二位参数表示下载路径
```

完事后返回 `Done! / 完工！` 。

### 程序系

#### 获取聊天室

```python
waziPicAcg.getChat()
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'chatList': [{'title': '嗶咔大眾澡堂', 'description': '這是一個讓大家討論本子和二次元的地方，開二次元車是歡迎的，同時歡迎成人話題討論，但請低調！', 'url': 'https://chat-public.wikawika.xyz', 'avatar': 'https://pica-pica.wikawika.xyz/images/chat-public.jpg'}, {'title': '嗶咔養老組織群', 'description': '歡迎各位過氣的官方、管理和熟人到這群交流養老心得。如果你被嗶咔服務器君打壓也歡迎你到這訴苦', 'url': 'https://chat-old.wikawika.xyz', 'avatar': 'https://pica-pica.wikawika.xyz/images/chat-old.jpg'}]}}
```

#### 获取小程序

```python
waziPicAcg.getAPPs()
```

返回字典：

```python
{'code': 200, 'message': 'success', 'data': {'apps': [{'title': '嗶咔包養', 'url': 'https://donate.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/support-app.jpg', 'showTitleBar': False, 'description': '透過 BitCoin 支援嗶咔 漫畫'}, {'title': '嗶咔商店', 'url': 'https://online-shop-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-shop.jpg', 'showTitleBar': False, 'description': '嗶咔商店，買買買!'}, {'title': '嗶咔鍋貼', 'url': 'https://post-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-post.jpg', 'showTitleBar': False, 'description': '嗶咔鍋貼，一起讓騎士們分享生活和快樂的地方'}, {'title': '嗶咔運動', 'url': 'https://move-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-move.jpg', 'showTitleBar': False, 'description': '嗶咔運動， 圖動起來'}, {'title': '嗶咔公會', 'url': 'https://group.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/group-app.jpg', 'showTitleBar': False, 'description': '嗶咔公會一個嶄新的社交小程序'}, {'title': '嗶咔小電視 beta', 'url': 'https://tv.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/tv-app.jpg', 'showTitleBar': True, 'description': '精彩影片不斷放送，不支援 iOS'}, {'title': '嗶咔小電影', 'url': 'https://av.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/movie-app.jpg', 'showTitleBar': False, 'description': '精彩小電影讓你看到飽嗎？！'}, {'title': ' 嗶咔小里番', 'url': 'https://h.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/h-app.jpg', 'showTitleBar': False, 'description': '里番之家'}, {'title': '嗶咔小黃油', 'url': 'https://game.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/game-app.jpg', 'showTitleBar': False, 'description': '電腦小黃油介紹'}, {'title': '嗶咔小禮物', 'url': 'https://gift-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-gift.jpg', 'showTitleBar': False, 'description': '福利盡在嗶咔小禮物'}, {'title': '嗶咔畫廊', 'url': 'https://paint-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-paint.jpg', 'showTitleBar': False, 'description': '由著名畫帥繪畫的嗶咔 相關作品'}]}}
```

#### 获取安卓程序

```python
waziPicAcg.getAndroidAPPs(1)

# 第一位参数表示页码，从 1 数起
```

返回字典：

```python
{
	'code': 200,
	'message': 'success',
	'data': {
		'applications': {
			'docs': [{
				'_id': '5dc58b151e103c60e7663b12',
				'downloadUrl': 'https://download.wikawika.xyz/apps/2.2.1.3.3.4_collections.apk',
				'updateContent': '【一般更新】\n\n1・新增漫畫推薦欄\n\n2・修改部份版本閃退問題\n\n後備下載連結\nhttps://download.wikawika.xyz/apps/2.2.1.3.3.4_collections.apk',
				'version': '2.2.1.3.3.4',
				'created_at': '2019-11-08T15:34:45.163Z',
				'apk': {
					'originalName': '2.2.1.3.3.4_collections.apk',
					'path': '4da05b12-3534-4b4d-b9bf-804de301d2e0.apk',
					'fileServer': 'https://storage1.picacomic.com'
				}
			}, ...],
			'total': 30,
			'limit': 20,
			'page': 1,
			'pages': 2
		},
		'apiLevel': 22,
		'minApiLevel': 22
	}
}
```

# PyWazi 高级文档

如果你需要开发 `PyWazi` 想要查找更多的细节，我的建议是阅读代码，因为我是条懒狗。

你会发现我的日志相当于一个屁话特多的注释，你一定能阅读的懂的，信我，如果还是不行，请发起个 issue 我会帮助你的。

我实在是没有精力去写一份事无巨细的开发文档了。
