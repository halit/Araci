# -*- coding: utf-8 -*-

# www.halitalptekin.com - Halit Alptekin

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(473, 291)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../src/icon/arama.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../src/icon/yer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../src/icon/dosya.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(-60, 20, 251, 161))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../src/icon/sahip.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(150, 10, 291, 181))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Araci v0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setShortcut(QtGui.QApplication.translate("MainWindow", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Arama", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Arama Yeri", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Dosya Tipi", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Ayarlar", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Araci v0.1 - Build 1</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Dosya icinde aramak istediginiz kelimeyi </span><span style=\" font-size:10pt; font-style:italic;\">Arama</span><span style=\" font-size:10pt;\"> sekmesindeki bosluga yaziniz.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Ayarlar </span><span style=\" font-size:10pt;\">sekmesinden arama yapacaginiz yeri ve arama yapilcak dosya uzantisini secebilirsiniz.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Halit Alptekin - </span><a href=\"http://www.halitalptekin.com\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">www.halitalptekin.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Hakkinda", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

