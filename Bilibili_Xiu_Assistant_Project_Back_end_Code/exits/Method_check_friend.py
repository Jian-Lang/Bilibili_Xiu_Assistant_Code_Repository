import requests


def check_friend(me_uid_list, friend_uid_list):
    # 获取朋友的特别关心列表的信息 同时判断朋友关注的up主我是否特别关心了
    """
    :param me_uid_list:用户自己的关注列表的UID（列表类）
    :param friend_uid_list:用户朋友的关注列表的UID（列表类）
    :return:朋友关注列表的信息（字典类）包括朋友关注的up主我是否特别关心了的信息
    """
    friend_message_dict = {}
    friend_message_dict['status'] = 200
    UP = []
    for n in range(0, len(friend_uid_list)):
        message_search_api = 'https://api.bilibili.com/x/space/acc/info?mid=%s' % friend_uid_list[n]
        response = requests.get(message_search_api)
        user_concern_list_dict = response.json()
        uid = user_concern_list_dict['data']['mid']
        name = user_concern_list_dict['data']['name']
        face = user_concern_list_dict['data']['face']
        if user_concern_list_dict['data']['official']['title'] == '':
            if user_concern_list_dict['data']['sign'] == '':
                information = '这个用户什么都没有留下~'
            else:
                information = user_concern_list_dict['data']['sign'].replace('\n', '  ')
        else:
            information = user_concern_list_dict['data']['official']['title'].replace('\n', '  ')
        has_special_concerned = 0
        for m in range(0, len(me_uid_list)):
            if friend_uid_list[n] == me_uid_list[m]:
                has_special_concerned = 1
                break
        if has_special_concerned == 1:
            up = {'up_uid': uid, 'up_name': name, 'up_face': face, 'up_information': information,
                  'has_special_concerned': 'TRUE'}
        else:
            up = {'up_uid': uid, 'up_name': name, 'up_face': face, 'up_information': information,
                  'has_special_concerned': 'FALSE'}
        UP.append(up)
    friend_message_dict['data'] = UP
    return friend_message_dict
