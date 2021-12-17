import calendar
import time

import requests


def judgeuserhasconcern(mid):
    # 判断该用户有无关注up主
    api = 'https://api.bilibili.com/x/relation/followings?vmid=' + mid
    response = requests.get(api)
    information = response.json()
    code = information['code']
    if code == 22115:
        return False
    number = information['data']['total']
    if number > 0:
        return True
    else:
        return False


def getconcernlistUID(vmid):
    # 用于获取单个用户的关注的UID
    api = 'https://api.bilibili.com/x/relation/followings?vmid=%s' % vmid
    response1 = requests.get(api)
    user_concern_list_dict = response1.json()
    code = user_concern_list_dict['code']
    if code == 22115:
        return {
            'status': 400,
            'message': '用户设置隐私'
        }
    concernlist = []
    for n in range(0, len(user_concern_list_dict['data']['list'])):
        name = user_concern_list_dict['data']['list'][n]['mid']
        concernlist.append(name)
    return concernlist


def getconcernlist(vmid):
    # 用于获取单个用户的关注
    api = 'https://api.bilibili.com/x/relation/followings?vmid=%s' % vmid
    response1 = requests.get(api)
    user_concern_list_dict = response1.json()
    concernlist = {}
    concernlist['user_UID'] = vmid
    code = user_concern_list_dict['code']
    if code == 22115:
        print('用户已设置隐私，无法查看关注列表')
        return concernlist
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


def getconcernlist1(vmid_list):
    # 用来获取多个用户的关注列表
    lists = []
    for n in range(0, len(vmid_list)):
        api = 'https://api.bilibili.com/x/relation/followings?vmid=' + vmid_list[n]
        response1 = requests.get(api)
        user_concern_list_dict = response1.json()
        concernlist = {}
        concernlist['user_UID'] = vmid_list[n]
        code = user_concern_list_dict['code']
        if code == 22115:
            print('用户' + vmid_list[n] + '已设置隐私，无法查看关注列表')
            lists.append(concernlist)
        else:
            concernlist['numberofconcern'] = user_concern_list_dict['data']['total']
            UP = []
            for n in range(0, len(user_concern_list_dict['data']['list'])):
                name = user_concern_list_dict['data']['list'][n]['uname']
                face = user_concern_list_dict['data']['list'][n]['face']
                if user_concern_list_dict['data']['list'][n]['sign'] == '':
                    if user_concern_list_dict['data']['list'][n]['official_verify']['desc'] == '':
                        information = '这个用户什么都没有留下~'
                    else:
                        information = user_concern_list_dict['data']['list'][n]['official_verify']['desc'].replace('\n',
                                                                                                                   '  ')
                else:
                    information = user_concern_list_dict['data']['list'][n]['sign'].replace('\n', '  ')
                UP.append({'up_name': name, 'up_face': face, 'up_information': information})
            concernlist['object'] = UP
            lists.append(concernlist)
    return lists


def getsearchresult(uid_list, keyword):
    # 显示用户搜索的结果
    """
    :param uid_list:用户的关心列表（列表类）
    :param keyword:搜索的关键词（str类）
    :return:搜素的结果（字典类）（按粉丝量排序的用户，包括是否被该用户关注的信息）
    """
    api = 'https://api.bilibili.com/x/web-interface/search/type?&page=1&keyword=' + keyword + '&search_type=bili_user&order=fans'
    response2 = requests.get(api)
    search_result_dict = response2.json()
    num = search_result_dict['data']['numResults']
    if num == 0:
        return '什么都没有找到啊TAT'
    else:
        searchresult = {}
        searchresult['search_keyword'] = keyword
        searchresult['number of result'] = num
        user = []
        for n in range(0, len(search_result_dict['data']['result'])):
            name = search_result_dict['data']['result'][n]['uname']
            face = 'https:' + search_result_dict['data']['result'][n]['upic']
            if search_result_dict['data']['result'][n]['usign'] == '':
                if search_result_dict['data']['result'][n]['official_verify']['desc'] == '':
                    information = '这个用户什么都没有留下~'
                else:
                    information = search_result_dict['data']['result'][n]['official_verify']['desc'].replace('\n', '  ')
            else:
                information = search_result_dict['data']['result'][n]['usign'].replace('\n', '  ')
            mid = search_result_dict['data']['result'][n]['mid']
            hasfollowed = 0
            for m in range(0, len(uid_list)):
                if uid_list[m] == mid:
                    hasfollowed = 1
            if hasfollowed == 1:
                user.append({'rname': name, 'rface': face, 'rinformation': information, 'hasfollowed': 'TRUE'})
            else:
                user.append({'rname': name, 'rface': face, 'rinformation': information, 'hasfollowed': 'FALSE'})
        searchresult['user'] = user
    return searchresult


def getupdatedmessage(vmid):
    # 获取某一个用户两天内的更新视频
    api = 'https://api.bilibili.com/x/space/arc/search?pn=1&ps=100&keyword=&mid=%s' % vmid
    response3 = requests.get(api)
    videomessage = response3.json()
    updatedmessage = {}
    updatedmessage['uper_UID'] = vmid
    video = []
    counter = 0
    now_time = calendar.timegm(time.gmtime())  # 获取当前系统时间戳
    for n in range(0, len(videomessage['data']['list']['vlist'])):
        title = videomessage['data']['list']['vlist'][n]['title']
        pic = videomessage['data']['list']['vlist'][n]['pic']
        updatetime = videomessage['data']['list']['vlist'][n]['created']
        bvid = videomessage['data']['list']['vlist'][n]['bvid']
        if (now_time - 172800) < updatetime:  # 减去两天的时间戳 判断是否为这两天所更新的视频
            video.append({'title': title, 'pic': pic, 'updatetime': updatetime, 'bvid': bvid})
            counter += 1
        else:
            break
    updatedmessage['number of late video'] = counter
    updatedmessage['video'] = video
    return updatedmessage

# dict = getconcernlist('562197')
# print(dict)
#
# dict = getconcernlist('34243853')
# print(dict)

# dict = getconcernlist1(['562197','34243853'])
# print(dict)

# dict = judgeuserhasconcern('34243853')
# print(dict)
#
# dict = getconcernlistUID('34243853')
# print(dict)

# dict = getsearchresult('awdawda')
# print(dict)

# dict = getupdatedmessage('1935882')
# print(dict)
