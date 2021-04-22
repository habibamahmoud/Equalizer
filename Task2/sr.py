# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 944)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spectro1 = QtWidgets.QLabel(self.frame_3)
        self.spectro1.setMaximumSize(QtCore.QSize(632, 304))
        self.spectro1.setText("")
        self.spectro1.setPixmap(QtGui.QPixmap("black.png"))
        self.spectro1.setObjectName("spectro1")
        self.gridLayout_4.addWidget(self.spectro1, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(657, 328))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.sig2 = PlotWidget(self.frame_5)
        self.sig2.setGeometry(QtCore.QRect(10, 14, 633, 149))
        self.sig2.setMaximumSize(QtCore.QSize(633, 304))
        self.sig2.setObjectName("sig2")
        self.fourier2 = PlotWidget(self.frame_5)
        self.fourier2.setGeometry(QtCore.QRect(10, 170, 633, 148))
        self.fourier2.setMinimumSize(QtCore.QSize(633, 148))
        self.fourier2.setMaximumSize(QtCore.QSize(633, 304))
        self.fourier2.setObjectName("fourier2")
        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem = QtWidgets.QSpacerItem(743, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 0, 8, 1, 1)
        self.right = QtWidgets.QPushButton(self.frame_7)
        self.right.setStyleSheet("border-image: url(right.png)")
        self.right.setText("")
        self.right.setObjectName("right")
        self.gridLayout_8.addWidget(self.right, 0, 5, 1, 1)
        self.pause2 = QtWidgets.QPushButton(self.frame_7)
        self.pause2.setStyleSheet("border-image: url(stop.png)")
        self.pause2.setText("")
        self.pause2.setObjectName("pause2")
        self.gridLayout_8.addWidget(self.pause2, 0, 0, 1, 1)
        self.left = QtWidgets.QPushButton(self.frame_7)
        self.left.setStyleSheet("border-image: url(left.png)")
        self.left.setText("")
        self.left.setObjectName("left")
        self.gridLayout_8.addWidget(self.left, 0, 4, 1, 1)
        self.up = QtWidgets.QPushButton(self.frame_7)
        self.up.setStyleSheet("border-image: url(up.png)")
        self.up.setText("")
        self.up.setObjectName("up")
        self.gridLayout_8.addWidget(self.up, 0, 2, 1, 1)
        self.zoom_in = QtWidgets.QPushButton(self.frame_7)
        self.zoom_in.setStyleSheet("border-image: url(plus.png)")
        self.zoom_in.setText("")
        self.zoom_in.setObjectName("zoom_in")
        self.gridLayout_8.addWidget(self.zoom_in, 0, 6, 1, 1)
        self.down = QtWidgets.QPushButton(self.frame_7)
        self.down.setStyleSheet("border-image: url(down.png)")
        self.down.setText("")
        self.down.setObjectName("down")
        self.gridLayout_8.addWidget(self.down, 0, 3, 1, 1)
        self.zoom_out = QtWidgets.QPushButton(self.frame_7)
        self.zoom_out.setStyleSheet("border-image: url(minus.png)")
        self.zoom_out.setText("")
        self.zoom_out.setObjectName("zoom_out")
        self.gridLayout_8.addWidget(self.zoom_out, 0, 7, 1, 1)
        self.play2 = QtWidgets.QPushButton(self.frame_7)
        self.play2.setStyleSheet("border-image: url(play1.png)")
        self.play2.setText("")
        self.play2.setObjectName("play2")
        self.gridLayout_8.addWidget(self.play2, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_7, 3, 0, 1, 2)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.spectro2 = QtWidgets.QLabel(self.frame_6)
        self.spectro2.setMaximumSize(QtCore.QSize(632, 304))
        self.spectro2.setText("")
        self.spectro2.setPixmap(QtGui.QPixmap("black.png"))
        self.spectro2.setScaledContents(True)
        self.spectro2.setObjectName("spectro2")
        self.gridLayout_7.addWidget(self.spectro2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 2, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(657, 328))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.sig1 = PlotWidget(self.frame_2)
        self.sig1.setGeometry(QtCore.QRect(12, 12, 633, 149))
        self.sig1.setMinimumSize(QtCore.QSize(633, 149))
        self.sig1.setMaximumSize(QtCore.QSize(633, 304))
        self.sig1.setObjectName("sig1")
        self.fourier1 = PlotWidget(self.frame_2)
        self.fourier1.setGeometry(QtCore.QRect(12, 168, 633, 148))
        self.fourier1.setMinimumSize(QtCore.QSize(633, 148))
        self.fourier1.setMaximumSize(QtCore.QSize(633, 304))
        self.fourier1.setObjectName("fourier1")
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(1320, 120))
        self.frame_4.setMaximumSize(QtCore.QSize(1320, 120))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.play1 = QtWidgets.QPushButton(self.frame_4)
        self.play1.setGeometry(QtCore.QRect(70, 40, 41, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play1.sizePolicy().hasHeightForWidth())
        self.play1.setSizePolicy(sizePolicy)
        self.play1.setMaximumSize(QtCore.QSize(41, 28))
        self.play1.setStyleSheet("border-image: url(play1.png)")
        self.play1.setText("")
        self.play1.setObjectName("play1")
        self.s1 = QtWidgets.QSlider(self.frame_4)
        self.s1.setGeometry(QtCore.QRect(221, 12, 41, 84))
        self.s1.setMaximum(5)
        self.s1.setSliderPosition(1)
        self.s1.setOrientation(QtCore.Qt.Vertical)
        self.s1.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s1.setObjectName("s1")
        self.s2 = QtWidgets.QSlider(self.frame_4)
        self.s2.setGeometry(QtCore.QRect(309, 12, 41, 84))
        self.s2.setMaximum(5)
        self.s2.setSliderPosition(1)
        self.s2.setOrientation(QtCore.Qt.Vertical)
        self.s2.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s2.setObjectName("s2")
        self.s3 = QtWidgets.QSlider(self.frame_4)
        self.s3.setGeometry(QtCore.QRect(397, 12, 41, 84))
        self.s3.setMaximum(5)
        self.s3.setSliderPosition(1)
        self.s3.setOrientation(QtCore.Qt.Vertical)
        self.s3.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s3.setObjectName("s3")
        self.s4 = QtWidgets.QSlider(self.frame_4)
        self.s4.setGeometry(QtCore.QRect(485, 12, 41, 84))
        self.s4.setMaximum(5)
        self.s4.setSliderPosition(1)
        self.s4.setOrientation(QtCore.Qt.Vertical)
        self.s4.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s4.setObjectName("s4")
        self.s5 = QtWidgets.QSlider(self.frame_4)
        self.s5.setGeometry(QtCore.QRect(573, 12, 41, 84))
        self.s5.setMaximum(5)
        self.s5.setSliderPosition(1)
        self.s5.setOrientation(QtCore.Qt.Vertical)
        self.s5.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s5.setObjectName("s5")
        self.s6 = QtWidgets.QSlider(self.frame_4)
        self.s6.setGeometry(QtCore.QRect(661, 12, 41, 84))
        self.s6.setMaximum(5)
        self.s6.setSliderPosition(1)
        self.s6.setOrientation(QtCore.Qt.Vertical)
        self.s6.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s6.setObjectName("s6")
        self.s7 = QtWidgets.QSlider(self.frame_4)
        self.s7.setGeometry(QtCore.QRect(749, 12, 41, 84))
        self.s7.setMaximum(5)
        self.s7.setSliderPosition(1)
        self.s7.setOrientation(QtCore.Qt.Vertical)
        self.s7.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s7.setObjectName("s7")
        self.s8 = QtWidgets.QSlider(self.frame_4)
        self.s8.setGeometry(QtCore.QRect(837, 12, 41, 84))
        self.s8.setMaximum(5)
        self.s8.setSliderPosition(1)
        self.s8.setOrientation(QtCore.Qt.Vertical)
        self.s8.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s8.setObjectName("s8")
        self.s10 = QtWidgets.QSlider(self.frame_4)
        self.s10.setGeometry(QtCore.QRect(1013, 12, 41, 84))
        self.s10.setMaximum(5)
        self.s10.setSliderPosition(1)
        self.s10.setOrientation(QtCore.Qt.Vertical)
        self.s10.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s10.setObjectName("s10")
        self.color = QtWidgets.QComboBox(self.frame_4)
        self.color.setGeometry(QtCore.QRect(1090, 10, 72, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color.sizePolicy().hasHeightForWidth())
        self.color.setSizePolicy(sizePolicy)
        self.color.setMaximumSize(QtCore.QSize(72, 22))
        self.color.setObjectName("color")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.pause1 = QtWidgets.QPushButton(self.frame_4)
        self.pause1.setGeometry(QtCore.QRect(10, 40, 41, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause1.sizePolicy().hasHeightForWidth())
        self.pause1.setSizePolicy(sizePolicy)
        self.pause1.setMaximumSize(QtCore.QSize(41, 28))
        self.pause1.setStyleSheet("border-image: url(stop.png)")
        self.pause1.setText("")
        self.pause1.setObjectName("pause1")
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox.setGeometry(QtCore.QRect(140, 40, 81, 20))
        self.checkBox.setMaximumSize(QtCore.QSize(81, 20))
        self.checkBox.setObjectName("checkBox")
        self.s9 = QtWidgets.QSlider(self.frame_4)
        self.s9.setGeometry(QtCore.QRect(920, 10, 41, 84))
        self.s9.setMaximum(5)
        self.s9.setSliderPosition(1)
        self.s9.setOrientation(QtCore.Qt.Vertical)
        self.s9.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s9.setObjectName("s9")
        self.spectrogram1 = QtWidgets.QSlider(self.frame_4)
        self.spectrogram1.setGeometry(QtCore.QRect(1192, 10, 41, 84))
        self.spectrogram1.setMaximum(10)
        self.spectrogram1.setSliderPosition(5)
        self.spectrogram1.setOrientation(QtCore.Qt.Vertical)
        self.spectrogram1.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.spectrogram1.setObjectName("spectrogram1")
        self.spectrogram2 = QtWidgets.QSlider(self.frame_4)
        self.spectrogram2.setGeometry(QtCore.QRect(1280, 10, 41, 84))
        self.spectrogram2.setMaximum(10)
        self.spectrogram2.setSliderPosition(5)
        self.spectrogram2.setOrientation(QtCore.Qt.Vertical)
        self.spectrogram2.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.spectrogram2.setObjectName("spectrogram2")
        self.gain1 = QtWidgets.QLabel(self.frame_4)
        self.gain1.setGeometry(QtCore.QRect(230, 100, 16, 16))
        self.gain1.setObjectName("gain1")
        self.gain1_2 = QtWidgets.QLabel(self.frame_4)
        self.gain1_2.setGeometry(QtCore.QRect(320, 100, 16, 16))
        self.gain1_2.setObjectName("gain1_2")
        self.gain1_3 = QtWidgets.QLabel(self.frame_4)
        self.gain1_3.setGeometry(QtCore.QRect(410, 100, 16, 16))
        self.gain1_3.setObjectName("gain1_3")
        self.gain1_4 = QtWidgets.QLabel(self.frame_4)
        self.gain1_4.setGeometry(QtCore.QRect(500, 100, 16, 16))
        self.gain1_4.setObjectName("gain1_4")
        self.gain1_5 = QtWidgets.QLabel(self.frame_4)
        self.gain1_5.setGeometry(QtCore.QRect(590, 100, 16, 16))
        self.gain1_5.setObjectName("gain1_5")
        self.gain1_6 = QtWidgets.QLabel(self.frame_4)
        self.gain1_6.setGeometry(QtCore.QRect(680, 100, 16, 16))
        self.gain1_6.setObjectName("gain1_6")
        self.gain1_7 = QtWidgets.QLabel(self.frame_4)
        self.gain1_7.setGeometry(QtCore.QRect(760, 100, 16, 16))
        self.gain1_7.setObjectName("gain1_7")
        self.gain1_8 = QtWidgets.QLabel(self.frame_4)
        self.gain1_8.setGeometry(QtCore.QRect(850, 100, 16, 16))
        self.gain1_8.setObjectName("gain1_8")
        self.gain1_9 = QtWidgets.QLabel(self.frame_4)
        self.gain1_9.setGeometry(QtCore.QRect(940, 100, 16, 16))
        self.gain1_9.setObjectName("gain1_9")
        self.gain1_10 = QtWidgets.QLabel(self.frame_4)
        self.gain1_10.setGeometry(QtCore.QRect(1030, 100, 16, 16))
        self.gain1_10.setObjectName("gain1_10")
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPrint_2 = QtWidgets.QMenu(self.menuFile)
        self.menuPrint_2.setObjectName("menuPrint_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionimport = QtWidgets.QAction(MainWindow)
        self.actionimport.setObjectName("actionimport")
        # self.actionas_PDF = QtWidgets.QAction(MainWindow)
        # self.actionas_PDF.setObjectName("actionas_PDF")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionNew.setObjectName("actionNew")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionas_PDF_2 = QtWidgets.QAction(MainWindow)
        self.actionas_PDF_2.setObjectName("actionas_PDF_2")
        self.menuPrint_2.addAction(self.actionas_PDF_2)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.menuPrint_2.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.s1.valueChanged['int'].connect(self.gain1.setNum)
        self.s2.valueChanged['int'].connect(self.gain1_2.setNum)
        self.s3.valueChanged['int'].connect(self.gain1_3.setNum)
        self.s4.valueChanged['int'].connect(self.gain1_4.setNum)
        self.s5.valueChanged['int'].connect(self.gain1_5.setNum)
        self.s6.valueChanged['int'].connect(self.gain1_6.setNum)
        self.s7.valueChanged['int'].connect(self.gain1_7.setNum)
        self.s8.valueChanged['int'].connect(self.gain1_8.setNum)
        self.s9.valueChanged['int'].connect(self.gain1_9.setNum)
        self.s10.valueChanged['int'].connect(self.gain1_10.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.right.setShortcut(_translate("MainWindow", "Right"))
        self.pause2.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.left.setShortcut(_translate("MainWindow", "Left"))
        self.up.setShortcut(_translate("MainWindow", "Up"))
        self.zoom_in.setShortcut(_translate("MainWindow", "+"))
        self.down.setShortcut(_translate("MainWindow", "Down"))
        self.zoom_out.setShortcut(_translate("MainWindow", "-"))
        self.play2.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.play1.setShortcut(_translate("MainWindow", "P"))
        self.color.setItemText(0, _translate("MainWindow", "Viridis"))
        self.color.setItemText(1, _translate("MainWindow", "Plasma"))
        self.color.setItemText(2, _translate("MainWindow", "Inferno"))
        self.color.setItemText(3, _translate("MainWindow", "Magma"))
        self.color.setItemText(4, _translate("MainWindow", "Cividis"))
        self.pause1.setShortcut(_translate("MainWindow", "O"))
        self.checkBox.setText(_translate("MainWindow", "hide/show"))
        self.gain1.setText(_translate("MainWindow", "1"))
        self.gain1_2.setText(_translate("MainWindow", "1"))
        self.gain1_3.setText(_translate("MainWindow", "1"))
        self.gain1_4.setText(_translate("MainWindow", "1"))
        self.gain1_5.setText(_translate("MainWindow", "1"))
        self.gain1_6.setText(_translate("MainWindow", "1"))
        self.gain1_7.setText(_translate("MainWindow", "1"))
        self.gain1_8.setText(_translate("MainWindow", "1"))
        self.gain1_9.setText(_translate("MainWindow", "1"))
        self.gain1_10.setText(_translate("MainWindow", "1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPrint_2.setTitle(_translate("MainWindow", "Print"))
        self.actionimport.setText(_translate("MainWindow", "import"))
        self.actionimport.setShortcut(_translate("MainWindow", "Ctrl+I"))
        # self.actionas_PDF.setText(_translate("MainWindow", "as PDF"))
        # self.actionas_PDF.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionImport.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionas_PDF_2.setText(_translate("MainWindow", "as PDF"))
        self.actionas_PDF_2.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.checkBox.stateChanged.connect(self.hide)
        self.actionNew.triggered.connect(self.newWindow)


    def newWindow(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


    def hide(self, state):

        if state == QtCore.Qt.Checked:
            self.spectro1.hide()
            self.spectro2.hide()
        else:
            self.spectro1.show()
            self.spectro2.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())