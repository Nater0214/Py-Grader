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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(200, 140)
        main_window.setStyleSheet(u"/*\n"
"    I did not create this\n"
"    This style was created by sommerc\n"
"    The original is here: https://github.com/sommerc/pyqt-stylesheets/blob/master/pyqtcss/src/dark_orange/style.qss\n"
"*/\n"
"\n"
"QToolTip {\n"
"    border: 1px solid black;\n"
"    background-color: #ffa02f;\n"
"    padding: 1px;\n"
"    border-radius: 3px;\n"
"    opacity: 100;\n"
"}\n"
"\n"
"QWidget {\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView {\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover {\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected {\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: transparent;\n"
"    border: 1px solid #ff"
                        "aa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(x1:0, y1:0,\n"
"            x2:0, y2:1,\n"
"            stop:1 #212121,\n"
"            stop:0.4 #343434\n"
"            /*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"        );\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QMenu {\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"    color: #808080;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus {\n"
"    /*border: 1px solid darkgray;*/\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, s"
                        "top: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox {\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #"
                        "464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,\n"
"QPushButton:hover {\n"
"    border: 2px solid QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on {\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    /* just a single line *"
                        "/\n"
"    border-top-right-radius: 3px;\n"
"    /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/dark_orange/img/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid darkgray;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus {\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #222222;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"    height: 7px;\n"
"    margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px solid #1b1b19;\n"
"    border-radius: 2px;\n"
""
                        "    background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    width: 14px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 1px solid #1b1b19;\n"
"    border-radius: 2px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    width: 14px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal,\n"
"QScrollBar::left-arrow:horizontal {\n"
"    border: 1px solid black;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"    background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"    width: 7px;\n"
"    margin: 16px 0 16px 0;\n"
"    border: 1px soli"
                        "d #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid #1b1b19;\n"
"    border-radius: 2px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    height: 14px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #1b1b19;\n"
"    border-radius: 2px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"    height: 14px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    border: 1px solid black;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"    background: white;\n"
"}\n"
""
                        "\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    text-align: center;\n"
"    spacing: 3px;\n"
"    /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button,\n"
"QDockWidget::float-button {\n"
"    text-align: center;\n"
"    spacing: 1px;\n"
"    /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient("
                        "x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover,\n"
"QDockWidget::float-button:hover {\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed,\n"
"QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator {\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px;\n"
"    /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px;\n"
"    /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle {\n"
"    spacin"
                        "g: 3px;\n"
"    /* spacing between items in the tool bar */\n"
"    background: url(:/dark_orange/img/handle.png);\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;"
                        "\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    margin-right: 0;\n"
"    /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first: !selected {\n"
"    margin-left: 0px;\n"
"    /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab: !selected {\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab: !selected:hover {\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4"
                        " #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:unchecked {\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: qradialgradient(cx: 0.5, cy: 0.5,\n"
"            fx: 0.5, fy: 0.5,\n"
"            radius: 1.0,\n"
"            stop: 0.25 #ffaa00,\n"
"            stop: 0.3 #323232);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover,\n"
"QCheckBox::indicator:hover {\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/dark_orange/img/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled,\n"
"QRadioButton::indica"
                        "tor:disabled {\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"            stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
""
                        "}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid darkgray;\n"
"\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}")
        self.main_frame = QFrame(main_window)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(0, 0, 200, 140))
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.main_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.buttons_frame = QFrame(self.main_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons_frame.sizePolicy().hasHeightForWidth())
        self.buttons_frame.setSizePolicy(sizePolicy)
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.buttons_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.run_test_button = QPushButton(self.buttons_frame)
        self.run_test_button.setObjectName(u"run_test_button")

        self.verticalLayout.addWidget(self.run_test_button)

        self.new_test_button = QPushButton(self.buttons_frame)
        self.new_test_button.setObjectName(u"new_test_button")

        self.verticalLayout.addWidget(self.new_test_button)

        self.view_grades_button = QPushButton(self.buttons_frame)
        self.view_grades_button.setObjectName(u"view_grades_button")
        self.view_grades_button.setEnabled(False)

        self.verticalLayout.addWidget(self.view_grades_button)


        self.gridLayout_2.addWidget(self.buttons_frame, 2, 1, 1, 1)

        self.greeting_text = QLabel(self.main_frame)
        self.greeting_text.setObjectName(u"greeting_text")
        self.greeting_text.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.greeting_text, 0, 1, 1, 1)

        self.line = QFrame(self.main_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 1, 1, 1)

        QWidget.setTabOrder(self.run_test_button, self.new_test_button)
        QWidget.setTabOrder(self.new_test_button, self.view_grades_button)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Py-Grader", None))
#if QT_CONFIG(tooltip)
        self.run_test_button.setToolTip(QCoreApplication.translate("main_window", u"Run a test that is available", None))
#endif // QT_CONFIG(tooltip)
        self.run_test_button.setText(QCoreApplication.translate("main_window", u"Run Test", None))
#if QT_CONFIG(tooltip)
        self.new_test_button.setToolTip(QCoreApplication.translate("main_window", u"Create a new test", None))
#endif // QT_CONFIG(tooltip)
        self.new_test_button.setText(QCoreApplication.translate("main_window", u"New Test", None))
#if QT_CONFIG(tooltip)
        self.view_grades_button.setToolTip(QCoreApplication.translate("main_window", u"View the grades from tests\n"
"Not implemented", None))
#endif // QT_CONFIG(tooltip)
        self.view_grades_button.setText(QCoreApplication.translate("main_window", u"View Grades", None))
        self.greeting_text.setText(QCoreApplication.translate("main_window", u"Welcome to Py-Grader", None))
    # retranslateUi

