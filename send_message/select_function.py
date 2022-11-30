from api.curriculum import send_class_table
from api.weather_query import get_the_weather
from api.juhe_api import *


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
