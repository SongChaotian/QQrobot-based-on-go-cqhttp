import requests
from random import randint
import re


# 每日心灵鸡汤语录， API地址: https://www.juhe.cn/docs/api/id/669
def get_chicken_soup():
    chicken_soup_url = 'https://apis.juhe.cn/fapig/soup/query'  # 聚合数据，API地址
    params = {
        'key': "14b12df87394785f5d585ea4bed65689",
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


# 笑话大全， API地址: https://www.juhe.cn/docs/api/id/95
def get_joke():
    joke_url = 'http://v.juhe.cn/joke/content/list.php'
    page = randint(1, 20)  # 从1-20页笑话中随机选一页
    params = {
        'sort': 'desc',  # 类型，desc:指定时间之前发布的，asc:指定时间之后发布的
        'page': page,  # 当前页数,默认1,最大20
        'pagesize': 20,  # 每次返回条数,默认1,最大20
        'time': "1418816972",  # 时间戳（10位），如：1418816972
        'key': "e271c8ea2cab71d8069718e642f7a394",
    }
    try:
        joke_res = requests.get(joke_url, params).json()
        item = randint(0, 19)  # 从返回的20条笑话中随机选一条
        joke_res_content = joke_res['result']['data'][item]['content']
        joke_msg = f"今日笑话:\n" \
                   f"[CQ:face,id=20]{joke_res_content}"
    except Exception as e:
        return "今天的查询次数超过上限啦，明天再来看看吧！"
    else:
        return joke_msg


# 生日花语， API地址: https://www.juhe.cn/docs/api/id/618
def get_birthdayFlower(birthday):
    try:
        birthday = birthday.split(' ')[1]
    except IndexError:
        return "输入格式有误\n" \
               "例:生日花语 2022-10-23  \n"
    birthdayFlower_url = 'http://apis.juhe.cn/fapig/birthdayFlower/query'
    params = {
        'keyword': birthday,  # 生日日期，如2021-01-01 或01-01
        'key': "29f9f91344198017d6a9e2042a1b8d18",
    }
    try:
        birthdayFlower_res = requests.get(birthdayFlower_url, params).json()
        title = birthdayFlower_res['result']['title']  # 标题
        name = birthdayFlower_res['result']['name']  # 生日花
        name_des = birthdayFlower_res['result']['name_des']  # 生日花含义
        name_des_re_list = re.findall(r"<p>(.+?)<", name_des)  # 正则匹配，去掉<p><\/p>,得到一个内容list
        name_des = name_des_re_list[0] + name_des_re_list[1]
        birthdayFlower_msg = f"{title}: {name}\n" \
                             f"{name_des}"
    except:
        return "请检查一下输入的生日格式是不是YYYY-MM-DD"
    else:
        return birthdayFlower_msg


# 星座配对 API地址: https://www.juhe.cn/docs/api/id/543
def get_ConstellationPairing(constellation):
    try:
        constellation_men = constellation.split(" ")[1]
        constellation_woman = constellation.split(" ")[2]
    except IndexError:
        return "输入格式有误\n" \
               "例：星座匹配 双子 金牛 \n"
    constellation_pairing_url = 'http://apis.juhe.cn/xzpd/query'
    params = {
        'men': constellation_men,  # 男方星座，如：白羊
        'women': constellation_woman,  # 女方星座，如：金牛
        'key': "29e9a36f4124cc78fb28e11fefe47cd4",
    }
    try:
        constellation_pairing_res = requests.get(constellation_pairing_url, params).json()
        zhi_shu = constellation_pairing_res['result']['zhishu']  # 配对指数
        jie_guo = constellation_pairing_res['result']['jieguo']  # 结果描述
        lian_ai = constellation_pairing_res['result']['lianai']  # 恋爱建议
        constellation_pairing_msg = f"[CQ:face,id=207]{constellation_men}和{constellation_woman}\n" \
                                    f"[CQ:face,id=66]配对指数：{zhi_shu}\n" \
                                    f"[CQ:face,id=85]结果为：{jie_guo}\n" \
                                    f"[CQ:face,id=42]表现为：\n" \
                                    f"{lian_ai}"
    except:
        return "检查一下输入星座是否正确"
    else:
        return constellation_pairing_msg


# 随机setu API地址: https://api.lolicon.app/#/setu
def get_setu():
    setu_url = 'https://api.lolicon.app/setu/v2'
    setu_res = requests.get(setu_url).json()
    setu_res_urls_original = setu_res['data'][0]['urls']['original']
    image_cq_msg = f"[CQ:image,file={setu_res_urls_original}]"
    return image_cq_msg


# 发送部署在服务端的视频
def get_video():
    video_url = 'http://106.52.78.177/wp-content/uploads/2022/10/1.mp4'
    video_msg = f"[CQ:video,file={video_url}]"
    return video_msg


if __name__ == '__main__':
    s_msg = get_ConstellationPairing("星座匹配 天蝎 金牛")
    print(s_msg)



