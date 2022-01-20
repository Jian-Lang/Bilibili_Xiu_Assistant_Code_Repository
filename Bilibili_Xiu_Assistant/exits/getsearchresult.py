import requests


def getsearchresult(uid_list, x, keyword):
    # 显示用户搜索的结果
    """
    :param uid_list:用户的关心列表（列表类）
    :param keyword:搜索的关键词（str类）
    :return:搜素的结果（字典类）（按粉丝量排序的用户，包括是否被该用户关注的信息）
    """
    api = 'https://api.bilibili.com/x/web-interface/search/type?&page=%s' % x + '&keyword=' + keyword + '&search_type=bili_user&order=fans'
    response2 = requests.get(api)
    search_result_dict = response2.json()
    print(search_result_dict)
    numResults = search_result_dict['data']['numResults']
    numPages = search_result_dict['data']['numPages']
    if numResults == 0:
        return {
            'status': 400,
            'message': '什么都没有找到啊TAT'
        }
    else:
        searchresult = {
            'status': 200,
        }
        user = []
        searchresult['search_keyword'] = keyword
        searchresult['number of result'] = numResults
        searchresult['number of pages'] = numPages
        if x <= numPages:
            searchresult['current page'] = x
            for n in range(0, len(search_result_dict['data']['result'])):
                name = search_result_dict['data']['result'][n]['uname']
                face = 'https:' + search_result_dict['data']['result'][n]['upic']
                if search_result_dict['data']['result'][n]['usign'] == '':
                    if search_result_dict['data']['result'][n]['official_verify']['desc'] == '':
                        information = '这个用户什么都没有留下~'
                    else:
                        information = search_result_dict['data']['result'][n]['official_verify']['desc'].replace('\n',
                                                                                                                 '  ')
                else:
                    information = search_result_dict['data']['result'][n]['usign'].replace('\n', '  ')
                mid = search_result_dict['data']['result'][n]['mid']
                hasfollowed = 0
                for m in range(0, len(uid_list)):
                    if uid_list[m] == mid:
                        hasfollowed = 1
                        break
                if hasfollowed == 1:
                    user.append(
                        {'uid': mid, 'rname': name, 'rface': face, 'rinformation': information, 'hasfollowed': 'TRUE'})
                else:
                    user.append(
                        {'uid': mid, 'rname': name, 'rface': face, 'rinformation': information, 'hasfollowed': 'FALSE'})
            searchresult['user'] = user
        else:
            searchresult['status'] = 400
            searchresult['message'] = '此页面没有结果，请跳转到上一页~'
    return searchresult
