import requests


def get_the_weather():
    # 专业实况天气接口v62
    # 请求参数:
    # appid: 用户appid
    # appsecret: 用户appsecret
    # version: 接口版本标识, 固定值: v62 每个接口的version值都不一样
    # city: 城市名称, 不要带市和区; 如: 青岛、铁西
    # unescape: 是否转义中文, 如果您希望json不被unicode, 直接输出中文, 请传此参数: 1
    weather_url = 'https://v0.yiketianqi.com/api'
    params_v62 = {
        'appid': "78424162",
        'appsecret': "RAAx3FoE",
        'version': "v62",
        'city': "湘潭",
        'unescape': "1",  # json不被unicode, 直接输出中文
    }

    # 实时降水, 降雨量接口
    # 请求参数:
    # appid: 用户appid
    # appsecret: 用户appsecret
    # version: 接口版本标识, 固定值: v11 每个接口的version值都不一样
    # lng: 经度, 如: 119.545023
    # lat: 纬度, 如: 36.044254
    # point: 坐标体系, 默认百度坐标, 如使用高德坐标, 请传参: gaode
    params_v11 = {
        'appid': "78424162",
        'appsecret': "RAAx3FoE",
        'version': "v11",
        'lng': "112.7844",
        'lat': "27.78155",
        'point': "gaode",
    }

    weather_v62_res = requests.get(weather_url, params_v62).json()
    weather_v11_res = requests.get(weather_url, params_v11).json()
    week = weather_v62_res["week"]
    city = weather_v62_res["city"]
    tem = weather_v62_res["hours"][0]["tem"]
    wea = weather_v62_res["hours"][0]["wea"]
    aqi = weather_v62_res["hours"][0]["aqi"]
    aqinum = weather_v62_res["hours"][0]["aqinum"]
    tem1 = weather_v62_res["tem1"]
    tem2 = weather_v62_res["tem2"]
    win = weather_v62_res["hours"][0]["win"]
    win_speed = weather_v62_res["hours"][0]["win_speed"]
    humidity = weather_v62_res["humidity"]
    visibility = weather_v62_res["visibility"]
    pressure = weather_v62_res["pressure"]
    time = weather_v11_res["time"]
    msg = weather_v11_res["msg"]
    update_time = weather_v11_res["update_time"]

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


if __name__ == '__main__':
    data = get_the_weather()
    print(data)
