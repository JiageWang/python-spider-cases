import re
import os
import json
import time
import pptx
import urllib3
import requests
from lxml import etree
urllib3.disable_warnings() # 禁用警告


class WenKuSpider(object):
    def __init__(self, url):
        self.__session = requests.session()
        self.__headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Referer": url,
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
        }
        self.__docTypePattern = re.compile(r"'docType':\s'(.*)'")
        self.__docIdPattern = re.compile(r"'docId':\s'(.*)'")
        self.__docTitlePattern = re.compile(r"'title':\s'(.*)'")
        self.__url = None
        self.__html = self.get(url, 'gb2312')
        self.__docId = self.__docIdPattern.findall(self.__html)[0]
        self.__docType = self.__docTypePattern.findall(self.__html)[0]
        self.__title = self.__docTitlePattern.findall(self.__html)[0]
        self.__content = ""
        self.run()

    def run(self):
        if self.__docType == "doc":
            # 获取类json文件的url地址
            pattern= re.compile(r'https://\w+.\w+.\w+/\w+/\w+/\w+/\w+/0.json\?(?:[\w-]+=[\d\w%-.]+&?){6}')
            html = etree.HTML(self.__html)
            script = html.xpath('//div[@id="hd"]/script/text()')[0]
            script = script.replace("\\\\\\/", "/")
            json_urls = pattern.findall(script)

            # 解析json文件以获取内容
            for json_url in json_urls:
                json_content = self.get(json_url, encoding='utf-8')
                self.__content += self.parseJson(json_content)

        elif self.__docType == "ppt":
            # 获取存储img地址的url
            url = 'https://wenku.baidu.com/browse/getbcsurl?doc_id={0}&pn=1&rn=99999&type=ppt&_={1}'.format(self.__docId, str(int( time.time() * 1000)))
            response = self.get(url, 'utf-8')
            json_content = json.loads(response)
            # 保存jpg
            path = './{}'.format(self.__title)
            if not os.path.exists(path):
                os.mkdir(path)
            for i, dic in enumerate(json_content):
                response = self.get(dic['zoom'], encoding='utf-8', type='bytes')
                with open(path+'/'+str(i + 1) + '.jpg', 'wb') as f:
                    f.write(response)
            self.__content="已保存到{}".format(path)

        elif self.__docType == "pdf":
            pattern= re.compile(r'https://\w+.\w+.\w+/\w+/\w+/\w+/\w+/0.png\?(?:[\w-]+=[\d\w%-.]+&?){6}')
            html = etree.HTML(self.__html)
            script = html.xpath('//div[@id="hd"]/script/text()')[0]
            script = script.replace("\\\\\\/", "/")
            img_urls = pattern.findall(script)

            path = './{}'.format(self.__title)
            if not os.path.exists(path):
                os.mkdir(path)

            for i, img in enumerate(img_urls):
                # img.replace('p')
                response = self.get(img, encoding='utf-8', type='bytes')
                with open(path+'/'+str(i + 1) + '.jpg', 'wb') as f:
                    f.write(response)
            self.__content="已保存到{}".format(path)




    def get(self, url, encoding='utf-8', type='str'):
        try:
            response = self.__session.get(url, headers=self.__headers, verify=False)
            response.encoding = encoding
            if type == 'str':
                return response.text
            elif type == 'bytes':
                return response.content
        except Exception as e:
            print(e)

    def get_title(self):
        return self.__title

    def get_content(self):
        return  self.__content

    def parseJson(self,json_content):
        index = json_content.find('(')
        if index != -1:
            result = json.loads(json_content[index+1:-1])
            body = result['body']
            content = ''
            for info in body:
                try:
                    content = content + info["c"].strip()
                except Exception as e:
                    pass
            return content



if __name__ == "__main__":
    print("*"*50)
    while True:
        url = input("input url or input q to quit:")
        if url=="q":
            break
        spider = WenKuSpider(url)
        print(spider.get_content())
    print("*"*50)





