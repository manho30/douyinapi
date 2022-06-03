# 抖音无水印下载API
这是一个免费，开源，简单，方便的抖音无水印下载API。
## 功能
- 抖音视频/图集解析
- 抖音视频/图集无水印下载
## 文档
接口地址如下：

```text
https://douyinapi.herokuapp.com/api
```
请求参数：
- url：抖音视频链接


1. 网页版直接复制
```text
https://www.douyin.com/video/7102408528748367136
```


2. 口令
```text
0.58 XZZ:/ 女孩子主动找你，是因为她喜欢你，她不再主动找你，是因为你回的太敷衍，不是她不喜欢你了，是你让她觉得她很多余
%情感 %治愈 %热门 %爱情 %正能量 %励志 %动漫 %文案%小陌治愈驿站  https://v.douyin.com/FEUgdxn/ 复制此链接，打开Dou音搜索，直接观看视频！
```

3. 缩短版
```text
https://v.douyin.com/FEUgdxn/
```

### 请求格式
```
http://douyinapi.herokuapp.com/api?url=<链接>
```

### 返回格式
- 视频
```json
{
    "ok":true,
    "result":{
        "author":{
            "avatar":"https://p6.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_e70b935d905b7f6b7520df99105d79f0.jpeg?from=116350172",
            "douyin_id":"liu1111525",
            "name":"小陌治愈驿站",
            "singnature":"可能是世界上最萌的(小笨蛋呐）\n        生活虽苦·但你很甜\n文案|投稿|拿视频|🛰：liu08091111《备注来意》"
        },
        "details":"https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=7102408528748367136",
        "music":{
            "author":"小陌治愈驿站",
            "duration":"11",
            "title":"@小陌治愈驿站创作的原声一小陌治愈驿站",
            "url":"https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/7102408551435668254.mp3"
        },
        "video":{
            "descriptions":"女孩子主动找你，是因为她喜欢你，她不再主动找你，是因为你回的太敷衍，不是她不喜欢你了，是你让她觉得她很多余\n#情感 #治愈 #热门 #爱情 #正能量 #励志 #动漫 #文案#小陌治愈驿站",
            "statistics":{
                "comment_count":"280",
                "create_time":"1653658351",
                "hashtag":[
                    "情感",
                    "治愈",
                    "热门",
                    "爱情",
                    "正能量",
                    "励志",
                    "动漫",
                    "文案",
                    "小陌治愈驿站"
                ],
                "likes_count":"5449",
                "play_count":"0",
                "share_count":"898"
            },
            "thumbnail_url":{
                "url_list":"https://p3-sign.douyinpic.com/tos-cn-p-0015/8c715b06d7694e9dbd8638a3e37ca169~c5_300x400.jpeg?x-expires=1655445600&x-signature=%2Fy1XkaAJxl5wtqYnBAgec47CqAw%3D&from=4257465056_large&s=PackSourceEnum_DOUYIN_REFLOW&se=false&sc=cover&l=202206031410500102120562260C670A3C"
            },
            "video_url":{
                "free_watermark":"https://v3-dy-o.zjcdn.com/3a61c2623a10f55017f1c09c702d0048/6299b406/video/tos/cn/tos-cn-ve-15c001-alinc2/3cb2379e02b44a03bc7c5b446989b95f/?a=1128&ch=0&cr=0&dr=0&cd=0%7C0%7C0%7C0&cv=1&br=502&bt=502&btag=80000&cs=0&ds=3&ft=ArkXtBnZqI2mo0PsxA-fkVQChw79HKJ&mime_type=video_mp4&qs=0&rc=OTlnZWc3OzU4Njk2ZzxoaUBpam9lOTo6ZnRnZDMzNGkzM0AwMS5fMS5fNi8xNV4yNmExYSNzZWxxcjRvMjVgLS1kLTBzcw%3D%3D&l=20220603141051010212142149486457ED",
                "free_watermark_1080p":"https://v3-dy-o.zjcdn.com/efe309acc3ebfaa3096213cbebd7d846/6299b405/video/tos/cn/tos-cn-ve-15c001-alinc2/3cb2379e02b44a03bc7c5b446989b95f/?a=1128&ch=0&cr=0&dr=0&cd=0%7C0%7C0%7C0&cv=1&br=502&bt=502&btag=80000&cs=0&ds=3&ft=ArkXtBnZqI2mo0P_xA-fkVQChw79HKJ&mime_type=video_mp4&qs=0&rc=OTlnZWc3OzU4Njk2ZzxoaUBpam9lOTo6ZnRnZDMzNGkzM0AwMS5fMS5fNi8xNV4yNmExYSNzZWxxcjRvMjVgLS1kLTBzcw%3D%3D&l=2022060314105001020812110132618720",
                "watermark_url":"https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fg10000ca8d5qrc77u7t6obhlvg&ratio=720p&line=0"
            }
        }
    },
    "status":"200"
}
```
- 图集
```json
{
    "ok":true,
    "result":{
        "album":{
            "descriptions":"为什么初中生不给过六一🥹",
            "heigth":"1920",
            "image_url":[
                "https://p6-sign.douyinpic.com/tos-cn-i-0813/d5c19515b21a4998bfb4eb6e213a19f2~noop.webp?x-expires=1656828000&x-signature=Fjk055diBz%2BJGcl91ZgJjksRFDg%3D&from=4257465056&s=PackSourceEnum_DOUYIN_REFLOW&se=false&biz_tag=aweme_images&l=202206031427520102081001702A638141",
                "https://p26-sign.douyinpic.com/tos-cn-i-0813/f4966b6edbeb4f969e5b72a3c1959183~noop.webp?x-expires=1656828000&x-signature=WpbPrd5AimKgxH3U3%2Bz0yOY2gNk%3D&from=4257465056&s=PackSourceEnum_DOUYIN_REFLOW&se=false&biz_tag=aweme_images&l=202206031427520102081001702A638141",
                "https://p6-sign.douyinpic.com/tos-cn-i-0813/4daeaca0dc7a4fb6b65c18535bc82aed~noop.webp?x-expires=1656828000&x-signature=1XGk6RFThE7CIA8pt2CGiIWO3Ww%3D&from=4257465056&s=PackSourceEnum_DOUYIN_REFLOW&se=false&biz_tag=aweme_images&l=202206031427520102081001702A638141"
            ],
            "width":"1440"
        },
        "author":{
            "avatar":"https://p6.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_874da29bfe40af6fefca313eae3cbf59.jpeg?from=116350172",
            "douyin_id":"zaizai77480",
            "name":"深",
            "singnature":"深爱zxy\n真的超级无敌无敌爱颜哥！😍\n颜哥让我等他回来！那我就勉为其难等一下吧😮‍💨\n颜宝我等你😘无论多久我都等你.\n异地恋中……..🥺"
        },
        "details":"https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=7104629824668372264",
        "music":{
            "author":"Good life",
            "duration":"9",
            "title":"@Good life创作的原声一Good life",
            "url":"https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/7101290689490160397.mp3"
        },
        "statistics":{
            "comment_count":"14",
            "create_time":"1654175537",
            "hashtag":[],
            "likes_count":"1108",
            "play_count":"0",
            "share_count":"36"
        }
    },
    "status":"200"
}
```

## 本地使用
1. 克隆本代码仓库
```bash
$ git clone https://github.com/manho30/douyinapi.git
$ cd douyinapi
```

2. 安装依赖
```bash
$ pip install -r requirements.txt
```

3. 启动服务器
>服务器默认启动断口为 `5000`, 如不喜欢可更改`config.ini`中的 `port` 参数
```bash
$ python3 api.py
```

## 部署到服务器
本教程使用免费的Heroku服务器，如果你想部署到服务器， 可以接着下面的步骤：

1. 创建一个新的Heroku应用
2. 将代码部署到Heroku应用， 输入命令：
```bash
$ heroku git:remote -a <app_name>
$ git push heroku master
```
看不明白？
自己看看 YouTube

## 免责声明
本项目仅用于学习交流，如有侵权，请联系作者删除。

使用本项目所产生的法律责任，请自行承担。
