import calendar
import time

import requests


def get_updated_message(vmid_list, days):
    # 获取多个up主设定天数内的更新视频
    """
    :param vmid_list: 用户特别关心列表
    :param days: 用户自己设定的更新天数
    :return: 用户关心up主在设定天数内的更新视频
    """
    if len(vmid_list) == 0:
        return {
            'status': 400,
            'message': "用户还没有特别关心的up主噢~"
        }
    else:
        now_time = calendar.timegm(time.gmtime())  # 获取当前系统时间戳
        message = {}
        message['status'] = 200
        updated_video_list = []
        num = 0
        for n in range(0, len(vmid_list)):
            message_search_api = 'https://api.bilibili.com/x/space/acc/info?mid=%s' % vmid_list[n]
            response = requests.get(message_search_api)
            user_concern_list_dict = response.json()
            name = user_concern_list_dict['data']['name']
            face = user_concern_list_dict['data']['face']
            api = 'https://api.bilibili.com/x/space/arc/search?keyword=&mid=%s' % vmid_list[n]
            response1 = requests.get(api)
            videomessage = response1.json()
            for m in range(0, len(videomessage['data']['list']['vlist'])):
                title = videomessage['data']['list']['vlist'][m]['title']
                pic = videomessage['data']['list']['vlist'][m]['pic']
                description = videomessage['data']['list']['vlist'][m]['description'].replace('\n', '  ')
                updatetime = videomessage['data']['list']['vlist'][m]['created']
                bvid = videomessage['data']['list']['vlist'][m]['bvid']
                time_length = videomessage['data']['list']['vlist'][m]['length']
                url = 'https://www.bilibili.com/video/' + bvid
                if (now_time - (86400 * days)) < updatetime:  # 判断是否为设定天数内所更新的视频
                    updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(updatetime))
                    updated_video_list.append({'up_name': name, 'up_face': face, 'video_title': title, 'video_pic': pic,
                                               'video_description': description, 'time_length': time_length,
                                               'update_time': updatetime, 'url': url})
                    num += 1
                else:
                    break
        message['number of updated video'] = num
        if num == 0:
            message['data'] = '最近没有新视频噢~'
        else:
            message['data'] = updated_video_list
        return message
