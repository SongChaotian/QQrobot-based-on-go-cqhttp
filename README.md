# 😝Part_ONE 总体设计

## 1 环境部署

### 1.1 开发环境

- 编译器：`PyCharm Community Edition 2022.2.3` , 下载网址：[PyCharm官网](https://www.jetbrains.com/pycharm/)
- `Python`版本：`3.9.13`， 下载网址：[Python官网](https://www.python.org/)
- 借用`go-cqhttp`框架：[go-cqhttp帮助中心](https://docs.go-cqhttp.org/) ， 选择`windows`版本进行下载，配置好`QQ`账号和`http、post`处的地址设置【要与代码中的地址保持一致性】



### 1.2 Windows下环境部署

####  1.2.1 服务端：

1. 将代码clone到本地，用Pycharm打开
2. 在Pycharm中为项目配置Python解释器， 然后需要在虚拟环境中安装`flask`、`requests`、`openpyxl`、`paddlepaddle`、`paddlenlp`模块。
   - 先点击`文件`------>`设置` ----->`项目`----->`Python解释器`，点击`+`号将pip更新为最新版本`22.3.1`（该版本在我使用时为最新）
   - 然后前三个模块比较小，直接鼠标悬浮在关键字下面，等Pycharm提示安装消息点击安装即可，
   - 后面两个模块比较大，建议用如下两个指令，切换镜像来下载安装

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple paddlepaddle==2.4.0
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple paddlenlp==2.4.4
```

#### 1.2.2 go-cqhttp端：

1. 下载：

   - 从[release](https://github.com/Mrs4s/go-cqhttp/releases)界面下载最新版本的go-cqhttp，建议下载`压缩文件`

   - |    系统类型    |          可执行文件           |            压缩文件             |
     | :------------: | :---------------------------: | :-----------------------------: |
     | Intel 版 Macos |         Not available         | `go-cqhttp_darwin_amd64.tar.gz` |
     |  M1 版 Macos   |         Not available         | `go-cqhttp_darwin_arm64.tar.gz` |
     |  32 位 Linux   |         Not available         |  `go-cqhttp_linux_386.tar.gz`   |
     |  64 位 Linux   |         Not available         | `go-cqhttp_linux_amd64.tar.gz`  |
     |  arm64 Linux   |         Not available         | `go-cqhttp_linux_arm64.tar.gz`  |
     |  armv7 Linux   |         Not available         | `go-cqhttp_linux_armv7.tar.gz`  |
     | 32 位 Windows  |  `go-cqhttp_windows_386.exe`  |   `go-cqhttp_windows_386.zip`   |
     | 64 位 Windows  | `go-cqhttp_windows_amd64.exe` |  `go-cqhttp_windows_amd64.zip`  |
     | arm64 Windows  | `go-cqhttp_windows_arm64.exe` |  `go-cqhttp_windows_arm64.zip`  |
     | armv7 Windows  | `go-cqhttp_windows_armv7.exe` |  `go-cqhttp_windows_armv7.zip`  |

   - 以系统类型`64位Windows`为例，下载压缩文件`go-cqhttp_windows_amd64.zip`

2. 解压：Windows下请使用自己熟悉的解压软件自行解压

3. 使用：

   - 双击`go-cqhttp_*.exe`,根据提示生成运行脚本
   - 双击运行脚本，输入数字`0`，选择HTTP通信，按`Enter`后生成默认配置文件`config.yml`

   - 参照[config.md](https://github.com/Mrs4s/go-cqhttp/blob/master/docs/config.md)修改配置文件`config.yml`

   - ```
     （主要是配置一下：QQ账号、密码、和监听端口号）
     第4行：uin  # QQ账号
     第5行：password  # 密码为空时使用扫码登录
     第96行：address: 0.0.0.0:10087 # HTTP监听地址(用于接收消息)
     第104行：url: http://0.0.0.0:10088/  # 返向HTTP POST地址(用于发送消息)
     ```

   - 双击运行脚本`go-cqhttp.bat`,登录后即可使用，如果还需要使用程序中的发送视频的功能，还需要安装ffmpeg。

4. 安装ffmpeg

   - 为了支持任意格式的语音发送, 你需要安装 ffmpeg 。

   - 从这里 [这里](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z) 下载 并解压, 并为 `bin` 这个文件夹添加环境变量。

   - 如果遇到下载速度缓慢的问题可以用 [这个源](https://downloads.go-cqhttp.org/ffmpeg-release-full.7z) 。

   - 然后在 cmd 输入 **(不能使用 powershell）**

   - ```shell
     setx /M PATH "C:\Program Files\ffmpeg\bin;%PATH%"
     ```

     自行将这个指令中的 `C:\Program Files` 替换成你的解压目录。



### 1.3 需求分析

- 天气查询
- 心灵鸡汤
- 每日笑话
- 星座配对
- 生日花语
- 课表推送【只针对`HNUST`教务网导出的课表】
- 。。。。等的推送与实时查询

> 通过`go-cqhttp`框架，采用`flask`轻量级服务器，编写一款能实现在后端登录一个机器人`QQ`账号，从而实现信息的推送



### 1.4 参考资料

- `go-cqhttp`: [go-cqhttp 帮助中心](https://docs.go-cqhttp.org/)

- 专业实况天气接口：[实况天气接口](http://www.yiketianqi.com/index/doc?version=v61)

- 实时降水, 降雨量接口：[实时降水降雨](http://www.yiketianqi.com/index/doc?version=v11)

- 聚合数据：获取各种`API`【[聚合数据](https://dashboard.juhe.cn/home)】

- 表情`CQ`码`ID`表：[CQ码](https://github.com/kyubotics/coolq-http-api/wiki/表情-CQ-码-ID-表)

  

### 1.5 设计流程

> 1. 需求分析
> 2. 确定框架
> 3. 资源准备
> 4. 代码敲定
> 5. 调试代码
> 6. 总结分析



# 😝Part_TWO 详细模块设计

## 2.1 `server.py` ：核心模块

> 作为项目的中枢，用于接收客户端发送的请求，并对其处理，将后端处理的结果返还给客户端。

**一个人工智能--交互式闲聊对话**

```
# 基于PLATO-MINI，模型在十亿级别的中文对话数据上进行了预训练，闲聊场景对话效果显著。
# 调用Taskflow工具集，智能对原始信息进行回复
dialogue = Taskflow("dialogue")
# 通过PaddleNLP中的Taskflow工具集，智能对原始信息进行回复，join函数用于去除方括号[]
s_message = " ".join(dialogue([raw_message]))
```

**1. 私聊消息；2. 群聊消息；3. 智能回复**

```
app = Flask(__name__)  # 监听端口，获取QQ信息
@app.route('/', methods=["POST"])  # 路由
def post_data():
    """下面的request.get_json().get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式"""
    if request.get_json().get('message_type') == 'private':  # 如果是私聊信息
        user_id = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        raw_message = request.get_json().get('raw_message')  # 获取原始信息
        s_message = select_function(raw_message)
        if len(s_message) != 0:
            send_private_msg(user_id, s_message)

    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        group_id = request.get_json().get('group_id')  # 获取群号
        raw_message = request.get_json().get('raw_message')  # 获取原始信息
        if '[CQ:at,qq=xxxx]' in raw_message:  # 如果@机器人则智能回复
            # 通过PaddleNLP中的Taskflow工具集，智能对原始信息进行回复，join函数用于去除方括号[]
            s_message = " ".join(dialogue([raw_message]))
        else:
            s_message = select_function(raw_message)
        if len(s_message) != 0:
            send_group_msg(group_id, s_message)
    return 'OK'
```

**主入口**

```
def main():
    t = threading.Thread(target=get_current_time)
    t.start()
    app.run(debug=True, host='127.0.0.1', port=5000)  # 此处的 host和 port对应上面 yml文件的设置

if __name__ == '__main__':
    main()
```

## 2.2 `send_message` 模块

> 主要分为俩个模块：
>
> 1. 对传入的消息进行功能的选择，获取到相应的数据
> 2. 发送消息的模块：私人消息和群消息，根据传入的信息将数据传给用户

### 2.2.1 `select_function.py` ：功能选择

**人为设置对消息的处理，并获取相应的结果**

```
def select_function(raw_message):
    s_message = ""
    if raw_message == "帮助" or raw_message == "help":
        s_message = get_help_message()
    elif raw_message == "天气查询" or raw_message == "天气" or raw_message == "tianqi" or raw_message == "tian qi" or raw_message == "weather":
        s_message = get_the_weather()
    elif raw_message[0:2] == "课表":
        s_message = send_class_table(raw_message)
    elif raw_message == '鸡汤' or raw_message == 'ChickenSoup':
        s_message = get_chicken_soup()
    elif raw_message == '笑话' or raw_message == 'joke':
        s_message = get_joke()
    elif raw_message == 'setu':
        s_message = get_setu()
    elif raw_message == '视频' or raw_message == '播放视频':
        s_message = get_video()
    elif raw_message[0:4] == '星座匹配':
        s_message = get_ConstellationPairing(raw_message)
    elif raw_message[0:4] == '生日花语':
        s_message = get_birthdayFlower(raw_message)
    return s_message
```

**告知用户我们的功能有哪些**

```
def get_help_message():
    help_message = "可根据所需功能，输入相应字段得到想到结果\n" \
                   "功能（1）：查询今日天气\n" \
                   "天气查询 | 天气 | tianqi | tian qi | weather\n" \
                   "功能（2）：查询近三天的课表\n" \
                   "课表 + 今天or明天or后天 + 班级\n" \
                   "例：课表 后天 19物一  \n" \
                   "功能（3）：享受每日鸡汤\n" \
                   "鸡汤 | ChickenSoup \n" \
                   "功能（4）：享受每日笑话\n" \
                   "笑话 | joke \n" \
                   "功能（5）：随机setu\n" \
                   "setu \n" \
                   "功能（6）：播放视频\n" \
                   "视频 | 播放视频 \n" \
                   "功能（7）：查询生日花语\n" \
                   "生日花语 YYYY-MM-DD \n" \
                   "功能（8）：星座匹配结果\n" \
                   "星座匹配 男生星座 女生星座\n" \
                   "例：星座匹配 双子 金牛  \n" \
                   "其他情况下@机器人会智能回复喔"
    return help_message
```

### 2.2.2 `send_message.py`：传送消息

**传送私人消息**

```
def send_private_msg(user_id, message):
    send_private_msg_url = 'http://127.0.0.1:10087/send_private_msg'
    params = {
        'user_id': user_id,
        'message': message,
    }
    requests.get(send_private_msg_url, params).json()
```

**传送群聊消息**

```
def send_group_msg(group_id, message):
    send_group_msg_url = 'http://127.0.0.1:10087/send_group_msg'
    params = {
        'group_id': group_id,
        'message': message,
    }
    requests.get(send_group_msg_url, params).json()
```



## 2.3 `API`模块

### 2.3.1 `weather_query.py`：天气查询

> 接口：`https://v0.yiketianqi.com/api`，再人为获取我们需要的内容，此处用的是专业实况天气接口v62和 实时降水, 降雨量接口，此处只展示部分代码，读者可根据自身需求定义

```
def get_the_weather():
    weather_url = 'https://v0.yiketianqi.com/api'
    params_v62 = {
        'appid': " ", # 自己获取
        'appsecret': " ", # 自己获
        'version': "v62",
        'city': "湘潭",
        'unescape': "1",  # json不被unicode, 直接输出中文
    }
    weather_v62_res = requests.get(weather_url, params_v62).json()
    week = weather_v62_res["week"]
    city = weather_v62_res["city"]
    tem = weather_v62_res["hours"][0]["tem"]
    wea = weather_v62_res["hours"][0]["wea"]
    aqi = weather_v62_res["hours"][0]["aqi"]
    aqinum = weather_v62_res["hours"][0]["aqinum"]
    tem1 = weather_v62_res["tem1"]
    tem2 = weather_v62_res["tem2"]
    win = weather_v62_res["hours"][0]["win"]
    s_message = f'{city}\n' \
                f'{time}，{week}\n' \
                f'气温{tem}度，{wea}\n' \
                f'{msg}\n' \
                f'最高温度:{tem1}度，最低温度:{tem2}度\n' \
                f'空气质量:{aqi}，指数:{aqinum}\n' \
                f'{win}，风力{win_speed}\n' \
                f'湿度:{humidity}，能见度:{visibility}\n' \
                f'气压:{pressure}\n\n' \
                f'消息更新时间:\n' \
                f'{update_time}'

    return s_message
```

### 2.3.2 `curriculum.py`：课表查询

> 用于获取课表信息，定义一个课程类，获取每一节课的课程名、时间和地点，此处用到了正则表达式的相关内容，需要对课表进行解析，获取我们需要的内容。【只针对从`HNUST`教务处导出的课表】

**课程类**

```
class Curriculum:
    # 星期几对应excel表中的哪一列
    week_to_char = {
        '星期一': 'B',
        '星期二': 'C',
        '星期三': 'D',
        '星期四': 'E',
        '星期五': 'F',
        '星期六': 'G',
        '星期日': 'H'
    }
    # 把excel中的行转换为对应的上课时间
    row_to_jie = {
        4: '时间:08:00-09:40',
        5: '时间:10:00-11:40',
        6: '时间:14:00-15:40',
        7: '时间:16:00-17:40',
        8: '时间:19:00-20:40'
    }

    def __init__(self, class_time, name, class_classroom):
        self.class_time = class_time  # 上课时间
        self.name = name  # 课程名称
        self.class_classroom = class_classroom  # 上课地点

    # 输入参数，schedule: 第几周， week： 星期几， day： 几月几日
    # which_day: 今天、明天、后天
    # class_tag: 19物一
    @classmethod
    def excel_to_print(cls, which_day, class_tag, schedule, week, day):
        """
        第二步: 从文件中读取课表
        """
        # print(f'../static/{class_tag}.xlsx')
        wb = load_workbook(f'static/{class_tag}.xlsx')  # 读取excel档案
        ws = wb.active  # 打开预设的工作表,等价于 -> ws = wb['Sheet1']
        class_num = 0  # 用来统计今天的课程数
        curriculum_list = []  # 用来储存curriculum对象
        for row in range(4, 8 + 1):  # 读取第4行到第8行,即第一二节、第三四节、第五六节、第七八节、第九十节
            char = Curriculum.week_to_char[week]  # 读取第char列的数据
            my_class = ws[char + str(row)].value  # 按char列读取当天的课表
            # print(my_class)
            # print("----")
            if my_class is not None:
                start_week = int("".join(re.findall(r"\n(\d+)", my_class)))  # 用正则表达式匹配课程的起始周， 4-15([周])， 4前面是换行\n，4后面是-
                end_week = int("".join(re.findall(r"(\d+)\(", my_class)))  # 用正则表达式匹配课程的结束周， 4-15([周])， 15前面是-， 15后面是(
                if start_week <= schedule <= end_week:  # 如果说当前schedule处在课程教学周，代表今天有这节课
                    class_num = class_num + 1
                    class_name = "".join(re.findall(r"^(.*)", my_class))
                    classroom = "".join(re.findall(r"]\n(.*)$", my_class))
                    curriculum_list.append(
                        Curriculum(Curriculum.row_to_jie[row], class_name, classroom))  # 加入到今天的课程list中

        class_table_msg = ""
        if class_num != 0:
            class_table_msg = class_table_msg + f"{class_tag}的同学们，你们{which_day}有{class_num}节课:\n\n" \
                                                "课表信息:\n"
            for class_info in curriculum_list:
                class_table_msg = class_table_msg + f"{class_info.name}\n" \
                                                    f"{class_info.class_time}\n" \
                                                    f"地点:{class_info.class_classroom}\n\n"
            class_table_msg = class_table_msg + f"上课日期:\n" \
                                                f"第{schedule}周 {week}({day.strftime('%m月%d日')}）"
        else:
            class_table_msg = class_table_msg + f'{which_day}没课，好好happy吧！'
        return class_table_msg
```

**发送课表消息**

> 定义第一周的第一天的日期，获取日期，计算当前是第几周星期几，发送课表信息

```
def send_class_table(raw_message):
    week_list = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
    first_date = date(2022, 9, 5)  # 新学期第一周的第一天
    try:
        which_day = raw_message.split(' ')[1]
        if which_day == "今天":
            search_date = date.today()  # 获取今天的日期
        elif which_day == "明天":
            search_date = (date.today() + timedelta(days=1))  # 获取明天的日期
        elif which_day == "后天":
            search_date = (date.today() + timedelta(days=2))  # 获取后天的日期
        search_in_schedule = ((search_date - first_date).days // 7) + 1  # 计算处在第几周
        # 格式化日期：strftime('%w'),  %w 星期, 0-6 (0是星期天)
        search_week = week_list[int(search_date.strftime('%w'))]  # 计算处在星期几
        class_table_msg = "【课表提醒】\n" + Curriculum.excel_to_print(which_day, raw_message.split(' ')[2], search_in_schedule,search_week, search_date)
    except FileNotFoundError as fe:
        return f"{raw_message.split(' ')[2]} 的课表目前还没有收录到数据库"
    except Exception as e:
        return "输入格式有误\n" \
               "例：课表 后天 21数二  \n"
    else:
        return class_table_msg
```

### 2.3.3 `juhe_api.py`：其他功能

> 从聚合数据上申请的`API`接口，此处只展示一个功能的代码，其他功能类似，可根据自身需求进行修改即可

**心灵鸡汤**

```
# 每日心灵鸡汤语录， API地址: https://www.juhe.cn/docs/api/id/669
def get_chicken_soup():
    chicken_soup_url = 'https://apis.juhe.cn/fapig/soup/query'  # 聚合数据，API地址
    params = {
        'key': "xx", # 聚合数据上获取即可
    }
    try:
        chicken_soup_res = requests.get(chicken_soup_url, params).json()
        chicken_soup_text = chicken_soup_res['result']['text']
        chicken_soup_msg = f"今日鸡汤:\n" \
                           f"[CQ:face,id=171]{chicken_soup_text}"
    except Exception as e:
        return "今天的查询次数超过上限啦，明天再来看看吧！"
    else:
        return chicken_soup_msg
```

**发送视频**

```
def get_video():
    video_url = 'http://106.52.78.177/wp-content/uploads/2022/10/1.mp4'
    video_msg = f"[CQ:video,file={video_url}]"
    return video_msg
```

> 备注：此处用到了`CQ`码，可以直接查询对应需求的标准就可【开头已附链接】

### 2.3.4 `get_current_time.py`：获取当前时间

> 此处设置的是一个自动发送消息的接口，将程序挂在服务器上，此处设置的是早上八点发送当天的天气情况，晚上9点发送明天的课表情况，读者可根据实际需求自定义，只需获取一下当前时间即可。
>
> ```
> now_time = datetime.datetime.now().strftime('%H:%M:%S')  # 获取当前时间
> ```



## 2.4 `static` 模块

- 存放`resource`文件，此项目用于存放课表文件



# 😝 Part_THREE 效果展示

## 3.1 `go-cqhttp` 框架

![在这里插入图片描述](https://img-blog.csdnimg.cn/50dd411fb34d436ca85e740a1f5acd56.jpeg#pic_center)

## 3.2 `Pycharm` 端

[![zJsVwn.png](https://img-blog.csdnimg.cn/img_convert/044fc99ca49e87e5efb2b9a2bc60581d.png)](https://imgse.com/i/zJsVwn)

## 3.3 功能帮助

[![zJsWp8.png](https://img-blog.csdnimg.cn/img_convert/c3f82ed74f16108831e61ba72cdddddb.png)](https://imgse.com/i/zJsWp8)

## 3.4 天气查询

[![zJs2ff.png](https://img-blog.csdnimg.cn/img_convert/6c109a279a868b7d0b15bba54f639b78.png)](https://imgse.com/i/zJs2ff)

## 3.5 课表查询

[![zwYmRO.png](https://img-blog.csdnimg.cn/img_convert/dfc9d8d884ea8f65302eae2d2724ffc5.png)](https://imgse.com/i/zwYmRO)

## 3.6 心灵鸡汤

[![zJsh6g.png](https://img-blog.csdnimg.cn/img_convert/035312e67f6094c5a354dc892186a047.png)](https://imgse.com/i/zJsh6g)

## 3.7 每日笑话

[![zJs4XQ.png](https://img-blog.csdnimg.cn/img_convert/1e3abaea12f71ce0d98e868e18027379.png)](https://imgse.com/i/zJs4XQ)

## 3.8 生日花语

[![zJsImj.png](https://img-blog.csdnimg.cn/img_convert/1815b39d2231b9f7f3ce28da2f08e212.png)](https://imgse.com/i/zJsImj)

## 3.9 星座匹配

[![zJsT7n.png](https://img-blog.csdnimg.cn/img_convert/3d81398d2e14224f471659fde2e9dda8.png)](https://imgse.com/i/zJsT7n)

## 3.10 视频播放

[![zJsbt0.png](https://img-blog.csdnimg.cn/img_convert/b2ea8ac2c5f35d4d2cc00614dda3c66b.png)](https://imgse.com/i/zJsbt0)

## 3.11 智能回复

[![zJyih6.png](https://img-blog.csdnimg.cn/img_convert/2e6c8622539ea9b89d6c300fdaaa9ba3.png)](https://imgse.com/i/zJyih6)



# 😝 Part-FOUR 总结和体会

**1. 学习到了什么？**

> 1. Python Flask 的基本框架
> 2. 正则表达式的应用 -- 课表解析
> 3. `JSON` 的基本使用
> 4. `API` 获取
> 5. 交互式闲聊对话 --- `PaddleNLP`
> 6. 如何模块化代码

**2. 体会**

> 1. 加强专业知识的学习
> 2. 提高自身的代码能力
> 3. 不懂的问题多请教
> 4. 实践出真知

**3. 致谢**

> 感谢`Chaotian Song` 和 `OneWan`  在学习此项目期间的帮助！
