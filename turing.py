import json
import requests
import webbrowser

API = 'http://www.tuling123.com/openapi/api'


# 填写注册后机器人接入页面的APIKEY以及用户名
API_KEY = ''
USER_ID = ''


# 填写机器人名字
NAME = 'AI'


# 生成请求信息，格式为json
def make_json(info):
    return {
        'key': API_KEY,
        'info': info,
        'userid': USER_ID}


# 获取返回数据
def fetch_text(j):
    result = requests.post(API, json=j)
    return result.text


# 根据返回数据类型打印信息
def print_response(response):
    print(NAME + ': ', response['text'])

    # 文本类回复
    if response['code'] == 100000:
        pass

    # 链接类回复
    elif response['code'] == 200000:
        # 浏览器自动打开链接
        webbrowser.open(response['url'])

    # 新闻类回复，美化输出格式
    elif response['code'] == 302000:
        i = 1
        for news in response['list']:
            print(i, '.', news['article'])
            print(news['detailurl'])
            print()
            i += 1

    # 菜谱类回复，美化输出格式
    elif response['code'] == 308000:
        j = 1
        for recipe in response['list']:
            print(j, '.', recipe['name'])
            print(recipe['info'])
            print(recipe['detailurl'])
            print()
            j += 1


def main():
    if API_KEY == '' or USER_ID == '':
        print('Please fill the APIKEY and username into tuling.py firstly.')
        return

    while True:
        info = input("I: ")
        result = fetch_text(make_json(info))
        response = json.loads(result)
        print_response(response)
        print()


main()
