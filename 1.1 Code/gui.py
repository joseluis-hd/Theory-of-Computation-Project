# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerDFvZtR.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 566)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 321, 531))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 301, 131))
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 20, 281, 31))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 60, 281, 24))
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 90, 281, 24))
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 160, 301, 361))
        self.listView = QListView(self.groupBox_2)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 20, 281, 331))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(340, 10, 501, 531))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox_4 = QGroupBox(self.frame_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 350, 199, 82))
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 131, 16))
        self.groupBox_5 = QGroupBox(self.frame_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 200, 199, 83))
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 131, 16))
        self.groupBox_6 = QGroupBox(self.frame_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(30, 50, 199, 82))
        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 131, 16))
        self.groupBox_7 = QGroupBox(self.frame_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(280, 200, 199, 83))
        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 131, 16))
        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(120, 130, 20, 81))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(120, 280, 20, 81))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.frame_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(230, 230, 51, 20))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ingresar Entarda", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Salida Actual", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Disco", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bloqueado y Suspendido", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Memoria RAM", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bloqueado y Suspendido", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Gestor de Procesos", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bloqueado y Suspendido", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Terminados", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bloqueado y Suspendido", None))
    # retranslateUi

