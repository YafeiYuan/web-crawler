#导入模块
from urllib import request,parse
#专门处理json的模块
import json

"功能介绍：利用百度翻译内核，制作自己的翻译简易工具"

#基础URL
base_url = 'https://fanyi.baidu.com/sug'

#封装函数
def fanyi(kw):
    #构造请求对象
    data = {
        'kw' : kw
    }
    #转换成字符串
    data = parse.urlencode(data)
    #检测长度
    length = len(data)
    #构造请求头
    headers = {
        'Content-Length': length
    }

    #构造请求对象
    req = request.Request(base_url,data= bytes(data,encoding='utf-8'), headers=headers)

    #读取对象里的内容
    response = request.urlopen(req)

    #变量接收，方便转换
    json_data = response.read().decode('utf-8')

    #把json字符串转换成字典
    json_data = json.loads(json_data)

    #格式化输出字典
    #把字典转成字符串
    # json_data = json.dumps(json_data,ensure_ascii=False,indent=4)

    #遍历搜索结果
    res = ''
    for item in json_data['data']:
        res += item['v'] + '\n'
    print(res)

#主程序入口
if __name__=='__main__':
    while True:
        kw = input('请输入要搜索的单词:')
        fanyi(kw)