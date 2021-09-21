# PyWazi Development Documentation

>Yazawazi, 2021

## Test Environment

Windows 11 - Python 3.9.6

- beautifulsoup4 4.9.3
- certifi 2021.5.30
- lxml 4.6.3
- urllib3 1.26.6

## Start

### Import PyWazi

Use this line of code to import all content:

```python
from pywazi import *
```

If you want to import only a part then:

```python
from pywazi import waziXXXX, waziXXXX
```

The following modules currently exist：

1. `waziJavBus` - A module that helps to get JavBus number magnet links.
2. `waziPicAcg` - A module that covers most of the PicAcg features (excluding chat, program specific features).
3. `waziDanbooru` - Get or download images from Danbooru type sites.
4. `waziExHentai` - A module that covers most of the ExHentai features (excluding the ability to give ratings, send comments, etc.).

## waziDanbooru Tutorial

Danbooru is an open source gallery display system, and it is open Api, the more widely known ones are: https://yande.re/ https://konochan.com/ and so on.
However, various Danbooru type sites have different Api return formats, I just based on Yande and Konochan, still not clear about the adaptability of other sites using Danbooru.

### Configuration

```python
from pywazi import waziDanbooru as Wdb

Wdb.giveParams({
    "useProxies": True,  # Whether to use a proxy
    "proxyAddress": "127.0.0.1",  # HTTPS / HTTP proxy address
    "proxyPort": "7890",  # HTTPS / HTTP proxy port
    "useHeaders": False,  # Whether to use custom header (not recommended to fill in, the program automatically set)
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.164 Safari/537.36"
    }  # Custom head content (not recommended to fill in, the program automatically set, fill in their own may lead to part of the module error)
})

Wdb.setApi("https://yande.re")  # Set up the Danbooru website
```

### Post Time Line

The access interface is：`URL/post.json`（Of course it can be `URL/post.xml`）Different sites have different return formats, but they are generally consistent.

#### Get

```python
Wdb.getPosts(0, "", 40)

# The first parameter indicates the page number, counting from 0
# The second parameter indicates the tags, only English characters are allowed, if there is no tag then use the empty string instead, multiple tags please use "+" inside the quotation marks to connect
# The third parameter indicates the number of limits per page, normally enter 40
```

Return List:

```python
[{
	'id': 823891,
	'tags': 'bikini erect_nipples swimsuits tomozero wet',
	'created_at': 1627717072,
	'updated_at': 1627717074,
	'creator_id': 225185,
	'approver_id': None,
	'author': 'hiroimo2',
	'change': 4291445,
	'source': 'https://i.pximg.net/img-original/img/2021/07/31/16/20/09/91622368_p0.jpg',
	'score': 0,
	'md5': 'c38d6a2e109414510d02bd963c66c970',
	'file_size': 1823848,
	'file_ext': 'jpg',
	'file_url': 'https://files.yande.re/image/c38d6a2e109414510d02bd963c66c970/yande.re%20823891%20bikini%20erect_nipples%20swimsuits%20tomozero%20wet.jpg',
	'is_shown_in_index': True,
	'preview_url': 'https://assets.yande.re/data/preview/c3/8d/c38d6a2e109414510d02bd963c66c970.jpg',
	'preview_width': 84,
	'preview_height': 150,
	'actual_preview_width': 169,
	'actual_preview_height': 300,
	'sample_url': 'https://files.yande.re/sample/c38d6a2e109414510d02bd963c66c970/yande.re%20823891%20sample%20bikini%20erect_nipples%20swimsuits%20tomozero%20wet.jpg',
	'sample_width': 844,
	'sample_height': 1500,
	'sample_file_size': 226287,
	'jpeg_url': 'https://files.yande.re/image/c38d6a2e109414510d02bd963c66c970/yande.re%20823891%20bikini%20erect_nipples%20swimsuits%20tomozero%20wet.jpg',
	'jpeg_width': 1000,
	'jpeg_height': 1777,
	'jpeg_file_size': 0,
	'rating': 'q',
	'is_rating_locked': False,
	'has_children': True,
	'parent_id': None,
	'status': 'pending',
	'is_pending': False,
	'width': 1000,
	'height': 1777,
	'is_held': False,
	'frames_pending_string': '',
	'frames_pending': [],
	'frames_string': '',
	'frames': [],
	'is_note_locked': False,
	'last_noted_at': 0,
	'last_commented_at': 0,
	'flag_detail': {
		'post_id': 823891,
		'reason': 'low-res',
		'created_at': '2021-07-31T07:37:52.765Z',
		'user_id': None,
		'flagged_by': 'system'
	}
}, ...]
```

Because of space constraints and the inconsistent JSON format returned by various Danbooru sites, I cannot explain it in detail.

#### Download

```python
Wdb.downloadPosts(0, "", 40, "./")

# The first parameter indicates the page number, counting from 0

# The second parameter indicates the tags, only English characters are allowed, if there is no tag then use the empty string instead, multiple tags please use "+" inside the quotation marks to connect

# The third parameter indicates the number of limits per page, please enter 40 for normal

# The fourth parameter indicates the download path, which can be relative or absolute
```

Download is not optimized, if you have multi-threaded needs can be viewed: [cloudwindy/yander: Yande.re 爬虫 (github.com)](https://github.com/cloudwindy/yander)

Return list after completion:

```python
['./853707.png', './853706.jpg', './853705.jpg', './853704.jpg', './853703.jpg', './853702.jpg', './853701.jpg', './853700.png', './853699.png', './853698.png', './853697.png', './853696.jpg', './853695.jpg', './853694.jpg', './853693.jpg', './853692.jpg', './853691.png', './853690.png', './853688.jpg', './853687.png', './853686.png', './853684.jpg', './853683.png', './853682.png', './853681.png', './853680.png', './853679.png', './853678.png', './853677.png', './853676.jpg', './853675.png', './853674.jpg', './853673.png', './853672.jpg', './853671.jpg', './853670.jpg', './853669.png', './853668.jpg', './853667.png', './853666.png']
```

Whether the path is relative or not depends on the path given by your parameters.

## waziJavBus Tutorial

Currently only number search, other functions and so on my next update.

### Configuration

```python
from pywazi import waziJavBus as Wjb

Wjb.giveParams({
    "useProxies": True,  # Whether to use a proxy
    "proxyAddress": "127.0.0.1",  # HTTPS / HTTP proxy address
    "proxyPort": "7890",  # HTTPS / HTTP proxy port
    "useHeaders": False,  # Whether to use custom header (not recommended to fill in, the program automatically set)
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.164 Safari/537.36"
    }  # Custom head content (not recommended to fill in, the program automatically set, fill in their own may lead to part of the module error)
})

# Optional content
Wjb.customUrl("https://www.javbus.icu/")  # Set up mirror station
Wjb.useDomainApi(True)  # Whether to use the Api of the master, some mirror stations need to be set to True
```


### Get the magnetic link

```python
Wjb.getMagnet("doks-539")

# The first parameter indicates the number, note the case
```

Return List:

```python
[{'title': 'DOKS-539', 'magnet': 'magnet:?xt=urn:btih:BD68655E788DA7B8CAAE739C7D46F3B4890F3A89&dn=DOKS-539', 'size': '5.01GB', 'date': '2021-03-31'}, {'title': 'DOKS-539', 'magnet': 'magnet:?xt=urn:btih:BD68655E788DA7B8CAAE739C7D46F3B4890F3A89&dn=DOKS-539', 'size': '5.01GB', 'date': '2021-03-31'}, {'title': 'DOKS-539', 'magnet': 'magnet:?xt=urn:btih:BD68655E788DA7B8CAAE739C7D46F3B4890F3A89&dn=DOKS-539', 'size': '5.01GB', 'date': '2021-03-31'}, {'title': 'DOKS-539', 'magnet': 'magnet:?xt=urn:btih:BD68655E788DA7B8CAAE739C7D46F3B4890F3A89&dn=DOKS-539', 'size': '5.01GB', 'date': '2021-03-31'}, {'title': 'DOKS-539', 'magnet': 'magnet:?xt=urn:btih:BD68655E788DA7B8CAAE739C7D46F3B4890F3A89&dn=DOKS-539', 'size': '5.01GB', 'date': '2021-03-31'}, {'title': 'DOKS-539', 'magnet': 'magnet:?xt=urn:btih:BD68655E788DA7B8CAAE739C7D46F3B4890F3A89&dn=DOKS-539', 'size': '5.01GB', 'date': '2021-03-31'}, {'title': 'DOKS-539', 'magnet': 'magnet:?xt=urn:btih:BD68655E788DA7B8CAAE739C7D46F3B4890F3A89&dn=DOKS-539', 'size': '5.01GB', 'date': '2021-03-31'}, {'title': 'DOKS-539', 'magnet': 'magnet:?xt=urn:btih:BD68655E788DA7B8CAAE739C7D46F3B4890F3A89&dn=DOKS-539', 'size': '5.01GB', 'date': '2021-03-31'}, {'title': 'DOKS-539', 'magnet': 'magnet:?xt=urn:btih:BD68655E788DA7B8CAAE739C7D46F3B4890F3A89&dn=DOKS-539', 'size': '5.01GB', 'date': '2021-03-31'}]
```

`title` indicates the number，`magnet` indicates the magnetic link，`size` indicates the size，`date` indicates upload date.

## waziExHentai Tutorial

ExHentai is the inner site of E-Hentai and requires an account with privileges to access it (which I do not provide). It is best if your display mode is set to `Extended` before using this program, although the program has adaptations for other display modes, but additional code configuration is required (although only one line is needed).

### Configuration

```python
from pywazi import waziExHentai as Weh

Weh.giveParams({
    "useProxies": True,  # Whether to use a proxy
    "proxyAddress": "127.0.0.1",  # HTTPS / HTTP proxy address
    "proxyPort": "7890",  # HTTPS / HTTP proxy port
    "useHeaders": False,  # Whether to use custom header (not recommended to fill in, the program automatically set)
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.164 Safari/537.36"
    }  # Custom head content (not recommended to fill in, the program automatically set, fill in their own may lead to part of the module error)
})

Weh.setCookies("xxxxxx=xxxxxxxxxx;xxxxxxx=xxxxxxxxxxxxxxx;xxxxxx=xxxxxxx")  # Set your Cookies
```

#### How to get your account's cookies

1. Open https://exhentai.org/ If you are not logged in, then log in first
2. Right click -> Check / Review Elements -> Console (or F12)
3. Type `document.cookie` and enter
4. Copy the returned content and this is your Cookies

#### Additional parsers

When enabled, it will automatically check the current home page display mode and use the parsing function to adapt it, if not enabled, the default display mode will be `Extended`.

```python
Weh.setParse(True)

# The first argument indicates whether to turn on additional parsers
```

### Browse

Home browsing mode, two built-in browsing modes.

#### General mode

Use the default settings of the home page to display content, using the `Extended` display mode as an example.

```python
Weh.browse(0)

# The first parameter indicates the page number, counting from 0
```

Return List (take one of the examples):

```python
[{
		'title': '[Dikk0] おかうちゃんといっぱい愛を深めあうCG集！',
		'URL': 'https://exhentai.org/g/2014688/179bbb9082/',
		'cat': 'Artist CG',
		'cover': 'https://exhentai.org/t/66/95/669535f2df520ac89d4d7a96250cd19b3fbdfd9b-3974303-1875-2500-jpg_250.jpg',
		'uploader': 'RepStormy',
		'uploaderURL': 'https://exhentai.org/uploader/RepStormy',
		'time': '2021-09-19 20:57',
		'hasTorrents': True,
		'rating': 4.5,
		'pages': 27,
		'others': {
			'type': 'Extended Own Information',
			'has': ['tags'],
			'tags': ['parody:hololive', 'character:nekomata okayu', 'female:kemonomimi', 'female:sole female', 'female:vtuber', 'male:first person perspective', 'male:sole male', 'artist:dikk0', ':variant set']
		}
 }, ...]
```

`title` indicates the Japanese title of the gallery, `URL` indicates the link to the gallery, `cat` indicates the category of the gallery, `cover` indicates the cover address of the gallery, `uploader` indicates the uploader of the gallery, `uploaderURL` indicates the uploader address of the gallery, `time` indicates the upload time of the gallery, `rating` indicates the rating of the gallery, `pages` indicates the page number of the gallery.

`others` indicates additional information in this display mode, `type` indicates the type of information, `has` indicates what content is present, and `tags` indicates tags.

#### All mode

Using this mode will ignore your default settings, turn off your filters, and show more content such as: expunged galleries, low power tags, etc.

```python
Weh.allBrowse(0)

# The first parameter indicates the page number, counting from 0
```

The format is the same as **General Mode**.

### Search

Built-in a variety of search modes, the search return format are the same as the browse, not to repeat.

#### General mode

Use the default settings to search.

```python
Weh.search(0, "maid")

# The first parameter indicates the page number, counting from 0

# The second parameter indicates the search content, multiple content please use "+" inside the quotation marks to connect
```

#### All mode

Ignore your default mode and allow other content.

```python
Weh.allSearch(0, "dress")

# The first parameter indicates the page number, counting from 0

# The second parameter indicates the search content, multiple content please use "+" inside the quotation marks to connect
```

#### Tag mode

Use default settings for tag search.

```python
Weh.tagSearch(0, "language:chinese")

# The first parameter indicates the page number, counting from 0

# The second parameter indicates the label, including the content before the ":" (if any)
```

Please use normal mode for multi-tab normal search, and use all mode for all-tab search.

#### Uploader mode

Use the default settings for uploader search.

```python
Weh.uploaderSearch(0, "如歌的行板")

# The first parameter indicates the page number, counting from 0

# The second parameter indicates the name of the uploader, without the "uploader:" prefix
```

Please use normal mode for multi-uploader normal search, and use all mode for multi-uploader all search, remember to bring `uploader:` prefix.

#### Uploader all mode

Ignore your default mode and allow other content for the uploader search.

```python
Weh.uploaderAllSearch(0, "如歌的行板")

# The first parameter indicates the page number, counting from 0

# The second parameter indicates the name of the uploader, without the "uploader:" prefix
```

#### Advanced mode

> Not recommended, because the parameter content of this thing is not so intuitive, it is recommended to use custom search.

```python
Weh.advancedSearch({
    "cats": ["Non-H"],  # Categories to search
    "search": "",  # Search Content
    "sgn": True,  # Whether to search for gallery names
    "sgt": True,  # Whether to search the gallery tags
    "sgd": False,  # Whether to search the gallery description
    "stf": False,  # Whether to search for torrent names
    "osgwt": False,  # Whether to view only those galleries with torrents
    "slpt": False,  # Search for cold tags or low power tags
    "sdt": False,  # Search poll over down tags
    "seg": False,  # Search for expunged galleries
    "mr": True,  # Whether to limit the minimum rating
    "mrs": 5,  # Minimum rating, range is 2 - 5
    "b": False,  # Whether to turn on the search results limited page range
    "b1": "",  # Start Page Number
    "b2": "",  # End Page Number
    "dfl": False,  # Turn off language filtering by default or settings
    "dfu": False,  # Turn off default or set filtering of uploaders
    "dft": False,  # Turn off default or set filtering on tags
    "page": 0  # Page number, counting from 0
})

```

#### Image mode

> Not recommended, because the parameter content of this thing is not so intuitive, it is recommended to use custom search.

Image search by default mode.

##### Give the picture of SHA-1

```python
Weh.imageSearch({
    "type": "sha1",
    "sha1": "C75774D8D2F003C8337F1EA57BA3184A9A4FD515",
    "similar": True,  # Whether to search for similar images
    "cover": True,  # Whether to search the cover
    "exp": True  # Whether to search for expunged galleries
})
```

##### Give the path to the image

```python
Weh.imageSearch({
    "type": "file",
    "path": "./11.jpg", # Both absolute and relative
    "similar": True, # Whether to search for similar images
    "cover": True, # Whether to search the cover
    "exp": True # Whether to search for expunged galleries
})
```

#### Custom mode

I highly recommend that developers use custom search to build a more rigorous search request.

```python
Weh.customSearch({
	"cats": ["Doujinshi", "Manga", "Artist CG", "Game CG"],  # Search for the desired category, or full search if no parameters are provided
	"uploaders": ["Pokom", "NekoHime27"],  # Search for uploader, not provided means no search
	"tags": ["female:lolicon"],  # Search by tags, not provided means no search
	"text": "",  # Search content, do not provide means do not search, three constraints on each other
	"advanced": {  # Advanced parameters, not provided means no advanced search
		"search": {
			"galleryName": True,  # Whether to search for gallery names
			"galleryTags": True,  # Whether to search the gallery tags
			"galleryDescription": False,  # Whether to search the gallery description
			"torrentFilenames": False,  # Whether to search for torrent name
			"low-powerTags": False,  # Whether to search for low power tags
			"downvotedTags": False,  # Whether the search poll has given down tags
			"expungedGalleries": False,  # Whether to search for expunged galleries
		},
		"limit": {
			"onlyShowGalleriesWithTorrents": False,  # Whether to search only galleries with torrents
			"minimumRating": False,  # Whether to enable minimum rating
			"minimumRatingNumber": 2,  # Minimum rating, range is 2 - 5
			"between": False,  # Whether to turn on the search results limited page range
			"betweenPages": [0, 0]  # Start page and end page
		},
		"disableFilters": {
			"language": False,  # Whether to turn off the language filter
			"uploader": False,  # Whether to turn off uploader filters
			"tags": False  # Whether to turn off tags filters
		}
	},
	"file": {  # File search, not provided means no file search
		"main": {
			"type": "path",  # type can be sha1 or path
			"value": "./a.jpg"  # If the type is sha1 then fill in the SHA1 value of the file here
		},
		"options": {
			"useSimilarityScan": True,  # Whether to enable similar search
			"onlySearchCovers": False,  # Whether to search only the cover
			"showExpunged": False  # Search for expunged galleries
		}
	}
})
```

### Information

Contains four main elements: torrent information, basic information, comment content and paging.

#### Torrent information

```python
Weh.getTorrent("https://exhentai.org/g/2011308/8263590d02/")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"
```

Return List:

```python
[{'time': '2021-09-15 17:48', 'size': '39.93 MB', 'seeds': '8', 'peers': '3', 'total': '268', 'link': 'https://exhentai.org/torrent/2011308/dcfecda8d01d5f928ed0a03d44a20bd753b86d92.torrent', 'name': '[Ramchi] 【巫女服を着た】茶髪ちゃん.zip'}]
```

`time` denotes upload time, `size` denotes file size, `seeds` denotes number of torrent, `peers` denotes number of users, `total` denotes total number of downloads, `link` denotes torrent download address, and `name` denotes file name.

#### Basic information

Two access methods were separated out:

1. Through the web;
2. Through the API.

##### Through the web

```python
Weh.getInfo("https://exhentai.org/g/2011308/8263590d02/")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"
```

Return Dictionary:

```python
{'title': '[Ramchi] [Mikofuku o Kita] Chapatsu-chan', 'jTitle': '[らむち] 【巫女服を着た】茶髪ちゃん', 'cat': 'Artist CG', 'tags': ['artist:ramchi', 'male:sole male', 'male:first person perspective', 'female:sole female', 'female:miko', 'variant set', 'mosaic censorship'], 'time': '2021-09-15 16:27', 'father': 'None', 'viewable': 'Yes', 'language': 'Japanese', 'size': '40.02 MB', 'pages': 24, 'favTimes': '171 times', 'uploader': 'RepStormy', 'rate': '4.36', 'cover': 'https://exhentai.org/t/6f/4c/6f4ce969fb06df5c588d0c608325dd51b6c80e6a-1775767-1152-2048-png_250.jpg'}
```

`title` means Roman/English title, `jTitle` means Japanese or other language title, `cat` means category, `tags` means tags, `time` means upload time, `father` means parent gallery, `viewable` means visible or not, `language` means language, `size` means size. `pages` indicates page number, `favTimes` indicates number of favorites, `uploader` indicates uploader, `rate` indicates rating, and `cover` indicates cover.

##### Through the API

```python
Weh.apiInfo("https://exhentai.org/g/2011308/8263590d02/")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"
```

Return Dictionary:

```python
{'gmetadata': [{'gid': 2011308, 'token': '8263590d02', 'archiver_key': '453359--2db256904a5e9dfedee04cb1fad9229abc723e43', 'title': '[Ramchi] [Mikofuku o Kita] Chapatsu-chan', 'title_jpn': '[らむち] 【巫女服を着た】茶髪ちゃん', 'category': 'Artist CG', 'thumb': 'https://exhentai.org/t/6f/4c/6f4ce969fb06df5c588d0c608325dd51b6c80e6a-1775767-1152-2048-png_l.jpg', 'uploader': 'RepStormy', 'posted': '1631723255', 'filecount': '24', 'filesize': 41959880, 'expunged': False, 'rating': '4.36', 'torrentcount': '1', 'torrents': [{'hash': 'dcfecda8d01d5f928ed0a03d44a20bd753b86d92', 'added': '1631728106', 'name': '[Ramchi] 【巫女服 を着た】茶髪ちゃん.zip', 'tsize': '13243', 'fsize': '41871590'}], 'tags': ['artist:ramchi', 'male:first person perspective', 'male:sole male', 'female:miko', 'female:sole female', 'mosaic censorship', 'variant set']}]}
```

`archiver_key` is the zip download address suffix, `title` is the title, `title_jpn` is the Japanese title, `category` is the category, `thumb` is the cover, `uploader` is the uploader, `posted` is the second-level timestamp, `filecount` is the number of files, ` filesize` is the file size, `expunged` is the removed status, `rating` is the rating, `torrentcount` is the number of torrents, `hash` is the torrent hash, `added` is the second-level timestamp, `name` is the seed filename, `tsize` and `fszie` are not clear to me, ` tags` is the tag.

#### Comment content

```python
Weh.getComments("https://exhentai.org/g/1948847/f81687b96e/")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"
```

Return List:

```python
[{'time': '02 July 2021, 17:41', 'uploader': 'https://exhentai.org/uploader/%E9%82%A3%E7%8F%82%E3%81%A1%E3%82%83%E3%82%93', 'uploaderName': '那珂ちゃん', 'scores': 'None / 不适用', 'htmlComments': '\n https://fantia.jp/posts/615177\n <br/>\n <br/>\n <a href="https://exhentai.org/s/0dcc07ddde/1948847-1">\n  001~010 文字あり\n </a>\n <br/>\n <a href="https://exhentai.org/s/0e34105f9a/1948847-11">\n  011~020 文字なし\n </a>\n\n'}, {'time': '30 July 2021, 04:56', 'uploader': 'https://exhentai.org/uploader/pop9', 'uploaderName': 'pop9', 'scores': '+76', 'htmlComments': '\n https://ehwiki.org/wiki/japanese\n <br/>\n <br/>\n Default language flag;\n <strong>\n  do NOT use this tag\n </strong>\n outside of legitimate dual-language galleries and translations to Japanese.\n\n'}]
```

`time` denotes comment time, `uploader` denotes commenter's homepage, `uploaderName` denotes commenter's nickname, `scores` denotes rating, and `htmlComments` denotes html version of the comment.

#### Paging

```python
Weh.getPages("https://exhentai.org/g/1948847/f81687b96e/")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"
```

Returns 0 for no page-turning, a positive integer for page-turning, and a value that indicates how many times the page needs to be manually turned.

### Image

There are thumbnails and normal images.

#### Thumbnails

The thumbnails are given in two modes: Large (large mode) and Normal (normal mode).

##### Large mode

```python
Weh.getLargeThumbnails("https://exhentai.org/g/1948847/f81687b96e/")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"
```

Return List:

```python
[{'url': 'https://exhentai.org/t/0d/cc/0dcc07ddde12dd84a128ae83f9ff48375e32f768-5456884-2921-4112-png_l.jpg', 'style': 'height:302px', 'alt': '01', 'title': 'Page 1: cien_2102_01_full.png', 'text': '01'}, ...]
```

`url` indicates the thumbnail download address, `style` indicates the overlay style sheet information for this image, `alt` indicates the content when it is missing, `title` indicates the image information, and `text` indicates other content such as the image location.

##### Normal mode

> Normal mode is not recommended, because you need to do image cutting when displaying.

```python
Weh.getNormalThumbnails("https://exhentai.org/g/1948847/f81687b96e/")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"
```

Return List:

```python
[{'style': 'height:161px', 'divMargin': '1px auto 0', 'divWidth': '100px', 'divHeight': '141px', 'url': 'https://exhentai.org/m/001948/1948847-00.jpg', 'transparent': '-0px 0 no-repeat', 'imgAlt': '01', 'imgTitle': 'Page 1: cien_2102_01_full.png', 'imgWidth': '100px', 'imgHeight': '140px', 'imgMargin': '-1px 0 0 -1px'}, ...]
```

For the explanation of the content, I suggest you read the source code of the site in Normal mode, because it involves information about border, transparent, cuts, margin, etc., which I can understand, but cannot express properly and concisely.

#### Gallery Pictures

##### List download address or download

```python
Weh.getNormalImages("https://exhentai.org/g/1948847/f81687b96e/", "get", {"path": "./download", "japanese": True})

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"

# The second parameter indicates the way, "get" means list the download address; "download" means download

# The third parameter is a dictionary indicating the details, "path" indicates your download path, and "japanese" indicates whether to use the Japanese title
```

get - Return List:

```python
['https://psnnstn.svbhzynmthvg.hath.network:6643/h/9a46b72d4e41e2cb71904e3f47a3a225041614f6-702136-2400-3379-jpg/keystamp=1627754700-3893ea4f9c;fileindex=94546547;xres=2400/cien_2102_01_full.jpg', ...]
```

Contains all gallery image addresses.

download - Return List:

```python
['./download\\[tokunocin (徳之ゆいか)] 妄想少女キクリちゃん #1\\cien_2102_01_full.jpg', ...]
```

Contains all downloaded files.

##### MPV Privileged Users

```python
Weh.getMPVImages("https://exhentai.org/g/1948847/f81687b96e/", "get", {"path": "./download", "japanese": True})

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"

# The second parameter indicates the way, "get" means list the download address; "download" means download

# The third parameter is a dictionary indicating the details, "path" indicates your download path, and "japanese" indicates whether to use the Japanese title
```

get - Return List:

```python
[{'name': 'cien_2102_01_full.png', 'url': 'https://vzwiuar.bgjtsezaekpi.hath.network:9880/h/219a879c79dddf63c230e02408ccebceebd9cccb-283462-1280-1802-jpg/keystamp=1627755900-c26b737547;fileindex=94546547;xres=1280/cien_2102_01_full.jpg'}, ...]
```

`name` denotes the file name and `url` denotes the download link.

download - Return List:

```python
['./download\\[tokunocin (徳之ゆいか)] 妄想少女キクリちゃん #1\\cien_2102_01_full.jpg', ...]
```

Contains all downloaded files.

### Compressed package download

Divided into three: H@H, get link, download

#### H@H

There are two: get download code and download

##### H@H Get

```python
Weh.getArchivesHATH("https://exhentai.org/g/1948847/f81687b96e/")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"
```

Return List:

```python
[{'sample': '780x', 'size': '1.42 MB', 'cost': 'Free', 'code': '780', 'url': 'https://exhentai.org/archiver.php?gid=1948847&token=f81687b96e&or=452154-1c41df26535532bfc35cff7874319017afed3418'}, ...]
```

`sample` means resolution, `size` means size, `cost` means number of points spent, `code` means code, and `url` means H@H request link.

##### H@H Download

```python
Weh.toHATH("https://exhentai.org/archiver.php?gid=1948847&token=f81687b96e&or=452154-1c41df26535532bfc35cff7874319017afed3418", "780")

# The first parameter indicates the URL returned by getArchivesHATH
# The second parameter indicates the code returned by getArchivesHATH
```

If it returns `Done! / 完成！` it means it's done, otherwise, follow the instructions.

#### Get link

```python
Weh.getArchives("https://exhentai.org/g/1948847/f81687b96e/")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"
```

Return List:

```python
[{'type': 'original', 'link': 'https://plprhexcngkbxoopaqlx.hath.network/archive/1948847/1d0756978bba0f6166cc5eafa1b05cc33257a77d/cxltzmu9ovu/2?start=1'}, {'type': 'resample', 'link': 'https://plprhexcngkbxoopaqlx.hath.network/archive/1948847/1d0756978bba0f6166cc5eafa1b05cc33257a77d/cxltzmu9ovu/3?start=1'}]
```

`type` indicates the zip type, `link` indicates the download address.

#### Download 

```python
Weh.downloadArchives("https://exhentai.org/g/1948847/f81687b96e/", {"path": "./download", "japanese": True}, "")

# The first parameter indicates the address of the gallery and requires "https://" starting and ending with "/"

# The second parameter is a dictionary indicating the details, "path" indicates your download path, and "japanese" indicates whether to use the Japanese title

# The third parameter indicates the resolution of the download, if the empty string means all downloads
```

Return list, but I can't return properly because I can only download the original image size.

## waziPicAcg Tutorial

### Configuration

```python
from pywazi import waziPicAcg as Wpa

WpagiveParams({
    "useProxies": True,  # Whether to use a proxy
    "proxyAddress": "127.0.0.1",  # HTTPS / HTTP proxy address
    "proxyPort": "7890",  # HTTPS / HTTP proxy port
    "useHeaders": False,  # Whether to use custom header (not recommended to fill in, the program automatically set)
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.164 Safari/537.36"
    }  # Custom head content (not recommended to fill in, the program automatically set, fill in their own may lead to part of the module error)
})

Wpa.login("你的用户名", "你的密码")
```

The token is returned after a normal login, and if it fails, the probability is the following:

1. Network problems, checking proxies;
2. Time synchronization problems, especially for dual-system computers;
3. Incorrect account password or non-existent account;
4. PicAcg is updated.

### Get categories

```python
Wpa.getCategories()
```

Return Dictionary:

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

### Get hot keywords

```python
Wpa.getKeywords()
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'keywords': ['乳汁', '短髮', '全彩', '自慰', '吞精', '橫切面', '無修正', '短篇合集', '校園', '人外娘', '開大車']}}
```

### Get collections

```python
Wpa.getCollections()
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'collections': [{'title': '本子神推薦', 'comics': [{'_id': '5f9e7e417193765a84d387c1', 'title': 'ナイショの夜ふかし(High☆Speed! -Free! Starting Days-)', 'author': 'B-LUSH(カウカウ)', 'totalViews': 136228, 'totalLikes': 8393, 'pagesCount': 40, 'epsCount': 1, 'finished': True, 'categories': ['短篇', '同人', '純愛', '耽美花園'], 'thumb': {'originalName': 'title 副本.jpg', 'path': 'eb9ccaf7-24f5-42ea-8f11-d57b1249718f.jpg', 'fileServer': 'https://storage1.picacomic.com'}}]}, {'title': '本子魔推薦', 'comics': [{'_id': '6072a5621397b71d7b466432', 'title': 'Lusty radroach', 'author': 'Chobonolly', 'totalViews': 498033, 'totalLikes': 7498, 'pagesCount': 27, 'epsCount': 3, 'finished': True, 'categories': ['短篇', '非人類', '重口地帶', '全彩', 'CG雜圖', '生肉'], 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': '5baeb887-2bb3-4fb9-a2dd-cbb42c21b45f.jpg', 'originalName': '1.jpg'}}, {'_id': '612628dbaa7eee38665221ce', 'title': '비밀유지보안법丨维持秘密的保安法', 'author': '팀딱콩', 'totalViews': 204856, 'totalLikes': 9110, 'pagesCount': 109, 'epsCount': 2, 'finished': False, 'categories': ['全彩', 'WEBTOON'], 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': 'b3b4d5c1-6413-40f4-9d15-6d76b7b351e2.jpg', 'originalName': 'E0H2BCCVUAAtxaA.jpg'}}]}]}}
```

### Get home banner

```python
Wpa.getBanners()
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'banners': [{'_id': '601d3abdcfeaee28f8d8cb72', 'title': '逆王傳說: 入侵女兒國', 'shortDescription': '想幹就幹！', '_game': '601d3abdcfeaee28f8d8cb72', 'type': 'game', 'thumb': {'fileServer': 'https://pica-pica.wikawika.xyz', 'path': 'banner_game.gif?v=1', 'originalName': 'banner_game.gif'}}, {'_id': 'qkwejqkwe', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '完美嫩乳!', 'type': 'web', 'link': 'https://ad-channel.wikawika.xyz/redirect/zone_3', 'thumb': {'fileServer': 'https://ad-channel.wikawika.xyz', 'path': 'TPl-6fggnqnd5qb_AgUvT.jpg', 'originalName': 'image.jpg'}}, {'_id': 'dsfsdf', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '😘 ', 'type': 'ads', 'link': 'https://ad-channel.wikawika.xyz/android/home_banner', 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': '369ca47f-e015-4acf-b2e3-cb4800c876f7.jpg', 'originalName': 'image.jpg'}}, {'_id': 'dsfsdf1', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '😘 ', 'type': 'ads', 'link': 'https://ad-channel.wikawika.xyz/android/home_banner_2', 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': '369ca47f-e015-4acf-b2e3-cb4800c876f7.jpg', 'originalName': 'image.jpg'}}, {'_id': 'fjg1', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '點就對了!', 'type': 'web', 'link': 'https://ad-channel.wikawika.xyz/redirect/zone_4', 'thumb': {'fileServer': 'https://ad-channel.wikawika.xyz', 'path': 'ANECmINT-izcsF208QM2y.jpg', 'originalName': 'image.jpg'}}, {'_id': 'toBe3', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '😘 ', 'type': 'ads', 'link': 'https://ad-channel.wikawika.xyz/android/home_banner_4', 'thumb': {'fileServer': 'https://storage1.picacomic.com', 'path': '369ca47f-e015-4acf-b2e3-cb4800c876f7.jpg', 'originalName': 'image.jpg'}}, {'_id': 'toBe4', 'title': '拯救嗶咔，點擊廣告！', 'shortDescription': '來征服我吧!', 'type': 'web', 'link': 'https://ad-channel.wikawika.xyz/redirect/zone_5', 'thumb': {'fileServer': 'https://ad-channel.wikawika.xyz', 'path': 'bI8uZ7Pdycuet_IBuh64O.jpg', 'originalName': 'image.jpg'}}]}}
```

### Get notifications

```python
Wpa.getNotifications(1)

# The first parameter indicates the page number, counting from 1
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'notifications': {'docs': [], 'total': 0, 'limit': 10, 'page': 1, 'pages': 1}}}
```

I'm still not sure what will be in the `docs`.

### Get announcements

```python
Wpa.getAnnouncements(1)

# The first parameter indicates the page number, counting from 1
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'announcements': {'docs': [{'_id': '6142e0880dac716f6aa09d01', 'content': '「Master，我快要抑制不住了魔主之力了，嗚、嗚啊——！」\n少女英靈卸除胸甲，展示腹部泛起的黑色旋渦\n她脫下身上皮甲和長裙，絲襪接連扯下，背對勇士翹起圓臀——\n「Master……？不快點的話，我就……嗯…♡」\n面對少女的挑逗，立即解開蠢蠢欲動的褲檔，插進你的「聖劍♂」，以高濃度魔力侵吞英靈的驅體！\n\n安卓及iOS下載連接:\nhttps://fgoatt13.star1818.net\n\n其餘遊戲請到嗶咔遊戲區下載！\n\n－－－－－－－－－－－－－－－－－－\n\n宅男成人社區，海量美圖視頻免費觀看 https://new-apk.99gezi.com/package/android/30_nlzljq_3.1.6.apk\n\n蘑菇加速器，翻牆看本子，再也不怕掉隊。牆外的世界很精彩！https://3.mogu91.com/\n\n騎士開發，老司機帶你看片子 https://dw.xiacangku.xyz/\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡有優惠哦~ http://mtw.so/5Urt0j\n\n視訊玩法，點擊下載送現金! https://down.sxshiye.com/gamecenter-release-android-shanhe-500019-7bb5d875dd0fe7d4939cad9b283d24a1.apk\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n91短視頻 記錄性福生活 https://app.dsppro.me/chan-1005/aff-Ghyw\n\n極速翻牆看嗶咔速度秒殺老王 https://VPN.bika.page\n\n－－－－－－－－－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j\n\n！！！！！\n由於嗶咔的淑女會員愈來愈多，為了了解淑女對本子的喜好，我們在 telegram 開了一個淑女群，希望透過交流了解淑女對嗶咔的感覺和意見，歡迎淑女們加入我們的群。進入群後你必須證實你是淑女，否則會被踢出群和封鎖喔😊\nhttps://t.me/joinchat/y7Q6G3n-Y_NhYzNl', 'title': '命運王座', 'created_at': '2021-09-16T06:13:28.578Z', 'thumb': {'originalName': '0915_FGO_800_1200.jpg', 'path': '304c55e0-a8cc-4fa9-a414-466a068e3393.jpg', 'fileServer': 'https://storage1.picacomic.com'}}, {'_id': '613a1dfcff488f6f443a54a7', 'content': '夕陽西下，浴場內有一女子洗濯 的背影\n豈料風一吹，藏匿在草叢的你馬上現形！\n「逆王大人，都看過我的身體了，還能就此作罷嘛♡～？」\n少女僅以薄布包裹半身 ，外露的北半球在夕照和水面的映襯下顯得碧波蕩漾\n她靠近輕撫你的褲檔，身上乳液混雜著少女體香，實在叫人欲罷不能！\n還不一手扯掉她的浴巾，盡情享受魚水之歡？\n立即降臨女兒國，以身下大炮廣結淫緣！\n\n安卓及iOS下載連接:\nhttp://xratt13.thejierou.net\n\n其餘遊戲請到嗶咔遊戲區下載！\n\n－－－－－－－－－－－－－－－－－－\n\n宅男成人社區，海量美圖視頻免費觀看 https://new-apk.99gezi.com/package/android/30_nlzljq_3.1.6.apk\n\n蘑菇加速器，翻牆看本子，再也不怕掉隊。牆外的世界很精彩！https://3.mogu91.com/\n\n騎士開發，老司機帶你看片子 https://dw.xiacangku.xyz/\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡 有優惠哦~ http://mtw.so/5Urt0j\n\n視訊玩法，點擊下載送現金! https://down.sxshiye.com/gamecenter-release-android-shanhe-500019-7bb5d875dd0fe7d4939cad9b283d24a1.apk\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n91短視頻 記錄性福生活 https://app.dsppro.me/chan-1005/aff-Ghyw\n\n極速翻牆看嗶咔速度秒殺老王 https://VPN.bika.page\n\n－－－－－－－ －－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j\n\n！！！！！\n由於嗶咔的淑女會員愈來愈多，為了了解淑女對本子的喜好，我們在 telegram 開了一個淑女群，希望透過交流了解淑女對嗶咔的感覺和意見，歡迎淑女們加入我們的群。進入群後你必須證實你是淑女，否則會被踢出群和封鎖喔😊\nhttps://t.me/joinchat/y7Q6G3n-Y_NhYzNl', 'title': '逆王傳說', 'created_at': '2021-09-09T14:45:16.557Z', 'thumb': {'originalName': 'Artboard 1.jpg', 'path': 'ad2c7950-e2f1-459f-b0a8-7bbd90cf3b51.jpg', 'fileServer': 'https://storage1.picacomic.com'}}, {'_id': '6081771007edd91d5adbfbdd', 'title': '棋牌公告', 'content': '盛夏燥熱無比？快來貼緊冰涼爆乳為你降溫！\n下載游戲，拯救bika~\n視訊發牌再升級，夏季限定比基尼爆乳荷官，冰冰涼涼貼緊你～同城真人陪玩，主人，約嗎？\n每晚整點准時抽獎，現金6666、iPhone12pro Max等，獎品upupup再up！\n刺激爽翻 天，安全公平，24小時客服服務，隨叫隨到，全新趨勢分析參考助你走上人生巔峰！\n實時聯網競技，盡享競技快感，爆乳在測波濤洶湧，助你今晚高潮！\n山河棋牌，2021年最新最火爆棋牌。真人在线，提款秒到！\n一秒開局萬人在線，德州撲克大佬互搏，今晚就要贏到人生高潮！還有豐富的游戲種類！\n主人快來～乳醬陪你激情一夏～～\n\n下載連結:\nhttps://down.sxshiye.com/gamecenter-release-android-shanhe-500019-7bb5d875dd0fe7d4939cad9b283d24a1.apk\n\n－－－－－－－－－－－－－－－－－－\n\n宅男成人社區，海 量美圖視頻免費觀看 https://new-apk.99gezi.com/package/android/30_nlzljq_3.1.6.apk\n\n蘑菇加速器，翻牆看本子，再也不怕掉 隊。牆外的世界很精彩！https://3.mogu91.com/\n\n騎士開發，老司機帶你看片子  https://dw.xiacangku.xyz/\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡有優惠哦~ http://mtw.so/5Urt0j\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n91短視頻 記錄性福生活 https://app.dsppro.me/chan-1005/aff-Ghyw\n\n極速翻牆看嗶咔速度秒殺老王 https://VPN.bika.page\n\n—－－－－－－－－－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j\n', 'created_at': '2021-04-22T13:16:00.766Z', 'thumb': {'originalName': '组1(9).jpg', 'path': '6585d1ee-0a6a-48dc-9075-5d22358d34f5.jpg', 'fileServer': 'https://storage1.picacomic.com'}}, {'_id': '5bf235bbd158ce4e17b8d09a', 'title': '嗶咔漫畫鳳凰計劃・一 順利完成 ！', 'content': '----------請注意個人衞生，配戴口罩，保護自己，努力活下去-------------\n\n嗶咔漫畫鳳凰計劃・一\n\n\n鳳凰計劃第一階行動雖然遇上一點點困難，但最後也順利完成，十分感謝大家的耐心等候。\n快與穩能夠同時存在！\n晚上的戒擼時段已經成為歷史！\n\n・・・\n\n要來的，總會來\n嗶咔漫畫會蛻變成鳳凰\nhttps://countdown.picacomic.com\n\n-----《特別公告》-----\n 遊戲區部份H遊暫停至1月25日！\n\n－－－－－－－－－－－－－－－－－－\n\n宅男成人社區，海量美圖視頻免費觀看 https://new-apk.99gezi.com/package/android/30_nlzljq_3.1.6.apk\n\n蘑菇加速器，翻牆看本子，再也不怕掉隊。牆外的世界很精彩！https://3.mogu91.com/\n\n騎士開發，老司機帶你看片子  https://dw.xiacangku.xyz/\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡有優惠哦~ http://mtw.so/5Urt0j\n\n91短视频 记录性福生活 https://app.dsppro.me/chan-1005/aff-Ghyw\n\n極速翻牆看嗶咔速度秒殺老王 https://VPN.bika.page\n\n\n—－－－－－－－－－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j', 'created_at': '2018-11-19T04:02:03.067Z', 'thumb': {'originalName': '34789.png', 'path': 'e7b7ea62-2ede-4521-92bc-7a044d4b3f07.png', 'fileServer': 'https://storage1.picacomic.com'}}, {'_id': '5acc60d0bc6b3779f41f681f', 'title': '漢化組及群組聲明公告', 'content': '嗶咔漢化組出現危機！\n\n漢化 組原話：\n" 勇士们哟！欢迎来到我的酒馆！快找个位子随便座~≧▽≦ 就像招募页里一样的啦，哔咔哔咔汉化组的图源酱不小心操劳过度 被沉到大西洋了，在这里向各位有志之士发出邀请òᆺó，欢迎新图源酱的到来哦！"\n\n請多多支持！詳細請看圖！ \n\n另外，又發現一 個冒認吾等的群組收錢賣免費軟件，在此聲明，無論你付不付款，你要用梯子就是要用，不需要用就是不需要用，並沒有付款後會增加的功能，我們也不會從任何的群收取任何金錢，以上！\n\n－－－－－－－－－－－－－－－－－－－－\n\n玩機動戰隊，告別枯燥回合操作\n安卓下載請去: http://package.jdzd.gameduchy.cn/jdzd_c10___.apk\n\n獲取禮包碼\x08:\n安卓: http://jdzd.gameduchy.cn:9152/get_code/?key=dujia\niOS: http://jdzd.gameduchy.cn:9252/get_code/?key=dujia\n\n－－－－－－－－－－－－－－－－－－\n\nAV裏番影片看到飽 http://iqq2.net/cn/?fromsite=adr.picaapp\n\n蘑菇加速器，翻牆看本子，再也不怕掉隊。牆外的世界很精彩！https://3.mogu86.com/\n\n日本進口飛機杯，讓她來代替你的手吧 備注嗶卡有優惠哦~ http://t.cn/AiQS1jH0\n\n91短视频 记录性福生活 http://invited.91porn005.me:2082/chan-1005/aff-Ghyw\n\n萝莉喷水裸聊 加微信一夜情约炮  http://www.yyuucity.com/index.html?id=kch64\n\n極速翻牆看本子看油管玩外服遊戲 https://bika.lsj.world\n\n—－－－－－－－－－－－－－－－－－－\n\n嗶咔官方社交\n推特 (技術支援/版權/日常): https://twitter.com/picapicacomic\nFB (日常): https://twitter.com/picapicacomic\n本子推薦頻道: https://t.me/joinchat/V86spB5e9c7so58j', 'created_at': '2018-04-10T06:59:28.003Z', 'thumb': {'originalName': 'sell_and_chinese_team.jpg', 'path': 'be75c212-0de4-40a7-bbc3-7e4369184e2b.jpg', 'fileServer': 'https://storage1.picacomic.com'}}], 'total': 30, 'limit': 5, 'page': '1', 'pages': 6}}}
```

### Get random comics

```python
Wpa.getRandomComics()
```

Return Dictionary:

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

### Modify request image quality

```python
Wpa.changeImageQuality(0)

# The first parameter indicates the quality number, 0 means original, 1 means low quality, 2 means medium, 3 means high quality
```

### Init

Two categories exist: general init, and Android init.

#### General int

```python
Wpa.init()
```

Return Dictionary:

```python
{'status': 'ok', 'addresses': ['104.20.180.50', '104.20.181.50'], 'waka': 'https://ad-channel.wikawika.xyz', 'adKeyword': 'wikawika'}
```

#### Android init

```python
Wpa.initAndroid()
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'isPunched': True, 'latestApplication': {'_id': '5dc58b151e103c60e7663b12', 'downloadUrl': 'https://download.wikawika.xyz/apps/2.2.1.3.3.4_collections.apk', 'updateContent': '【一般更新】\n\n1・ 新增漫畫推薦欄\n\n2・修改部份版本閃退問題\n\n後備下載連結\nhttps://download.wikawika.xyz/apps/2.2.1.3.3.4_collections.apk', 'version': '2.2.1.3.3.4', 'updated_at': '2019-11-08T15:38:45.706Z', 'created_at': '2019-11-08T15:34:45.163Z', 'apk': {'originalName': '2.2.1.3.3.4_collections.apk', 'path': '4da05b12-3534-4b4d-b9bf-804de301d2e0.apk', 'fileServer': 'https://storage1.picacomic.com'}}, 'imageServer': 'https://storage.wikawika.xyz/static/', 'apiLevel': 22, 'minApiLevel': 22, 'categories': [{'_id': '5821859b5f6b9a4f93dbf6e9', 'title': '嗶咔漢化'}, {'_id': '5821859b5f6b9a4f93dbf6d1', 'title': '全彩'}, {'_id': '5821859b5f6b9a4f93dbf6cd', 'title': '長篇'}, {'_id': '5821859b5f6b9a4f93dbf6ca', 'title': '同人'}, {'_id': '5821859b5f6b9a4f93dbf6ce', 'title': '短篇'}, {'_id': '584ea1f45a44ac4f7dce3623', 'title': '圓神領域'}, {'_id': '58542b601b8ef1eb33b57959', 'title': '碧藍幻想'}, {'_id': '5821859b5f6b9a4f93dbf6e5', 'title': 'CG雜圖'}, {'_id': '5821859b5f6b9a4f93dbf6e8', 'title': '英語 ENG'}, {'_id': '5821859b5f6b9a4f93dbf6e0', 'title': '生肉'}, {'_id': '5821859b5f6b9a4f93dbf6de', 'title': '純愛'}, {'_id': '5821859b5f6b9a4f93dbf6d2', 'title': '百合花園'}, {'_id': '5821859b5f6b9a4f93dbf6e2', 'title': '耽美花園'}, {'_id': '5821859b5f6b9a4f93dbf6e4', 'title': '偽娘哲學'}, {'_id': '5821859b5f6b9a4f93dbf6d3', 'title': '後宮閃光'}, {'_id': '5821859b5f6b9a4f93dbf6d4', 'title': '扶他樂園'}, {'_id': '5abb3fd683111d2ad3eecfca', 'title': '單行本'}, {'_id': '5821859b5f6b9a4f93dbf6da', 'title': '姐姐系'}, {'_id': '5821859b5f6b9a4f93dbf6db', 'title': '妹妹系'}, {'_id': '5821859b5f6b9a4f93dbf6cb', 'title': 'SM'}, {'_id': '5821859b5f6b9a4f93dbf6d0', 'title': '性轉換'}, {'_id': '5821859b5f6b9a4f93dbf6df', 'title': '足の恋'}, {'_id': '5821859b5f6b9a4f93dbf6cc', 'title': '人妻'}, {'_id': '5821859b5f6b9a4f93dbf6d8', 'title': 'NTR'}, {'_id': '5821859b5f6b9a4f93dbf6d9', 'title': '強暴'}, {'_id': '5821859b5f6b9a4f93dbf6d6', 'title': '非人類'}, {'_id': '5821859b5f6b9a4f93dbf6cf', 'title': '艦隊收藏'}, {'_id': '5821859b5f6b9a4f93dbf6d7', 'title': 'Love Live'}, {'_id': '5821859b5f6b9a4f93dbf6dc', 'title': 'SAO 刀劍神域'}, {'_id': '5821859b5f6b9a4f93dbf6e1', 'title': 'Fate'}, {'_id': '5821859b5f6b9a4f93dbf6dd', 'title': '東方'}, {'_id': '59041d54ccc747074b47dae4', 'title': 'WEBTOON'}, {'_id': '5821859b5f6b9a4f93dbf6e3', 'title': '禁書目錄'}, {'_id': '5bd66e7e8ff47f7c46cf999d', 'title': '歐美'}, {'_id': '5821859b5f6b9a4f93dbf6e6', 'title': 'Cosplay'}, {'_id': '5821859b5f6b9a4f93dbf6d5', 'title': '重口地帶'}], 'notification': None, 'isIdUpdated': True}}
```

### Search

There are three categories: `comics` mode, keyword mode, and advanced mode.

#### Comics mode

```python
Wpa.getComics("1", "足の恋", "全彩", "ua")

# The first parameter indicates the page number, counting from 1

# The second parameter indicates the name of the partition and should be the title in categories

# The third parameter is the tag name, which is obtained from the tags in the info return data

# The fourth parameter indicates the sorting basis and has these elements:
# 	ua -> Default sorting
#	dd -> From new to old
#	da -> From old to new
#	vd -> Most people named
#	ld -> Most like
```

Return Dictionary:

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

#### Keyword mode

```python
Wpa.search("1", "伪娘")

# The first parameter indicates the page number, counting from 1

# The second parameter indicates the keyword.
```

The format is the same as above, and the format of the advanced mode is exactly the same.

#### Advanced mode

```python
Wpa.advancedSearch(["純愛"], "女僕", "ld", 1)

# The first parameter indicates the partition, supports multiple partitions, should be a list type, if you do not want to fill [] directly

# The second parameter indicates the keyword.

# The third parameter indicates the sorting method

# The fourth parameter indicates the page number, counting from 1
```

### Comic

#### Basic information

```python
Wpa.getComic("60f5aab6e239c4708507c5d9")

# The first parameter is the comic ID, visible in _id
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'comic': {'_id': '60f5aab6e239c4708507c5d9', '_creator': {'_id': '58b2fe52288c3778fcbaba4d', 'gender': 'f', 'name': 'Selestial', 'verified': False, 'exp': 4586, 'level': 7, 'characters': ['knight'], 'role': 'knight', 'title': '萌新', 'avatar': {'originalName': 'avatar.jpg', 'path': 'f959bc38-94c0-4793-bc02-b1465d74f0bc.jpg', 'fileServer': 'https://storage1.picacomic.com'}, 'slogan': '......', 'character': 'https://pica-web.wakamoment.tk/images/halloween_f.png'}, 'title': 'ホクロ流星群せかんど [中国翻訳] [DL版]', 'description': '早该好好学学了\n（05 后别看05后别看05后别看）', 'thumb': {'originalName': 'QQ图片20210718224515.png', 'path': 'tobeimg/Gxkeem7A4h_VvYKYnIJbQx3ZCAcWFNj38-CFbeOfhZ4/fill/300/400/sm/0/aHR0cHM6Ly9zdG9yYWdlMS5waWNhY29taWMuY29tL3N0YXRpYy9jMjJjODVjNi0yYzUzLTQxMWQtYmIwNi1jZjg0NzBmZGVmZmEucG5n.png', 'fileServer': 'https://storage1.picacomic.com'}, 'author': '書肆マガジンひとり (ホクロ流 星群)', 'chineseTeam': '观星能治颈椎病个人渣翻', 'categories': ['偽娘哲學', '全彩', '短篇'], 'tags': ['偽娘', '口交', ' 制服', '雌墜', '女裝'], 'pagesCount': 30, 'epsCount': 1, 'finished': True, 'updated_at': '2021-07-19T16:39:18.121Z', 'created_at': '2021-07-18T15:12:14.015Z', 'allowDownload': True, 'allowComment': True, 'totalLikes': 438, 'totalViews': 51574, 'viewsCount': 51574, 'likesCount': 438, 'isFavourite': False, 'isLiked': False, 'commentsCount': 97}}}
```

#### Chapter information

```python
Wpa.getComicEps("60f5aab6e239c4708507c5d9", "1")

# The first parameter is the comic ID

# The second parameter indicates the number of chapter to get
#   The returned epsCount indicates the number of pagination
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'eps': {'docs': [{'_id': '60f5aab6e239c4708507c5da', 'title': '第1話', 'order': 1, 'updated_at': '2021-07-18T15:17:47.711Z', 'id': '60f5aab6e239c4708507c5da'}], 'total': 1, 'limit': 40, 'page': 1, 'pages': 1}}}
```

#### Chapter content information

```python
Wpa.getComicPages("60f5aab6e239c4708507c5d9", "1", "1")

# The first parameter is the comic ID

# The second parameter indicates the number of chapter to get

# The third parameter indicates which page to get
#   The returned pages indicate the full page number, and the page indicates the current page.
```

Return Dictionary:

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

#### Recommend information

```python
Wpa.getComicRecommend("60f5aab6e239c4708507c5d9")

# The first parameter is the comic ID
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'comics': []}}
```

If it returns comics, it should be similar to: [AnkiKong/picacomic: 哔咔漫画相关api (github.com)](https://github.com/AnkiKong/picacomic#recommend-看了這本子的人也在看) .

#### Like or unlike

```python
Wpa.likeOrUnLikeComic("60f5aab6e239c4708507c5d9")

# The first parameter is the comic ID
```

Return Dictionary:

```python
{'code': 200, 'message': 'success'}
```

The first time it was a like, the second time it was a dislike.

#### Favorite or unfavorite

```python
Wpa.favOrUnFavComic("60f5aab6e239c4708507c5d9")

# The first parameter is the comic ID
```

Return Dictionary:

```python
{'code': 200, 'message': 'success'}
```

Ditto; the first time it was a favorite, the second time it was an unfavorite.

#### Comments

```python
Wpa.getComicComments("60f5aab6e239c4708507c5d9", "1")

# The first parameter is the comic ID

# The second parameter indicates the page number of the comment, counting from 1
```

Return Dictionary:

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

#### Post a comment

```python
Wpa.postComicComment("60f5aab6e239c4708507c5d9", "支持")

# The first parameter is the comic ID

# The second parameter indicates the content of the comment
```

I'm not sure what will return, and I don't have the courage to give my opinion.

### Leaderboard

There are four categories: daily leaderboard, weekly leaderboard, monthly leaderboard and knight leaderboard.

#### Get daily leaderboard

```python
Wpa.getH24LeaderBoard()
```

Return Dictionary:

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

#### Get weekly leaderboard

```python
Wpa.getD7LeaderBoard()
```

The return format is the same as above, as is the monthly leaderboard.

#### Get monthly leaderboard

```python
Wpa.getD30LeaderBoard()
```

#### Get knight leaderboard

```python
Wpa.knightLeaderBoard()
```

Return Dictionary:

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

### Person

#### Login

```python
Wpa.login("username", "password")
```

Return token.

#### Register

```python
Wpa.register("pywazi2022", "pywazi2022520", 0, "m", "深空時計", [{"question": "是为了什么而流着血", "answer": "是为了谁而流眼泪"}, {"question": "我躲在夜里取笑着黑", "answer": "因为没有人能杀死鬼"}, {"question": "鬼", "answer": "草东没有派对"}])

# The first parameter indicates the user name and requires the regular expression: /^(?!.*\\.\\.)(?!.*\\.$)[^\\W][\\w.]{0,29}$/i

# The second parameter indicates the plaintext password

# The third parameter indicates the birthday, and it is not clear whether it is accurate to the second

# The fourth parameter indicates gender. support m (female), f (male) and bot (robot)

# The fifth parameter indicates the nickname

# The sixth parameter is a list that requires three dictionaries, with only two keys, question and answer, corresponding to the three secret questions
```

Return Dictionary:

```python
{'code': 200, 'message': 'success'}
```

#### Punch in

```python
Wpa.punchIn()
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'res': {'status': 'ok', 'punchInLastDay': '2021-08-04'}}}
```

#### Get published comments

```python
Wpa.getMyComments(1)

# The first parameter indicates the page number, counting from 1
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'comments': {'docs': [], 'total': 0, 'limit': 20, 'page': '1', 'pages': 1}}}
```

#### Get favorite comics

```python
Wpa.getMyFavourites(1, "ld")

# The first parameter indicates the page number, counting from 1

# The second parameter indicates the sorting method, which seems to be only from new to old or old to new
```

Return Dictionary:

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

#### Get personal information

```python
Wpa.getMyProfile()
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'user': {'_id': '5f92f94fa94c02192e0d5c6a', 'birthday': '1999-10-08T00:00:00.000Z', 'email': 'yazawazi520', 'gender': 'f', 'name': '鸭杂袜子', 'slogan': '你所热爱的，就是你的生活。', 'title': '萌新', 'verified': False, 'exp': 720, 'level': 3, 'characters': ['dirty'], 'created_at': '2020-10-23T15:39:59.824Z', 'avatar': {'originalName': 'avatar.jpg', 'path': '1e649daf-9f96-4a8f-9a95-4a77a7f84f00.jpg', 'fileServer': 'https://storage1.picacomic.com'}, 'isPunched': True, 'character': 'https://pica-pica.wikawika.xyz/special/frame-dirty.png?r=3'}}}
```

#### Upload avatar

```python
Wpa.uploadAvatar({"type": "file", "path": "./avatar.jpeg"})
Wpa.uploadAvatar({"type": "base64", "format": "jpeg", "data": "qwertyuiopasdfghjklzxcvbnm"})

# The first one is to upload via file: type -> file, path enter the path of your avatar file

# The second is to upload directly via base64: type enter base64, format enter the type of your avatar file, data enter the base64 value of your avatar file
```

Return Dictionary:

```python
{'code': 200, 'message': 'success'}
```

#### Reset password

```python
Wpa.resetPassword("username", 1, "answer")

# The first parameter indicates the user name

# The second parameter indicates the number of the question

# The third parameter indicates the answer to the question
```

When I tested it returned:

```python
{'code': 400, 'error': '1015', 'message': 'invalid request', 'detail': ':('}
```

#### Forgot password

```python
Wpa.forgotPassword("username")

# The first parameter indicates the user name
```

When I tested it returned:

```python
{'code': 400, 'error': '1015', 'message': 'invalid request', 'detail': ':('}
```

#### Change password

```python
Wpa.changePassword("old password", "new password")

# The first parameter indicates your old password

# The second parameter indicates your new password
```

Return Dictionary:

```python
{'code': 200, 'message': 'success'}
```

#### Change nickname

```python
Wpa.changeDisplayName("username", "new nickname")

# The first parameter indicates your username

# The second parameter indicates your new nickname
```

Officially, it's not available right now.

#### Change slogan

```python
Wpa.changeSlogan("new slogan")

# The first parameter indicates your new slogan
```

Return Dictionary:

```python
{'code': 200, 'message': 'success'}
```

#### Change Q&A

```python
Wpa.changeQA([{"q": "First question", "a": "First answer"}, {"q": "Second question", "a": "Second answer"}, {"q": "Third question", "a": "Third answer"}])
```

Return Dictionary:

```python
{'code': 200, 'message': 'success'}
```

### Game

#### Get games

```python
Wpa.getGames(1)

# The first parameter indicates the page number, counting from 1
```

Return Dictionary:

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

#### Get game information

```python
Wpa.getGameInfo("5ded08947cd2ce4ed0f5e101")

# The first parameter indicates the game ID, which is visible in _id
```

Return Dictionary:

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

#### Like or unlike

```python
Wpa.likeOrUnLikeGame("5ded08947cd2ce4ed0f5e101")

# The first parameter indicates the game ID
```

The same comic like: the first time is like, the second time is cancel like, return to the content is not repeated.

#### Comments

```python
Wpa.getGameComments("5ded08947cd2ce4ed0f5e101", "1")

# The first parameter indicates the game ID

# The second parameter indicates the page of the comment distinction, counting from 1
```

The same as the comics to get comments, the return content will not be repeated.

#### Post a comment

```python
Wpa.postGameComment("5ded08947cd2ce4ed0f5e101", "非常支持")

# The first parameter indicates the game ID

# The second parameter indicates the content of the comment
```

I'll be honest: I don't dare to comment or test. Try it yourselves.

### Comment

#### Like or unlike

```python
Wpa.likeOrUnLikeComment("612b191cb3a8b0f946b87139")

# The first parameter indicates the comment ID
```

I dare not test, you guys test it.

#### Hide or unhide

```python
Wpa.hideOrUnHideComment("612b191cb3a8b0f946b87139")

# The first parameter indicates the comment ID
```

I don't have permission, it returns 1005.

#### Get children

```python
Wpa.getCommentsChildren("60fc1228af308a2d7d7c2991")

# The first parameter indicates the comment ID
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'comments': {'docs': [{'_id': '60feee91b2ce8a24cbed7cae', 'content': '天…天堂…', '_user': {'_id': '5d048a078297f2110498899c', 'gender': 'f', 'name': 'Blue Pink', 'title': '萌新', 'verified': False, 'exp': 1640, 'level': 4, 'characters': [], 'role': 'member', 'avatar': {'originalName': 'avatar.jpg', 'path': '77b6f4c6-3681-4332-9ef2-ecd6cd15b598.jpg', 'fileServer': 'https://storage1.picacomic.com'}, 'slogan': '1', 'character': 'https://pica-web.wakamoment.tk/images/halloween_f.png'}, '_parent': '60fc1228af308a2d7d7c2991', '_comic': '60f5aab6e239c4708507c5d9', 'isTop': False, 'hide': False, 'created_at': '2021-07-26T17:19:13.003Z', 'id': '60feee91b2ce8a24cbed7cae', 'likesCount': 4, 'isLiked': False}, {'_id': '60fd1d70eacb85326231bf73', 'content': '有就怪了', '_user': {'_id': '5b744884d179b4579b3c5b22', 'gender': 'm', 'name': '离殇ボ', 'title': '萌新', 'verified': False, 'exp': 590, 'level': 2, 'characters': [], 'role': 'member', 'avatar': {'fileServer': 'https://storage1.picacomic.com', 'path': '3d3f9619-a386-4a46-9ca7-49fe8db8b4cd.jpg', 'originalName': 'avatar.jpg'}, 'slogan': 'null', 'character': 'https://pica-web.wakamoment.tk/images/halloween_m.png'}, '_parent': '60fc1228af308a2d7d7c2991', '_comic': '60f5aab6e239c4708507c5d9', 'isTop': False, 'hide': False, 'created_at': '2021-07-25T08:14:40.035Z', 'id': '60fd1d70eacb85326231bf73', 'likesCount': 0, 'isLiked': False}], 'total': 2, 'limit': 5, 'page': '1', 'pages': 1}}}
```

#### Reply

```python
Wpa.replyComment("60fc1228af308a2d7d7c2991", "真的会有吗")

# The first parameter indicates the comment ID

# The second parameter indicates the content of the comment
```

#### Report

```python
Wpa.reportComment("60fc1228af308a2d7d7c2991")

# The first parameter indicates the comment ID
```

#### Top

```python
Wpa.topComment("60fc1228af308a2d7d7c2991")

# The first parameter indicates the comment ID
```

May return 1005.

### Management

#### Set title

```python
Wpa.setTitle("5f92f94fa94c02192e0d5c6a", "awa")

# The first parameter indicates the user ID

# The second parameter indicates title
```

When I tested it, it returned:

```python
{'code': 400, 'error': '1015', 'message': 'invalid request', 'detail': ':('}
```

#### Modify experience

```python
Wpa.adjustExp("5f92f94fa94c02192e0d5c6a", 7200)

# The first parameter indicates the user ID

# The second parameter indicates the experience value
```

When I tested it, it returned:

```python
{'code': 404, 'error': '1007', 'message': 'not found', 'detail': ':('}
```

#### Remove user comments

```python
Wpa.removeComment("5f92f94fa94c02192e0d5c6a")

# The first parameter indicates the user ID
```

When I tested it, it returned:

```python
{'code': 401, 'error': '1007', 'message': 'not found', 'detail': ':('}
```

#### Block user

```python
Wpa.blockUser("5f92f94fa94c02192e0d5c6a")

# The first parameter indicates the user ID
```

When I tested it, it returned:

```python
{'code': 404, 'error': '1007', 'message': 'not found', 'detail': ':('}
```

#### Get dirty

```python
Wpa.getUserDirty("5f92f94fa94c02192e0d5c6a")

# The first parameter indicates the user ID
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'dirty': False}}
```

#### Get user profile

```python
Wpa.getUserProfile("5f92f94fa94c02192e0d5c6a")

# The first parameter indicates the user ID
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'user': {'_id': '5f92f94fa94c02192e0d5c6a', 'gender': 'f', 'name': '鸭杂袜子', 'slogan': '你所热爱的，就是你的生活。', 'title': '萌新', 'verified': False, 'exp': 720, 'level': 3, 'avatar': {'originalName': 'avatar.jpg', 'path': '1e649daf-9f96-4a8f-9a95-4a77a7f84f00.jpg', 'fileServer': 'https://storage1.picacomic.com'}}}}
```

### Download

#### Download cover

```python
Wpa.getThumbImage("60f5aab6e239c4708507c5d9", "./")

# The first parameter indicates the comic ID

# The second parameter indicates the download path
```

Return String:

```python
'./ホクロ流星群せかんど [中国翻訳] [DL版]\\thumb_QQ图片20210718224515.png'
```

#### Download comic

```python
Wpa.downloadComic("60f5aab6e239c4708507c5d9", "./")

# The first parameter indicates the comic ID

# The second parameter indicates the download path
```

Return `Done! / 完工！` after success.

### APP

#### Get chat room

```python
Wpa.getChat()
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'chatList': [{'title': '嗶咔大眾澡堂', 'description': '這是一個讓大家討論本子和二次元的地方，開二次元車是歡迎的，同時歡迎成人話題討論，但請低調！', 'url': 'https://chat-public.wikawika.xyz', 'avatar': 'https://pica-pica.wikawika.xyz/images/chat-public.jpg'}, {'title': '嗶咔養老組織群', 'description': '歡迎各位過氣的官方、管理和熟人到這群交流養老心得。如果你被嗶咔服務器君打壓也歡迎你到這訴苦', 'url': 'https://chat-old.wikawika.xyz', 'avatar': 'https://pica-pica.wikawika.xyz/images/chat-old.jpg'}]}}
```

#### Get apps

```python
Wpa.getAPPs()
```

Return Dictionary:

```python
{'code': 200, 'message': 'success', 'data': {'apps': [{'title': '嗶咔包養', 'url': 'https://donate.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/support-app.jpg', 'showTitleBar': False, 'description': '透過 BitCoin 支援嗶咔 漫畫'}, {'title': '嗶咔商店', 'url': 'https://online-shop-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-shop.jpg', 'showTitleBar': False, 'description': '嗶咔商店，買買買!'}, {'title': '嗶咔鍋貼', 'url': 'https://post-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-post.jpg', 'showTitleBar': False, 'description': '嗶咔鍋貼，一起讓騎士們分享生活和快樂的地方'}, {'title': '嗶咔運動', 'url': 'https://move-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-move.jpg', 'showTitleBar': False, 'description': '嗶咔運動， 圖動起來'}, {'title': '嗶咔公會', 'url': 'https://group.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/group-app.jpg', 'showTitleBar': False, 'description': '嗶咔公會一個嶄新的社交小程序'}, {'title': '嗶咔小電視 beta', 'url': 'https://tv.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/tv-app.jpg', 'showTitleBar': True, 'description': '精彩影片不斷放送，不支援 iOS'}, {'title': '嗶咔小電影', 'url': 'https://av.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/movie-app.jpg', 'showTitleBar': False, 'description': '精彩小電影讓你看到飽嗎？！'}, {'title': ' 嗶咔小里番', 'url': 'https://h.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/h-app.jpg', 'showTitleBar': False, 'description': '里番之家'}, {'title': '嗶咔小黃油', 'url': 'https://game.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/game-app.jpg', 'showTitleBar': False, 'description': '電腦小黃油介紹'}, {'title': '嗶咔小禮物', 'url': 'https://gift-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-gift.jpg', 'showTitleBar': False, 'description': '福利盡在嗶咔小禮物'}, {'title': '嗶咔畫廊', 'url': 'https://paint-web.wikawika.xyz', 'icon': 'https://pica-pica.wikawika.xyz/images/picacomic-paint.jpg', 'showTitleBar': False, 'description': '由著名畫帥繪畫的嗶咔 相關作品'}]}}
```

#### Get android apps

```python
Wpa.getAndroidAPPs(1)

# The first parameter indicates the page number, counting from 1
```

Return Dictionary:

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
