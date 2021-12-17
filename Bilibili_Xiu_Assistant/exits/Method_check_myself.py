import requests


def check_myself(my_follow_list, my_uid):
    # 获取自己b站的关注列表 并和自己的特别关心列表相比较
    """
    :param my_follow_list:用户自己的特别关心列表的UID（列表类）
    :param my_uid:用户自己的UID（int）
    :return:用户自己的关注列表信息（字典类）包括自己关注的up主自己是否特别关心了的信息
    """

    api = 'https://api.bilibili.com/x/relation/followings?vmid=%s' % my_uid
    response = requests.get(api)
    user_concern_list_dict = response.json()
    code = user_concern_list_dict['code']
    if code == 22115:
        print('用户已设置隐私，无法查看关注列表')
        return 0
    dict = {
        'status': 200
    }
    UP = []
    for n in range(0, len(user_concern_list_dict['data']['list'])):
        has_special_concerned = 0
        uid = user_concern_list_dict['data']['list'][n]['mid']
        name = user_concern_list_dict['data']['list'][n]['uname']
        face = user_concern_list_dict['data']['list'][n]['face']
        mid = user_concern_list_dict['data']['list'][n]['mid']
        for m in range(0, len(my_follow_list)):
            if mid == my_follow_list[m]:
                has_special_concerned = 1
                break
        if user_concern_list_dict['data']['list'][n]['sign'] == '':
            if user_concern_list_dict['data']['list'][n]['official_verify']['desc'] == '':
                information = '这个用户什么都没有留下~'
            else:
                information = user_concern_list_dict['data']['list'][n]['official_verify']['desc'].replace('\n', '  ')
        else:
            information = user_concern_list_dict['data']['list'][n]['sign'].replace('\n', '  ')
        if has_special_concerned == 1:
            up = {'uid': uid, 'name': name, 'face': face, 'information': information, 'has_special_concerned': 'TRUE'}
        else:
            up = {'uid': uid, 'name': name, 'face': face, 'information': information, 'has_special_concerned': 'FALSE'}
        UP.append(up)
    dict['data'] = UP
    return dict
