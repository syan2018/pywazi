# PyWazi 文档

*哈哈哈哈哈哈哈哈，思考使人沉醉，而文档不会，描写什么东西呢？太阳为了你绘制一个一个一个童话般的梦，随着生机勃勃的春天伸出……*

咳咳，这是一份正经的文档，而不是什么后现代文学作品，请跟紧鸭鸭的脚步，让我们一起走进这个世界吧！

## PyWazi 是什么？

*它是上帝，是不够格的上帝，因为全能自恋，哈哈哈哈哈哈哈哈哈口合~*

一个收集信息的模块，是一个支持以下网址的爬虫：

+ [AsianSister](https://asiansister.com/)
+ [Danbooru](https://danbooru.donmai.us/) *等一系列基于 Danbooru 的网站 (API 相近)*
+ [ExHentai](https://exhentai.org/)
+ [JavBus](https://javbus.com/)
+ [PicAcg](https://picacomic.xyz/)

使用 Python3 实现，事实上，它的前身只是我失眠的时候花了一晚上做出来的东西，所以，why so serious？*它是一个简单的爬虫，只是为了收集信息而已，没有什么特别的功能，只是为了收集信息而已。*

## PyWazi 支持的网站还会增加吗？

*我把人对终极价值的思考和自我的解构后的行为再解析全部写进一本厚厚的书，我叫它《精神病学》。*

当然，但是不是现在，作者需要生活，我会随着心情进行创作。

## PyWazi 速度好慢，代码好拖沓，怎么办？

*呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃...*

1. 很抱歉，请等待我的*下一个版本*，我会*改进*的；
2. 请提交 Pull Request，我会*审阅*的；
3. 如果你有什么好的建议，请在 GitHub 上提交 Issue，我会*及时回复*的；
4. *放弃使用* PyWazi，请*自行创造*一个*神明*，我会*支持*的。

## 测试环境

*物理上面应该是一些无机物和有机物之类的东西吧，我也不知道。*

> Windows 11 - Python 3.9.6
>
> beautifulsoup4 4.9.3
> certifi 2021.5.30
> lxml 4.6.3
> urllib3 1.26.6

## 更新内容

*像创造艺术品那样增加一些破坏美感的东西，真是糟透了，就像这样，好き...*

1. 我*忘*了，呃呃呃呃，*对不起*；
2. 对于 `AsianSister` 的支持，使我感到极端地幸福，*我*也是这样的；
3. 对于 `Danbooru` 的支持，使我感到极端地幸福，*我*也是这样的；
4. 对于 `ExHentai` 的支持，使我感到极端地幸福，*我*也是这样的；
5. 对于 `JavBus` 的支持，使我感到极端地幸福，*我*也是这样的；
6. 对于 `PicAcg` 的支持，使我感到极端地幸福，*我*也是这样的；
7. 对于 `PyWazi` 的支持，使我感到极端地幸福，*我*也是这样的；
8. 对于 `Python` 的支持，使我感到极端地幸福，*我*也是这样的；
9. 呃呃呃呃，*对不起*，Copilot 的自动补全像磕了药一样。

# 开始开发 PyWazi 吧！

*因为踏上旅途的艰辛和不尽人意，所以我选择随波逐流...*

很抱歉，前面都是废话，接下来也是，我对我的文档风格感到非常抱歉，这不是一个非常好的开发文档，我只是在进行一场面向互联网的拙劣的行为艺术，如果你真的需要开发 PyWazi 请：

1. *阅读旧版本*的*开发文档*；
2. 尝试*阅读我*的*代码*；
3. 尝试*阅读我*的*示例*；
4. 继续进行*阅读*，尽管非常困难，但是*我*会一直阅读的；
5. 呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃，怎么就双重人格了呢？

## 导入 PyWazi

*我需要工具，我需要使用木头，木头是工具。*

使用这行代码导入所有内容：

```python
from pywazi import *
```

如果只想导入部分则：

```python
from pywazi import waziXXXX, waziXXXX
```

目前存在以下站点模块：

* waziJavBus - 帮助获取 JavBus 番号磁力链接以及信息的模块。
* waziPicAcg - 涵盖了大部分 PicAcg 功能（除去聊天、程序的具体功能）的模块。
* waziDanbooru - 获取或下载 Danbooru 类型网站的图片和标签。
* waziExHentai - 涵盖了大部分 ExHentai 功能（除去给予评分、发送评论等功能）的模块。
* waziAsianSister - 收集 AsianSister 中画廊和视频的信息。

导入时自动读取目录下的 config.json 作为默认配置。

### 高级导入

*一切都指向了，因为自定义选项的臃肿，我喜欢。*

以下为高级导入教程，以方便用户和*我*导入自己所需要的或需要开发的模块。

#### 对于站点的导入

*我和**我**还有个 AI，至少有个肯定磕了点东西...*

```python
from sites.wazi站点名 import wazi站点名 [as xxx]
```

并且实例化它：

```python
aaa = xxx()
```

接着你就可以通过 aaa 来访问该站点模块的所有接口了。

#### 对于基础模块的导入

*这跟棍子非常丑陋，但是世界基于这跟棍子，而不是基于一个好看的棍子。*

如果你仅需要使用 `pywazi` 中的 `waziRequest` 等模块来开发自己的项目，那么可以这么做。以下我给出几个最好不使用我基础模块的理由：

1. 这些基础模块具有仅针对我程序的局限性，如果需要在你的程序中使用请修改相关内容或格式；
2. `waziRequest` 基础模块使用的是 `urllib3` ，这是一个简单但繁琐的模块以处理用户参数并发动网络请求的模块，它的逻辑我看一次忘一次，如果你只是需要网络请求为何不试试同样基于 `urllib3` 的 `requests`；
3. *我*觉得*她们*丑陋至*极*，显得*非常可爱*，所以我*不*建议你使用*她们*。

导入：

```python
from mods.wazi基础模块名 import wazi基础模块名 [as xxx]
```

同样，你需要实例化它。

#### 对于实例化模块的导入

*躯壳，复制了一百一千一万份，灵魂，依旧是那样的，唯一的，美丽，好棒。*

以下是我的建议：

1. 如果你需要使用 PyWazi，你应该修改或导入 `pywazi` 主模块，并通过主模块允许的接口以操控实例化模块；
2. 如果你开发 PyWazi，那么你可以导入实例化模块以控制配置，日志和其他内容以及*我*。

导入：

```python
from ins.wazi实例化模块名 import wazi实例化模块名
```

## 主模块教程

*为什么，呃呃呃，我考虑一切的都在 __init__ 中，像火焰一样灼烧着，谁的懦弱。*

主模块存在两个函数，以用于读取配置并设置，还有两个变量（请阅读*我*的代码）。

### 全局配置

*强迫症（obsessive-compulsive disorder, OCD）是一种以反复出现的强迫观念、强迫冲动或强迫行为等为主要临床表现的精神疾病。*

使用 `globalParams` 以读取全局配置，会给所有模块传入同样的 `giveParams` 函数。

```python
from pywazi import *

globalParams("./config.json") # 你的 JSON 文件目录
```

json 应该是类似 `params` 的以下内容：

```python
{
    "useProxies": true,
    ...
}
```

### 读取配置

*对立违抗障碍和品行障碍属于破坏性行为和反社会性行为障碍，以持续的行为问题为特点。*

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

在导入 `pywazi` 的时候会默认尝试 `defConfig` 当前目录下的 `config.json`。*如果没有的话，他要吃掉你。*

## 实例化模块教程

*如何使用这些躯壳是我们天生就能掌握的技能，所以我决定不写入教科书以确保保守派对我的支持和赞美。*

<!--
1. 创建一个新的模块，继承 `pywazi.Module` 类；
2. 在 `__init__` 中调用 `super().__init__()`；
3. 在 `__init__` 中调用 `self.setName(name)`；
4. 在 `__init__` 中调用 `self.setParams(params)`；
5. 在 `__init__` 中调用 `self.setConfig(config)`；
6. 在 `__init__` 中调用 `self.setLogger(logger)`；
7. 在 `__init__` 中调用 `self.setSession(session)`；
8. 在 `__init__` 中调用 `self.setProxy(proxy)`；
9. 在 `__init__` 中调用 `self.setSession(session)`；
10. 在 `__init__` 中调用 `self.setProxy(proxy)`；
11. 在 `__init__` 中调用 `self.setSession(session)`；
12. 在 `__init__` 中调用 `self.setProxy(proxy)`；
13. 在 `__init__` 中调用 `self.setSession(session)`；
14. 在 `__init__` 中调用 `self.setProxy(proxy)`；
15. 关掉工作，调用 `self.close()`；
16. 在 `yourSelf.room.bed` 中调用 `yourSelf.addModule(yourSelf)`；
17. 呃呃呃呃，试着 `yourSelf.goToBed()`；
18. 呃呃呃呃，试着 `yourSelf.wakeUp()`；
19. 呃呃呃呃，试着 `yourSelf.goToBed()`；
20. 呃呃呃呃，试着 `yourSelf.wakeUp()`；
21. 呃呃呃呃，试着 `yourSelf.takeDrugs("XXX", 1000mg)`；
22. 呃呃呃呃，等待有人来收尸；
23. 在 `__init__` 中不要调用 `self.sleep()`；
24. 在 `__init__` 中不要调用 `self.wakeUp()`；
25. 在 `__init__` 中不要调用 `self.takeDrugs()`；
26. 在 `__init__` 中不要调用 `self.addModule()`；
27. 在 `__init__` 中不要调用 `self.removeModule()`；
28. 在 `__init__` 中不要调用 `self.setName()`；
29. 在 `__init__` 中不要调用 `self.setParams()`；
30. 在 `__init__` 中不要调用 `self.setConfig()`；
31. 在 `__init__` 中不要调用 `self.setLogger()`；
32. 在 `__init__` 中不要调用 `self.setSession()`；
33. 在 `__init__` 中不要调用 `self.setProxy()`；
34. 在 `__init__` 中不要调用 `self.setSession()`；
35. 在 `__init__` 中不要调用 `self.setProxy()`；
36. 在 `__init__` 中不要调用 `self.setSession()`；
37. 在 `__init__` 中不要自动补全代码；
38. 呃呃呃呃呃，我在说什么胡话。
-->

请不要阅读 \<!-- --> 中的内容，*我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*只是为了让你们更好地理解我的代码。真的吗？真的吗？  *我*

1. `waziInsConfig` 是用于管理配置、读取配置文件的实例化模块，它的灵魂位于基础模块中的 `waziLog`，阅读它的资料以获取详细帮助；
2. `waziInsLog` 是用于日志记录的实例化模块，它的灵魂位于基础模块中的 `waziLog`，阅读它的资料以获取详细帮助；
3. `waziIns*` 是用于 * 的实例化模块，它没有灵魂，等待*我们*的指示。

## 基础模块教程

*这些人的后裔，将各国的地土，海岛，分开居住，各随各的方言，宗族立国。——大概就是创世纪的第十章第五节*

存在以下基础模块：

1. `waziCheck` - 单独的校验和密码系统，针对 ExHentai 的搜索和 PicAcg 的加解密处理；
2. `waziColor` - 颜色处理系统，针对于支持 256 色控制台的格式化输出；
3. `waziConfig` - 配置文件管理系统，针对于配置文件的读取和保存；
4. `waziFileName` - 文件名检查系统，以帮助避免文件名不合法；
5. `waziFun` - 用于获取函数名；
6. `waziLog` - 日志记录系统，针对于日志记录；
7. `waziRequest` - 用于请求网页的系统，使用 `urllib3` 模块；
8. `waziURL` - 用于组合 URL 地址，以帮助 URL 参数的合成。

神明需要分工合作来创造世界，我也不例外，黑暗漫漫路迢迢...

### waziCheck

*Cryptography is the art and science of encrypting and decrypting data.*

**waziCheck** 中包含了一些关于宇宙的秘密，以及一些关于程式的秘密。

#### 相关变量

*一切的变量都是常量，我觉得可以这么说，大概吧，或许，额，我应该睡觉了。*

1. `self.sha1` 是 `waziCheck` 的唯一实例，它是一个 `hashlib.sha1` 实例，用于对字符串进行 SHA1 加密；
2. `self.tags` 是一个列表，用于存储所有的 ExHentai 分类；
3. `self.tagsNumber` 是一个字典，用于存储所有的 ExHentai 分类所对应的数值；
4. `self.ratingPos` 是一个字典，用于储存所有的 ExHentai 评分 CSS 样式所对应的评分数值；
5. `self.name` 储存着 `waziCheck` 的名字，默认为 `waziCheck`。

#### returnHasTorrents

*一种流水线工作需要，所以呃呃，就业，算了。*

这是一个函数，需要有提供两个参数：`self` 和 `soup`，其中 `self` 是 `waziCheck` 的实例，`soup` 是需要检查的 Soup。最后一定返回 `True` 或者 `False`。

它的逻辑是：检查是否存在 `src` 属性，如果存在，则继续检查，如果内容是 `https://exhentai.org/img/t.png` 返回 `True`，否则返回 `False`；如果不存在，则返回 `False` 并提示相关错误。

你可以在 `waziExHentai` 中找到 `returnHasTorrents` 的相关代码：

```python
"hasTorrents": self.check.returnHasTorrents(soup.find(class_ = "gl6m").find("img")),
```
> waziExHentai.py: line 232

它检查该元素（即 img 元素）的 `src` 属性，因为互联网静态资源存储时间长，不易改变，所以可以直接检查。

#### returnRatingNum

*一一对应，啊，对称加密算法，嗯嗯嗯嗯嗯嗯讷讷讷讷恩*

这是一个函数（当然），也是一个接口（当然），也是通往 `waziCheck` 的一个秘密（当然）。你需要提供两个参数：`self` 和 `pos`，其中 `self` 是 `waziCheck` 的实例，`pos` 是位移字符串。最后一定返回一个东西（当然）。

它的逻辑是，直接访问 `self.ratingPos[pos]` 中的数据并返回，如果不存在则返回错误信息。

同样的，你可以在 `waziExHentai` 中找到 `returnRatingNum` 的相关代码：

```python
ratingNum = self.check.returnRatingNum(
    soup.find(class_ = "ir").attrs["style"].split("background-position:")[1].split(";")[0]
)
```
> waziExHentai.py: line 192 - 194

*真是天才般的想法...*

#### getFileSHA1

*我询问世界上是否存在一模一样的东西，估计是肯定的，肯定被估计了，所以一定存在，大概吧，呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃*

这是一个函数，需要提供两个参数：`self` 和 `path`，其中 `self` 是 `waziCheck` 的实例，`path` 是文件的路径。最后一定返回一个东西（当然）。

`path` 可以是相对的，也可以是绝对的，但是必须是对的。我从互联网上*剽窃*了与之相关的代码，因为分块读取的原因，我没有注明源码取自，呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃。

如果*我*无法打开，总之就会返回空字符串，*我*打开之后我会尝试进行解码，如果解码失败，*我*会返回致命信息。

请阅读 `waziExHentai` 相关内容：

```python
sha1 = self.check.getFileSHA1(params["path"])
```
> waziExHentai.py: line 674

*就是这样...*

#### getSources

*位运算还有不及格的数学，呀哈哈，世界在雨中融化，所以我直接从 ehg_index.c.js 中获取相关信息。*

一个函数，提供两个参数：`self` 和 `params`，其中 `self` 是 `waziCheck` 的实例，`params` 是一个字典，包含了 `tags` （其实是分类）的参数。最后一定返回一个东西（当然）。

原始代码：

```javascript
// Form: https://exhentai.org/z/0352/ehg_index.c.js
// I do not know this code's license, but I think it's private.
// So I do not know how to use it, but I think it's safe to use it in here.
// But think about it, I'm using the relevant technology to get pirated resources on the Internet.
// What exactly do the administrators and developers of these resource sharing sites think of the existence of people like me?
// And what do they think of my use of their code?

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

请阅读相关代码：

```python
queryParams = {
    "f_cats": str(self.check.getSources(params))
}
```

> waziExHentai.py: line 605 - 607

#### signature

*签名，信任机制，信任我吧，我只是一只鼠鼠，呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃*

**你要找的密钥不在这里**

它的参数列表：`self, url, times, method, baseURL, uuids, apiKey, secretKey`。

`self` 是 `waziCheck` 的实例，`url` 是要签名的 url，`times` 是时间戳，`method` 是请求方法，`baseURL` 是基础 url，`uuids` 是 uuid，`apiKey` 是 apiKey，`secretKey` 是密钥。

最终返回字符串。

#### construct

*没有多么省事的方法，只是像酒一样的慰藉，哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈*

跟 `signature` 相比丢掉了 `times`。

请阅读相关代码：

```python
sig = self.check.construct(url, method, self.info["baseUrl"], self.info["uuid"], self.info["apiKey"],
                           self.info["secretKey"])
```
> waziPicAcg.py: line 128 - 129

#### needFilterIt

*审查制度和信息过滤，少冲浪上网，多阅读报纸，呃呃呃，当我没说。*

需要三个参数：`self, backJson, filters`。

`self` 是 `waziCheck` 的实例，`backJson` 是需要过滤的数据，`filters` 是过滤器。

*我要燃烧整个数据*，它的逻辑是：检查该数据的标签是否为 `filters` 中的标签，存在一个标签符合即可直接被*过滤*，就像*尸体*可以直接被放进*垃圾桶*一样。

在 `waziPicAcg.py` 中，你可以见到：

```python
def filterIt(self, backJson, filters):
    fuName = waziFun.getFuncName()
    waziLog.log("debug", f"({self.name}.{fuName}) 收到需要过滤的内容和过滤标签，正在通过 needFilterIt 完成过滤。")
    returnJson = backJson
    returnJson["data"]["comics"]["docs"] = self.check.needFilterIt(backJson["data"]["comics"]["docs"], filters)
    waziLog.log("info", f"({self.name}.{fuName}) 过滤完成： {returnJson}")
    return returnJson
```

*丑陋！*

*躯体变形障碍（body dysmorphic disorder, BDD）是指身体外表并无缺陷或仅是轻微缺陷，但患者却总认为自己存在缺陷，或过分夸大其轻微缺陷，觉得自己丑陋不堪或令人厌恶，且已引起他人注意，为此而苦恼的一种精神疾病。*

### waziColor

*我是彩虹色的，我爱你，我是美少女，呃呃呃呃，白色过膝袜和短裙，呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃*

RGB 是一个三位数，每一位代表一个颜色，比如：0，0，0 是黑色。十六进制颜色值是：#000000。

#### HexToRGB

*只是一个数学操作...*

静态，静态，需要三个参数，`R`, `G`, `B`。最后返回字典：

```python
{"R": XXX, "G": XXX, "B": XXX}
```

例如：0xff, 0xe9, 0x00 -> {"R": 255, "G": 233, "B": 0}

#### print

*打印世界的大小，也没有多少，最多一张 A4 纸的长 × 宽。*

是一个静态方式，需要一个参数 `jsons` 其实是字典。

它的格式如下：

```python
{
	"color": {
		"R": 255,
		"G": 233,
		"B": 0
	},
	"bgColor": {
		"R": 255,
		"G": 233,
		"B": 0
	},
	"effects": {
		"normal": True,
		"highLight": True,
	}
}
```