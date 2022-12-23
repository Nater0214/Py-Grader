# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_mainFrame(object):
    def setupUi(self, mainFrame):
        if not mainFrame.objectName():
            mainFrame.setObjectName(u"mainFrame")
        mainFrame.resize(500, 140)
        mainFrame.setMaximumSize(QSize(500, 140))
        self.formLayout = QFormLayout(mainFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.buttonsFrame = QFrame(mainFrame)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.buttonsFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.greetingText = QLabel(self.buttonsFrame)
        self.greetingText.setObjectName(u"greetingText")
        self.greetingText.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.greetingText)

        self.pushButton = QPushButton(self.buttonsFrame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.buttonsFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.buttonsFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.buttonsFrame)


        self.retranslateUi(mainFrame)

        QMetaObject.connectSlotsByName(mainFrame)
    # setupUi

    def retranslateUi(self, mainFrame):
        mainFrame.setWindowTitle(QCoreApplication.translate("mainFrame", u"Form", None))
        self.greetingText.setText(QCoreApplication.translate("mainFrame", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("mainFrame", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainFrame", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainFrame", u"PushButton", None))
    # retranslateUi

