import requests


# 发送私聊消息
# 参数: user_id: 对方 QQ 号, message: 要发送的内容
# 响应数据: message_id: 消息 ID
def send_private_msg(user_id, message):
    send_private_msg_url = 'http://127.0.0.1:10087/send_private_msg'
    params = {
        'user_id': user_id,
        'message': message,
    }
    send_private_msg_res = requests.get(send_private_msg_url, params).json()
    message_id = send_private_msg_res['data']['message_id']
    print(message_id)
    return message_id


# 发送群消息
# 参数: group_id: 群号, message: 要发送的内容
# 响应数据: message_id: 消息 ID
def send_group_msg(group_id, message):
    send_group_msg_url = 'http://127.0.0.1:10087/send_group_msg'
    params = {
        'group_id': group_id,
        'message': message,
    }
    send_group_msg_res = requests.get(send_group_msg_url, params).json()
    message_id = send_group_msg_res['data']['message_id']
    print(message_id)
    return message_id


# 撤回消息
# 参数: message_id: 消息 ID
def delete_msg(message_id):
    delete_msg_url = 'http://127.0.0.1:10087/delete_msg'
    params = {
        'message_id': message_id,
    }
    requests.get(delete_msg_url, params)


# # 获取消息
# def get_msg(message_id):
#     get_msg_url = 'http://127.0.0.1:10087/get_msg'
#     params = {
#         'message_id': message_id,
#     }
#     get_msg_res = requests.get(get_msg_url, params).json()
#     message = get_msg_res['data']['message']
#     print(get_msg_res)


if __name__ == '__main__':
    pass
