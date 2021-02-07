from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from Warehouse_registration_card import Warehouse_registration_card
from In_Re_management import In_Re_management
from User_registration import User_registration
from Employee_accounting import Employee_accounting
from backup_is import Backup_is
from Warehouse_management import Warehouse_management
class Ui_MainWindow(object):
    def User(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Employee_accounting()
        self.ui.setupUi(self.window)
        self.window.show()
    def TehRep(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Warehouse_registration_card()
        self.ui.setupUi(self.window)
        self.window.show()
    def Doc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = In_Re_management()
        self.ui.setupUi(self.window)
        self.window.show()
    def Inv(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = User_registration()
        self.ui.setupUi(self.window)
        self.window.show()
    def Teh(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Employee_accounting()
        self.ui.setupUi(self.window)
        self.window.show()
    def Back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Backup_is()
        self.ui.setupUi(self.window)
        self.window.show()
    def Div(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Warehouse_management()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(228, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.closeEvent)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 61, 21))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 40, 131, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Div)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.Inv)
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Doc)
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.Teh)
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.TehRep)
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.Back)
        self.verticalLayout.addWidget(self.pushButton_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Chose:"))
        self.pushButton_3.setText(_translate("MainWindow", "Warehouse_management"))
        self.pushButton_4.setText(_translate("MainWindow", "User_registration"))
        self.pushButton_5.setText(_translate("MainWindow", "In_Re_management"))
        self.pushButton_6.setText(_translate("MainWindow", "Employee_accounting"))
        self.pushButton_7.setText(_translate("MainWindow", "Warehouse_registration_card"))
        self.pushButton_8.setText(_translate("MainWindow", "Backup_is"))

    def closeEvent(self, event):
            self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
