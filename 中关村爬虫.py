# coding=utf-8
import requests
import urllib
import pandas as pd
from lxml import etree
import argparse

host = 'http://detail.zol.com.cn'
http_headers = {"Host": "detail.zol.com.cn",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Referer": "http://detail.zol.com.cn/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                # "Cookie": "ip_ck=5cWB5P3xj7QuMjIwMzc2LjE1NDA2MTk1OTI%3D; UM_distinctid=166d98bdb6b5c5-0796be4e908aba-594c2a16-1fa400-166d98bdb6c84; gr_user_id=cd63d221-ad8c-4ecf-9a47-ac80ba0971b9; z_pro_city=s_provice%3Dshanghai%26s_city%3Dshanghai; userProvinceId=2; userCityId=0; userCountyId=0; userLocationId=26; realLocationId=26; userFidLocationId=26; Adshow=1; listSubcateId=57; Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1542877522,1543917762,1543926936,1543933043; lv=1543973953; vn=9; gr_session_id_9b437fe8881a7e19=08ae7982-640f-4393-a286-b8f2de93a7e0; gr_session_id_9b437fe8881a7e19_08ae7982-640f-4393-a286-b8f2de93a7e0=true; questionnaire_pv=1543968010"
                "Cookie": 'ip_ck=5cWB5P3xj7QuMjIwMzc2LjE1NDA2MTk1OTI%3D; UM_distinctid=166d98bdb6b5c5-0796be4e908aba-594c2a16-1fa400-166d98bdb6c84; gr_user_id=cd63d221-ad8c-4ecf-9a47-ac80ba0971b9; Adshow=0; lv=1544426834; vn=12; Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1543926936,1543933043,1543979694,1544426834; z_pro_city=s_provice%3Dshanghai%26s_city%3Dshanghai; userProvinceId=2; userCityId=0; userCountyId=0; userLocationId=26; realLocationId=26; userFidLocationId=26; gr_session_id_9b437fe8881a7e19=621e3b31-0588-4892-bbb5-1a237c26cec3; gr_session_id_9b437fe8881a7e19_621e3b31-0588-4892-bbb5-1a237c26cec3=true; questionnaire_pv=1544400004; listSubcateId=57',
}
session = requests.session()



def main(keyword, pages):
    # if keyword == "手机":
    #     items = ['品牌', '价格', 'CPU型号', 'CPU频率', '核心数', 'RAM容量', 'ROM容量', '主屏尺寸', '主屏分辨率', '屏幕占比', '电池容量', '后置摄像头', '前置摄像头']
    # else:
    #     items = ['品牌', '价格']
    # # 初始化
    # infos = {}
    # for item in items:
    #     infos[item] = []
    # # 发送搜索页请求
    # keyword = urllib.parse.quote(keyword)
    # url = 'http://detail.zol.com.cn/index.php?c=SearchList&kword={}'.format(keyword)
    # print(url)
    # response = session.get(url, headers=http_headers, allow_redirects=False)
    # # response.encoding = "gb2312"

    # 重定向
    # redirect_url = response.headers['location'].split('?')[0]
    # if redirect_url.endswith('/'):
    #     redirect_url += '1.html'
    redirect_url = 'http://detail.zol.com.cn/notebook_index/subcate16_list_1http://detail.zol.com.cn/notebook_index/subcate16_0_list_1_0_3_2_0_1.html'
    items = ['品牌', '价格']
    infos = {}
    for item in items:
        infos[item] = []

    # 爬取每一页所有商品
    for i in range(1, pages+1):
        response = requests.get(redirect_url, headers=http_headers)
        content = response.text
        html = etree.HTML(content)

        res = html.xpath('//div[@class="content"]//h3/a/@href')
        for url_ in res:
            info = {}
            new_url = host + url_
            print("正在爬取：", new_url)
            response = requests.get(url=new_url, headers=http_headers)
            content = response.text
            html = etree.HTML(content)

            # 更多参数
            more_url = host + html.xpath('//a[@class="_j_MP_more section-more"]/@href')[0]
            response = requests.get(url=more_url,headers=http_headers)
            content = response.text
            html = etree.HTML(content)

            name = html.xpath('//h1/text()')[0]
            price = html.xpath('//div[@class="goods-card__price"]/span/text()')[0]
            info['品牌'] = name.split(' ')[0]
            info['价格'] = price

            values = html.xpath('//td[@class="hover-edit-param"]/span')
            keys = html.xpath('//th/span')
            assert len(keys) == len(values)
            for key, value in zip(keys, values):
                info[key.xpath("string()")] = value.xpath("string()")

            for item in items:
                infos[item].append(info.get(item, ' '))

    # 保存excel
    data = pd.DataFrame(infos)
    data.to_excel('{}.xlsx'.format(keyword), sheet_name='Sheet1')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pages", default=1, type=int)
    parser.add_argument("-k", "--keyword", default='手机', type=str)
    args = parser.parse_args()

    keyword = args.keyword
    pages = args.pages
    main(keyword, pages)





