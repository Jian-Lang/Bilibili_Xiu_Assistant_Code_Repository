import requests
def getconcernlist(vmid):
    api = 'https://api.bilibili.com/x/relation/followings?vmid=%s'%vmid
    response1 = requests.get(api)
    user_concern_list_dict = response1.json()
    concernlist = {}
    concernlist['user_UID'] = vmid
    concernlist['numberofconcern'] = user_concern_list_dict['data']['total']
    UP = []
    for n in range(0, len(user_concern_list_dict['data']['list'])):
        name = user_concern_list_dict['data']['list'][n]['uname']
        face = user_concern_list_dict['data']['list'][n]['face']
        if user_concern_list_dict['data']['list'][n]['sign'] == '':
            if user_concern_list_dict['data']['list'][n]['official_verify']['desc'] == '':
                information = '这个用户什么都没有留下~'
            else:
                information = user_concern_list_dict['data']['list'][n]['official_verify']['desc'].replace('\n', '  ')
        else:
            information = user_concern_list_dict['data']['list'][n]['sign'].replace('\n', '  ')
        UP.append({'up_name': name, 'up_face': face, 'up_information': information})
    concernlist['object'] = UP
    return concernlist