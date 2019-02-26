import re
import sys
import json
import time
import execjs
import hashlib
import requests
from urllib import parse
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from translate_ui import Ui_translator

class Translator(QMainWindow, QSystemTrayIcon, Ui_translator):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("在线翻译")
        self.setWindowIcon(QIcon('./logo.ico'))
        ti = TrayIcon(self)
        ti.show()
        style = """
            #pushButton_translate:hover{
            background-color:blue;
            }
        """
        self.setStyleSheet(style)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.session = requests.session()
        self.headers = {
            "Connection": "keep - alive",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
        }
        self.youdao_html = self.session.get('http://fanyi.youdao.com', headers=self.headers).text
        self.google_html = self.session.get('https://translate.google.cn', headers=self.headers).text
        self.bing_html = self.session.get('https://cn.bing.com/translator/?mkt=zh-CN', headers=self.headers).text
        self.pushButton_translate.clicked.connect(self.translate)
        self.lineEdit_input.returnPressed.connect(self.translate)
        self.show()



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.translate()

    def closeEvent(self, event):
        # 隐藏代替关闭
        event.ignore()
        self.hide()

    def translate(self):
        word = self.lineEdit_input.text()
        if word == "":
            return
        type = 'ch2en' if self.isChinese(word) else 'en2ch'
        youdao_result = self.getYoudaoResult(word)
        self.lineEdit_youdao.setText(youdao_result)
        google_result = self.getGoogleResult(word, type)
        self.lineEdit_google.setText(google_result)
        bing_result = self.getBingResult(word, type)
        self.lineEdit_bing.setText(bing_result)

    def getYoudaoResult(self, word):
        salt = str(int(time.time()*1000))
        ts = salt[:-1]
        md5 = hashlib.md5()
        md5.update(("fanyideskweb" + word + salt + "p09@Bn{h02_BIEe]$P^nG").encode('utf-8'))
        sign = md5.hexdigest()
        data = {
            "i":word,
            "from":"AUTO",
            "to":"AUTO",
            "smartresult":"dict",
            "client":"fanyideskweb",
            "salt":salt,
            "sign":sign,
            "ts":ts,
            "bv":"f2ab46dbebb82fcaeb5d20151861f2b9",
            "doctype":"json",
            "version":"2.1",
            "keyfrom":"fanyi.web",
            "action":"FY_BY_CLICKBUTTION",
            "typoResult":"false",
        }
        headers = self.headers.copy()
        headers["Referer"] = "http://fanyi.youdao.com/" #没有referer会返回错误代码
        response = self.session.post('http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule', headers=headers, data=data).text
        response = json.loads(response)
        # print(response)
        # 获取结果
        result = ''
        for i in response['translateResult'][0]:
            result += i['tgt']

        return result

    def getGoogleResult(self, word, type):
        tkk = re.findall("tkk:'([\d.]*)'", self.google_html)[0]
        word_parsed = parse.quote(word)
        tk_value=execjs.compile(open("googletrans.js").read()).call('tk', word, tkk)
        tl = 'zh-CH' if type=='en2ch' else 'en'
        url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl={}&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=gt&otf=1&pc=1&ssel=0&tsel=3&kc=2&tk={}&q={}'.format(tl, tk_value, word_parsed)
        response = self.session.get(url, headers=self.headers).text
        response = json.loads(response)
        # print(response)
        # 获取结果
        result = ''
        for i in response[0]:
            if i[0] != None:
                result += i[0]
        return result

    def getBingResult(self, word, type):
        if type == "ch2en":
            data = {
                "text":word,
                "from":"zh-CHS",
                "to":"en"
            }
        else:
            data = {
                "text":word,
                "from":"en",
                "to":"zh-CHS"
            }
        ig = re.findall(r'IG:"([\w\d]*)"', self.bing_html)[0]
        iid = re.findall(r'_iid="([\w\d.]*)"', self.bing_html)[0]+'.1'
        response = self.session.post('https://cn.bing.com/ttranslate?&category=&IG={}&IID={}'.format(ig, iid), headers=self.headers, data=data).text
        response = json.loads(response)
        # print(response)
        return response['translationResponse']

    @staticmethod
    def isChinese(word):
        for charactor in word:
            if u'\u4e00' <= charactor <= u'\u9fff':
                return True
        else:
            return False

class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.showMenu()
        self.other()

    def showMenu(self):
        "设计托盘的菜单，这里我实现了一个二级菜单"
        self.menu = QMenu()

        self.quitAction = QAction("退出", self, triggered=self.quit)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

    def other(self):
        self.activated.connect(self.iconClied)
        #把鼠标点击图标的信号和槽连接
        self.setIcon(QIcon('logo.ico'))
        self.icon = self.MessageIcon()
        #设置图标

    def iconClied(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        print(reason)

    # def mClied(self):
    #     self.showMessage("提示", "你点了消息", self.icon)

    # def showM(self):

    #     self.showMessage("测试", "我是消息", self.icon)

    def quit(self):
        "保险起见，为了完整的退出"
        self.setVisible(False)
        self.parent().exit()
        qApp.quit()
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.keys()[2])
    window = Translator()
    sys.exit(app.exec_())

