# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 603)
        MainWindow.setFixedSize(363, 603)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet("background-color:#f8faff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(300, 540, 41, 41))
        self.send.setStyleSheet("background-color:#f8faff;\n"
                                "border-radius: 45px;")
        self.send.setText("")
        self.send.setObjectName("pushButton")
        self.send.setIcon(QtGui.QIcon('res/send1/1.jpg'))
        self.send.setIconSize(QtCore.QSize(38, 38))
        self.message_obv = QtWidgets.QLabel(self.centralwidget)
        self.message_obv.setGeometry(QtCore.QRect(20, 540, 270, 41))
        self.message_obv.setStyleSheet("border-radius: 20px;\n"
                                       "background-color:#f8faff;\n"
                                       "border: 1px solid #9C9C9C")
        self.message_obv.setObjectName("message_obv")
        self.message = QtWidgets.QLineEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(35, 545, 240, 31))
        self.message.setStyleSheet("border-radius: 20px;\n"
                                   "background-color:#f8faff;\n"
                                   "color:#123467;")
        self.message.setObjectName("message")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.message.setFont(font)
        self.message.setMaxLength(150)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.label.setStyleSheet("background-color:#f8faff;\n"
                                 "border-radius: 45px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(320, 10, 31, 41))
        self.settings.setStyleSheet("background-color:#f8faff;\n"
                                    "border-radius: 45px;")
        self.settings.setText("")
        self.settings.setObjectName("settings")
        self.labl4blu = QtWidgets.QLabel(self.centralwidget)
        self.labl4blu.setGeometry(QtCore.QRect(220, 400, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labl4blu.setFont(font)
        self.labl4blu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labl4blu.setStyleSheet("background-color:#77d8fb;\n"
                                    "border-radius: 20px;\n"
                                    "color:#123467;")
        self.labl4blu.setText("!")
        self.labl4blu.setTextFormat(QtCore.Qt.AutoText)
        self.labl4blu.setAlignment(QtCore.Qt.AlignCenter)
        self.labl4blu.setObjectName("labl4blu")
        self.labl3blu = QtWidgets.QLabel(self.centralwidget)
        self.labl3blu.setGeometry(QtCore.QRect(220, 320, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labl3blu.setFont(font)
        self.labl3blu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labl3blu.setStyleSheet("background-color:#77d8fb;\n"
                                    "border-radius: 20px;\n"
                                    "color:#123467;")
        self.labl3blu.setText("!")
        self.labl3blu.setTextFormat(QtCore.Qt.AutoText)
        self.labl3blu.setAlignment(QtCore.Qt.AlignCenter)
        self.labl3blu.setObjectName("labl3blu")
        self.labl2blu = QtWidgets.QLabel(self.centralwidget)
        self.labl2blu.setGeometry(QtCore.QRect(220, 240, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labl2blu.setFont(font)
        self.labl2blu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labl2blu.setStyleSheet("background-color:#77d8fb;\n"
                                    "border-radius: 20px;\n"
                                    "color:#123467;")
        self.labl2blu.setText("!")
        self.labl2blu.setTextFormat(QtCore.Qt.AutoText)
        self.labl2blu.setAlignment(QtCore.Qt.AlignCenter)
        self.labl2blu.setObjectName("labl2blu")
        self.labl1blu = QtWidgets.QLabel(self.centralwidget)
        self.labl1blu.setGeometry(QtCore.QRect(220, 160, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labl1blu.setFont(font)
        self.labl1blu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labl1blu.setStyleSheet("background-color:#77d8fb;\n"
                                    "border-radius: 20px;\n"
                                    "color:#123467;")
        self.labl1blu.setText("!")
        self.labl1blu.setTextFormat(QtCore.Qt.AutoText)
        self.labl1blu.setAlignment(QtCore.Qt.AlignCenter)
        self.labl1blu.setObjectName("labl1blu")
        self.labl0blu = QtWidgets.QLabel(self.centralwidget)
        self.labl0blu.setGeometry(QtCore.QRect(220, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labl0blu.setFont(font)
        self.labl0blu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labl0blu.setStyleSheet("background-color:#77d8fb;\n"
                                    "border-radius: 20px;\n"
                                    "color:#123467;")
        self.labl0blu.setText("!")
        self.labl0blu.setTextFormat(QtCore.Qt.AutoText)
        self.labl0blu.setAlignment(QtCore.Qt.AlignCenter)
        self.labl0blu.setObjectName("labl0blu")
        self.labl1red = QtWidgets.QLabel(self.centralwidget)
        self.labl1red.setGeometry(QtCore.QRect(20, 160, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labl1red.setFont(font)
        self.labl1red.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labl1red.setStyleSheet("background-color:#F08080;\n"
                                    "border-radius: 20px;\n"
                                    "color:#FFFFFF;")
        self.labl1red.setText("!")
        self.labl1red.setTextFormat(QtCore.Qt.AutoText)
        self.labl1red.setAlignment(QtCore.Qt.AlignCenter)
        self.labl1red.setObjectName("labl1red")
        self.labl2red = QtWidgets.QLabel(self.centralwidget)
        self.labl2red.setGeometry(QtCore.QRect(20, 240, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labl2red.setFont(font)
        self.labl2red.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labl2red.setStyleSheet("background-color:#F08080;\n"
                                    "border-radius: 20px;\n"
                                    "color:#FFFFFF;")
        self.labl2red.setText("!")
        self.labl2red.setTextFormat(QtCore.Qt.AutoText)
        self.labl2red.setAlignment(QtCore.Qt.AlignCenter)
        self.labl2red.setObjectName("labl2red")
        self.labl0red = QtWidgets.QLabel(self.centralwidget)
        self.labl0red.setGeometry(QtCore.QRect(20, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labl0red.setFont(font)
        self.labl0red.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labl0red.setStyleSheet("background-color:#F08080;\n"
                                    "border-radius: 20px;\n"
                                    "color:#FFFFFF;")
        self.labl0red.setText("!")
        self.labl0red.setTextFormat(QtCore.Qt.AutoText)
        self.labl0red.setAlignment(QtCore.Qt.AlignCenter)
        self.labl0red.setObjectName("labl0red")
        self.labl3red = QtWidgets.QLabel(self.centralwidget)
        self.labl3red.setGeometry(QtCore.QRect(20, 160, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labl3red.setFont(font)
        self.labl3red.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labl3red.setStyleSheet("background-color:#F08080;\n"
                                    "border-radius: 20px;\n"
                                    "color:#FFFFFF;")
        self.labl3red.setText("!")
        self.labl3red.setTextFormat(QtCore.Qt.AutoText)
        self.labl3red.setAlignment(QtCore.Qt.AlignCenter)
        self.labl3red.setObjectName("labl1red")
        for i in [self.labl0red, self.labl1red, self.labl2red, self.labl3red,
                  self.labl0blu, self.labl1blu, self.labl2blu, self.labl3blu, self.labl4blu]:
            i.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """----------------------------------------------"""
        self.weather_label = QtWidgets.QLabel(self.centralwidget)
        self.weather_label.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.weather_label.setStyleSheet("background-color:#f8faff;\n"
                                         "border-radius: 20px;")
        self.weather_label.setText("")
        self.weather_label.setScaledContents(True)
        self.weather_label.setObjectName("weather_label")
        self.about_weather = QtWidgets.QTextBrowser(self.centralwidget)
        self.about_weather.setGeometry(QtCore.QRect(10, 90, 281, 131))
        self.about_weather.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.about_weather.setStyleSheet("background-color:#f8faff;\n"
                                         "border-radius: 20px;")
        self.about_weather.setObjectName("about_weather")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.about_weather.setFont(font)
        self.weather_label.hide()
        self.about_weather.hide()
        self.weather = QtWidgets.QLabel(self.centralwidget)
        self.weather.setGeometry(QtCore.QRect(80, 62, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.weather.setFont(font)
        self.weather.setText("")
        self.weather.setAlignment(QtCore.Qt.AlignCenter)
        self.weather.setObjectName("weather")
        """----------------------------------------------"""
        self.media_player = QMediaPlayer()
        self.labelG = QtWidgets.QLabel(self.centralwidget)
        self.labelG.setGeometry(QtCore.QRect(10, 10, 160, 160))
        self.labelG.setStyleSheet("background-color:#f8faff;\n"
                                  "border-radius: 20px;")
        self.labelG.setText("")
        self.labelG.setObjectName("labelG")
        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setGeometry(QtCore.QRect(10, 190, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.author.setFont(font)
        self.author.setText("")
        self.author.setAlignment(QtCore.Qt.AlignCenter)
        self.author.setObjectName("author")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(10, 230, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setText("")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.name.setStyleSheet("background-color:#2864fe;\n"
                                "border-radius: 10px;\n"
                                "color: #f8faff;")
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(14, 126, 40, 40))
        self.pause.setStyleSheet("background-color:#f8faff;\n"
                                 "border-radius: 20px;")
        self.pause.setText("")
        self.pause.setObjectName("pause")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(120, 190, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.time.setFont(font)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.time.setText('0:0')
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(142, 135, 29, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.verticalSlider.setFont(font)
        self.verticalSlider.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
                                          "color:blue;"
                                          "")
        self.verticalSlider.setSingleStep(10)
        self.verticalSlider.setProperty("value", 25)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        self.gif = QtGui.QMovie('res/Music/recorder.gif')
        self.gif.setScaledSize(QtCore.QSize(160, 160))
        self.labelG.setMovie(self.gif)
        self.gif.start()
        self.pause.setIcon(QtGui.QIcon('res/Music/play.jpg'))
        self.pause.setIconSize(QtCore.QSize(40, 40))
        self.n = 1
        self.pause.clicked.connect(self.click)
        self.verticalSlider.valueChanged.connect(lambda: self.media_player.setVolume(self.verticalSlider.value()))
        for i in [self.author, self.name, self.time, self.labelG, self.pause, self.verticalSlider]:
            i.hide()
        # self.set_data(('res\\Music\\Green Day - 21 Guns.mp3', '21 Guns', 'Green Day', '5:22', '??????'))
        # self.click()
        """-----------------------------------------------------------"""

    def click(self):
        if self.n:
            self.pause.setIcon(QtGui.QIcon('res/Music/pause.jpg'))
            self.gif.start()
            self.n = 0
            self.media_player.play()
        else:
            self.pause.setIcon(QtGui.QIcon('res/Music/play.jpg'))
            self.gif.stop()
            self.n = 1
            self.media_player.pause()
        with open('res/Music/pause.txt', 'w') as f:
            f.write(str(self.n))

    def set_data(self, data):
        #  ('res\\Music\\Green Day - 21 Guns.mp3', '21 Guns', 'Green Day', '5:22', '??????')

        pas, name, author, time, genre = data
        self.name.setText(name)
        self.author.setText(author)
        self.time.setText(time)
        url = QUrl.fromLocalFile(pas)
        content = QMediaContent(url)
        self.media_player.setMedia(content)
        self.media_player.setVolume(25)

    def set_weather(self, pas):
        self.gif = QtGui.QMovie(pas)
        self.gif.setScaledSize(QtCore.QSize(71, 71))
        self.weather_label.setMovie(self.gif)
        self.gif.start()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('res/LOGO.jpg'))
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
