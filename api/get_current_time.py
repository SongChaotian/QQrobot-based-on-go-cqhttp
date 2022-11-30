import datetime
import time
import threading

from api.curriculum import send_class_table
from api.weather_query import get_the_weather
from send_message.send_message import send_private_msg, send_group_msg

"""
格式化成我们想要的日期：strftime（）
%d 日期, 01-31
%f 小数形式的秒，SS.SSS
%H 小时, 00-23
%j 算出某一天是该年的第几天，001-366
%m 月份，00-12
%M 分钟, 00-59
%s 从1970年1月1日到现在的秒数
%S 秒, 00-59
%w 星期, 0-6 (0是星期天)
%W 算出某一天属于该年的第几周, 01-53
%Y 年, YYYY
%% 百分号
"""


def get_current_time():
    while True:
        now_time = datetime.datetime.now().strftime('%H:%M:%S')  # 获取当前日期和时间
        print(now_time)
        if now_time == "08:00:00":
            weather_message = get_the_weather()
            send_group_msg(747668503, weather_message)
            time.sleep(1)
        elif now_time == "21:30:00":
            tomorrow_schedule_message = send_class_table("课表 明天 21数二")
            send_group_msg(747668503, tomorrow_schedule_message)
            time.sleep(1)
        time.sleep(0.5)  # 每0.2秒获取一次系统时钟


if __name__ == '__main__':
    t = threading.Thread(target=get_current_time)
    t.start()
