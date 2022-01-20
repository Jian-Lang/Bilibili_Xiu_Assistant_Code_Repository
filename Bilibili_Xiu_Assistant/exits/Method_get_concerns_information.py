import requests


def get_concerns_information(vmid_list):
    # 通过up主UID获取up主的信息
    message = {
        'status': 200
    }
    lists = []
    if len(vmid_list) != 0:
        message['number of concerns'] = len(vmid_list)
        for n in range(0, len(vmid_list)):
            message_search_api = 'https://api.bilibili.com/x/space/acc/info?mid=%s' % vmid_list[n]
            response2 = requests.get(message_search_api)
            user_concern_list_dict = response2.json()
            print(user_concern_list_dict)
            name = user_concern_list_dict['data']['name']
            face = user_concern_list_dict['data']['face']
            uid = vmid_list[n]
            if user_concern_list_dict['data']['official']['title'] == '':
                if user_concern_list_dict['data']['sign'] == '':
                    information = '这个用户什么都没有留下~'
                else:
                    information = user_concern_list_dict['data']['sign'].replace('\n', '  ')
            else:
                information = user_concern_list_dict['data']['official']['title'].replace('\n', '  ')
            UP = {'up_uid': uid, 'up_name': name, 'up_face': face, 'up_information': information}
            lists.append(UP)
        message['data'] = lists
        return message
    else:
        return {
            'status': 400,
            'message': '还没有特别关心的up主呢'
        }
