# #导包
# import requests
# #step_1:指定url
# url = 'https://www.sogou.com/'
# #step_2:发起请求:使用get方法发起get请求，该方法会返回一个响应对象。参数url表示请求对应的url
# response = requests.get(url=url)
# #step_3:获取响应数据:通过调用响应对象的text属性，返回响应对象中存储的字符串形式的响应数据（页面源码数据）
# page_text = response.text
# #step_4:持久化存储
# with open('./sogou.html','w',encoding='utf-8') as fp:
#     fp.write(page_text)
# print('爬取数据完毕！！！')
#
#
#
# #指定搜索关键字
# word = input('enter a word you want to search:')
# #自定义请求头信息:UA伪装,将包含了User-Agent的字典作用到请求方法的headers参数中即可
# headers={
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
#     }
# #指定url，原始url可能是https://www.sogou.com/web?query=撩妹，发现该url携带了参数
# url = 'https://www.sogou.com/web'
# #封装get请求参数：如果请求携带了参数，则可以将参数封装到字典中结合这requests请求方法中的data/params参数进行url参数的处理
# param = {
#     'query':word,
# }
# #发起请求
# response = requests.get(url=url,params=param,headers=headers)
# #获取响应数据
# page_text = response.text
# #持久化存储
# fileName = word+'.html'
# with open(fileName,'w',encoding='utf-8') as fp:
#     fp.write(page_text)
#
#
# import requests
# import json
# word = input('enter a English word:')
# #自定义请求头信息:UA伪装,将包含了User-Agent的字典作用到请求方法的headers参数中即可
# headers={
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
#     }
# #指定url，原始url可能是https://www.sogou.com/web?query=撩妹，发现该url携带了参数
# url = 'https://fanyi.baidu.com/sug'
# #封装post请求参数：如果请求携带了参数，则可以将参数封装到字典中结合这requests请求方法中的data/params参数进行url参数的处理
# data = {
#     'kw':word,
# }
# #发起请求
# response = requests.post(url=url,data=data,headers=headers)
# #获取响应数据:如果响应回来的数据为json，则可以直接调用响应对象的json方法获取json对象数据
# json_data = response.json()
# #持久化存储
# fileName = word+'.json'
# fp = open(fileName,'w',encoding='utf-8')
# json.dump(json_data,fp,ensure_ascii=False)

# import requests
# if __name__ == "__main__":
#     #指定ajax-get请求的url（通过抓包进行获取）
#     url = 'https://movie.douban.com/j/chart/top_list?'
#     #定制请求头信息，相关的头信息必须封装在字典结构中
#     headers = {
#         #定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
#     }
#     #定制get请求携带的参数(从抓包工具中获取)
#     param = {
#         'type':'5',
#         'interval_id':'100:90',
#         'action':'',
#         'start':'0',
#         'limit':'20'
#     }
#     #发起get请求，获取响应对象
#     response = requests.get(url=url,headers=headers,params=param)
#     #获取响应内容
#     print(response.json())

import requests
# from fake_useragent import UserAgent
# ua = UserAgent(use_cache_server=False,verify_ssl=False).random
headers = {
    # 'User-Agent':ua
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',

}
url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
pageNum = 3
for page in range(3,5):
    data = {
        'on': 'true',
        'page': str(page),
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':''
    }
    json_text = requests.post(url=url,data=data,headers=headers).json()
    all_id_list = []
    for dict in json_text['list']:
        id = dict['ID']#用于二级页面数据获取
        #下列详情信息可以在二级页面中获取
        # name = dict['EPS_NAME']
        # product = dict['PRODUCT_SN']
        # man_name = dict['QF_MANAGER_NAME']
        # d1 = dict['XC_DATE']
        # d2 = dict['XK_DATE']
        all_id_list.append(id)
    #该url是一个ajax的post请求
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in  all_id_list:
        post_data = {
            'id':id
        }
        response = requests.post(url=post_url,data=post_data,headers=headers)
        if response.headers['Content-Type'] == 'application/json;charset=UTF-8':
            #print(response.json())
            #进行json解析
            json_text = response.json()
            print(json_text['businessPerson'])