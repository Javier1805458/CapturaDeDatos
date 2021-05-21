import mysql.connector as mysql
from mysql.connector.errors import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QErrorMessage, QMessageBox

lstDatos = []
mtzDatos = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 462)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.tbnAgregar.setGeometry(QtCore.QRect(100, 170, 81, 41))
        self.tbnAgregar.setObjectName("tbnAgregar")
        self.btnMostrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnMostrar.setGeometry(QtCore.QRect(250, 170, 81, 41))
        self.btnMostrar.setObjectName("btnMostrar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(250, 370, 81, 41))
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(100, 370, 81, 41))
        self.btnGuardar.setObjectName("btnGuardar")
        self.tblDatos = QtWidgets.QTableWidget(self.centralwidget)
        self.tblDatos.setGeometry(QtCore.QRect(10, 230, 411, 131))
        self.tblDatos.setObjectName("tblDatos")
        self.tblDatos.setColumnCount(4)
        self.tblDatos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblDatos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDatos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDatos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDatos.setHorizontalHeaderItem(3, item)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 190, 108))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtNombre = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNombre.setObjectName("txtNombre")
        self.horizontalLayout.addWidget(self.txtNombre)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtAPaterno = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtAPaterno.setObjectName("txtAPaterno")
        self.horizontalLayout_2.addWidget(self.txtAPaterno)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.txtAMaterno = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtAMaterno.setObjectName("txtAMaterno")
        self.horizontalLayout_3.addWidget(self.txtAMaterno)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spnEdad = QtWidgets.QSpinBox(self.layoutWidget)
        self.spnEdad.setObjectName("spnEdad")
        self.horizontalLayout_4.addWidget(self.spnEdad)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tbnAgregar.clicked.connect(self.btnAgregar_Cicked)
        self.btnGuardar.clicked.connect(self.btnGuardar_Clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Captura de datos"))
        self.tbnAgregar.setText(_translate("MainWindow", "Agregar"))
        self.btnMostrar.setText(_translate("MainWindow", "Mostrat Datos"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar"))
        item = self.tblDatos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tblDatos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "APaterno"))
        item = self.tblDatos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "AMaterno"))
        item = self.tblDatos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Edad"))
        self.label.setText(_translate("MainWindow", "Nombre     "))
        self.label_2.setText(_translate("MainWindow", "A Paterno "))
        self.label_3.setText(_translate("MainWindow", "A Materno"))
        self.label_4.setText(_translate("MainWindow", "Edad"))

    def btnAgregar_Cicked(self):
        if(int(self.spnEdad.text()) < 18):

            Msg = QMessageBox()
            Msg.setWindowTitle("Advertencia")
            Msg.setText("No puedes registrar Menores de edad")
            Msg.setIcon(QMessageBox.Critical)
            Msg.exec_()
        else:

            lstDatos.append(self.txtNombre.text())
            lstDatos.append(self.txtAPaterno.text())
            lstDatos.append(self.txtAMaterno.text())
            lstDatos.append(self.spnEdad.text())

            mtzDatos.append(lstDatos.copy())
            lstDatos.clear()

            row = 0
            for registro in mtzDatos:
                self.tblDatos.setRowCount(row + 1)
                self.tblDatos.setItem(row, 0, QtWidgets.QTableWidgetItem(registro[0]))
                self.tblDatos.setItem(row, 1, QtWidgets.QTableWidgetItem(registro[1]))
                self.tblDatos.setItem(row, 2, QtWidgets.QTableWidgetItem(registro[2]))
                self.tblDatos.setItem(row, 3, QtWidgets.QTableWidgetItem(registro[3]))

                row += 1
            self.borrarDatos()

    def btnGuardar_Clicked(self):
        if(len(mtzDatos) >= 1):
            self.ConexionDB()
            self.tblDatos.setRowCount(0)

            lstDatos.clear()
            mtzDatos.clear()

            Msg = QMessageBox()
            Msg.setWindowTitle("Advertencia")
            Msg.setText("La información se cargó con exito")
            Msg.exec_()
        
        else:
            Msg = QMessageBox()
            Msg.setWindowTitle("Advertencia")
            Msg.setText("Tienes que hacer un registro")
            Msg.setIcon(QMessageBox.Critical)
            Msg.exec_()

    def ConexionDB(self):
        try:
            dbConn = mysql.connect(user="root", password="", host="localhost", database="libreria_db")

            dbCommand = dbConn.cursor()

            for lst in mtzDatos:
                SqlScript = "CALL spInsertEscritor (%s, %s, %s, %s)"
                SqlVal = lst

                dbCommand.execute(SqlScript, SqlVal)
                dbConn.commit()

        except mysql.Error as e:
            print(e)
        finally:
            dbCommand.close()
            dbConn.close()

    def borrarDatos(self):
        self.txtNombre.clear()
        self.txtAPaterno.clear()
        self.txtAMaterno.clear()
        self.spnEdad.setValue(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
