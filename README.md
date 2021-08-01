# PyWazi
针对 ExHentai, JavBus, Danbooru, PicAcg 的一个数据采集和处理、操作模块。

目前版本是 1.0.0，已经完成了大部分内容。并完成了 Danbooru, JavBus, ExHentai（部分） 的测试，因为 PicAcg 我的移动网络不允许，挂梯子也不行，所以还未测试。年底之前（草）我会把开发文档（中英文双版）整出来，优化和功能增加会在以后完成。

## 开发文档
详见 doc.md

## TODO
1. 想办法测试 picacg
2. 写中英文版的文档

## 针对 Danbooru 的功能
1. Posts 时间线
    1. 获取 Posts 时间线
    2. 下载 Posts 时间线

## 针对 JavBus 的功能
1. 搜索番号磁链

## 针对 ExHentai 的功能
1. Cookies 登录
2. 浏览
    1. 普通模式（可能展示不全或经过设置）
    2. 全部模式（无视设置并允许其他内容）
3. 搜索
    1. 普通模式
    2. 全部模式
    3. 标签模式
    4. 上传者模式
    5. 上传者全部模式
    6. 高级模式
    7. 图片模式
    8. 自定义模式
4. 信息获取
    1. 种子信息
    2. 基础信息
        1. 通过网页端的模式
        2. 通过 API 接口
    3. 评论内容
    4. 手动翻页次数
5. 图片
    1. 缩略图
        1. Large 模式
        2. Normal 模式
    2. 列出下载地址或进行下载
        1. 普通模式
        2. （MPV 权限用户限定）API MPV 下载
    3. 压缩包
        1. H@H 下载（不清楚，看代码）
        2. 列出原图压缩包下载地址或直接下载
        3. 列出普通画质压缩包下载地址或直接下载

## 针对 PicAcg 的功能（未测试）
1. 登录
2. 获取分区
3. 搜索
    1. 只允许关键字模式（或许是分区，未测试）
    2. 可排序模式
    3. 高级搜索
4. 漫画
    1. 基本信息
    2. 分页
    3. 分页内容
    4. 针对该本漫画的推荐
    5. 喜欢或取消喜欢
    6. 收藏或取消收藏
    7. 获取评论
    8. 进行评论（或许能在游戏区能用同样的）
5. 获取热词
6. 个人
    1. 评论
    2. 收藏
    3. 个人信息
    4. 签到
7. 游戏
    1. 游戏列表
    2. 游戏信息
8. 其它
    1. 获取单独的图片地址
