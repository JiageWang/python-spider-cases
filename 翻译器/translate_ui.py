# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'translate_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_translator(object):
    def setupUi(self, translator):
        translator.setObjectName("translator")
        translator.resize(612, 164)
        self.centralwidget = QtWidgets.QWidget(translator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_translate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_translate.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_translate.setFont(font)
        self.pushButton_translate.setObjectName("pushButton_translate")
        self.horizontalLayout.addWidget(self.pushButton_translate)
        self.lineEdit_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_input.sizePolicy().hasHeightForWidth())
        self.lineEdit_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.horizontalLayout.addWidget(self.lineEdit_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_youdao = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_youdao.sizePolicy().hasHeightForWidth())
        self.lineEdit_youdao.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_youdao.setFont(font)
        self.lineEdit_youdao.setObjectName("lineEdit_youdao")
        self.horizontalLayout_2.addWidget(self.lineEdit_youdao)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_google = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_google.sizePolicy().hasHeightForWidth())
        self.lineEdit_google.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_google.setFont(font)
        self.lineEdit_google.setObjectName("lineEdit_google")
        self.horizontalLayout_3.addWidget(self.lineEdit_google)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_bing = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_bing.sizePolicy().hasHeightForWidth())
        self.lineEdit_bing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_bing.setFont(font)
        self.lineEdit_bing.setObjectName("lineEdit_bing")
        self.horizontalLayout_4.addWidget(self.lineEdit_bing)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        translator.setCentralWidget(self.centralwidget)

        self.retranslateUi(translator)
        QtCore.QMetaObject.connectSlotsByName(translator)

    def retranslateUi(self, translator):
        _translate = QtCore.QCoreApplication.translate
        translator.setWindowTitle(_translate("translator", "MainWindow"))
        self.pushButton_translate.setText(_translate("translator", "翻译"))
        self.label.setText(_translate("translator", "有道"))
        self.label_2.setText(_translate("translator", "谷歌"))
        self.label_3.setText(_translate("translator", "必应"))

