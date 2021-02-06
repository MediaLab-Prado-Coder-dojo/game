# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coder_dojo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

def nombre_completo_label(nombre, apellido):
    return str(nombre + " "+ apellido)

def sumar_numeros_label(n1, n2):
    return str(float(float(n1) + float(n2)))

def modificar_ui(ui):
    ui.nombre_completo.setText(nombre_completo_label(ui.lineEdit_nombre.text(), ui.lineEdit_apellido.text()))
    ui.suma_total.setText(sumar_numeros_label(ui.suma_1.text(),ui.suma_2.text()))



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 315)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_apellido = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.gridLayout.addWidget(self.lineEdit_apellido, 5, 2, 1, 1)
        self.nombre_completo = QtWidgets.QLabel(Dialog)
        self.nombre_completo.setObjectName("nombre_completo")
        self.gridLayout.addWidget(self.nombre_completo, 7, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 9, 2, 1, 1)
        self.label_nombre = QtWidgets.QLabel(Dialog)
        self.label_nombre.setObjectName("label_nombre")
        self.gridLayout.addWidget(self.label_nombre, 2, 0, 1, 1)
        self.suma_1 = QtWidgets.QLineEdit(Dialog)
        self.suma_1.setObjectName("suma_1")
        self.gridLayout.addWidget(self.suma_1, 6, 0, 1, 1)
        self.suma_2 = QtWidgets.QLineEdit(Dialog)
        self.suma_2.setObjectName("suma_2")
        self.gridLayout.addWidget(self.suma_2, 6, 2, 1, 1)
        self.lineEdit_nombre = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.gridLayout.addWidget(self.lineEdit_nombre, 2, 2, 1, 1)
        self.label_apellido = QtWidgets.QLabel(Dialog)
        self.label_apellido.setObjectName("label_apellido")
        self.gridLayout.addWidget(self.label_apellido, 5, 0, 1, 1)
        self.simbolo = QtWidgets.QLabel(Dialog)
        self.simbolo.setObjectName("simbolo")
        self.gridLayout.addWidget(self.simbolo, 6, 1, 1, 1)
        self.suma_total = QtWidgets.QLabel(Dialog)
        self.suma_total.setObjectName("suma_total")
        self.gridLayout.addWidget(self.suma_total, 8, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.clicked.connect(lambda x: modificar_ui(self))
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nombre_completo.setText(_translate("Dialog", "Resultado"))
        self.label_nombre.setText(_translate("Dialog", "Nombre"))
        self.label_apellido.setText(_translate("Dialog", "Apellido"))
        self.simbolo.setText(_translate("Dialog", "+"))
        self.suma_total.setText(_translate("Dialog", "Suma"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)


    Dialog.show()
    sys.exit(app.exec_())
