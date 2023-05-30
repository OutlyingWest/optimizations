# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(400, 400))
        MainWindow.setBaseSize(QSize(385, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, 10)
        self.ProjectsButton = QPushButton(self.centralwidget)
        self.ProjectsButton.setObjectName(u"ProjectsButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ProjectsButton.sizePolicy().hasHeightForWidth())
        self.ProjectsButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.ProjectsButton.setFont(font)

        self.verticalLayout.addWidget(self.ProjectsButton)

        self.MeasurersButton = QPushButton(self.centralwidget)
        self.MeasurersButton.setObjectName(u"MeasurersButton")
        sizePolicy1.setHeightForWidth(self.MeasurersButton.sizePolicy().hasHeightForWidth())
        self.MeasurersButton.setSizePolicy(sizePolicy1)
        self.MeasurersButton.setFont(font)

        self.verticalLayout.addWidget(self.MeasurersButton)

        self.ArchitectsButton = QPushButton(self.centralwidget)
        self.ArchitectsButton.setObjectName(u"ArchitectsButton")
        sizePolicy1.setHeightForWidth(self.ArchitectsButton.sizePolicy().hasHeightForWidth())
        self.ArchitectsButton.setSizePolicy(sizePolicy1)
        self.ArchitectsButton.setFont(font)

        self.verticalLayout.addWidget(self.ArchitectsButton)

        self.VolumeButton = QPushButton(self.centralwidget)
        self.VolumeButton.setObjectName(u"VolumeButton")
        sizePolicy1.setHeightForWidth(self.VolumeButton.sizePolicy().hasHeightForWidth())
        self.VolumeButton.setSizePolicy(sizePolicy1)
        self.VolumeButton.setFont(font)

        self.verticalLayout.addWidget(self.VolumeButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Optimizations", None))
        self.ProjectsButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.MeasurersButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b \u043b\u043e\u0433\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.ArchitectsButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b \u0444\u0438\u043d\u0430\u043d\u0441\u043e\u0432", None))
        self.VolumeButton.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0445\u0433\u0430\u043b\u0442\u0435\u0440\u0438\u044f", None))
    # retranslateUi

