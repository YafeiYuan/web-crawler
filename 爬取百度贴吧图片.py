#导入模块
from urllib import request,parse
import os

"""爬取百度贴吧的一些图片数据"""

#基础URL
base_url = 'https://tieba.baidu.com/f?ie=utf-8&'

#用户输入
kw = input('贴吧名称:')
start = input('开始位置:')
end = input('结束位置:')

#函数封装
def tieba(kw,start,end):
    #根据输入内容建立相应文件夹
    dir_name = './tieba/' + kw + '/'
    if not os.path.exists(dir_name):  #不存在就建立
        os.makedirs(dir_name)

    #构造请求对象
    qs = {
        'kw' : kw
    }

    #构造pn查询参数
    for i in range(int(start),int(end) + 1):
        #算出pn值
        # 关系
        # 1  0
        # 2  50
        # 3  100
        pn = (i-1) * 50
        qs['pn'] = str(pn)

        #转换成字符串
        qs_data = parse.urlencode(qs)
        # 构建完整的url
        fullurl = base_url +qs_data
        #显示执行过程位置
        print(f'downlong page {fullurl}')
        #发起请求
        response = request.urlopen(fullurl)

        #将爬取到的数据存入文件夹中
        with open(dir_name + str(i) + '.html','w',encoding='utf-8') as f:
            # 读取响应内容
            html = response.read().decode('utf-8')
            f.write(html)

#主程序入口
if __name__ == '__main__':
    #调用函数
    tieba(kw,start,end)