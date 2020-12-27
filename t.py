from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 600)
        self.TEXT = QtWidgets.QTextBrowser(Dialog)
        self.TEXT.setGeometry(QtCore.QRect(890, 30, 131, 81))
        self.TEXT.setObjectName("TEXT")
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(275, 115, 743, 483))
        self.imgLabel.setAutoFillBackground(False)
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        

        self.CAPTURE = QtWidgets.QPushButton(Dialog)
        self.CAPTURE.setGeometry(QtCore.QRect(200, 30, 181, 81))
        self.CAPTURE.setObjectName("CAPTURE")

        self.imgLabel_2 = QtWidgets.QLabel(Dialog)
        self.imgLabel_2.setGeometry(QtCore.QRect(0, 0, 1922,30))
        self.imgLabel_2.setAutoFillBackground(False)
        self.imgLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel_2.setText("")
        self.imgLabel_2.setPixmap(QtGui.QPixmap("ngang1.png"))
        self.imgLabel_2.setObjectName("imgLabel_2")
        # creating a combo box for selecting camera
        self.camera_selector1 = QtWidgets.QComboBox(Dialog)
        self.camera_selector1.setGeometry(QtCore.QRect(550, 30, 171, 81))
        # adding status tip to it
        #self.camera_selector1.addItems("TỰ động chụp")
       # self.camera_selector1.setToolTip("TỰ động chụp")

        # creating a combo box for selecting camera
        self.camera_selector = QtWidgets.QComboBox(Dialog)
        self.camera_selector.setGeometry(QtCore.QRect(0, 30, 201, 81))
        # adding status tip to it
        self.camera_selector.setStatusTip("Choose camera to take pictures")

        # adding tool tip to it
        self.camera_selector.setToolTip("Select Camera")
        self.camera_selector.setToolTipDuration(2500)


        self.NEXT_3 = QtWidgets.QPushButton(Dialog)
        self.NEXT_3.setGeometry(QtCore.QRect(380, 30, 171, 81))
        self.NEXT_3.setObjectName("NEXT_3")
        self.NEXT_7 = QtWidgets.QPushButton(Dialog)
        self.NEXT_7.setGeometry(QtCore.QRect(720, 30, 171, 81))
        self.NEXT_7.setObjectName("NEXT_7")

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(5, 115, 265, 475))
        self.listWidget.setObjectName("ListWidgetItem")
        self.listWidget.setIconSize(QtCore.QSize(188, 190))
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        
#         self.camera_selector3 = QtWidgets.QComboBox(self.listWidget)
#         self.camera_selector3.setGeometry(QtCore.QRect(2, 2, 220, 60))
  
        

        self.it = QtWidgets.QListWidgetItem(self.listWidget)
        self.checkBox_4 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_4.setGeometry(QtCore.QRect(5, 5, 50, 50))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_5.setGeometry(QtCore.QRect(5, 50, 50, 50))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_4")
        self.checkBox_6 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_6.setGeometry(QtCore.QRect(180, 100, 50, 50))
        self.checkBox_7 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_7.setGeometry(QtCore.QRect(180, 150, 50, 50))
        self.checkBox_8 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_8.setGeometry(QtCore.QRect(180, 200, 50, 50))
        self.checkBox_9 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_9.setGeometry(QtCore.QRect(180, 250, 50, 50))
        self.checkBox_10 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_10.setGeometry(QtCore.QRect(180, 300, 50, 50))
        self.checkBox_11 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_11.setGeometry(QtCore.QRect(180,350, 50, 50))
        self.checkBox_12 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_12.setGeometry(QtCore.QRect(180, 500, 50, 50))
        self.checkBox_13 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_14 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_15 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_16 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_17 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_18 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_19 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_20 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_21 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_22 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_23 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_24 = QtWidgets.QCheckBox(self.listWidget)
        self.checkBox_25 = QtWidgets.QCheckBox(self.listWidget)

        self.it1 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it2 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it3 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it4 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it5 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it6 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it7 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it8 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it9 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it10 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it11 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it12 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it13 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it14 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it15 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it16 = QtWidgets.QListWidgetItem(self.listWidget)
        self.it17 = QtWidgets.QListWidgetItem(self.listWidget)

        self.TEXT.raise_()
        self.imgLabel.raise_()
#         self.checkBox_4.raise_()

        self.imgLabel_2.raise_()
        self.CAPTURE.raise_()
        self.NEXT_3.raise_()
        self.NEXT_7.raise_()

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CAPTURE.setText(_translate("Dialog", "Chụp Ảnh"))
        self.NEXT_3.setText(_translate("Dialog", "Chẩn Đoán"))
        self.NEXT_7.setText(_translate("Dialog", "Đóng"))



