from flask import Flask, request
from paddlenlp import Taskflow
import threading

from api.get_current_time import get_current_time
from send_message.send_message import send_private_msg, send_group_msg
from send_message.select_function import select_function

# 人工智能，交互式闲聊对话，PaddleNLP
# 基于PLATO-MINI，模型在十亿级别的中文对话数据上进行了预训练，闲聊场景对话效果显著。
# 调用Taskflow工具集，智能对原始信息进行回复
dialogue = Taskflow("dialogue")

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
        if '[CQ:at,qq=1815743854]' in raw_message:  # 如果@机器人则智能回复
            # 通过PaddleNLP中的Taskflow工具集，智能对原始信息进行回复，join函数用于去除方括号[]
            s_message = " ".join(dialogue([raw_message]))
        else:
            s_message = select_function(raw_message)
        if len(s_message) != 0:
            send_group_msg(group_id, s_message)
    return 'OK'


def main():
    t = threading.Thread(target=get_current_time)
    t.start()
    app.run(debug=True, host='0.0.0.0', port=10088)  # 此处的 host和 port对应上面 yml文件的设置


if __name__ == '__main__':
    main()
