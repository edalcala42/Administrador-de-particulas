from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from almacen_particulas import Almacen_Particulas
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
       super(MainWindow, self).__init__() 
       self.almacen_de_particulas = Almacen_Particulas()
       self.ui = Ui_MainWindow()
       self.ui.setupUi(self)
       self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
       self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
       self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
       self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
       self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.almacen_de_particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print (ubicacion)
        if self.almacen_de_particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_spinBox.value()
        origenX = self.ui.ox_spinBox.value()
        origenY = self.ui.oy_spinBox.value()
        destinoX = self.ui.dx_spinBox.value()
        destinoY = self.ui.dy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox_2.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.almacen_de_particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_spinBox.value()
        origenX = self.ui.ox_spinBox.value()
        origenY = self.ui.oy_spinBox.value()
        destinoX = self.ui.dx_spinBox.value()
        destinoY = self.ui.dy_spinBox.value()
        velocidad = self.ui.id_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.almacen_de_particulas.agregar_inicio(particula)

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.almacen_de_particulas))