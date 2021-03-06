from PyQt5 import QtCore, QtGui, QtWidgets
from Employee_war_card import  Empl
import MySQLdb   as mysql

class In_Re_management(object):
    def show_Users(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Empl()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 31, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 50, 101, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 50, 81, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 50, 81, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 50, 151, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(520, 50, 91, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(620, 50, 71, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 30, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(630, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 130, 161, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_Users)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(190, 80, 381, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton")
        self.pushButton_5.clicked.connect(self.change)
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton")
        self.pushButton_6.clicked.connect(self.change)
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton")
        self.pushButton_7.clicked.connect(self.change)
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton")
        self.pushButton_8.clicked.connect(self.change)
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.dels)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
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
        self.label.setText(_translate("MainWindow", "Warehouse_number"))
        self.label_2.setText(_translate("MainWindow", "Date"))
        self.label_3.setText(_translate("MainWindow", "Name_of_inventory"))
        self.label_4.setText(_translate("MainWindow", "Number_of_inventory_items"))
        self.label_5.setText(_translate("MainWindow", "Firstname"))
        self.label_6.setText(_translate("MainWindow", "Lastname"))
        self.label_7.setText(_translate("MainWindow", "Position"))
        self.pushButton_4.setText(_translate("MainWindow", "Get_invoice_data"))
        self.pushButton.setText(_translate("MainWindow", "Update_invoice_data"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_invoice_data"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_invoice_data"))
        self.pushButton_5.setText(_translate("MainWindow", "Get_receipt_data"))
        self.pushButton_6.setText(_translate("MainWindow", "Update_receipt_data"))
        self.pushButton_7.setText(_translate("MainWindow", "Add_receipt_data"))
        self.pushButton_8.setText(_translate("MainWindow", "Delete_receipt_data"))

    def change(self):

        try:
            Warehouse_num = int(self.lineEdit.text())
            date = self.lineEdit_2.text()
            Name_of_inventory = self.lineEdit_3.text()
            Number_of_inventory_items = int(self.lineEdit_4.text())
            Firstname = self.lineEdit_6.text()
            Lastname = self.lineEdit_7.text()
            Position = self.lineEdit_5.text()
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="root", db="lab4")
            cur = db.cursor()
            ch1="""UPDATE Warehouse_registration_card SET date = %s, Name_of_inventory = %s, Number_of_inventory_items = %s, Position = %s, Firstname = %s, Lastname = %s, Division_Division_num = %s WHERE user_id = %s"""
            ch2=(date, Name_of_inventory, Number_of_inventory_items, Position, Firstname, Lastname, Warehouse_num )
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            Warehouse_num = int(self.lineEdit.text())
            date = self.lineEdit_2.text()
            Name_of_inventory = self.lineEdit_3.text()
            Number_of_inventory_items = int(self.lineEdit_4.text())
            Firstname = self.lineEdit_6.text()
            Lastname = self.lineEdit_7.text()
            Position = self.lineEdit_5.text()
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="root", db="lab4")
        cur = db.cursor()
        cur.execute('insert into Warehouse_registration_card values(%s, %s, %s, %s, %s, %s, %s, %s)', \
                    (int(Warehouse_num), date, Name_of_inventory,Number_of_inventory_items, Position, Firstname, Lastname,))
        db.commit()
        cur.close()
        db.close()

    def dels(self):


        db = mysql.connect(host="localhost", user="root", passwd="root", db="lab4")
        cur = db.cursor()
        try:
            Warehouse_num = int(self.lineEdit.text())
        except:
            return
        cur.execute("DELETE FROM Warehouse_registration_card WHERE Warehouse_num = %s",(int(Warehouse_num),))
        db.commit()
        cur.close()
        db.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = In_Re_management()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
