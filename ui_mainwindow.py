# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(717, 504)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.velocidad_spinBox_2 = QSpinBox(self.groupBox)
        self.velocidad_spinBox_2.setObjectName(u"velocidad_spinBox_2")
        self.velocidad_spinBox_2.setMaximum(1000000)

        self.gridLayout.addWidget(self.velocidad_spinBox_2, 6, 1, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.blue_spinBox, 10, 1, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.red_spinBox, 8, 1, 1, 1)

        self.ox_spinBox = QSpinBox(self.groupBox)
        self.ox_spinBox.setObjectName(u"ox_spinBox")
        self.ox_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.ox_spinBox, 2, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)

        self.oy_spinBox = QSpinBox(self.groupBox)
        self.oy_spinBox.setObjectName(u"oy_spinBox")
        self.oy_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.oy_spinBox, 3, 1, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 12, 0, 1, 2)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.green_spinBox, 9, 1, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(1000000)

        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 1)

        self.dx_spinBox = QSpinBox(self.groupBox)
        self.dx_spinBox.setObjectName(u"dx_spinBox")
        self.dx_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.dx_spinBox, 4, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 11, 0, 1, 2)

        self.dy_spinBox = QSpinBox(self.groupBox)
        self.dy_spinBox.setObjectName(u"dy_spinBox")
        self.dy_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.dy_spinBox, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 13, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 4, 0, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 2)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 4, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 2, 0, 1, 1)

        self.Orden_ID_pushButton = QPushButton(self.tab_2)
        self.Orden_ID_pushButton.setObjectName(u"Orden_ID_pushButton")

        self.gridLayout_4.addWidget(self.Orden_ID_pushButton, 4, 2, 1, 1)

        self.Orden_Distancia_pushButton = QPushButton(self.tab_2)
        self.Orden_Distancia_pushButton.setObjectName(u"Orden_Distancia_pushButton")

        self.gridLayout_4.addWidget(self.Orden_Distancia_pushButton, 2, 1, 1, 1)

        self.Orden_Velocidad_pushButton = QPushButton(self.tab_2)
        self.Orden_Velocidad_pushButton.setObjectName(u"Orden_Velocidad_pushButton")

        self.gridLayout_4.addWidget(self.Orden_Velocidad_pushButton, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.pushButton_Dibujar = QPushButton(self.tab_3)
        self.pushButton_Dibujar.setObjectName(u"pushButton_Dibujar")

        self.gridLayout_5.addWidget(self.pushButton_Dibujar, 1, 0, 1, 1)

        self.pushButton_Limpiar = QPushButton(self.tab_3)
        self.pushButton_Limpiar.setObjectName(u"pushButton_Limpiar")

        self.gridLayout_5.addWidget(self.pushButton_Limpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 717, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Captura de part\u00edculas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"origen en y: ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"blue: ", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"green: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"destino x:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"origen en x: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"destino y:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"color (rgb)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"velocidad: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"red: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"id: ", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de la part\u00edcula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Orden_ID_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Id", None))
        self.Orden_Distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por distancia", None))
        self.Orden_Velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por velocidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.pushButton_Dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.pushButton_Limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Impresi\u00f3n", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

